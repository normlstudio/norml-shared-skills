# Testimonials block

> Social proof — quotes from real people, with name, role, company, photo.

## Purpose

Reduce purchase risk. Show that real humans got real value. Match the testimonial to the page's claim (don't put a generic "great team" testimonial on a service page about SEO).

## Required elements

- **Section heading** (H2) — e.g., "What our clients say" / "Why teams choose us"
- **Quote items** — minimum 1, ideally 3–6
- Each item: **quote text** (the testimonial itself), **name**, **role + company**, **photo** (optional but strongly recommended)

## Optional elements

- Section dek
- Star rating per quote (only if collected from a review platform — don't invent stars)
- Company logo per quote (instead of or alongside photo)
- Link to full case study per quote
- Video testimonial (embedded)

## Gutenberg + ACF default (primary)

**Block name:** `acf/testimonials`
**ACF field group:** `Testimonials`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `layout` — radio: `grid-3 | carousel | single-large | quote-strip` (default: `grid-3`)
- `items` — repeater, min 1:
  - `quote` — textarea, required
  - `name` — text, required
  - `role` — text, optional
  - `company` — text, optional
  - `photo` — image, optional
  - `company_logo` — image, optional
  - `rating` — number 1–5, optional (only set if real)
  - `case_study_link` — link, optional (relationship field to case-study post)
  - `video_url` — url, optional

**Blade template:** `resources/views/blocks/testimonials.blade.php`

## Elementor fallback

Use Elementor's Testimonial Carousel widget. Configure with the same fields (quote, name, role, company, photo).

## Variations

- **Grid of 3** — default, balanced for home / service pages
- **Carousel** — for 6+ testimonials when space is tight (rotates on tap/swipe, never auto-rotates on desktop without a pause-on-hover)
- **Single large quote** — one hero-style testimonial for landing pages; quote + photo + name big
- **Quote strip** — slim row of 3 short pull-quotes, no photos; works above CTA bands
- **Video grid** — 3 video testimonials in a row, click-to-play, no autoplay

## Used on

Home, service, case study, landing, about, even contact (small strip above the form).

## Don'ts

- Don't invent or paraphrase testimonials — only real quotes from real people
- Don't auto-rotate carousels on desktop — visitor loses control of reading pace
- Don't use only first names ("John D.") — looks fake; use full name or get explicit permission to anonymize
- Don't put 5-star ratings if you didn't actually collect them
- Don't show a "verified by [platform]" badge if you can't link to the verification
- Don't use stock-photo people as testimonial avatars — credibility-destroying if anyone notices
