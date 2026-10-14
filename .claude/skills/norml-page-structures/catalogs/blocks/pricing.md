# Pricing block

> Service or subscription pricing display. 2–4 plans side-by-side OR single price card OR "starts at $X" placeholder.

## Purpose

Set price expectations. Pre-qualify leads (people who can't afford it self-select out). Make the buy decision easier — price visibility is a conversion lever even for high-consideration services.

## Required elements

- **Section heading** — "Pricing" / "Plans" / "What it costs"
- **One or more plan cards** — each with: plan name + price + feature list + CTA
- **Plan name** (e.g., "Starter," "Pro," "Enterprise")
- **Price** — large, prominent; billing period if recurring
- **Feature list** — bullet list of what's included
- **CTA button** — primary action per plan

## Optional elements

- **Plan recommendation badge** — "Most popular" on the recommended plan
- **Comparison table** — feature × plan grid below the cards
- **Monthly vs annual toggle** — switch view between billing periods
- **Per-plan trial / demo CTA**
- **"Custom pricing" plan** — last card with "Contact us" instead of price
- **Savings indicator on annual** — "Save 20% on annual"
- **Currency switcher** — for global products

## Gutenberg + ACF default (primary)

**Block name:** `acf/pricing`
**ACF field group:** `Pricing`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `billing_period_toggle` — true_false, default false
- `plans` — repeater, min 1, max 4:
  - `name` — text
  - `price` — text (allow non-numeric like "Custom")
  - `currency_symbol` — text, default `"$"`
  - `billing_period` — text (e.g., `"/month"`, `"/year"`, `"one-time"`)
  - `tagline` — text, optional (one-liner above price)
  - `features` — repeater (text)
  - `cta_label` — text
  - `cta_url` — URL
  - `is_recommended` — true_false (renders "Most popular" badge)
  - `annual_price` — text, conditional on `billing_period_toggle`
  - `annual_savings_label` — text, optional
- `show_comparison_table` — true_false, default false
- `currency_switcher_enabled` — true_false, default false

**Blade template:** `resources/views/blocks/pricing.blade.php`

## Elementor fallback

Elementor's Price Table widget (Pro) — has all spec features natively.

## Variations

- **3-tier ladder** — Good / Better / Best — default
- **2-tier** — simpler, for productized services
- **Single plan card** — flat-rate offerings
- **4 columns with enterprise** — last column is "Contact us"
- **Comparison table only** — no cards, just a feature × plan grid
- **Hourly / day-rate** — for consultancies — "starts at $X / day"

## Used on

- Service page (when pricing is public)
- Landing pages (most have pricing)
- Home page (rare — only if pricing is the primary conversion message)

## Don'ts

- Don't ship pricing that's wildly wrong — buyers will get angry
- Don't have 5+ plans — choice overload
- Don't have a plan with no features listed — looks broken
- Don't make the "most popular" badge default on the cheapest plan unless it's genuinely the most popular
- Don't auto-detect currency without user override option
- Don't hide pricing behind a form unless the offering genuinely requires consultation — most "request a quote" gates lose more than they qualify
- Don't include a "Free" plan that's actually a 14-day trial — call it "Free trial," not "Free"
- Don't ship a comparison table with 30 rows — pick the 8–12 features that genuinely differentiate
- Don't change pricing without a sunset notice for existing customers
