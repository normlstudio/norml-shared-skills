# FAQPage Schema

Read [current eligibility guidance](../standards/eligibility.md) first. Field tables
are planning profiles; current provider requirements and verified facts override
old example defaults. Adapt and lint PHP before use; ACF must be available.


For pages that contain a genuine Q&A section. Search appearance is not guaranteed.

Reference: <https://schema.org/FAQPage>  
Google guidance: <https://developers.google.com/search/docs/appearance/structured-data/faqpage>

## Real visible Q&A only

The questions and answers must match visible content. An accessible expandable
answer is valid visible content; do not require every answer to be open initially.
FAQPage remains a vocabulary type, but Google FAQ rich results were retired in
May 2026. Do not promise search accordions or substitute unrelated types.

## Required + recommended fields

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `FAQPage` |
| `@id` | recommended | `{permalink}#faqpage` |
| `mainEntity` | required | Array of `Question` |

Each `Question`:

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Question` |
| `name` | required | The question text |
| `acceptedAnswer` | required | `Answer` object with `text` |

Each `Answer`:

| Field | Required? | Notes |
|---|---|---|
| `@type` | required | `Answer` |
| `text` | required | Plain text or HTML (HTML allowed for links/lists/emphasis) |

## ACF mapping

Field group: **FAQ Schema** — location: Page == faq, or as an attached group on any post/page that uses a FAQ block.

| ACF field | Type |
|---|---|
| `faq_items` | repeater |
| ↳ `question` | text |
| ↳ `answer` | wysiwyg (HTML allowed) |

Alternatively, if the theme uses ACF Flexible Content or Gutenberg blocks, detect the FAQ block(s) and extract Q&A from there.

## PHP template — `/inc/schema/faq-schema.php`

```php
<?php
/**
 * FAQPage schema (JSON-LD).
 * Only emits when ACF `faq_items` has at least one populated row.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

$faqs = get_field( 'faq_items' );
if ( ! is_array( $faqs ) || ! $faqs ) { return; }

$questions = [];
foreach ( $faqs as $row ) {
    $q = trim( $row['question'] ?? '' );
    $a = trim( $row['answer']   ?? '' );
    if ( $q === '' || $a === '' ) { continue; }

    $questions[] = [
        '@type'          => 'Question',
        'name'           => $q,
        'acceptedAnswer' => [
            '@type' => 'Answer',
            'text'  => wp_kses_post( $a ),
        ],
    ];
}

if ( ! $questions ) { return; }

$schema = [
    '@context'   => 'https://schema.org',
    '@type'      => 'FAQPage',
    '@id'        => get_permalink() . '#faqpage',
    'mainEntity' => $questions,
];

echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>';
```

## Hook in `functions.php`

```php
add_action( 'wp_head', function () {
    if ( ( is_singular() || is_page() ) && have_rows_of( 'faq_items' ) ) {
        include get_template_directory() . '/inc/schema/faq-schema.php';
    }
}, 20 );

// Helper:
function have_rows_of( $field ) {
    $v = get_field( $field );
    return is_array( $v ) && count( $v ) > 0;
}
```

## Gotchas

- Each `Question.name` must match the visible question text exactly. Don't reword.
- Answers can contain HTML (links, `<p>`, lists, `<strong>`). Run through `wp_kses_post()` to strip scripts/iframes.
- Max 1 FAQPage block per URL. If the page has multiple FAQ sections, merge them.
- Emit only actual Q&A supported by the page; no universal minimum-question rule.
- Preserve real authored questions without fabricating or capping them for a retired feature.
- Coordinate with the existing article/schema renderer so the same Q&A is not duplicated.
