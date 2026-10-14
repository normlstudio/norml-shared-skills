# Product category page

> Filtered subset of the [product listing](product-listing.md) — `/shop/{category}/` or `/products/category/{slug}/`. Same shape as the listing, but scoped to one category with category-specific copy and SEO.

> **Source note:** the canonical SEO doc tab for this page type is empty as of 2026-05-22. This spec is derived from common ecommerce patterns + [product-listing](product-listing.md) inheritance. Update when the SEO framework doc is filled in.

## Purpose

Help visitors browse within a focused product set. Important for SEO: category pages typically rank for category-level search terms ("alcohol markers," "running shoes," "wireless headphones") that compete with the product-level pages but at a higher volume.

## Required structural elements (top → bottom)

1. **Header** — with cart icon + count
2. **[Breadcrumb](../blocks/breadcrumb.md)** — `Home > Shop > {Category}`
3. **Category hero** — H1 = category name + intro paragraph specific to this category (NOT a generic shop intro)
4. **Filter / sort bar** — same as [product-listing](product-listing.md), but with current category locked in
5. **Product grid** — products in this category only
6. **Pagination**
7. **Category SEO text** — unique 200–400 word category description below the grid (helps rank for category-level terms)
8. **Related categories strip** — links to 3–5 sibling categories
9. **Footer**

## Recommended (situational) blocks

- **Sub-category cards** — if this category has children, show them as visual cards above the product grid
- **Editor's pick** — featured product within this category
- **Category benefits / "how to choose"** — explainer content for high-consideration categories (e.g., "How to pick the right alcohol marker")
- **Comparison table** — for categories where buyers compare across variants (e.g., the product-catalog example Sketch vs Brush vs Junior)

## Common variations

- **Flat category** — no sub-categories, simple grid
- **Parent category with sub-categories** — sub-category cards above grid
- **Editorial category page** — heavy on guide-style content above the grid; product grid lower

## SEO / schema notes

- Unique H1 per category — never reuse the main shop H1
- Unique meta description per category
- Schema: `CollectionPage` with `mainEntity` → `ItemList` of products in this category
- Don't `noindex` category pages (they typically drive significant organic traffic)
- Avoid thin category pages with 1–2 products + no descriptive copy (Google may treat as low-quality)
- Internal links: from category page to top-N products inside it; from main shop to category pages; from blog posts to relevant category pages

## Common page-level ACF fields (on the category taxonomy term)

- `category_h1` — text, default to category name
- `category_intro` — wysiwyg
- `category_seo_text` — wysiwyg (200–400 word body below grid)
- `category_image` — image (used in parent-shop sub-category cards)
- `featured_product` — relationship, optional
- `subcategory_card_style` — see [product-listing.md](product-listing.md)
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't reuse the generic shop intro as the category intro — every category page needs unique copy
- Don't ship a category page with <3 products and no descriptive content — looks thin to Google and users
- Don't put the SEO text block above the product grid — keep grid above the fold, SEO text below
- Don't auto-generate category descriptions with placeholder text — editor must write real category copy
- Don't link to category pages that don't exist (broken sub-category cards)
- Don't show out-of-stock products in featured-product slots — pick something currently buyable
