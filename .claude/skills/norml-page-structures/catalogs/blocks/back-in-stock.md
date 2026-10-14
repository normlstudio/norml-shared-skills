# Back-in-stock block

> Email-capture form shown when a product is out of stock. "Notify me when available."

## Purpose

Capture demand for out-of-stock items. Send the buyer an email when stock returns. Recovers what would otherwise be lost sales.

## Required elements

- **Headline** — "Out of stock" or "Sold out"
- **Sub-copy** — "Get notified when this is back in stock"
- **Email input** — `type="email"`, required
- **Submit button** — "Notify me" / "Let me know"
- **Consent line** — link to privacy policy

## Optional elements

- **Estimated restock date** — when known
- **Discount incentive** — "Subscribers get 10% off when this is back"
- **Variant-specific** — separate signup per variant (color / size)
- **SMS option** — text-message alert alternative to email

## Gutenberg + ACF default (primary)

**Block name:** `acf/back-in-stock`
**ACF field group:** `Back in stock`

Fields:
- `headline` — text, default `"Out of stock"`
- `subcopy` — text, default `"Get notified when this is back in stock"`
- `button_label` — text, default `"Notify me"`
- `restock_estimate` — text, optional (e.g., `"Expected back: late June"`)
- `incentive_text` — text, optional (e.g., `"Subscribers get 10% off restock"`)
- `enable_sms` — true_false, default false

**Theme Options:**
- `provider` — select: same providers as [newsletter-cta](newsletter-cta.md), plus product-aware tools (Klaviyo, Back-in-Stock plugin, custom webhook)
- `confirmation_message` — wysiwyg, default `"We'll email you when it's back."`

**Blade template:** `resources/views/blocks/back-in-stock.blade.php`

Hidden under normal conditions; rendered only when `stock_status = 'out-of-stock'` on the product.

## Elementor fallback

Elementor's Form widget configured to submit to a webhook that triggers the email/SMS automation.

## Variations

- **Inline replacement** — replaces the "Add to cart" button when out of stock
- **Below CTA** — sits below the disabled "Add to cart" + "Out of stock" badge
- **Modal** — clicking "Notify me" opens a modal with the form
- **Per-variant** — when only one variant is out of stock, this block sits next to that variant selector

## Used on

- [Product](../pages/product.md) — when stock status is out
- Product variant selector (per-variant notification)

## Don'ts

- Don't show "Add to cart" + "Notify me" at the same time — pick one based on stock state
- Don't ship without a real provider hookup — collecting emails that never get an alert is fraud
- Don't promise a restock estimate you can't keep
- Don't auto-subscribe to the newsletter when the buyer signs up for back-in-stock — two different opt-ins
- Don't show the block on a discontinued product — discontinued ≠ out of stock; different messaging
