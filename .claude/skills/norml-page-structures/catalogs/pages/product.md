# Product page (ecommerce single)

> The product detail page. Image gallery + name + price + buy button + everything a buyer needs to decide. The single most important conversion page on an ecom site.

## Purpose

Convert a browser into a buyer. Reduce purchase anxiety with proof, policy, and clarity. Support SEO with structured data so the product surfaces in Google Shopping / rich snippets / AI overviews.

## Required structural elements (top → bottom)

1. **Header** — with cart icon + count
2. **[Breadcrumb](../blocks/breadcrumb.md)** — `Home > Shop > Category > Product Name`
3. **Product hero (two-column)** — [product gallery](../blocks/product-gallery.md) (left) + [product info](../blocks/product-info.md) (right)
4. **Unique description** — 300–800 words of unique, keyword-rich content (H2/H3 headers, bullet lists, paragraphs). Includes materials, dimensions, care instructions, "why buy this"
5. **[Product instructions](../blocks/product-instructions.md)** — step-by-step usage (accordion / tab), safety warnings, maintenance, troubleshooting; optional video tutorial
6. **[Product reviews](../blocks/product-reviews.md)** — aggregate rating + breakdown + 5–10 recent reviews with verified-purchase badges
7. **[FAQ](../blocks/faq.md)** — product-specific questions
8. **Trust strip** — [payment info](../blocks/payment-info.md) + [delivery info](../blocks/delivery-info.md) + [return policy](../blocks/return-policy.md) icons / accordions
9. **[Related products](../blocks/related-products.md)** — 4–8 products in a horizontal carousel
10. **[Newsletter CTA](../blocks/newsletter-cta.md)** — optional, especially for first-time buyers
11. **Footer**

## Required elements inside [Product info](../blocks/product-info.md)

Per SEO doc 4.3.7:
- Product name (H1)
- Price — prominent, with strikethrough on original if discounted, plus savings amount/percentage
- **Buy CTA** — high-contrast, above-the-fold, clear action ("Add to cart" / "Buy now")
- Key specifications
- Real-time stock status badge (In stock / Low stock — Only N left / Out of stock / Pre-order)
- Quantity selector
- Variant selectors (size / color / etc.) where applicable
- Social sharing icons
- "Back in stock" email capture when out of stock — see [back-in-stock.md](../blocks/back-in-stock.md)

## Recommended (situational) blocks

- **Subscribe-and-save** — for consumable products
- **Bundle deals** — "Frequently bought together"
- **Size guide** — modal / accordion for apparel
- **Care instructions** — separate accordion or section
- **Sustainability info** — materials, carbon footprint (for brands where it matters)
- **Live chat / chatbot** — for high-consideration products
- **AR / 360° viewer** — for furniture / appliances / fashion

## Common variations

- **Single-variant product** — no variant selector, simpler info column
- **Multi-variant product** — color swatches + size selector
- **Subscription product** — buy-once vs subscribe-and-save toggle
- **Pre-order product** — different CTA + release date displayed
- **Custom / made-to-order** — CTA → quote form, no immediate buy button

## SEO / schema notes

- H1 on product name (only one)
- Schema: `Product` with `name`, `image`, `description`, `sku`, `brand`, `offers` (Offer with `price`, `priceCurrency`, `availability`, `priceValidUntil`), `aggregateRating`, `review` (Review[])
- Include `Product` schema with `priceCurrency` matching project locale
- `OfferAvailability` enum: `InStock`, `OutOfStock`, `PreOrder`, `Discontinued`
- Breadcrumb schema as always
- `og:type=product`, `og:image` from primary product image, `product:price:amount` + `product:price:currency` open-graph extensions

## Common product-level ACF fields (when not using WooCommerce / EDD)

- `sku` — text
- `price` — number (currency formatted at render)
- `original_price` — number, optional (renders strikethrough)
- `gallery` — gallery field (3–5+ images)
- `key_specs` — repeater (label, value)
- `unique_description` — wysiwyg (the 300–800 word body)
- `instructions` — wysiwyg or repeater (step + image)
- `stock_status` — radio: `in-stock | low-stock | out-of-stock | pre-order | discontinued`
- `stock_count` — number (used for "Only N left" badge when stock_status = low)
- `variants` — repeater (variant type + options + price modifier)
- `delivery_estimate_days` — number
- `return_window_days` — number, default 30
- `faq` — repeater
- `related_products` — relationship to 4–8 products
- `seo_title`, `seo_description`, `og_image`

## When to use WooCommerce vs. custom

- **Use WooCommerce** when the project is a real ecom store with checkout, inventory, taxes, shipping zones
- **Use custom ACF** when the project displays products but checkout happens elsewhere (e.g., the product-catalog example: products listed on WP, sales drive to external dealer flow)
- **Use a third-party headless** (Shopify Buy Button, Snipcart) when the site is content-led but has a small product catalog

## Don'ts

- Don't ship a product page without `Product` schema — losing rich snippets is a measurable conversion / SEO loss
- Don't hide the buy button below the fold — must be above the fold on mobile
- Don't ship a product image gallery without zoom on click — buyers want detail
- Don't fake reviews — Google + Trustpilot detect; brand reputation hits
- Don't combine "Add to cart" with "Add to wishlist" / "Save for later" — primary action stays singular
- Don't auto-add product to cart with one click without a confirm step — feels manipulative
- Don't show the price in one currency on the product page and a different currency at checkout
- Don't ship without payment-method icons in the trust strip — buyers want to know what's accepted before clicking buy
- Don't auto-show modals (size guide, related products) on page load — distracts from the buy decision
- Don't ship a low-stock badge when stock is actually plentiful — false urgency erodes trust
