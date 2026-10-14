# Product Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For ecommerce product pages. Search appearance is not guaranteed.

Reference: <https://schema.org/Product>  
Google guidance: <https://developers.google.com/search/docs/appearance/structured-data/product>

## Before you start

**If WooCommerce is active, it already emits Product schema.** Do not output a second `Product` block. Instead, extend WooCommerce's via the `woocommerce_structured_data_product` filter. Only use this template on a non-WooCommerce custom `product` CPT.

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Product` |
| `@id` | recommended | `{permalink}#product` |
| `name` | required | |
| `image` | required | URL or array of URLs; Use high-resolution representative images |
| `description` | recommended | |
| `sku` | recommended | |
| `brand` | recommended | `{ "@type": "Brand", "name": "..." }` |
| `offers` | required | See `Offer` below |
| `aggregateRating` | recommended IF real reviews exist | See below |
| `review` | recommended IF real reviews exist | Never self-review |

### `Offer`

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Offer` |
| `price` | required | Number as string, no currency symbol |
| `priceCurrency` | required | ISO 4217, e.g. `USD`, `EUR`, `UAH` |
| `availability` | required | `https://schema.org/InStock` / `OutOfStock` / `PreOrder` / `Discontinued` / `LimitedAvailability` |
| `url` | required | |
| `priceValidUntil` | recommended | ISO 8601 date, required if price is a sale |
| `itemCondition` | optional | `https://schema.org/NewCondition` etc. |

### `AggregateRating` (only if real reviews exist)

| Field | Required? | Notes |
|---|---|---|
| `ratingValue` | required | Number 1–5 |
| `reviewCount` | required | Integer > 0 |
| `bestRating` | recommended | Usually 5 |

**Hard rule:** never fabricate reviews or ratings. If there are no real reviews, omit both blocks — a missing `aggregateRating` is fine, a fake one is a manual action.

## ACF mapping

Field group: **Product Schema** — location: Post Type == `product`.

| Schema property | ACF field | Type |
|---|---|---|
| `name` | `product_name` | text (fallback `get_the_title()`) |
| `description` | `product_description` | textarea |
| `image` | `product_image` + `product_gallery` | image + gallery |
| `offers.price` | `product_price` | number |
| `offers.priceCurrency` | `product_currency` | select (USD / EUR / UAH / ...) |
| `offers.availability` | `product_stock` | select (InStock / OutOfStock / PreOrder / Discontinued) |
| `offers.priceValidUntil` | `product_price_valid_until` | date picker |
| `brand.name` | `product_brand` | text |
| `sku` | `product_sku` | text |

## PHP template — `/inc/schema/product-schema.php`

```php
<?php
/**
 * Product schema (JSON-LD) for product CPT singulars.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$name        = get_field( 'product_name' ) ?: get_the_title();
$description = get_field( 'product_description' );
$image       = get_field( 'product_image' );
$image_url   = is_array( $image ) ? ( $image['url'] ?? '' ) : '';
$gallery     = get_field( 'product_gallery' );
$price       = get_field( 'product_price' );
$currency    = get_field( 'product_currency' );
$stock       = get_field( 'product_stock' );
$valid_until = get_field( 'product_price_valid_until' );
$brand       = get_field( 'product_brand' );
$sku         = get_field( 'product_sku' );

$images = [];
if ( $image_url ) { $images[] = esc_url( $image_url ); }
if ( is_array( $gallery ) ) {
    foreach ( $gallery as $img ) {
        if ( ! empty( $img['url'] ) ) { $images[] = esc_url( $img['url'] ); }
    }
}

$schema = [
    '@context' => 'https://schema.org',
    '@type'    => 'Product',
    '@id'      => get_permalink() . '#product',
    'name'     => $name,
    'url'      => get_permalink(),
];

if ( $description ) { $schema['description'] = $description; }
if ( $images )      { $schema['image']       = count( $images ) === 1 ? $images[0] : $images; }
if ( $brand )       { $schema['brand']       = [ '@type' => 'Brand', 'name' => $brand ]; }
if ( $sku )         { $schema['sku']         = $sku; }

if ( $price !== '' && $price !== null && $price !== false && $currency && $stock ) {
    $offer = [
        '@type'         => 'Offer',
        'price'         => (string) $price,
        'priceCurrency' => $currency,
        'availability'  => 'https://schema.org/' . $stock,
        'url'           => get_permalink(),
    ];
    if ( $valid_until ) {
        // ACF date picker returns Ymd by default; convert to ISO.
        $offer['priceValidUntil'] = gmdate( 'Y-m-d', strtotime( $valid_until ) );
    }
    $schema['offers'] = $offer;
}

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_singular( 'product' ) && ! class_exists( 'WooCommerce' ) ) {
        include get_template_directory() . '/inc/schema/product-schema.php';
    }
}, 20 );
```

## Gotchas

- Use an accurate numeric value without currency symbol; string or number is acceptable to Schema.org.
- `priceCurrency` must be ISO 4217 — `USD`, not `$`.
- If you emit `aggregateRating`, the page must show that rating visibly to users.
- Publish sale dates only when verified; follow current chosen-result requirements.
- Multiple images: use an array, not a comma-separated string.
