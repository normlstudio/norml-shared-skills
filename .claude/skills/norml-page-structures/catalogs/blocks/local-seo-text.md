# Local SEO text block

> Long-form, uniquely-written body content that anchors a local page's SEO signal. The single most important block on a local page — without it, the page is templated spam.

## Purpose

Give Google a 400–600-word reason to treat this `(service × city)` page as a unique landing page rather than a duplicate of every other city's page. The block holds the unique-per-page copy: city-specific situations, local landmarks/highways/hospitals/courts referenced naturally, and a city-specific bridge to the firm's value prop.

This block exists **only** on the local-page page-type. It's not reusable on the home, canonical service, blog post, or any other page type.

## Required elements

- **Heading** — typically "{Why choose us for | What to know about | Understanding} {service} in {city}". One line, sentence case or title case per brand voice.
- **Body** — 400–600 words. Unique per page. Must include:
  - At least one location-specific reference (landmark, highway, hospital, neighborhood, courthouse, regional statistic)
  - At least one city-specific scenario for the service ("Miami's high tourist traffic generates a disproportionate share of rental-car injury claims")
  - A natural mention of the city 2–4 times across the body (not stuffed)
  - One internal link back to the canonical service page

## Optional elements

- **Sub-headings** (H3) inside the body — for readability on longer pages
- **Bullet list of common case types / situations** for this city
- **A local statistic** sourced from a public dataset (city population, traffic crash data, court filings) — only if verifiable; don't fabricate numbers
- **A link out to a local resource** (city .gov page, local hospital, regional bar association) — credibility-building but optional

## Gutenberg + ACF default (primary)

**Block name:** `acf/local-seo-text`
**ACF field group:** `Local SEO Text`

Fields:
- `heading` — text, required
- `body` — WYSIWYG, required (tall height in the editor — this field holds the bulk of the page's unique content)
- `internal_link_label` — text, optional (defaults to "Learn more about our {service} →")
- `layout` — radio: `centered | left-aligned | two-column` (default: `left-aligned`, max-width set by design tokens)

**Blade template:** `resources/views/blocks/local-seo-text.blade.php`

The Blade template should:
- Render the heading as `<h2>` (it's a major page-level section heading)
- Render the body inside a `<div class="prose ...">` (or the project's equivalent rich-text wrapper) so the rich-text formatting comes through
- Append the internal link to the canonical service page at the bottom of the body, using the `parent_service` page-level ACF field to resolve the URL (don't hardcode it in this block — the block doesn't know which service this is)

## Elementor fallback (site already on Elementor)

Use Elementor's Heading + Text Editor widgets in a single-column Section. Save as a Reusable Template named `Local SEO Text` so edits propagate. The body content will need to be set per page (it's unique each time) but the structural template can be shared.

## Variations

- **Standard layout** — heading + body, left-aligned, full content width — default for almost every case
- **Centered narrow** — narrower max-width, centered — fits brands with magazine-style typography
- **Two-column with sub-section** — body splits into "Common scenarios in {city}" + "Why choose us" — for longer (600+ word) bodies where readability suffers in one column

## Used on

Local pages only (the `local_service` CPT, per the local-pages workflow). Not on the canonical service page (that page has its own structure). Not on home, blog, or other page types.

## Don'ts

- **Don't reuse the body across pages.** Even with the city name swapped, near-duplicate text gets penalized. The whole point of this block is the unique content.
- **Don't fabricate local references.** If you don't know which is the largest hospital network in the city, use a different anchor (a highway, a neighborhood) you can confirm. Hallucinated landmarks make the page worse, not better.
- **Don't keyword-stuff the body.** 2–4 natural mentions of the city, 2–4 natural mentions of the service. Not 15 each.
- **Don't pad the body to hit a word count.** 400 strong words beats 600 watered-down words. The 400–600 range is a target; never inflate by repeating the same point in different words.
- **Don't link to competitors.** Internal link goes to the firm's canonical service page. External links (if any) go to credibility sources (.gov, .edu, regional bar associations) — never to other law firms or directly competing services.
- **Don't use this block on non-local pages.** If you're tempted to add a `local-seo-text` block to a canonical service page or a blog post, you probably want a `text-content` block instead.
- **Don't write the body in the voice of a different service or city.** This is the most common failure mode in bulk generation — Claude drifts mid-batch and starts writing about car accidents on a personal-injury page, or referencing Miami on the Orlando page. The locked content rubric in `template-decisions.md` is what guards against this.
