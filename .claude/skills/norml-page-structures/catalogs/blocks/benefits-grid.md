# Benefits grid block

> 3–6 outcome-focused benefit cards. Distinct from [features](features.md) — features describe what the product IS, benefits describe what the buyer GETS.

## Purpose

Translate features into reader-relevant outcomes. "We have version control" is a feature; "Never lose a draft again" is a benefit. Benefits convert; features inform.

## Required elements

- **Section heading** (H2) — "Why teams choose us" / "What you'll get" / "The outcomes"
- **3–6 benefit cards** in a grid (3 columns desktop, 1–2 columns mobile)
- Each card: icon + benefit headline + 1–2 sentence body

## Optional elements

- **Section dek** under heading
- **Numerical proof per benefit** — "Save 12 hours/week" / "47% fewer support tickets"
- **Per-card CTA link** — "Learn more →"
- **Per-card visual** instead of icon (small photo / illustration)

## Gutenberg + ACF default (primary)

**Block name:** `acf/benefits-grid`
**ACF field group:** `Benefits grid`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `benefits` — repeater, min 3, max 6:
  - `icon` — image or icon select
  - `headline` — text (outcome-led: starts with verb)
  - `body` — textarea (1–2 sentences)
  - `proof_stat` — text, optional (e.g., `"Save 12 hours/week"`)
  - `link_label` — text, optional
  - `link_url` — URL, optional
- `columns` — radio: `2 | 3 | 4`, default `3`
- `style` — radio: `cards | minimal-with-icons | bordered`, default `cards`

**Blade template:** `resources/views/blocks/benefits-grid.blade.php`

## Elementor fallback

Elementor's Icon Box widget repeated 3–6 times inside a Columns container.

## Variations

- **3-up cards** — most common, balanced
- **4-up minimal** — smaller cards, less body copy
- **2-up large** — wider cards, more body, for fewer-but-deeper benefits
- **With stats** — proof number prominent on each card
- **With illustrations** — replaces icons for more brand-distinct treatment

## Used on

- Home page (often)
- Service page (key conversion lever)
- Service listing
- Landing pages

## Don'ts

- Don't write benefits like features ("Fast hosting" → "Pages that load instantly")
- Don't repeat the same icon across 6 cards
- Don't write a body that contradicts the headline
- Don't include 8 benefits — diminishing returns; pick 3–4
- Don't write generic benefits ("Better business," "Save time and money") — specific outcomes win
- Don't link the card to nowhere — either link properly or skip the link
