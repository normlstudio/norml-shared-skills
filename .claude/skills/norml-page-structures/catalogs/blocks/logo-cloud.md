# Logo cloud block

> Trust strip — row of client / partner / "as seen in" logos.

## Purpose

Prove credibility in 1 second. The visitor doesn't have to read anything — they see logos they recognize and trust transfers.

## Required elements

- **Section label** — short framing line ("Trusted by" / "Our clients" / "As featured in")
- **Logo grid / strip** — minimum 4, ideally 6–12 logos
- Each logo: image (SVG preferred), name (for alt text)

## Optional elements

- Section heading (H2) above the label — when the block is a standalone "Our clients" section, not just a strip
- Per-logo link to case study or external mention
- Marquee animation (scrolling row, only when there are 10+ logos)
- Background variation (alt color band)

## Gutenberg + ACF default (primary)

**Block name:** `acf/logo-cloud`
**ACF field group:** `Logo Cloud`

Fields:
- `label` — text, required (default: "Trusted by")
- `heading` — text, optional (only used when block is a standalone section)
- `logos` — repeater, min 4:
  - `logo` — image, required (SVG preferred, transparent background)
  - `name` — text, required (used for alt text and tooltip)
  - `link` — link, optional
- `layout` — radio: `grid | strip | marquee` (default: `strip`)
- `grayscale` — toggle: render logos in grayscale with hover-to-color (default: on, looks more cohesive than mixed-color logos)
- `background` — radio: `default | alt | dark` (uses project tokens)

**Blade template:** `resources/views/blocks/logo-cloud.blade.php`

## Elementor fallback

Use Elementor's Image Gallery widget OR multiple Image widgets in a multi-column section. For marquee, use the Image Carousel widget with autoplay + infinite loop.

## Variations

- **Inline trust strip** — slim row under hero, no heading, just "Trusted by" + 5–6 logos
- **Standalone clients section** — H2 + grid of 8–12 logos, separates services and testimonials
- **Marquee** — scrolling row, useful when you have 15+ logos and grid would feel cramped
- **Logo + quote combo** — logo with a one-line quote underneath; bridge between logo cloud and testimonials

## Used on

Home (almost always, as trust strip), service (for service-specific clients), about (in "our clients" or "partners" section), case study index, landing pages.

## Logo hygiene

- **SVG > PNG** — sharper, smaller, color-controllable
- **Transparent background** — never logos with their own colored block behind them
- **Consistent size** — pad shorter logos so visual height feels equal
- **Grayscale by default** — color logos with wildly different palettes look chaotic; grayscale unifies, hover-to-color rewards interaction
- **Same row count on mobile** — collapse 6-column grid to 2 columns (3 rows), not 1 column (6 rows)

## Don'ts

- Don't include logos of companies you haven't actually worked with (legal + reputational risk)
- Don't include logos so faintly-related that they raise eyebrows ("we used their API once" doesn't count)
- Don't auto-rotate marquee at jarring speeds — slow scroll, pause-on-hover
- Don't size logos at random — pad them to a consistent visual weight
- Don't include sub-brands of one parent logo (counts as one trust signal, looks like padding)
- Don't repeat the same logo cloud 3 times on one page
