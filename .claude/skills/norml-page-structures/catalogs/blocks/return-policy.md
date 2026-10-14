# Return policy block

> Return window + conditions + refund process on a product page. Usually accordion or icon strip.

## Purpose

Reduce purchase anxiety by surfacing return policy before checkout. A clear, generous return policy is one of the highest-conversion levers on a product page (buyers commit because the downside is bounded).

## Required elements

- **Return window** — "30-day returns" / "60-day returns" with visible badge
- **Conditions** — accepted condition (unopened / unused / original packaging) + non-returnable categories (e.g., final sale, custom orders)
- **Refund method** — original payment method / store credit / exchange
- **Who pays for return shipping** — buyer or brand

## Optional elements

- **"Easy returns" badge** — small icon next to return window for visual emphasis
- **Step-by-step return process** — accordion or numbered list
- **Exchange option** — different from refund
- **Restocking fee disclosure** — when applicable

## Gutenberg + ACF default (primary)

**Block name:** `acf/return-policy`
**ACF field group:** `Return policy`

Fields:
- `heading` — text, default `"Returns & exchanges"`
- `return_window_days` — number, default 30
- `return_window_label` — text, auto-rendered: `"{days}-day returns"`
- `conditions` — wysiwyg (renders as bullet list)
- `refund_method` — radio: `original-payment | store-credit | exchange-only`, default `original-payment`
- `return_shipping_paid_by` — radio: `buyer | brand | conditional`, default `buyer`
- `non_returnable_categories` — text repeater
- `restocking_fee` — number (percentage), optional
- `process_steps` — repeater (step_title, step_body), optional
- `policy_page_url` — URL, link to full policy page

**Theme Options:**
- Defaults for all the above; per-product can override only when policy differs from site-wide

**Blade template:** `resources/views/blocks/return-policy.blade.php`

## Elementor fallback

Elementor's Accordion widget with a "Returns" section.

## Variations

- **Badge + link** — small "30-day returns" badge linking to full policy
- **Accordion item** — collapsed under "Returns"
- **Trust-strip icon** — small icon in the trust strip
- **Inline bullets** — short bulleted list inline in product info column

## Used on

- [Product](../pages/product.md) — trust strip
- Cart / checkout
- Policy / terms pages (link target)

## Don'ts

- Don't bury the return policy 3 clicks deep — surface it on the product page
- Don't write the policy in legalese — plain language wins
- Don't claim "easy returns" if the process has 7 steps
- Don't omit the restocking fee if there is one — disclosure post-purchase erodes trust
- Don't make non-returnable categories surprise the buyer — visible disclaimer is fairer and more legal
- Don't auto-extend return windows during holidays without updating the visible value
- Don't ship without a real link to the full policy page — short summary on product page, full policy on dedicated page
