# Post card (template part)

> One tile in a post grid. Used inside blog archives, category archives, related-posts, and featured-post layouts. Not a standalone editable block — a template part the query loops render.

## Purpose

Canonical card shape for every post listing on the site. Defines what fields show, in what order, with what styling. Centralizing this avoids divergence between archive cards, related cards, sidebar cards, etc.

## Required elements (per the editorial example reference, May 2026)

- **Featured image** — 16:9 crop, lazy-loaded, `srcset` for retina
- **Category badge(s)** — small pill above title; can show multiple if post has multiple categories
- **Title** — H3 on archives (where card is the primary content), H4 in related/sidebar (where card is secondary), linked to post
- **Meta row** — author · date · read time
- **Whole card clickable** — wrapping `<a>` for accessibility + clickable area

## Optional elements

- **Excerpt** — 1–2 sentences below title (default OFF per the editorial example — kills scannability)
- **Hover state** — subtle elevation, image scale, or accent color (consistent across all cards in the listing)
- **"New" badge** — auto-rendered for posts published in last N days (default: 7)
- **Author photo** — small circular avatar next to name (more editorial)
- **Read time** — auto-calculated from word count (words ÷ 225)

## Gutenberg + ACF default (primary)

Not a standalone ACF block — a Blade template part included by:
- The blog archive Query Loop
- The category archive Query Loop
- The related-posts block
- The featured-post block (in the variant where it shares card layout)
- The home page blog feed strip

**Template part path:** `resources/views/partials/post-card.blade.php`

Parameters passed in via Blade `@include`:
- `$post` — the post object
- `$size` — `large | medium | small` (controls font sizing only, not layout)
- `$show_excerpt` — boolean, default false
- `$show_author_photo` — boolean, default false
- `$tag` — `h3` or `h4` (which heading level for the title)

**Theme Options page** (`ACF Options → Site → Blog → Post card`):
- `card_show_excerpt_default` — true_false, default false
- `card_show_author_photo_default` — true_false, default false
- `card_meta_order` — radio: `author-date-read | date-read-author | category-meta-inline`, default `author-date-read`
- `image_aspect_ratio` — select: `16:9 | 4:3 | 1:1`, default `16:9`
- `new_badge_threshold_days` — number, default 7 (set to 0 to disable)

## Elementor fallback

Elementor's Posts widget with custom layout. Configure to mirror the spec — image top, category badge, title, author + date + read time underneath.

## Variations

- **Large** (archive default) — wide image, H3 title, full meta row, no excerpt
- **Medium** (related / 3-up) — same shape as large but tighter
- **Small** (sidebar / 4-up below the fold) — H4 title, image smaller or top-cropped, no excerpt, no read time
- **Horizontal** — image left, content right (uncommon; used for list-style archives)
- **No-image** — for posts without featured images, drop image entirely rather than show placeholder

## Used on

- Blog archive grid (3-up desktop, 1-up mobile)
- Category archive grid
- Related posts (3–4 cards below post body)
- Featured-post-as-card variant
- Home page blog teaser strip (3 most recent)
- Sidebar "More from this category"
- Search results listing

## Don'ts

- Don't show a stretched or zoom-cropped featured image when the original aspect doesn't fit — define the aspect ratio in CSS, let `object-fit: cover` handle the crop
- Don't show 4 lines of excerpt + 6 metadata fields per card — readers scan; trim
- Don't make the read-time field manual; auto-calculate
- Don't show the category badge linked to the category archive on every card — Google's been known to flag this as "internal link spam" when 20 cards on a page each contain a category link
- Don't put cards in equal-height rows when titles vary wildly — use `display: flex; flex-direction: column; justify-content: space-between` to keep meta rows aligned at the bottom
- Don't link only the image OR only the title — the whole card should be clickable (or use proper `<a>` wrapping with redundant text inside)
- Don't ship a card with placeholder lorem ipsum — if a post is missing fields, show real fallbacks (default brand image, "Unknown date") or hide the card
