# Organization + WebSite Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For the site entity and the company/brand entity. Both should appear on the homepage, linked via `@id`. The entities describe:

- `Organization` → verified publisher identity, logo and profiles
- `WebSite` → site identity; optional SearchAction describes a real search action

Reference: <https://schema.org/Organization> · <https://schema.org/WebSite>

## Where to emit

- **Homepage only** — one `Organization` + one `WebSite` block for the whole site.
- On every other page, reference the org by `@id` (don't re-declare it).

## Required + recommended fields — Organization

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Organization` (or a subtype like `Corporation`, `NGO`, `LocalBusiness`) |
| `@id` | required for linking | `https://site.com/#organization` |
| `name` | required | Legal or brand name |
| `url` | required | Homepage URL |
| `logo` | required for rich result | 112×112 min, square, transparent BG preferred |
| `sameAs` | recommended | Array of social profile URLs — LinkedIn, X, Facebook, Instagram, YouTube, GitHub, Crunchbase |
| `description` | recommended | One-sentence positioning |
| `foundingDate` | optional | ISO 8601 date |
| `founders` | optional | Array of `Person` refs |
| `contactPoint` | recommended | `{ "@type": "ContactPoint", "telephone": "+1...", "contactType": "customer service" }` |
| `address` | recommended for physical orgs | `PostalAddress` |

## Required + recommended fields — WebSite

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `WebSite` |
| `@id` | required | `https://site.com/#website` |
| `url` | required | Homepage URL |
| `name` | required | Site name |
| `publisher` | recommended | `{ "@id": "...#organization" }` — links to the Organization |
| `potentialAction` | recommended | Optional SearchAction; no retired search-box promise |

### Optional `SearchAction` semantics

```json
{
  "@type": "SearchAction",
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://site.com/?s={search_term_string}"
  },
  "query-input": "required name=search_term_string"
}
```

The search URL template must match the site's actual search URL (usually `/?s=` for WordPress).

## ACF mapping

Field group: **Organization Schema** — location: Page == front page (or use Options Page for site-wide values).

| Schema property | ACF field | Type |
|---|---|---|
| `name` | `org_name` | text |
| `logo` | `org_logo` | image (return array) |
| `sameAs` | `org_social_profiles` | repeater → url subfield `url` |
| `description` | `org_description` | textarea |
| `foundingDate` | `org_founding_date` | date picker |
| `contactPoint.telephone` | `org_phone` | text |
| `contactPoint.email` | `org_email` | email |
| `address.streetAddress` | `org_street` | text |
| `address.addressLocality` | `org_city` | text |
| `address.postalCode` | `org_postal_code` | text |
| `address.addressCountry` | `org_country` | text (ISO code) |

Recommendation: put these on an **ACF Options Page** (`acf_add_options_page`) so they're site-wide, not per-post.

## PHP template — `/inc/schema/organization-schema.php`

Emits `Organization` + `WebSite` together in a single `@graph` so `publisher` can reference the org by `@id`.

```php
<?php
/**
 * Organization + WebSite schema (JSON-LD), homepage only.
 * Site-wide values come from ACF Options Page.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$home      = home_url( '/' );
$org_id    = $home . '#organization';
$site_id   = $home . '#website';
$logo_id   = $home . '#logo';

$name      = get_field( 'org_name', 'option' ) ?: get_bloginfo( 'name' );
$desc      = get_field( 'org_description', 'option' ) ?: get_bloginfo( 'description' );
$logo      = get_field( 'org_logo', 'option' );
$logo_url  = is_array( $logo ) ? ( $logo['url'] ?? '' ) : '';
$founding  = get_field( 'org_founding_date', 'option' );
$phone     = get_field( 'org_phone', 'option' );
$email     = get_field( 'org_email', 'option' );
$socials   = get_field( 'org_social_profiles', 'option' );

$organization = [
    '@type' => 'Organization',
    '@id'   => $org_id,
    'name'  => $name,
    'url'   => $home,
];

if ( $desc ) { $organization['description'] = $desc; }

if ( $logo_url ) {
    $organization['logo'] = [
        '@type' => 'ImageObject',
        '@id'   => $logo_id,
        'url'   => esc_url( $logo_url ),
    ];
    $organization['image'] = [ '@id' => $logo_id ];
}

if ( $founding ) {
    $organization['foundingDate'] = gmdate( 'Y-m-d', strtotime( $founding ) );
}

if ( $phone || $email ) {
    $cp = [ '@type' => 'ContactPoint', 'contactType' => 'customer service' ];
    if ( $phone ) { $cp['telephone'] = $phone; }
    if ( $email ) { $cp['email']     = $email; }
    $organization['contactPoint'] = $cp;
}

if ( is_array( $socials ) && $socials ) {
    $organization['sameAs'] = array_values( array_filter( array_map(
        fn( $row ) => esc_url_raw( $row['url'] ?? '' ),
        $socials
    ) ) );
}

$website = [
    '@type'     => 'WebSite',
    '@id'       => $site_id,
    'url'       => $home,
    'name'      => get_bloginfo( 'name' ),
    'publisher' => [ '@id' => $org_id ],
    'potentialAction' => [
        '@type'       => 'SearchAction',
        'target'      => [
            '@type'       => 'EntryPoint',
            'urlTemplate' => $home . '?s={search_term_string}',
        ],
        'query-input' => 'required name=search_term_string',
    ],
];

$schema = [
    '@context' => 'https://schema.org',
    '@graph'   => [ $organization, $website ],
];

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_front_page() ) {
        include get_template_directory() . '/inc/schema/organization-schema.php';
    }
}, 20 );
```

## Gotchas

- The `urlTemplate` for `SearchAction` must match the actual search URL. For WordPress that's almost always `/?s={search_term_string}`; if a custom search plugin uses a different route, use that.
- Google retired the Sitelinks Search Box in November 2024. Only describe an actual search action; this is not a search-result enhancement requirement.
- `LocalBusiness` is a subtype of `Organization` — if the site is a physical business, use `LocalBusiness` here (see `schemas/local.md`) and do not emit both.
- Don't list social URLs you're not sure about — wrong `sameAs` confuses Knowledge Graph.
