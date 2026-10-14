# Features block

> 3–4 offerings or value props side-by-side, each with icon / headline / description.

## Purpose

Communicate breadth of offering or value at a glance. Each feature is scannable in 2 seconds; the whole block is digested in 10 seconds.

## Required elements

- **Section heading** (H2) — frames what the features add up to
- **Feature items** — minimum 3, maximum 4 per row (6 max with 2 rows)
- Each item: **icon or small visual**, **item title** (H3), **item description** (1–2 sentences)

## Optional elements

- Section dek under the H2 (one sentence)
- Per-item CTA link ("Learn more →")
- Background variation (alternate color band)
- Section-level CTA below the features grid

## Gutenberg + ACF default (primary)

**Block name:** `acf/features`
**ACF field group:** `Features`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `layout` — radio: `grid-3 | grid-4 | grid-2x2 | grid-2x3` (default: `grid-3`)
- `items` — repeater, min 3, max 6:
  - `icon` — image OR icon-name (from project's icon set)
  - `title` — text, required
  - `description` — textarea, required
  - `link` — link, optional
- `section_cta` — link, optional

**Blade template:** `resources/views/blocks/features.blade.php`

## Elementor fallback

Use Elementor's Icon Box widget inside a multi-column Inner Section. Save the section as a Global Widget if reused.

## Variations

- **Icon-first grid** — small icon + title + description (default, fits most cases)
- **Number-led grid** — replace icon with a large number (01, 02, 03) for process-style features
- **Image-led grid** — replace icon with a square image (for "what's included" or product features)
- **Compact list** — 2 columns, no icons, dense text (for legal / spec pages)

## Used on

Home, service, landing, about ("what we believe"), pricing ("what's included").

## Don'ts

- Don't use 5+ features in one row — drops below scannable
- Don't make every feature description 4 sentences — keep it 1–2
- Don't use random emoji as icons on professional sites — use a real icon set (Lucide, Heroicons, Phosphor, or a custom Norml set)
- Don't have features that contradict each other in style (3 with icons + 1 with a photo = visually broken)
- Don't link to a 404 from "Learn more" — wire up the links before shipping
