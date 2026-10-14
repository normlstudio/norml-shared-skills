# Related posts block

> 3–4 [post cards](post-card.md) shown after a blog post body. "If you liked this, read this."

## Purpose

Surface adjacent content the reader is likely to want next. Increases time-on-site, reduces bounce, supports internal link equity, gives the editor a curation slot.

## Required elements

- **Heading** — "Related articles" / "Keep reading" / "You might also like"
- **3–4 [post cards](post-card.md)** in a row
- Query strategy: same category > same tag > latest (fallback chain)

## Optional elements

- **Section dek** ("More from the {Category} category")
- **Manual override** — pick 3 specific posts instead of auto-query (editor's curation)
- **Exclude current post** — automatic; never include the post the reader is currently reading
- **"See all posts" link** — at end of row, → `/blog/`

## Gutenberg + ACF default (primary)

**Block name:** `acf/related-posts`
**ACF field group:** `Related posts`

Fields:
- `heading` — text, default `"Related articles"`
- `mode` — radio: `auto_same_category | auto_same_tag | manual_pick | latest`, default `auto_same_category`
- `count` — number, default 3, max 6
- `manual_posts` — relationship field, conditional on `mode = manual_pick`
- `show_see_all_link` — true_false, default false
- `see_all_url` — URL, conditional, default `/blog/`

**Blade template:** `resources/views/blocks/related-posts.blade.php`

Includes `partials/post-card.blade.php` for each result with `$size = 'medium'`.

Query logic:
```
mode = auto_same_category:
  WP_Query: posts in same category as current, exclude current ID, order DESC by date, limit count
  If fewer than {count} results, fall back to latest from any category to fill the row

mode = auto_same_tag:
  WP_Query: posts sharing ≥1 tag with current, exclude current ID
  fallback to latest

mode = manual_pick:
  Render only the picked posts, in order; if a picked post is unpublished, skip it

mode = latest:
  Most recent N posts excluding current
```

## Elementor fallback

Elementor Pro's Posts widget configured to show 3, filtered by current category. Set "Exclude current post" if available; else add it via custom Posts Query filter.

## Variations

- **3-up row** — default
- **4-up row** — for desktop-wide layouts
- **Vertical list** — used in sidebars
- **2-up horizontal** — magazine-style for editorial blogs with bigger cards
- **Manual + auto blend** — first card is a manual editor's pick, next 2 are auto same-category

## Used on

- Blog post (default — every post)
- Long-form service page (variant: "Related services" but same block shape)
- Case study (variant: "More case studies")
- Resource pages

## Don'ts

- Don't show a related-posts block on a post that genuinely has nothing related — if the auto-query returns 0, hide the block, don't pad with unrelated latest posts
- Don't show the same post in the related row that's already on the page (current post) — always exclude current ID
- Don't show 6+ related cards — 3–4 is the sweet spot; more is bottomless content rabbit hole
- Don't auto-rotate the related set every page load — caching breaks; pick once on render
- Don't link to draft / private / scheduled posts — filter by `post_status = 'publish'`
- Don't manually pick a related-posts list for every single post — auto-query handles 95% of cases; manual only when needed
- Don't render related posts above the FAQ or other end-of-article blocks — order should be: body → FAQ → key-takeaways → sources → share-ai → preferred-source → share-social → author-bio → related-posts → newsletter
