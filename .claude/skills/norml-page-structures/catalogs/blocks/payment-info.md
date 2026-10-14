# Payment info block

> Icons + label strip showing accepted payment methods. Usually in the product page trust strip and the footer.

## Purpose

Reduce purchase anxiety by signaling what payment methods are accepted before checkout. Builds trust through recognizable card / wallet brand logos.

## Required elements

- **Payment method icons** — SVG logos of accepted methods (Visa, Mastercard, PayPal, Apple Pay, Google Pay, etc.)
- **Section heading** (optional, often skipped) — "We accept"
- **"Secure checkout" badge** — small, with lock icon

## Optional elements

- **Buy-now-pay-later providers** — Affirm, Klarna, Afterpay icons
- **Local payment methods** — IBAN, SEPA, regional wallets
- **Crypto** — only if actually accepted
- **Bank transfer / wire icon** — for B2B

## Gutenberg + ACF default (primary)

**Block name:** `acf/payment-info`
**ACF field group:** `Payment info`

Fields:
- `heading` — text, optional
- `methods` — checkbox group (multi-select):
  - `visa`, `mastercard`, `amex`, `discover`, `paypal`, `apple-pay`, `google-pay`, `shop-pay`, `klarna`, `afterpay`, `affirm`, `crypto`, `bank-transfer`
- `show_secure_badge` — true_false, default true
- `secure_badge_label` — text, default `"Secure checkout"`
- `layout` — radio: `horizontal | grid`, default `horizontal`

**Theme Options** (project-wide default — usually set once, applied everywhere):
- `default_payment_methods` — checkbox group (same options) — sets default for new blocks

**Blade template:** `resources/views/blocks/payment-info.blade.php`

## Elementor fallback

Elementor's Image Carousel or Icon List widget with manually-added payment-method SVGs.

## Variations

- **Horizontal strip** — single row of icons, default
- **Grid** — 4-column grid for 12+ methods
- **Compact footer strip** — small, no heading
- **Trust-strip variant** — combined with "Secure checkout" badge in a single bordered box

## Used on

- [Product](../pages/product.md) — trust strip
- Checkout page
- Footer (canonical — every page)
- Cart page

## Don'ts

- Don't show payment methods you don't actually accept — buyers click through and discover the lie
- Don't use low-res or non-official brand logos — every brand has SVG / vector assets available
- Don't make the icons gigantic — they're trust signals, not branding; small/compact reads better
- Don't put the icons inside a colored band that clashes with brand identity — neutral background
- Don't ship without `Secure checkout` if the site actually has SSL — small thing, big trust lift
- Don't show 20 methods to look impressive — pick the actually-used 4–6
