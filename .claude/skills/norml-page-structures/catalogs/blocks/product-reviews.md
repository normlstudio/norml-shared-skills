# Product reviews block

> Aggregate rating + breakdown + individual review cards on a product page.

## Purpose

Social proof. Buyers trust other buyers more than the brand. Reviews are also one of the most powerful schema signals — `AggregateRating` and `Review` give rich snippets (star rating in SERPs) which lift CTR.

## Required elements

- **Aggregate rating** — `4.7 / 5` with star visual + total review count ("based on 247 reviews")
- **Rating breakdown** — bar chart of 5 / 4 / 3 / 2 / 1 star counts
- **Review cards** — 5–10 most recent reviews with: reviewer name, date, rating, title, body, verified-purchase badge
- **Schema emission** — `AggregateRating` + `Review[]` JSON-LD

## Optional elements

- **"Write a review" CTA** — button that opens a review submission form
- **Filter by rating** — show only 1-star, 5-star, etc.
- **Sort options** — most recent / most helpful / highest / lowest rating
- **"Was this helpful?" voting** per review
- **Review photos** — buyers attach images of the product in use
- **Reply from brand** — owner response to specific reviews
- **Verified-purchase only filter**

## Gutenberg + ACF default (primary)

**Block name:** `acf/product-reviews`
**ACF field group:** `Product reviews`

When using a reviews plugin (Trustpilot, Yotpo, Stamped.io, WooCommerce Reviews):
- `provider` — select: `woocommerce | trustpilot | yotpo | stamped | judgeme | custom`
- `provider_widget_id` — text (provider's embed ID)
- Most reviews data comes from the provider; only display config lives in fields

When using custom ACF (rare):
- `reviews` — repeater (reviewer_name, date, rating, title, body, verified, photos)
- `aggregate_rating` — number, auto-calculated
- `total_reviews` — number, auto-calculated

**Blade template:** `resources/views/blocks/product-reviews.blade.php`

## Elementor fallback

Elementor's WooCommerce Reviews widget (when on WooCommerce). For non-WC sites, embed the reviews provider's widget directly via an HTML widget.

## Variations

- **Inline section** — reviews block sits in the product page body
- **Tabbed** — Description / Reviews / Q&A as tabs
- **Sidebar summary** — aggregate rating in the product info column, full reviews below
- **Verified-only mode** — only show verified-purchase reviews (more trustworthy)

## Used on

- [Product](../pages/product.md) — canonical
- Service page (variant — same shape but for service reviews)

## Don'ts

- Don't fake reviews — Google detects, Trustpilot detects, customers detect
- Don't ship without `AggregateRating` schema — losing the SERP star is a real CTR hit
- Don't only show 5-star reviews — readers know real products get mixed reviews; transparency wins trust
- Don't moderate reviews invisibly (hiding negatives) — let buyers reply or address; deletion erodes trust
- Don't show "0 reviews" loudly — hide the block or use a soft "Be the first to review" CTA
- Don't show review submission without spam protection (reCAPTCHA, honeypot, rate limit)
- Don't paginate reviews into many small pages — show 5–10, then "Load more" or one page with infinite scroll
- Don't auto-submit a review from a logged-in user without explicit consent
