# MerchantReturnPolicy Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For returns/refund policy pages on ecommerce sites. Search appearance is not guaranteed.

Reference: <https://schema.org/MerchantReturnPolicy>  
Google guidance: <https://developers.google.com/search/docs/appearance/structured-data/return-policy>

## When to use

- A dedicated returns/refund policy page.
- As a nested property on `Product.offers.hasMerchantReturnPolicy` — per-product return rules.
- On a global return-policy page for the site.

Only useful if the site sells products. Skip for services, SaaS, content sites.

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `MerchantReturnPolicy` |
| `@id` | recommended | `{permalink}#return-policy` |
| `applicableCountry` | required | Array of ISO 3166-1 alpha-2 codes, e.g. `["US", "CA"]` |
| `returnPolicyCategory` | required | One of: `MerchantReturnFiniteReturnWindow`, `MerchantReturnNotPermitted`, `MerchantReturnUnlimitedWindow`, `MerchantReturnUnspecified` |
| `merchantReturnDays` | required if finite window | Integer — number of days |
| `returnMethod` | recommended | `ReturnByMail`, `ReturnInStore`, `ReturnAtKiosk` |
| `returnFees` | recommended | `FreeReturn`, `OriginalShippingFees`, `RestockingFees`, `ReturnShippingFees`, `ReturnFeesCustomerResponsibility` |
| `returnShippingFeesAmount` | required if customer pays | `MonetaryAmount` |
| `refundType` | recommended | `FullRefund`, `ExchangeRefund`, `StoreCreditRefund` |

## ACF mapping

Field group: **Return Policy Schema** — location: Page == returns OR Options Page (for site-wide).

| Schema property | ACF field | Type |
|---|---|---|
| `applicableCountry` | `return_countries` | repeater → text (ISO 3166 code) OR select (multi) |
| `returnPolicyCategory` | `return_category` | select (options above) |
| `merchantReturnDays` | `return_days` | number |
| `returnMethod` | `return_method` | select |
| `returnFees` | `return_fees` | select |
| `returnShippingFeesAmount.value` | `return_shipping_fee` | number |
| `returnShippingFeesAmount.currency` | `return_shipping_currency` | text (ISO 4217) |
| `refundType` | `refund_type` | select |

## PHP template — `/inc/schema/returnpolicy-schema.php`

```php
<?php
/**
 * MerchantReturnPolicy schema (JSON-LD) for the return policy page.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$countries    = get_field( 'return_countries' );
$category     = get_field( 'return_category' );
$days         = get_field( 'return_days' );
$method       = get_field( 'return_method' );
$fees         = get_field( 'return_fees' );
$fee_amount   = get_field( 'return_shipping_fee' );
$fee_currency = get_field( 'return_shipping_currency' ) ?: 'USD';
$refund_type  = get_field( 'refund_type' );

$country_list = [];
if ( is_array( $countries ) ) {
    foreach ( $countries as $row ) {
        $code = is_array( $row ) ? ( $row['code'] ?? '' ) : (string) $row;
        if ( $code ) { $country_list[] = strtoupper( $code ); }
    }
}

$schema = [
    '@context'             => 'https://schema.org',
    '@type'                => 'MerchantReturnPolicy',
    '@id'                  => get_permalink() . '#return-policy',
    'url'                  => get_permalink(),
    'returnPolicyCategory' => 'https://schema.org/' . $category,
];

if ( $country_list )                     { $schema['applicableCountry']  = $country_list; }
if ( $category === 'MerchantReturnFiniteReturnWindow' && $days !== '' && $days !== null && $days !== false ) {
    $schema['merchantReturnDays'] = (int) $days;
}
if ( $method )                           { $schema['returnMethod']       = 'https://schema.org/' . $method; }
if ( $fees )                             { $schema['returnFees']         = 'https://schema.org/' . $fees; }
if ( $refund_type )                      { $schema['refundType']         = 'https://schema.org/' . $refund_type; }

if ( $fees === 'ReturnShippingFees' && $fee_amount ) {
    $schema['returnShippingFeesAmount'] = [
        '@type'    => 'MonetaryAmount',
        'value'    => (string) $fee_amount,
        'currency' => strtoupper( $fee_currency ),
    ];
}

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_page( [ 'returns', 'return-policy', 'refund-policy' ] ) ) {
        include get_template_directory() . '/inc/schema/returnpolicy-schema.php';
    }
}, 20 );
```

## Gotchas

- Country codes must be ISO 3166-1 alpha-2, uppercase: `US`, `GB`, `UA`, `DE`. Not country names.
- `returnPolicyCategory` values are enum URLs — prepend `https://schema.org/` to the keyword.
- If returns are not permitted, use `MerchantReturnNotPermitted` and omit `merchantReturnDays`.
- For per-product policies that differ from the global page, nest under `Product.offers.hasMerchantReturnPolicy` in `product-schema.php` rather than emitting a second block.
- Return policy must match what's visibly stated on the page — Google cross-checks.
