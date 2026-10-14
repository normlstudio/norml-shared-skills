# Person Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For author bios, team member pages, public figures. Not a direct rich result, but a strong E-E-A-T signal — Google uses it to associate authors with the content they write.

Reference: <https://schema.org/Person>

## When to use

- Author bio pages (one per author)
- Team / about-us team member cards
- Public figure profiles

Never stack `Person` onto every post — emit it only on the author's own page, and reference the author from `Article` via `author: { "@id": "..." }`.

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Person` |
| `@id` | required for entity linking | `https://site.com/author/slug/#person` |
| `name` | required | Full name |
| `url` | required | Canonical URL of the author page |
| `image` | recommended | Headshot, square, 500×500 minimum |
| `jobTitle` | recommended | |
| `worksFor` | recommended | Reference the `Organization` by `@id` |
| `sameAs` | recommended | Array of social profile URLs (LinkedIn, X, Mastodon, GitHub) |
| `description` | recommended | Short bio |
| `knowsAbout` | recommended | Topics the author writes about (helps topical authority) |
| `alumniOf` | optional | Education |
| `award` | optional | Published awards |

## ACF mapping

Field group: **Person Schema** — location: Post Type == `author` (or a user meta group if using WP author profiles).

| Schema property | ACF field | Type |
|---|---|---|
| `name` | `person_name` | text |
| `jobTitle` | `person_job_title` | text |
| `image` | `person_photo` | image (return array) |
| `description` | `person_bio` | textarea |
| `sameAs` | `person_social_profiles` | repeater → url subfield `url` |
| `knowsAbout` | `person_topics` | repeater → text subfield `topic` |
| `alumniOf` | `person_education` | text |

Fallbacks: `name` → `get_the_title()` or `get_the_author_meta('display_name')`; `url` → `get_permalink()` or `get_author_posts_url( $user_id )`; `image` → Gravatar via `get_avatar_url()`.

## PHP template — `/inc/schema/person-schema.php`

```php
<?php
/**
 * Person schema (JSON-LD) for author bio pages.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$name        = get_field( 'person_name' ) ?: get_the_title();
$job_title   = get_field( 'person_job_title' );
$photo       = get_field( 'person_photo' );
$photo_url   = is_array( $photo ) ? ( $photo['url'] ?? '' ) : '';
$bio         = get_field( 'person_bio' );
$socials     = get_field( 'person_social_profiles' );
$topics      = get_field( 'person_topics' );
$education   = get_field( 'person_education' );
$org_id      = home_url( '/#organization' );

$schema = [
    '@context' => 'https://schema.org',
    '@type'    => 'Person',
    '@id'      => get_permalink() . '#person',
    'name'     => $name,
    'url'      => get_permalink(),
    'worksFor' => [ '@id' => $org_id ],
];

if ( $job_title ) { $schema['jobTitle']    = $job_title; }
if ( $photo_url ) { $schema['image']       = esc_url( $photo_url ); }
if ( $bio )       { $schema['description'] = $bio; }
if ( $education ) { $schema['alumniOf']    = $education; }

if ( is_array( $socials ) && $socials ) {
    $schema['sameAs'] = array_values( array_filter( array_map(
        fn( $row ) => esc_url_raw( $row['url'] ?? '' ),
        $socials
    ) ) );
}

if ( is_array( $topics ) && $topics ) {
    $schema['knowsAbout'] = array_values( array_filter( array_map(
        fn( $row ) => $row['topic'] ?? '',
        $topics
    ) ) );
}

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( is_author() || is_singular( 'team_member' ) ) {
        include get_template_directory() . '/inc/schema/person-schema.php';
    }
}, 20 );
```

## Gotchas

- Do not emit `Person` for every blog post — one per author page only. Reference from `Article.author` by `@id`.
- `sameAs` is the single biggest Knowledge-Graph signal here — always encourage editors to fill it.
- Don't invent social URLs. Missing `sameAs` is better than wrong `sameAs`.
