# Delivery info block

> Shipping / delivery information on a product page. Estimated delivery time, shipping cost or free-shipping threshold, available shipping options, optional zip-code checker.

## Purpose

Answer "when will I get it?" and "how much will shipping cost?" before the buyer clicks add-to-cart. Removes the most common pre-purchase friction.

## Required elements

- **Estimated delivery window** — "Ships in 2–3 business days, delivered in 5–7"
- **Shipping cost summary** — "Free shipping over $50" or flat cost line
- **Shipping options list** — Standard / Express / Overnight, with prices and ETAs

## Optional elements

- **Zip / postal code checker** — input field that returns specific ETA for the buyer's location
- **International shipping callout** — "Ships to 40+ countries" with link to full list
- **Track-your-order** info — post-purchase, but sometimes hinted pre-purchase
- **Cut-off time** — "Order in the next X hours for same-day dispatch" — only if real
- **Carrier badges** — UPS / FedEx / DHL logos

## Gutenberg + ACF default (primary)

**Block name:** `acf/delivery-info`
**ACF field group:** `Delivery info`

Fields:
- `heading` — text, default `"Delivery"`
- `default_estimate` — text (e.g., `"5–7 business days"`)
- `free_shipping_threshold` — number, optional (currency-aware; blank disables the line)
- `free_shipping_label` — text, default `"Free shipping over {currency}{threshold}"`
- `shipping_options` — repeater (label, eta, cost)
- `enable_zip_checker` — true_false, default false
- `zip_checker_endpoint` — URL, conditional (API that returns ETA per zip)
- `international_shipping` — true_false, default false
- `international_destinations_count` — number, conditional (renders as "ships to N countries")
- `cut_off_time` — text, optional (e.g., `"Order by 2 PM EST for same-day dispatch"`)

**Theme Options:**
- `default_shipping_options` — same repeater (used as block-level default)
- `default_free_shipping_threshold` — number

**Blade template:** `resources/views/blocks/delivery-info.blade.php`

## Elementor fallback

Elementor's Icon List widget for shipping options. Manually-added Custom Field widget for ETA logic.

## Variations

- **Inline section** — sits inside product page body
- **Accordion item** — collapsed under "Shipping & Delivery"
- **Trust-strip icon** — small icon + tooltip
- **With zip checker** — input + API-driven ETA
- **Cart-page summary** — different shape: shows shipping cost based on cart contents

## Used on

- [Product](../pages/product.md) — trust strip
- Cart page
- Checkout — full shipping picker
- FAQ / shipping policy pages (link target)

## Don'ts

- Don't ship vague estimates ("usually a few days") — give a real window
- Don't promise "free shipping" without surfacing the threshold
- Don't show carrier logos if the carrier isn't actually used
- Don't auto-detect location via IP for delivery estimates without consent (privacy + accuracy issues)
- Don't update ETA every page load with fake "high-demand" urgency
- Don't hide international shipping if it's available — surface it; it converts global buyers
