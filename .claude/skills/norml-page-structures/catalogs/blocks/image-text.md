# Image + text block

> Split section — visual one side, copy the other. The workhorse "feature highlight" pattern.

## Purpose

Pair a visual with focused copy. Used for: introducing a concept with a screenshot, telling a story with a photo, showing "how it works" with a diagram, contrasting before/after.

## Required elements

- **Image / visual** — photo, illustration, screenshot, diagram, mockup
- **Heading** (H2 or H3) — frames what the visual shows
- **Body copy** — 1–3 short paragraphs supporting the heading
- Layout: image on one side, copy on the other (flip-able)

## Optional elements

- Eyebrow tag above the heading
- Bulleted list under the body (3–5 short bullets)
- CTA link or button under the body
- Stat / metric callout overlaid on the image
- Multiple images (small gallery on the visual side)

## Gutenberg + ACF default (primary)

**Block name:** `acf/image-text`
**ACF field group:** `Image + Text`

Fields:
- `eyebrow` — text, optional
- `heading` — text, required
- `body` — wysiwyg, required
- `bullets` — repeater (`text` per item), optional, max 5
- `cta` — link, optional
- `image` — image, required
- `layout` — radio: `image-left | image-right` (default: `image-right`)
- `image_treatment` — radio: `flat | shadowed | bordered | rounded | overflow-bleed` (default: `rounded`)
- `background` — radio: `default | alt | dark | accent` (uses project tokens)

**Blade template:** `resources/views/blocks/image-text.blade.php`

## Elementor fallback

Use Elementor's Image Box widget OR a 2-column Inner Section with Image + Text Editor + Button widgets. Save as a Global Widget if the layout is reused.

## Variations

- **Standard split** — 50/50 image and copy
- **Asymmetric** — 60/40 or 40/60, drawing attention to one side
- **Stacked alternating** — multiple image-text blocks in a row, alternating image-left / image-right for visual rhythm
- **Video instead of image** — embedded autoplay-muted-loop video on the visual side
- **Stat-overlay variant** — small image with a big stat callout floating over it

## Used on

Home ("how we work" / "what we believe"), service ("the process" / "what's included"), about, case study (between narrative sections), landing pages.

## Visual rhythm rule

When using **multiple** image-text blocks in a row, alternate `image-right` and `image-left` so the eye zig-zags down the page. Three in a row all `image-left` looks monotonous.

## Don'ts

- Don't use a stock-photo handshake / smiling team on the image side
- Don't write 6 paragraphs of body copy — split into multiple blocks if that much is needed
- Don't put the CTA in the middle of the body paragraph — put it under, as a separate action
- Don't use an image so abstract that it adds no information — every visual should reinforce the headline
- Don't have an image that's wider than the copy column on a wide split — it dominates and the copy feels orphaned
- Don't forget the alt text — accessibility AND SEO
