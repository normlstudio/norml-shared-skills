# Most popular block

> Sidebar or dedicated section showing the top-N posts by traffic or hand-picked editor's choice.

## Purpose

Surface high-performing content. Helps new readers find proven content, supports internal linking signal, gives sticky content a longer shelf life.

## Required elements

- **Heading** — "Most popular" / "Most read" / "Trending"
- **3–6 post cards** in compact form (smaller than archive grid cards)
- Each card: title + minimal meta (date or category)

## Optional elements

- **Ranking number** — `1`, `2`, `3` before each title
- **Time scope toggle** — "This week / This month / All time"
- **View count** — small `"3.2K reads"` per item
- **Hand-pick override** — editor can manually pick instead of auto-ranking

## Gutenberg + ACF default (primary)

**Block name:** `acf/most-popular`
**ACF field group:** `Most popular`

Fields:
- `heading` — text, default `"Most popular"`
- `mode` — radio: `auto_by_views | auto_by_comments | manual_pick | most_recent`, default `auto_by_views`
- `manual_posts` — relationship, conditional on `manual_pick`
- `time_scope` — radio: `last_week | last_month | all_time`, default `last_month`
- `count` — number, default 5
- `show_ranking_numbers` — true_false, default true
- `show_view_count` — true_false, default false
- `layout` — radio: `vertical-list | sidebar-card | horizontal-strip`, default `vertical-list`

**Blade template:** `resources/views/blocks/most-popular.blade.php`

Requires a view-counter (track post page views via a small JS + REST endpoint, or use a plugin like WP-PostViews). Without view data, fall back to `auto_by_comments` or `most_recent`.

## Elementor fallback

Elementor's Posts widget configured with a custom WP query ordered by meta_key view-count value.

## Variations

- **Vertical list** — small cards in a column, sidebar default
- **Sidebar card** — bordered block with heading
- **Horizontal strip** — 3-up row above the post grid on the blog archive
- **Numbered list (1–5)** — emphasizes ranking
- **Tabbed (week / month / all time)** — interactive scope switcher

## Used on

- Blog archive (optional, off by default)
- Blog post sidebar (variant — list under TOC)
- Home page blog teaser strip (variant)

## Don'ts

- Don't ship without a real view counter — defaulting to "most recent" makes the block dishonest
- Don't show ranking numbers without real underlying data
- Don't surface 10+ items — readers stop scanning after 5
- Don't auto-rotate items on a timer — visitors who come back want consistency
- Don't show "All time" on a brand-new blog with 3 posts — block looks broken
- Don't track views without a privacy banner in EU
- Don't include the current post in the most-popular list when block sits inside a post's sidebar
