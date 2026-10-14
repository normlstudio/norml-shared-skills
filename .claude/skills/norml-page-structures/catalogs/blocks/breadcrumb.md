# Breadcrumb block

> Linked path showing the reader's location in the site hierarchy: `Home / Blog / Category / Post Title`.

## Purpose

Orientation + secondary navigation + SEO signal. Google uses breadcrumbs to display the URL hierarchy in SERPs (via `BreadcrumbList` schema). Readers use them to go up one level.

## Required elements

- **Linked path** — each segment is a link except the current page (last segment is plain text)
- **Separator** — `/`, `>`, or `›`
- **Current page label** (un-linked last segment)
- Emit `BreadcrumbList` schema JSON-LD

## Optional elements

- **Hide on home** — breadcrumb is meaningless when the user is on `/`
- **Truncate long titles** — current page label can be truncated to ~40 chars with ellipsis
- **Back link variant** — single "← Back to {parent}" link instead of full path (the editorial example uses this)
- **Mobile-only collapse** — show only home + current + back-arrow on mobile

## Gutenberg + ACF default (primary)

**Block name:** `acf/breadcrumb`
**ACF field group:** `Breadcrumb` (rarely needs editor-facing fields — usually auto-rendered)

Fields (Theme Options):
- `style` — radio: `full-path | back-link`, default `full-path`
- `separator` — radio: `slash | chevron | arrow`, default `slash`
- `hide_on_home` — true_false, default true
- `home_label` — text, default `"Home"`

**Blade template:** `resources/views/blocks/breadcrumb.blade.php`

Prefer Yoast SEO's `yoast_breadcrumb()` if Yoast is the project's SEO plugin — Yoast handles schema emission and most edge cases (CPT hierarchy, custom taxonomies, paginated archives). Wrap Yoast's output in the block's own markup for styling control.

For non-Yoast projects, build manually:
- Walk `get_the_terms()` for the primary category
- Compose path: `[Home] → [parent CPT archive] → [category] → [current title]`
- Emit `BreadcrumbList` schema with `position` + `name` + `item` (URL) for each non-current step

## Elementor fallback

Elementor Pro's Breadcrumbs widget. Configure separator + home label per spec. Schema is emitted by Yoast (or whatever SEO plugin is installed) — Elementor itself doesn't emit `BreadcrumbList`.

## Variations

- **Full path** — `Home / Blog / Ecosystems / The human side of digital transformation` — default
- **Back link** — `← Back to Blog` — single link, no full path — used by the editorial example, cleaner on long titles
- **Compact mobile** — full path on desktop, back-link variant on mobile
- **No-link last segment** — current page text is not a link (correct semantics)

## Used on

- Every page except home (default)
- Especially important on: blog post, blog archive, case study, service page, product page, resource pages
- Hide on: home, landing pages with no parent, single-page sites

## Don'ts

- Don't link the last segment (current page) — it should be plain text
- Don't ship without `BreadcrumbList` schema — losing the SERP breadcrumb display for no reason
- Don't show breadcrumbs on the home page
- Don't make breadcrumbs look like the main nav — they're secondary; smaller, lighter weight
- Don't render `Home / Page` when the page has no real parent — single-segment breadcrumbs are noise
- Don't include URL parameters or hash fragments in the breadcrumb labels
- Don't translate the home label in the URL but not the visible text — Polylang/WPML projects must localize both
- Don't render a breadcrumb in a hero with a background image without sufficient contrast — accessibility fail
