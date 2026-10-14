# BreadcrumbList + ItemList Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


Two navigation-oriented types:

- **`BreadcrumbList`** — the breadcrumb trail for the current page. Should appear on almost every non-homepage URL. Can support eligible breadcrumb presentation; appearance is not guaranteed.
- **`ItemList`** — an ordered list of items (e.g. category pages, "Top 10" articles). Carousel eligibility depends on current supported type/region/feature rules.

Reference: <https://schema.org/BreadcrumbList> · <https://schema.org/ItemList>

---

## BreadcrumbList

### Required fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `BreadcrumbList` |
| `itemListElement` | required | Array of `ListItem` |

Each `ListItem`:

| Field | Required? |
|---|---|
| `@type` | required — `ListItem` |
| `position` | required — 1-based |
| `name` | required |
| `item` | required for all except the last (last may omit or include) |

### PHP template — `/inc/schema/breadcrumb-schema.php`

Auto-builds the trail from WP's taxonomy / ancestor hierarchy. Works without a breadcrumb plugin.

```php
<?php
/**
 * BreadcrumbList schema (JSON-LD), auto-built from WP context.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$items = [];
$pos   = 1;

$items[] = [
    '@type'    => 'ListItem',
    'position' => $pos++,
    'name'     => __( 'Home', 'theme' ),
    'item'     => home_url( '/' ),
];

if ( is_singular() ) {
    $post_type = get_post_type();

    // Post type archive link for CPTs (not 'post' or 'page')
    if ( $post_type && $post_type !== 'post' && $post_type !== 'page' ) {
        $pto = get_post_type_object( $post_type );
        if ( $pto && ! empty( $pto->has_archive ) ) {
            $items[] = [
                '@type'    => 'ListItem',
                'position' => $pos++,
                'name'     => $pto->labels->name,
                'item'     => get_post_type_archive_link( $post_type ),
            ];
        }
    }

    // Primary category for posts
    if ( $post_type === 'post' ) {
        $cats = get_the_category();
        if ( $cats ) {
            $cat = $cats[0];
            $items[] = [
                '@type'    => 'ListItem',
                'position' => $pos++,
                'name'     => $cat->name,
                'item'     => get_category_link( $cat ),
            ];
        }
    }

    // Page ancestors
    if ( $post_type === 'page' ) {
        $ancestors = array_reverse( get_post_ancestors( get_the_ID() ) );
        foreach ( $ancestors as $ancestor_id ) {
            $items[] = [
                '@type'    => 'ListItem',
                'position' => $pos++,
                'name'     => get_the_title( $ancestor_id ),
                'item'     => get_permalink( $ancestor_id ),
            ];
        }
    }

    $items[] = [
        '@type'    => 'ListItem',
        'position' => $pos++,
        'name'     => get_the_title(),
        'item'     => get_permalink(),
    ];
}

if ( is_category() || is_tag() || is_tax() ) {
    $items[] = [
        '@type'    => 'ListItem',
        'position' => $pos++,
        'name'     => single_term_title( '', false ),
        'item'     => get_term_link( get_queried_object() ),
    ];
}

$schema = [
    '@context'        => 'https://schema.org',
    '@type'           => 'BreadcrumbList',
    '@id'             => ( is_singular() ? get_permalink() : home_url( add_query_arg( null, null ) ) ) . '#breadcrumb',
    'itemListElement' => $items,
];

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

### Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( ! is_front_page() && ( is_singular() || is_category() || is_tag() || is_tax() ) ) {
        include get_template_directory() . '/inc/schema/breadcrumb-schema.php';
    }
}, 20 );
```

### Gotchas

- The schema trail must match what's visible on the page. If the theme doesn't render breadcrumbs, don't emit this.
- Position starts at 1 (not 0).
- Last item can optionally omit `item` — include it for safety.

---

## ItemList

### When to use

- Category pages (list of products or posts)
- Archive pages
- "Top 10" / listicle articles (combine with `Article`)
- Search result pages (rarely worth it)

ItemList alone does not establish carousel eligibility; verify current type, region and feature requirements.

### Required fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `ItemList` |
| `itemListElement` | required | Array of `ListItem` |
| `numberOfItems` | recommended | |

### PHP template — `/inc/schema/itemlist-schema.php`

Works on archive and category pages. Lists items from the current query.

```php
<?php
/**
 * ItemList schema (JSON-LD) for category / archive / listing pages.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

global $wp_query;
if ( ! $wp_query->have_posts() ) { return; }

$items = [];
$pos   = 1;

foreach ( $wp_query->posts as $p ) {
    $items[] = [
        '@type'    => 'ListItem',
        'position' => $pos++,
        'url'      => get_permalink( $p ),
        'name'     => get_the_title( $p ),
    ];
}

$current_url = is_post_type_archive() ? get_post_type_archive_link( get_post_type() )
             : ( ( is_category() || is_tag() || is_tax() ) ? get_term_link( get_queried_object() ) : home_url() );

$schema = [
    '@context'        => 'https://schema.org',
    '@type'           => 'ItemList',
    '@id'             => trailingslashit( $current_url ) . '#itemlist',
    'numberOfItems'   => count( $items ),
    'itemListElement' => $items,
];

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

### Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_post_type_archive() || is_category() || is_tag() || is_tax() ) {
        include get_template_directory() . '/inc/schema/itemlist-schema.php';
    }
}, 20 );
```

### Gotchas

- For the carousel rich result, each list item must itself be a rich-result-eligible type (Product, Recipe, Movie, Course). A list of plain pages won't produce a carousel.
- `position` is 1-based and must be sequential.
- Don't emit `ItemList` on paginated archive pages beyond page 1 — it's misleading to Google.
