# LocalBusiness Schema (+ subtypes)

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For physical businesses with a location customers can visit. Search appearance is not guaranteed.

Reference: <https://schema.org/LocalBusiness>  
Google guidance: <https://developers.google.com/search/docs/appearance/structured-data/local-business>

## Pick the most specific subtype

`LocalBusiness` has many subtypes — always use the most specific one that matches:

- `Restaurant`, `Bakery`, `CafeOrCoffeeShop`, `FoodEstablishment`
- `Store`, `ClothingStore`, `BookStore`, `HardwareStore`
- `Dentist`, `MedicalBusiness`, `Physician`, `Hospital`
- `AutomotiveBusiness`, `AutoRepair`, `GasStation`
- `ProfessionalService`, `LegalService`, `AccountingService`
- `LodgingBusiness`, `Hotel`, `BedAndBreakfast`
- `BeautySalon`, `HairSalon`, `DaySpa`, `NailSalon`
- `FinancialService`, `InsuranceAgency`
- `RealEstateAgent`
- `Electrician`, `Plumber`, `HVACBusiness`, `HomeAndConstructionBusiness`

If none fit, fall back to `LocalBusiness`.

Full list: <https://schema.org/LocalBusiness>

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | Specific subtype |
| `@id` | required | `https://site.com/#organization` (doubles as the Organization entity) |
| `name` | required | |
| `url` | required | Homepage or location page |
| `image` | required | At least one exterior photo, 1200×675 |
| `address` | required | `PostalAddress` — street, locality, region, postal code, country |
| `telephone` | required | Include country code, e.g. `+1-555-555-0123` |
| `geo` | recommended | `GeoCoordinates` with `latitude`, `longitude` |
| `openingHoursSpecification` | recommended | Array of `OpeningHoursSpecification` |
| `priceRange` | recommended | `$`, `$$`, `$$$`, or textual e.g. `"$10–$30"` |
| `servesCuisine` | restaurants only | |
| `sameAs` | recommended | Social profile URLs |
| `hasMap` | optional | Google Maps URL |
| `currenciesAccepted` | optional | ISO 4217 codes |
| `paymentAccepted` | optional | Text |
| `areaServed` | optional if delivery-only | |

### `PostalAddress`

```json
{
  "@type": "PostalAddress",
  "streetAddress": "123 Main Street",
  "addressLocality": "Kyiv",
  "addressRegion": "Kyiv Oblast",
  "postalCode": "01001",
  "addressCountry": "UA"
}
```

### `OpeningHoursSpecification`

```json
{
  "@type": "OpeningHoursSpecification",
  "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
  "opens": "09:00",
  "closes": "18:00"
}
```

One entry per distinct hours block (weekdays vs Saturday vs closed Sunday = 2 entries).

## ACF mapping

Field group: **Local Business Schema** — location: Options Page (site-wide) OR Post Type == `location` for multi-location sites.

| Schema property | ACF field | Type |
|---|---|---|
| `@type` (subtype) | `business_type` | select (list of subtypes) |
| `name` | `business_name` | text |
| `image` | `business_photos` | gallery |
| `telephone` | `business_phone` | text |
| `priceRange` | `business_price_range` | select (`$`, `$$`, `$$$`, `$$$$`) |
| `address.streetAddress` | `business_street` | text |
| `address.addressLocality` | `business_city` | text |
| `address.addressRegion` | `business_region` | text |
| `address.postalCode` | `business_postal_code` | text |
| `address.addressCountry` | `business_country` | text (ISO code) |
| `geo.latitude` | `business_lat` | number |
| `geo.longitude` | `business_lng` | number |
| `openingHoursSpecification` | `business_hours` | repeater → `days` (checkbox), `opens` (time), `closes` (time), `closed` (true/false) |
| `sameAs` | `business_social_profiles` | repeater → `url` |
| `hasMap` | `business_google_maps_url` | url |
| `servesCuisine` | `business_cuisine` (if restaurant) | text |

## PHP template — `/inc/schema/localbusiness-schema.php`

