# Service listing page (All services)

> The "services" index — every service offering listed with summary card, linking to dedicated [service](service.md) pages.

> **Source note:** the canonical SEO doc tab for this page type is empty as of 2026-05-22. This spec is derived from common service-business patterns + [service](service.md) inheritance.

## Purpose

Surface the full service catalog. Help visitors who know they need help but aren't sure which service applies. The "menu" before they pick a meal.

## Required structural elements (top → bottom)

1. **Header**
2. **Page hero** — H1 ("Our services" / "What we do" / "Services") + one-paragraph intro
3. **Service grid** — one card per service, 3 columns desktop, 1 column mobile
4. **Final [CTA](../blocks/cta.md)** — "Not sure which service fits? Let's talk" → contact form / calendar
5. **Footer**

## Required: service card structure

Each card:
- Icon or small image
- Service name (H3, linked to [service](service.md) page)
- One-line description (the service's `service_short_description` field)
- "Learn more →" link or whole card clickable

## Recommended (situational) blocks

- **Service categories filter** — if services group into clusters (Strategy / Design / Engineering)
- **[Testimonials](../blocks/testimonials.md)** — one strong quote per service area, or a single brand-wide quote at the bottom
- **[Process overview](../blocks/process-steps.md)** — short 3–4 step framework that applies across services
- **[Logo cloud](../blocks/logo-cloud.md)** — clients served
- **[FAQ](../blocks/faq.md)** — meta-questions ("How do I pick a service?" / "Can I combine services?")
- **Comparison table** — services vs each other (price, scope, ideal client) — useful for agencies with productized offerings

## Common variations

- **Flat grid** — all services equal weight
- **Featured + secondary** — primary services in larger cards, secondary in compact grid below
- **By-category grid** — services grouped under category headers
- **Editorial layout** — services described in alternating image-text rows instead of cards

## SEO / schema notes

- H1 on the listing title
- Schema: `OfferCatalog` with `itemListElement` → `Offer` per service
- Internal links: from this page to each service page; from home → here; from blog → relevant service pages

## Common page-level ACF fields

- `intro_dek` — paragraph under H1
- `services_query` — relationship to service CPT (defaults to all published)
- `card_layout` — radio: `icon-top | image-top | minimal`, default `icon-top`
- `enable_category_filter` — true_false, default false
- `featured_services` — relationship to 2–4 services, conditional
- `seo_title`, `seo_description`

## Don'ts

- Don't list 15 services equally — pick 4–7 primary; rest goes under "More" or sub-categories
- Don't hide pricing if any service has it visible — consistency across services
- Don't ship a service card with no destination — every card → real service page
- Don't write generic descriptions ("We help businesses grow") — be specific per service
- Don't use abstract icons that don't communicate the service
