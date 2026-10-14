# Product listing page (All Products)

> The ecommerce "shop" index. Grid of products, filterable by category / price / attribute. Sometimes equivalent to the home of an ecommerce site.

## Purpose

Help visitors find a product. Show breadth. Surface featured / best-selling / new arrivals. The primary discovery surface for ecommerce.

## Required structural elements (top → bottom)

1. **Header** — site nav with prominent **Cart icon + count**
2. **Page hero / archive header** — H1 ("Shop" / "All products" / "Browse") + 1-sentence intro
3. **Filter / sort bar** — category, price range, attribute (color, size, brand), sort by (popular / price / newest)
4. **Product grid** — 12–24 product cards per page, 3–4 columns desktop, 2 columns mobile
5. **Pagination** — numbered or "load more" (load more more common on ecom)
6. **[Newsletter CTA](../blocks/newsletter-cta.md)** — opt-in
7. **Footer** — full nav + payment-method icons + shipping info + return policy link

## Required: product card structure

Each card in the grid:
- Featured image (square or 4:5, hover swap to second image if available)
- Product name (linked to product page)
- Price (with strikethrough if discounted)
- Optional: rating stars, "New" / "Sale" badge, color swatches, quick-add-to-cart button
- Hover state: alt image OR overlay with quick-shop action

## Recommended (situational) blocks

- **Featured products row** — large editorial picks above the grid
- **Sale banner** — promo strip at the top during sales
- **Category cards** — visual category nav (especially for fashion / lifestyle brands)
- **Best sellers strip** — horizontal scroll of top sellers
- **New arrivals** — same shape, different query

## Common variations

- **Single-category shop** — flat grid, no category filter (e.g., a brand that sells only markers)
- **Multi-category shop** — left sidebar filter, top sort bar
- **Magazine-style shop** — editorial banners + grid mixed, less utilitarian
- **B2B shop** — login-gated prices, request-quote buttons instead of add-to-cart

## SEO / schema notes

- H1 on the archive title
- Schema: `CollectionPage` with `mainEntity` → `ItemList` of products
- Category archives get their own H1 + intro (see [product-category.md](product-category.md))
- Each product card uses `Product` schema (offered at the product page; here, schema is summary-level)
- `hreflang` per language; for ecom, also per-currency / per-region storefront

## Common page-level ACF fields

- `archive_intro` — paragraph under H1
- `featured_products` — relationship to 2–4 products shown in editorial row
- `default_sort` — radio: `popularity | newest | price-asc | price-desc | random`, default `popularity`
- `products_per_page` — number, default 24
- `seo_title`, `seo_description`

## Theme Options (project-wide)

- `default_product_card_style` — radio: `image-top-text-below | overlay | minimal`
- `quick_add_enabled` — true_false, default false
- `show_ratings_on_card` — true_false, default true
- `low_stock_badge_threshold` — number, default 5 (show "Only N left" badge when stock ≤ threshold)

## Don'ts

- Don't paginate at 8 products / page — too many clicks to browse
- Don't show 50+ products on a single page without pagination — kills performance
- Don't auto-load more on scroll without a manual "load more" trigger — accessibility + SEO suffer
- Don't ship with a broken filter — every filter combination must return real results or "no products found" gracefully
- Don't hide the price on commerce sites — B2B may justify request-quote, B2C never
- Don't show out-of-stock products without an "Out of stock" badge
- Don't put a non-clickable category card at the top — every navigation element should lead somewhere
