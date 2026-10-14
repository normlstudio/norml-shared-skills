# Featured post block

> Large card highlighting one hand-picked or auto-latest post at the top of the blog archive. Magazine-layout signature element.

## Purpose

Give the editor an editorial slot — the "if you read one thing, read this." Above the regular post grid. Configured globally (in Theme Options) so the same Featured Post can drive traffic across the site; can be overridden per archive page if needed.

## Required elements

- **Large featured image** — wide aspect ratio (16:9 or 2:1)
- **Category badge** (or "Featured" label)
- **Post title** — H2, linked to the post
- **Excerpt** — 1–2 sentences
- **Read more link** or whole card clickable
- **Meta row** — author, date, read time

## Optional elements

- "Editor's pick" badge — when this is intentionally curated
- Visual treatment that distinguishes it from regular post cards (larger, asymmetric layout, accent border, tinted background)
- Author photo inline with name

## Gutenberg + ACF default (primary)

**Block name:** `acf/featured-post`
**ACF field group:** `Featured post`

Fields (block-level — for per-archive override):
- `mode` — radio: `auto_latest | manual_pick | theme_default`, default `theme_default`
- `manual_post` — post object, conditional on `mode = manual_pick`
- `label` — text, default `"Featured"`
- `layout` — radio: `wide-image-left | wide-image-right | full-bleed-overlay`, default `wide-image-left`

**Theme Options page** (`ACF Options → Site → Blog → Featured post`):
- `enabled` — true_false, default false — master toggle; when false, archive skips the block entirely
- `default_post` — post object, the canonical Featured Post used site-wide unless overridden per archive
- `default_layout` — same options as block-level

**Per-post field** (optional, on the post itself):
- `mark_as_featured` — true_false, default false — used when Theme Options `default_post` is empty and the project wants "most recent post marked as featured" behavior

**Blade template:** `resources/views/blocks/featured-post.blade.php`

Resolution order at render time:
1. If block has `mode = manual_pick` and a post is set → use that
2. Else if block has `mode = auto_latest` → use `wp_get_recent_posts(['posts_per_page' => 1])`
3. Else if Theme Options `enabled` and `default_post` is set → use that
4. Else hide the block

## Elementor fallback

Use Elementor's Posts widget configured to show 1 post, with featured layout style applied. Manually swap to the picked post via Elementor's query filter.

## Variations

- **Wide image left** — image fills left half, text fills right (default)
- **Wide image right** — same, mirrored
- **Full-bleed overlay** — image spans full archive width, title + meta overlaid (high visual impact, less readable)
- **Sticky featured** — same post stays featured indefinitely until editor changes it (default behavior with `default_post` set)
- **Editor's pick + latest** — featured slot + most recent 2 posts in a 3-up row above the regular grid

## Used on

- Blog archive (top of page, above the regular grid) — when the project opts in via Theme Options
- Resource library
- News / announcements archive

## Don'ts

- Don't auto-rotate the featured post — visitors who come back want consistency; editorial choice is the whole point
- Don't ship Featured Post enabled with no `default_post` set — the block will be invisible or render empty
- Don't pull the same post into both Featured AND the regular post grid below — dedupe; exclude the featured post ID from the main query
- Don't make the Featured layout so visually loud that it overshadows the rest of the archive — it's a highlight, not the only thing on the page
- Don't link the Featured Post to a non-canonical URL (preview link, draft ID) — only to the published canonical URL
- Don't enable Featured Post on archives with fewer than 6 total posts — the proportions look ridiculous (featured + 2 grid posts = sparse page)
- Don't hard-code "Featured" as the badge label — let editors localize it via the field, especially on multilingual sites
