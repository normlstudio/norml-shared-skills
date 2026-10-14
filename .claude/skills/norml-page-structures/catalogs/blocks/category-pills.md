# Category pills block

> Horizontal row of category filter buttons under the archive hero. "All / Access / AI / Automation / Data / …" — click to filter the archive by category.

## Purpose

Let readers narrow the archive by topic without leaving the page. The default browse UI on a content-heavy site. the editorial example uses this as the primary filter mechanism; tag clouds are rarely justified.

## Required elements

- **"All" pill** — first in row, default selected on the unfiltered archive
- **One pill per category** — limit to top-level categories or hand-picked taxonomy (don't dump every tag)
- Each pill: label (= category name), link (= `/blog/category/{slug}/`), selected state when current
- Horizontal scroll on overflow (mobile especially)

## Optional elements

- Post count per category — `Access (12)` — useful when counts are stable
- Multi-select — let user filter by 2+ categories (requires JS + query-string state)
- "More ▾" overflow dropdown — when categories exceed visible width
- Search input on the right (very rare — usually skip)

## Gutenberg + ACF default (primary)

**Block name:** `acf/category-pills`
**ACF field group:** `Category pills`

Fields:
- `taxonomy_source` — select: `category | post_tag | custom_taxonomy_slug`, default `category`
- `selection_mode` — radio: `all_top_level | hand_picked`, default `all_top_level`
- `picked_terms` — relationship field, conditional on `hand_picked`
- `show_counts` — true_false, default false
- `show_all` — true_false, default true
- `all_label` — text, default `"All"`
- `style` — radio: `pills | tabs | buttons`, default `pills`
- `mobile_behavior` — radio: `horizontal-scroll | dropdown`, default `horizontal-scroll`

**Blade template:** `resources/views/blocks/category-pills.blade.php`

Generates an unstyled HTML list at render time from the configured taxonomy. Active state determined by `is_category()` / `get_queried_object()`. URLs use the standard category permalink structure — no JS routing required.

## Elementor fallback

Elementor doesn't have a native category-pills widget. Either:
- Use a custom HTML widget with a hand-coded pill list (loses dynamic category sourcing)
- Use a third-party Elementor plugin with archive filter capability (e.g., JetSmartFilters)

## Variations

- **Pill style** — rounded full, default
- **Tab style** — rectangular, bottom-border on active — more editorial / magazine
- **Button style** — solid background, more prominent
- **Vertical sidebar list** — instead of horizontal row (uncommon)
- **Two-row** — when there are 10+ categories, split into two rows rather than horizontal scroll
- **With dropdown** — top 5 visible + "More ▾" overflow

## Used on

- Blog archive (default)
- Case studies index (filtered by industry/service)
- Resource library (filtered by type: guide / template / video)
- Portfolio archives

## Don'ts

- Don't show every tag — 6–10 categories is the sweet spot; 20+ becomes noise
- Don't put the active-state pill at the end of the row — keep "All" first; categories follow in stable order
- Don't ship without horizontal scroll on mobile — the row will overflow on small screens
- Don't render counts that include unpublished/drafts
- Don't use JS-only routing if you can avoid it — server-side category URLs are crawlable; JS-only filters aren't
- Don't make "All" toggle off (active-state pill that you click to deselect) — clicking "All" should always show all posts
- Don't auto-scroll the active pill into view on mobile if it causes layout shift — handle CLS carefully
