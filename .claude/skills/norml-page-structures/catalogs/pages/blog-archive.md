# Blog archive

> The blog landing / index page. Lists posts, filterable by category, paginated. Optional editor-curated featured slot at the top.

## Purpose

Help visitors find articles. Showcase the breadth of content. Provide an entry point from the main nav.

## Required structural elements (top → bottom)

1. **Header**
2. **[Archive hero](../blocks/archive-hero.md)** — H1 ("Blog" / "Resources" / "Insights") + short intro paragraph
3. **[Category pills](../blocks/category-pills.md)** — horizontal filter row, current category highlighted
4. **[Featured post](../blocks/featured-post.md)** — large card, **opt-in via Theme Options** (off by default; the project's editor decides per-site)
5. **Post grid** — 6–12 [post cards](../blocks/post-card.md) per page, 2–3 columns desktop, 1 column mobile
6. **Pagination** — numbered page links + prev/next (not "load more" — needs crawlable page links and bookmarkable states)
7. **[Newsletter CTA](../blocks/newsletter-cta.md)** — at bottom, before footer
8. **Footer**

## Required: post card structure

See [post-card.md](../blocks/post-card.md) for the canonical shape. Summary: featured image (16:9) → category badge(s) → title (H3) → meta row (author, date, read time). **No excerpt by default** — the editorial example convention; the title plus category does the work.

## Recommended (situational) blocks

- **[Most popular](../blocks/most-popular.md)** — sidebar or dedicated section showing top-N posts by traffic. **Off by default**; add per project when content team uses it
- **Search bar** — only if content volume justifies it (50+ posts) — **off by default**
- **Topic landing pages** — hand-curated topic pages instead of just category archives (separate page-type, not a block)
- **Tag cloud** — only if tags are actively used; otherwise clutter — usually skip
- **Featured authors** — sidebar / strip surfacing prolific authors — skip unless brand-byline mode is off

## Common variations

- **Magazine layout** — Featured Post + grid below; works for editorial-heavy sites — opt-in via Theme Options
- **Grid-only layout** — equal-weight grid; simpler, fits most cases — **default**
- **List layout** — vertical list with horizontal cards; works for long-form / fewer posts

## SEO / schema notes

- H1 on the archive title — single H1 per page
- Schema: `Blog` with `mainEntityOfPage` (Yoast / RankMath emit automatically when post type is `post`)
- Paginated pages: expose crawlable links and unique page URLs; Google does not use rel="next"/"prev" as an indexing signal
- Category archives get their own H1 (category name) and short description
- Don't `noindex` paginated pages by default (only if duplicate-content issue confirmed)
- `hreflang` per language via Polylang / WPML

## Common page-level ACF fields

- `archive_intro` — paragraph under H1 (also editable via [archive-hero](../blocks/archive-hero.md) block fields)
- `posts_per_page` — number, default 9 (sweet spot — 5 is frustrating, 24 is overwhelming)
- `show_category_filter` — true_false, default true
- `seo_title`, `seo_description` — Yoast / RankMath fields

## Theme Options for archive (project-wide defaults)

Set under `ACF Options → Site → Blog`:

- `featured_post_enabled` — true_false, default false (opt-in per project)
- `featured_default_post` — post object — the canonical Featured Post
- `card_show_excerpt_default` — true_false, default false
- `default_posts_per_page` — number, default 9
- `default_category_filter_enabled` — true_false, default true
- `default_pagination_style` — radio: `numbered | load-more`, default `numbered`

## Decisions locked at framework level (default, project may override)

- **Featured post:** disabled by default; project editor enables in Theme Options and picks the post manually
- **Search bar:** disabled by default; add per project only if content volume justifies it
- **Most popular widget:** disabled by default; opt-in per project
- **Excerpt on card:** off by default (the editorial example convention)
- **Posts per page:** 9 default
- **Pagination:** numbered (not "load more") default
- **Brand-vs-human author byline:** decided per project — ask the editor before scaffolding

## Don'ts

- Don't show post excerpts longer than 2 sentences in cards — kills scannability (default to no excerpt at all)
- Don't auto-rotate the featured post — visitors who come back want consistency
- Don't put the search bar in the hero unless content volume justifies it (>50 posts)
- Don't paginate at 5 posts per page — frustrating; 9–12 is the sweet spot
- Don't have a different layout for category archives unless there's a real reason
- Don't enable Featured Post when there are fewer than 6 published posts — proportions look broken
- Don't show "All" filter as un-selectable when actually all posts are showing — clicking "All" should always reset to unfiltered
