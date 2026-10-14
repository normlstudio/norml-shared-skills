# Case-study-card block

> One anonymized client story rendered as a card: industry label + challenge / approach / outcome prose + a metric strip (1–4 emphasized numbers).

## Purpose

The atomic unit of any proof / comparison / results page. Reused on the homepage as a "selected results" strip and on individual service pages as inline proof. ONE block, many instances per page, never bespoke per-card markup.

## Required elements

- **Industry + stage label** (e.g., "B2B SaaS — Series A," "Manufacturing — Industrial Equipment") — pill / eyebrow at top of card
- **Anonymization note** (italic, one line, optional) — e.g., "Certain details are anonymized for confidentiality but the findings and conclusions remain valid"
- **Challenge** (prose, ~1–2 sentences)
- **What was done** (prose, ~1–2 sentences) — often paired with a duration label ("30-day Marketing Alignment Audit")
- **Key findings** (prose, ~1–2 sentences) — what the diagnostic surfaced
- **Outcome** (prose, ~1–2 sentences) — the narrative result
- **Metric strip** — repeater of 1–4 items, each: `label` (e.g., "Lead quality") + `value` (e.g., "+32%"). Rendered mono-tabular, emphasized.

## Optional elements

- Duration chip (e.g., "30 days") — small pill near the industry label
- Closing summary line (optional second outcome sentence in lighter ink)

## Gutenberg + ACF default (primary)

**Block name:** `acf/case-study-card`
**ACF field group key:** `group_case_study_card_block`
**ACF field group title:** `Block: Case study card`

Fields:
- `industry_label` — text, required (e.g., "B2B SaaS — Series A Stage")
- `duration_label` — text, optional (e.g., "30-day Marketing Alignment Audit") — rendered as a small mono chip near the industry label
- `anonymization_note` — text, optional (italic line under the title)
- `challenge` — textarea, required
- `what_was_done` — textarea, required
- `key_findings` — textarea, required
- `outcome` — textarea, required
- `metrics` — repeater, min 1 max 4:
  - `label` — text, required (e.g., "Lead quality")
  - `value` — text, required (e.g., "+32%", "81%")

**Blade template:** `resources/views/blocks/case-study-card.blade.php` (or `resources/views/sections/case-study-card.blade.php` — match the host theme's existing convention for ACF block render callbacks)
**Layer-3 CSS:** `resources/css/blocks/case-study-card.css` (layout only — composes Layer-2 `.surface-tile`, `.eyebrow`, `.block-title`, `.section-container`, `.tnum`, `.mono`; no hex literals, no font overrides)

## Variations

- **1-metric strip** — single hero number; for cards where one outcome dominates
- **2-metric strip** — paired numbers; for compact card grids
- **3-metric strip** — default for proof pages (B2B SaaS card in the Tom Opp comparison)
- **4-metric strip** — wider card or 2-up grid only; metric strip wraps onto 2 rows at desktop, 1-per-row at mobile (Manufacturing card)
- **With anonymization note** — adds italic line under the title (default in Tom Opp)
- **Without anonymization note** — for named clients; omit the field
- **Horizontal (default)** — metric strip is a row at the bottom of the card
- **Stacked (mobile)** — metric strip stacks one-per-row at <640px

## Used on

- Case studies / comparison / proof page (this is the primary use)
- Homepage — selected-results strip (1–3 instances, often with shorter prose)
- Service pages — inline proof (1 instance per service)

## Don'ts

- **Don't put metrics inline in prose.** They live in the metric strip, period. The prose mentions outcomes narratively ("improved revenue predictability"); the strip carries the numbers.
- **Don't render the card with bespoke CSS.** All visual primitives come from Layer 2 — `.surface-tile`, `.eyebrow`, `.block-title`, `.tnum`, `.mono`. Layer-3 file is grid-and-gap only.
- **Don't allow more than 4 metrics.** If a client genuinely has 5+ outcomes, pick the 4 strongest. More than 4 dilutes the strip visually and breaks the wrap.
- **Don't bold the value AND color it accent.** Pick one emphasis lane: the value is `.tnum` mono in `--color-ink` at large size; if accent color is used, drop the weight increase.
- **Don't write the industry label as a sentence.** It's an eyebrow / chip — `INDUSTRY — STAGE` in mono caps. Not "Our B2B SaaS client was a fast-growing…"
- **Don't show the metric strip without labels.** "+32%" alone is meaningless; "Lead quality +32%" sells.
- **Don't reuse the same metric label across cards in a page** without a reason. If two cards both show "Lead quality +32% / +29%," consider merging them into one card. If they're genuinely different stories, fine.
- **Don't put a CTA inside the card.** The page's closing CTA carries the conversion. Cards are proof, not buttons.
