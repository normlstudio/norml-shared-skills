# Service category page

> Filtered subset of the [service listing](service-listing.md) — `/services/{category}/` or similar. Groups services under a theme (e.g., "Design services" / "Engineering services").

> **Source note:** the canonical SEO doc tab is empty as of 2026-05-22. Spec inferred from common patterns + [service-listing](service-listing.md).

## Purpose

Help visitors browsing for a category-level need. SEO: category-level pages can rank for broader terms ("design services," "SEO consulting") that compete at higher volume than individual service pages.

## Required structural elements (top → bottom)

1. **Header**
2. **[Breadcrumb](../blocks/breadcrumb.md)** — `Home > Services > {Category}`
3. **Category hero** — H1 = category name + intro paragraph specific to this category
4. **Service grid** — services in this category, [service-listing](service-listing.md) card shape
5. **Category SEO text** — 200–400 unique words below the grid (helps rank for category-level terms)
6. **Related categories** — links to sibling categories, 3–5 items
7. **Final [CTA](../blocks/cta.md)**
8. **Footer**

## Recommended (situational) blocks

- **Sub-category cards** — if the category has children
- **[Process overview](../blocks/process-steps.md)** — common framework applied across all services in this category
- **Category-specific testimonial** — proof from a client who used services in this category

## Common variations

- **Flat** — no sub-categories, simple grid + body
- **Parent with sub-categories** — sub-category cards above grid
- **Editorial** — heavy on guide content, services lower

## SEO / schema notes

- Unique H1 per category — never reuse the main service-listing H1
- Unique meta description per category
- Schema: `CollectionPage` with `mainEntity` → `ItemList` of services
- Don't `noindex` category pages
- Avoid thin pages: <3 services + no descriptive copy = low quality signal

## Common page-level ACF fields (on the category taxonomy term)

- `category_h1` — text
- `category_intro` — wysiwyg
- `category_seo_text` — wysiwyg (200–400 words below grid)
- `category_image` — image (used in parent-listing sub-category cards)
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't reuse the generic services intro
- Don't ship a category with 1 service in it
- Don't auto-generate category descriptions
- Don't link to category pages with no services
