# Service Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For service pages — a particular service the business offers (consulting, web design, cleaning, legal advice, etc.). Not a direct rich result, but it clarifies the entity for Google and helps with local + industry-specific query matching.

Reference: <https://schema.org/Service>

## When to use

- One per service page. Don't emit `Service` on the homepage or on blog posts.
- If the site is a single-service business, the service may be represented on the homepage alongside `LocalBusiness` instead (via `makesOffer`).

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Service` |
| `@id` | recommended | `{permalink}#service` |
| `name` | required | Service name |
| `description` | required | What the service delivers |
| `provider` | required | Reference the `Organization` by `@id` |
| `serviceType` | recommended | Short category label (e.g. "SEO consulting") |
| `areaServed` | recommended | Geographic scope — city, region, country, or `Place` object |
| `offers` | recommended | Price range or `Offer` with price |
| `hasOfferCatalog` | optional | Bundled offerings — `OfferCatalog` with nested `Offer`s |
| `image` | recommended | |
| `url` | recommended | Canonical URL |

### Multi-service sites — `hasOfferCatalog`

When a service page bundles multiple sub-offerings:

```json
{
  "@type": "Service",
  "name": "SEO Services",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "SEO Services",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Technical SEO Audit" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Keyword Research" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Content Writing" } }
    ]
  }
}
```

## ACF mapping

Field group: **Service Schema** — location: Post Type == `service`.

| Schema property | ACF field | Type |
|---|---|---|
| `name` | `service_name` | text (fallback `get_the_title()`) |
| `description` | `service_description` | textarea |
| `serviceType` | `service_category` | text |
| `areaServed` | `service_area` | text OR repeater (multiple regions) |
| `image` | `service_image` | image |
| `offers.price` | `service_price_from` | number (optional) |
| `hasOfferCatalog` | `service_sub_offerings` | repeater → `name`, `description` |

## PHP template — `/inc/schema/service-schema.php`

```php
<?php
/**
 * Service schema (JSON-LD) for service CPT singulars.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$name        = get_field( 'service_name' ) ?: get_the_title();
$description = get_field( 'service_description' ) ?: get_the_excerpt();
$type_label  = get_field( 'service_category' );
$area        = get_field( 'service_area' );
$image       = get_field( 'service_image' );
$image_url   = is_array( $image ) ? ( $image['url'] ?? '' ) : '';
$price_from  = get_field( 'service_price_from' );
$catalog     = get_field( 'service_sub_offerings' );

$schema = [
    '@context'   => 'https://schema.org',
    '@type'      => 'Service',
    '@id'        => get_permalink() . '#service',
    'name'       => $name,
    'url'        => get_permalink(),
    'provider'   => [ '@id' => home_url( '/#organization' ) ],
];

if ( $description ) { $schema['description'] = $description; }
if ( $type_label )  { $schema['serviceType'] = $type_label; }
if ( $image_url )   { $schema['image']       = esc_url( $image_url ); }

if ( $area ) {
    $schema['areaServed'] = is_array( $area )
        ? array_values( array_filter( array_map( fn( $r ) => $r['area'] ?? '', $area ) ) )
        : $area;
}

if ( $price_from !== '' && $price_from !== null ) {
    $schema['offers'] = [
        '@type'         => 'Offer',
        'price'         => (string) $price_from,
        'priceCurrency' => 'USD',
        'url'           => get_permalink(),
    ];
}

if ( is_array( $catalog ) && $catalog ) {
    $items = [];
    foreach ( $catalog as $row ) {
        $item_name = trim( $row['name'] ?? '' );
        if ( $item_name === '' ) { continue; }
        $items[] = [
            '@type'       => 'Offer',
            'itemOffered' => array_filter( [
                '@type'       => 'Service',
                'name'        => $item_name,
                'description' => $row['description'] ?? null,
            ] ),
        ];
    }
    if ( $items ) {
        $schema['hasOfferCatalog'] = [
            '@type'           => 'OfferCatalog',
            'name'            => $name,
            'itemListElement' => $items,
        ];
    }
}

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_singular( 'service' ) ) {
        include get_template_directory() . '/inc/schema/service-schema.php';
    }
}, 20 );
```

## Gotchas

- `Service` is not a rich-result type on its own. Its value is entity clarity + sitelinks-style matching.
- If the business is local, prefer `LocalBusiness.makesOffer → Service` on the homepage/location page, and keep `Service` on individual service pages.
- Don't use `Product` for services — use `Service`.
- Price info should use ranges or `priceSpecification` if variable — don't fake a single price.