```php
<?php
/**
 * LocalBusiness schema (JSON-LD). Site-wide values from ACF Options Page,
 * or per-location ACF group on a `location` CPT.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$source    = is_singular( 'location' ) ? get_the_ID() : 'option';

$type      = get_field( 'business_type', $source )         ?: 'LocalBusiness';
$name      = get_field( 'business_name', $source )         ?: get_bloginfo( 'name' );
$phone     = get_field( 'business_phone', $source );
$range     = get_field( 'business_price_range', $source );
$street    = get_field( 'business_street', $source );
$city      = get_field( 'business_city', $source );
$region    = get_field( 'business_region', $source );
$postal    = get_field( 'business_postal_code', $source );
$country   = get_field( 'business_country', $source );
$lat       = get_field( 'business_lat', $source );
$lng       = get_field( 'business_lng', $source );
$hours     = get_field( 'business_hours', $source );
$socials   = get_field( 'business_social_profiles', $source );
$map_url   = get_field( 'business_google_maps_url', $source );
$cuisine   = get_field( 'business_cuisine', $source );
$photos    = get_field( 'business_photos', $source );

$images = [];
if ( is_array( $photos ) ) {
    foreach ( $photos as $img ) {
        if ( ! empty( $img['url'] ) ) { $images[] = esc_url( $img['url'] ); }
    }
}

$url = $source === 'option' ? home_url( '/' ) : get_permalink( $source );
$id  = $source === 'option' ? home_url( '/#organization' ) : get_permalink( $source ) . '#localbusiness';

$schema = [
    '@context' => 'https://schema.org',
    '@type'    => $type,
    '@id'      => $id,
    'name'     => $name,
    'url'      => $url,
];

if ( $images ) { $schema['image'] = count( $images ) === 1 ? $images[0] : $images; }
if ( $phone )  { $schema['telephone'] = $phone; }
if ( $range )  { $schema['priceRange'] = $range; }
if ( $cuisine && str_contains( $type, 'Restaurant' ) ) { $schema['servesCuisine'] = $cuisine; }

if ( $street || $city ) {
    $schema['address'] = array_filter( [
        '@type'           => 'PostalAddress',
        'streetAddress'   => $street ?: null,
        'addressLocality' => $city ?: null,
        'addressRegion'   => $region ?: null,
        'postalCode'      => $postal ?: null,
        'addressCountry'  => $country ? strtoupper( $country ) : null,
    ] );
}

if ( $lat !== false && $lng !== false && $lat !== '' && $lng !== '' && $lat !== null && $lng !== null ) {
    $schema['geo'] = [
        '@type'     => 'GeoCoordinates',
        'latitude'  => (float) $lat,
        'longitude' => (float) $lng,
    ];
}

if ( is_array( $hours ) && $hours ) {
    $hours_out = [];
    foreach ( $hours as $row ) {
        if ( ! empty( $row['closed'] ) ) { continue; }
        $days = $row['days'] ?? [];
        if ( ! $days ) { continue; }
        $hours_out[] = [
            '@type'     => 'OpeningHoursSpecification',
            'dayOfWeek' => $days,
            'opens'     => $row['opens']  ?? null,
            'closes'    => $row['closes'] ?? null,
        ];
    }
    if ( $hours_out ) { $schema['openingHoursSpecification'] = $hours_out; }
}

if ( is_array( $socials ) && $socials ) {
    $schema['sameAs'] = array_values( array_filter( array_map(
        fn( $row ) => esc_url_raw( $row['url'] ?? '' ),
        $socials
    ) ) );
}

if ( $map_url ) { $schema['hasMap'] = esc_url_raw( $map_url ); }

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_front_page() || is_singular( 'location' ) ) {
        include get_template_directory() . '/inc/schema/localbusiness-schema.php';
    }
}, 20 );
```

## Gotchas

- **Single-location site:** emit `LocalBusiness` on the homepage instead of `Organization` — it inherits from Organization, so you get both entity signals.
- **Multi-location site:** emit one `LocalBusiness` per location page, each with its own address and hours. The homepage can still emit `Organization` for the brand.
- Phone format: include country code with `+`. `555-0123` is parsed as ambiguous.
- Hours: use 24-hour format (`09:00`, `17:30`) — not `9 AM`.
- `priceRange` must be either `$`/`$$`/`$$$`/`$$$$` OR a range like `"$10–$30"` (use em dash or hyphen consistently).
- Photos: at least one exterior shot helps Google populate the knowledge panel.
- Do NOT emit both `Organization` AND `LocalBusiness` with the same `@id` — `LocalBusiness` IS an `Organization`. Pick one based on whether it's a physical business.
- Google verifies local listings against Google Business Profile — keep name, address, phone (NAP) identical across schema, GBP, and visible page content.
