# Product info block (composite)

> The right-column information panel on a product page: name, price, CTA, variants, quantity, stock status, key specs, share. Sits next to the [product gallery](product-gallery.md).

## Purpose

Make the buy decision in one panel. Everything the buyer needs to commit — name, price, options, action — concentrated in one above-the-fold column.

## Required elements

- **Product name** (H1)
- **Price** — current price, prominent; strikethrough on original if discounted; "Save $X (Y%)" line if discount
- **Variant selectors** (size / color / etc.) — visible swatches preferred for color, dropdown for size
- **Quantity selector** — +/- or input, default 1
- **Buy CTA** — large, high-contrast, single primary action ("Add to cart" / "Buy now")
- **Stock status badge** — In stock (green) / Low stock — Only N left (orange) / Out of stock (red) / Pre-order (blue) / Discontinued
- **Key specifications** — 3–5 bullet rows (material, dimensions, weight, brand)

## Optional elements

- **Short description** — 2–3 sentence summary above the CTA
- **Social share icons** — small row of share targets
- **Wishlist / save button** — secondary action, lower visual weight than buy
- **Sticky CTA on mobile** — fixed bottom bar with price + add-to-cart as user scrolls
- **Subscription toggle** — for consumable products, buy-once vs subscribe
- **Bulk pricing tiers** — table showing quantity-based discounts
- **Affirm / Klarna / Afterpay** — "or 4 payments of $X" line under price
- **Estimated delivery** — "Ships in 2-3 business days"

## Gutenberg + ACF default (primary)

**Block name:** `acf/product-info`
**ACF field group:** `Product info`

Fields (typically on the product CPT, not per-block):
- See full field list in [product.md](../pages/product.md)
- Key fields: `price`, `original_price`, `sku`, `key_specs` repeater, `stock_status`, `stock_count`, `variants` repeater, `short_description`

**Theme Options** (`ACF Options → Site → Product`):
- `cta_label_default` — text, default `"Add to cart"`
- `cta_secondary_label` — text, default `"Buy now"` (renders only when enabled per product)
- `show_wishlist` — true_false, default false
- `show_share_icons` — true_false, default true
- `sticky_mobile_cta` — true_false, default true
- `low_stock_badge_threshold` — number, default 5
- `currency_symbol_position` — radio: `before | after`, default `before`

**Blade template:** `resources/views/blocks/product-info.blade.php`

## Elementor fallback

Elementor WooCommerce product widgets (Product Title, Price, Add to Cart, Short Description, etc.) composed in a column.

## Variations

- **Simple product** — no variants, single CTA
- **Variant product** — color/size selectors, CTA dynamically reflects current selection
- **Subscription product** — buy-once vs subscribe-and-save toggle
- **Made-to-order / quote** — CTA becomes "Request a quote" → form modal
- **B2B / login-gated price** — price hidden until login

## Used on

- [Product](../pages/product.md) — canonical
- Quick-view modal on product listing

## Don'ts

- Don't bury the price below the fold
- Don't show "Add to cart" when stock is 0 — disable + show "Out of stock" + back-in-stock signup
- Don't list 12 specifications in the right column — pick the 3–5 that matter; rest goes in description body
- Don't use a small CTA — the buy button is the most important pixel on the page
- Don't auto-add to cart on color swatch click — clicking a swatch is variant selection, not purchase
- Don't show inconsistent prices across pages (listing card vs detail vs checkout)
- Don't combine 4 secondary buttons (Save, Compare, Share, Print) with the primary buy button — choose one secondary at most
- Don't ship a product info column without `Product` schema emission
