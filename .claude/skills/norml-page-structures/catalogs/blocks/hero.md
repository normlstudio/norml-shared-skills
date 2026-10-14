# Hero block

> The first section the visitor sees. Headline + value prop + one clear action.

## Purpose

Hook the visitor in 1 second. Answer "what is this and why should I care." Give one obvious next step.

## Required elements

- **Headline** — H1 on home / landing / top-of-funnel pages; H1 on case-study and post pages too. Only one H1 per page.
- **Dek / sub-headline** — one supporting sentence
- **Primary CTA** — button with URL + label
- **Visual** — image, video, illustration, or styled background

## Optional elements

- Eyebrow / pre-heading tag (e.g., "Marketing services")
- Secondary CTA (lower-emphasis link or ghost button)
- Trust strip directly under CTA (logo cloud, stat, badge, review snippet)
- Breadcrumb (for inner pages)

## Gutenberg + ACF default (primary)

**Block name:** `acf/hero`
**ACF field group:** `Hero`

Fields:
- `eyebrow` — text, optional
- `headline` — text, required
- `dek` — textarea, optional
- `primary_cta` — link, required (URL + label + new tab toggle)
- `secondary_cta` — link, optional
- `media_type` — radio: `image | video | none`
- `media_image` — image (shown when media_type = image)
- `media_video_url` — url (shown when media_type = video)
- `layout` — radio: `image-right | image-left | image-bg | centered` (default: `image-right`)

**Blade template:** `resources/views/blocks/hero.blade.php`

## Elementor fallback (site already on Elementor)

Use Elementor's built-in Heading + Text Editor + Button widgets in a 2-column Section. Add an Image widget for media. Save as a Global Widget so edits propagate.

## Variations

- **Marketing landing hero** — large headline, big visual, single bold CTA, no breadcrumb
- **Inner page hero** — smaller headline, no media or simple background, breadcrumb + dek
- **Blog post hero** — title + meta row (author / date / read time) + featured image, no CTA
- **Case study hero** — client name + outcome line + project visual, breadcrumb back to portfolio

## Used on

Home, service, landing, case study, blog post (variant), about, most top-level pages.

## Don'ts

- Don't put two H1s on a page (e.g., one in nav, one in hero)
- Don't have a hero without a CTA on a money page (home, landing, service)
- Don't use a carousel — accessibility, analytics, conversion all suffer
- Don't use auto-playing video with sound
- Don't use generic stock photos of smiling teams — kills credibility on sites using this catalog
