# Article / BlogPosting Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For blog posts and editorial content. Search appearance is not guaranteed.

Reference: <https://schema.org/Article> · <https://schema.org/BlogPosting>  
Google guidance: <https://developers.google.com/search/docs/appearance/structured-data/article>

## Which @type?

- **`BlogPosting`** — default for blog posts on a marketing/company blog. Use this.
- **`Article`** — generic editorial content.
- **`NewsArticle`** — for genuine news content; choose the type by content rather than publisher registration.

For this package, use **`BlogPosting`** when the content is an ordinary blog article.

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `BlogPosting` |
| `@id` | recommended | `{permalink}#article` |
| `headline` | required | Accurate full article headline |
| `image` | required | High-resolution representative images; ideally 3 ratios (16:9, 4:3, 1:1) |
| `datePublished` | required | ISO 8601 with timezone |
| `dateModified` | recommended | ISO 8601 |
| `author` | required | `Person` or `Organization`, referenced by `@id` |
| `publisher` | required | `Organization` ref by `@id` — points to site Organization |
| `description` | recommended | Short summary (~155 chars) |
| `mainEntityOfPage` | recommended | `{ "@type": "WebPage", "@id": "{permalink}" }` |
| `keywords` | optional | Array of tag names |
| `articleSection` | optional | Primary category |
| `wordCount` | optional | |
| `inLanguage` | recommended on multilingual sites | `en`, `uk`, etc. |

## ACF mapping

Most fields come from WP core, not ACF — the theme already knows title, author, dates, featured image.

| Schema property | Source |
|---|---|
| `headline` | `get_the_title()` |
| `image` | `get_the_post_thumbnail_url( null, 'full' )` + registered WP image sizes |
| `datePublished` | `get_the_date( 'c' )` |
| `dateModified` | `get_the_modified_date( 'c' )` |
| `description` | ACF `article_summary` OR `get_the_excerpt()` |
| `author` | Linked to `Person` by `@id` — `get_author_posts_url( $user_id ) . '#person'` |
| `publisher` | `home_url( '/#organization' )` |
| `articleSection` | Primary category name |
| `keywords` | `get_the_tags()` |
| `wordCount` | `str_word_count( strip_tags( get_the_content() ) )` |

Add an ACF field only if the theme wants editor-controlled overrides:

Field group: **Article Schema** — location: Post Type == `post`.

| ACF field | Type | Purpose |
|---|---|---|
| `article_summary` | textarea | Overrides excerpt for schema `description` |
| `article_headline_override` | text | Overrides title if SEO title ≠ editorial title |
| `article_inline_faq` | repeater → `question`, `answer` | Inline FAQ — emits FAQPage schema alongside |

## PHP template — `/inc/schema/article-schema.php`

```php
<?php
/**
 * Article / BlogPosting schema (JSON-LD) for blog posts.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$post_id   = get_the_ID();
$permalink = get_permalink();
$headline  = get_field( 'article_headline_override' ) ?: get_the_title();
$summary   = get_field( 'article_summary' ) ?: get_the_excerpt();
$thumb_id  = get_post_thumbnail_id( $post_id );
$author_id = (int) get_post_field( 'post_author', $post_id );

$images = [];
if ( $thumb_id ) {
    foreach ( [ 'schema-16x9', 'schema-4x3', 'schema-1x1', 'full' ] as $size ) {
        $src = wp_get_attachment_image_src( $thumb_id, $size );
        if ( $src && ! empty( $src[0] ) ) { $images[] = esc_url( $src[0] ); }
    }
    $images = array_values( array_unique( $images ) );
}

$cats    = get_the_category( $post_id );
$section = $cats ? $cats[0]->name : null;

$tag_terms = get_the_tags( $post_id );
$keywords  = $tag_terms ? wp_list_pluck( $tag_terms, 'name' ) : [];

$content    = get_post_field( 'post_content', $post_id );
$word_count = str_word_count( wp_strip_all_tags( $content ) );

$schema = [
    '@context'         => 'https://schema.org',
    '@type'            => 'BlogPosting',
    '@id'              => $permalink . '#article',
    'mainEntityOfPage' => [ '@type' => 'WebPage', '@id' => $permalink ],
    'headline'         => $headline,
    'datePublished'    => get_the_date( 'c', $post_id ),
    'dateModified'     => get_the_modified_date( 'c', $post_id ),
    'author'           => [ '@id' => get_author_posts_url( $author_id ) . '#person' ],
    'publisher'        => [ '@id' => home_url( '/#organization' ) ],
    'inLanguage'       => str_replace( '_', '-', get_locale() ),
];

if ( $summary )    { $schema['description']    = $summary; }
if ( $images )     { $schema['image']          = count( $images ) === 1 ? $images[0] : $images; }
if ( $section )    { $schema['articleSection'] = $section; }
if ( $keywords )   { $schema['keywords']       = $keywords; }
if ( $word_count ) { $schema['wordCount']      = $word_count; }

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_singular( 'post' ) ) {
        include get_template_directory() . '/inc/schema/article-schema.php';
    }
}, 20 );

// Register schema image sizes once, in the theme setup:
add_action( 'after_setup_theme', function () {
    add_image_size( 'schema-16x9', 1200, 675, true );
    add_image_size( 'schema-4x3',  1200, 900, true );
    add_image_size( 'schema-1x1',  1200, 1200, true );
} );
```

## Gotchas

- Preserve the accurate full headline; no fixed 110-character validity cap.
- Use real crawlable article images where available; recommended fields are not universal required fields.
- `author` must link to a real `Person` entity. If the site has no author bio pages, emit an `Organization` as `author` instead.
- Use `BlogPosting`, not `NewsArticle`, when the content is an ordinary blog article.
- If the post has an inline FAQ, emit `FAQPage` as a **separate** schema block on the same page (see `schemas/qa.md`). Don't nest FAQ questions inside `Article`.
