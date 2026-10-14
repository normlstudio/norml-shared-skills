# Related products block

> Horizontal carousel or grid of 4–8 products related to the current product. "You may also like" / "Frequently bought together" / "Customers also viewed."

## Purpose

Cross-sell. Surface complementary or alternative products. Standard ecom convention — buyers expect it.

## Required elements

- **Heading** — "You may also like" / "Related products" / "Customers also bought"
- **4–8 product cards** in a horizontal scrollable row OR a 4-column grid
- Each card uses the same product-card shape as the [product-listing](../pages/product-listing.md) grid

## Optional elements

- **Filter logic** — same category / same tag / hand-picked / personalized (cookie-based)
- **"Frequently bought together"** — bundles with combined price + add-all-to-cart button
- **Carousel arrows or pagination dots** on horizontal layout

## Gutenberg + ACF default (primary)

**Block name:** `acf/related-products`
**ACF field group:** `Related products`

Fields:
- `heading` — text, default `"You may also like"`
- `mode` — radio: `auto_same_category | auto_same_tag | manual_pick | bundle`, default `auto_same_category`
- `manual_products` — relationship, conditional on `manual_pick`
- `count` — number, default 4, max 8
- `layout` — radio: `carousel | grid`, default `carousel`

**Theme Options:**
- `default_related_mode` — same options
- `default_related_count` — number

**Blade template:** `resources/views/blocks/related-products.blade.php`

## Elementor fallback

Elementor's WooCommerce Upsells / Cross-sells / Related Products widget when on WooCommerce. Else manual Posts widget with product CPT.

## Variations

- **Carousel** — horizontal scroll, arrow controls, snap-scroll
- **Grid** — 4-column static grid
- **Vertical sidebar** — for product pages with sidebar layout
- **Bundle / FBT** — 2–3 products grouped with combined price + bulk-add-to-cart

## Used on

- [Product](../pages/product.md) — canonical
- Cart / pre-checkout pages
- Order confirmation page

## Don'ts

- Don't show the current product in its own related row — exclude current product ID from query
- Don't show out-of-stock products in related — filter by availability
- Don't ship with 10+ related products visible at once — 4–8 is the cognitive limit
- Don't auto-rotate the carousel on a timer — invasive
- Don't link to discontinued products
- Don't mix product cards with non-product items (blog posts, articles) in the same row — different content types confuse expectations
- Don't render Related Products on category / listing pages — they belong on single product pages only
