# Product instructions block

> Step-by-step usage instructions on a product page. Accordion or tabs. Includes safety warnings, maintenance, troubleshooting, optional video.

## Purpose

Reduce post-purchase support load. Build buyer confidence pre-purchase ("they show me how to use it before I buy"). Surfaces accidentally — search traffic for "how to use {product}" lands here.

## Required elements

- **Section heading** — "How to use" / "Instructions" / "Getting started"
- **Steps** — numbered list or accordion items, ideally with images per step
- Each step: title + body text

## Optional elements

- **Video tutorial** — embedded at top of section
- **Safety warnings** — separate callout box (often with warning icon)
- **Maintenance / care instructions** — separate sub-section
- **Troubleshooting** — Q&A list of common issues
- **Downloadable PDF guide** — when the instructions are long-form

## Gutenberg + ACF default (primary)

**Block name:** `acf/product-instructions`
**ACF field group:** `Product instructions`

Fields:
- `heading` — text, default `"How to use"`
- `format` — radio: `accordion | tabs | numbered-list | steps-with-images`, default `steps-with-images`
- `steps` — repeater (step_title, step_body, step_image, optional)
- `video_url` — URL, optional (embed at top)
- `safety_warnings` — wysiwyg, optional (rendered as callout)
- `maintenance_section` — wysiwyg, optional
- `troubleshooting` — repeater (issue, solution), optional
- `download_pdf_url` — URL, optional

**Blade template:** `resources/views/blocks/product-instructions.blade.php`

## Elementor fallback

Elementor's Accordion widget for steps + Image widget for video + Tabs widget for sections.

## Variations

- **Steps with images** — each step has a small image showing the action
- **Accordion** — collapsed sections, click to expand
- **Tabs** — Instructions / Maintenance / Troubleshooting as tabs
- **Video-first** — embedded video + transcript below
- **Numbered list** — simple ordered list, no accordions

## Used on

- [Product](../pages/product.md) — canonical
- Service page (variant — process steps; use [process-steps](process-steps.md) instead)
- Resource pages (DIY / how-to content)

## Don'ts

- Don't show safety warnings buried in step 5 — surface in a separate callout at the top
- Don't include 30 steps without images — break into smaller chunks or use video
- Don't auto-play instruction videos
- Don't ship instructions with placeholder steps
- Don't embed YouTube without privacy mode (`youtube-nocookie.com` URL)
