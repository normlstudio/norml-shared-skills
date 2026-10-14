# Archive hero block

> The H1 + intro band at the top of an archive page (blog, case studies, resources). Distinct from the homepage [hero](hero.md) — no primary CTA, no big visual, focus is on orientation.

## Purpose

Tell the visitor what this archive is and why it exists. One sentence of "Industry insights that matter" beats nothing; two paragraphs of marketing copy is too much.

## Required elements

- **H1** — archive title ("Blog" / "Resources" / "Insights" / "Case studies")
- **Intro paragraph** — 1–2 sentences

## Optional elements

- Background image (full-width hero treatment, with text overlay) — the editorial example uses one
- Background color (tinted band, no image)
- Secondary line: short stat ("47 articles" / "Updated weekly")
- Primary CTA — only when there's a real conversion goal at the archive level (e.g., "Subscribe to our newsletter") — usually defer to bottom newsletter block

## Gutenberg + ACF default (primary)

**Block name:** `acf/archive-hero`
**ACF field group:** `Archive hero`

Fields:
- `h1` — text, required (localizable via Polylang/WPML)
- `intro` — textarea, optional
- `background_image` — image, optional
- `background_color` — color picker, optional
- `style` — radio: `image-overlay | tinted-band | plain`, default `tinted-band`
- `overlay_opacity` — range 0–100, conditional on `image-overlay`, default 40
- `text_color` — radio: `light | dark | auto`, default `auto`

Used inside the archive page template; the H1 and intro are set per-archive in the page's ACF fields rather than per-block.

**Blade template:** `resources/views/blocks/archive-hero.blade.php`

## Elementor fallback

Use Elementor's standard hero (Heading + Text Editor inside a Container with background image and overlay). Set H1 tag explicitly.

## Variations

- **Image overlay** — full-width photo + dark gradient + centered white text (the editorial example)
- **Tinted band** — solid color band, no image, dark or light text
- **Plain** — just H1 + intro, no background treatment
- **Stat strip** — adds a numeric stat below the intro ("48 articles published, 12K monthly readers")
- **Category-specific hero** — when archive is filtered (e.g., `/blog/category/{slug}/`), H1 = category name, intro = category description

## Used on

- Blog archive (default)
- Category archives (with category-name H1)
- Resource library / knowledge base
- Case studies index
- News / announcements archive
- Author archive (with author name + bio as intro)

## Don'ts

- Don't omit the H1 — every archive needs an H1, missing it is an SEO own-goal
- Don't write the intro as a marketing pitch ("Discover transformative insights…") — it's an archive header, not a landing page
- Don't put a primary CTA in the archive hero — readers came to browse content, not convert
- Don't use a 4000px hero image without a `srcset` — performance fail
- Don't auto-rotate hero images — visitors who come back want consistency
- Don't put filter UI inside the hero — keep [category-pills](category-pills.md) below the hero as a separate section
- Don't make the hero so tall that the post grid is below the fold on a 1080p screen — 240–360px desktop is the sweet spot
