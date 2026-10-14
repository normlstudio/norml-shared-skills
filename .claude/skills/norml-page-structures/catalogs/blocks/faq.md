# FAQ block

> Interactive or static Q&A — last-mile objection handling.

## Purpose

Resolve the questions that hold visitors back from converting. Preserve structured question/answer data for the required FAQ schema; rendering schema is not a promise of search-result treatment.

## Required elements

- **Section heading** (H2) — "Frequently asked questions" or context-specific ("Pricing FAQ" / "Onboarding FAQ")
- **FAQ items** — minimum 3, ideally 5–8, max 12
- Each item: **question** (plain text), **answer** (rich text)
- Visibility follows the selected variant: accordion answers expand; static rows/cards remain visible

## Optional elements

- Section dek
- Category filter (when 10+ FAQs)
- "Didn't find your answer?" CTA at the bottom (→ contact form)
- Search within FAQs (only for a separately approved long collection of 20+ items; not the default 3–12-item block)

## Gutenberg + ACF default (primary)

**Block name:** `acf/faq`
**ACF field group:** `FAQ`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `items` — repeater, min 3, max 12 by default; a selected variant may reduce the maximum:
  - `question` — text, required
  - `answer` — wysiwyg, required (allows links, lists, bold)
  - `category` — taxonomy or select, optional
- `default_state` — accordion-only radio: `all-collapsed | first-expanded | all-expanded` (default: `all-collapsed`); single-open behavior cannot use all-expanded
- `cta` — group: `text` + `link`, optional

**Blade template:** `resources/views/blocks/faq.blade.php`

**Schema:** must emit `FAQPage` JSON-LD with each question/answer.

## Elementor fallback

Use Elementor's Accordion widget. Manually add FAQ schema via a Code block on the page (or via the SEO plugin if it supports manual schema).

## Variations

Use [the variant contract](../variant-contract.md). The three concrete prototype
variants below retain their existing IDs. No brand styling is implied.

| ID | Composition and behavior | Desktop → tablet → mobile | Use when / avoid when |
|---|---|---|---|
| `faq.accordion` | One stacked Q&A list; independent expand/collapse | One column throughout | Default for 5–8 mixed-length answers; prefer cards for very short uniform answers; categorize at the upper end |
| `faq.two-column` | Static paired rows: each question left, its own answer right; not two independent FAQ lists or one switching panel | Two cells per row → two → question above its answer | Short answers, wide layout, at most eight items; avoid uneven long answers |
| `faq.grid-cards` | Static cards, each containing its question above its answer | Three columns → two → one | Short, balanced Q&A, ideally 6–9 items; avoid long answers or fewer than three items |

Exact pixel breakpoints come from the project's responsive contract. Preserve
each question/answer pair and its reading order when stacking. The accordion
prototype allows independent open items; a single-open mode is an explicit
documented behavior configuration, not an assumption based on its chevron.

### Prototype content envelope

These are the v0.1.0 source budgets, not universal copy limits. Validate real
content before choosing the variant; do not truncate answers. Record overrides.

| ID | Items | Question budget | Rich-text answer budget | Bottom CTA in prototype |
|---|---|---|---|---|
| `faq.accordion` | 3–12 | 120 characters | 800 characters | Optional |
| `faq.two-column` | 3–8 | 80 characters | 400 characters | Not declared |
| `faq.grid-cards` | 3–9 | 60 characters | 200 characters | Optional |

All three prototypes declare heading (required, 80-character budget) and
subheading (optional, 200-character budget). The catalog's `dek` maps to the
prototype's `subheading`; `cta.text`/`cta.link` map to `cta.label`/`cta.url`.
Keep these aliases explicit rather than creating duplicate fields. Do not add
a CTA to a generated two-column variant without documenting its slot revision.
The generic block's optional CTA remains available to custom implementations.

### Other existing catalog choices

- `faq.answer-panel` — preserves the older “questions left, answer panel right” choice, distinct from static paired rows; panel selection, keyboard behavior and mobile layout require a recorded project decision before implementation
- `faq.categorized` — tabs filter Pricing / Process / Support items; resolve category/filter state and mobile behavior for the project; collections above 12 require an explicit quantity override
- `faq.static-list` — all questions/answers visible in one list; suitable for short FAQs with 3–4 items

These choices are structural descriptions, not verified prototype adapters.

### Implementation evidence and lineage

The variants below are structural contracts. Generator/runtime proof must be obtained on the target implementation.

## Used on

Service, pricing, landing, blog post (end-of-article), product, contact, support pages.

## Don'ts

- Don't bury the FAQ at the bottom of a long page if it's the conversion-critical content — surface it sooner
- Don't write questions like "What are your services?" — write the question the prospect actually asks ("Do you work with B2B SaaS startups?")
- Don't use HTML in question text — only in answers
- Don't have FAQ items that go on for 4 paragraphs — that's a blog post; link to it
- Don't emit FAQ schema for questions that aren't really FAQs (Google penalizes spammy schema)
- Don't have 1 FAQ item — if you can't think of 3, skip the block
