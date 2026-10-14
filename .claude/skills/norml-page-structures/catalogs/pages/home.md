# Home page

> The most-trafficked page on most sites. Visitor decides in 5 seconds whether to keep clicking.

## Purpose

Answer: who are you, what do you do, who is it for, why should I trust you, what should I do next. Drive the visitor to one of: read more, contact, sign up, buy.

## Required structural elements (top → bottom)

1. **Header** — site nav, logo, primary CTA in header (clean, simple, ≤6 items)
2. **[Hero](../blocks/hero.md)** — H1 + dek + primary CTA + visual
3. **Trust strip** — [logo-cloud](../blocks/logo-cloud.md) (client / partner / certification / media logos) — proof you're real
4. **What you do** — [features](../blocks/features.md) or [benefits-grid](../blocks/benefits-grid.md), 3–6 core offerings / outcomes
5. **Why you** — [testimonials](../blocks/testimonials.md) — short client testimonials with names and ideally ratings
6. **Summary of services** — brief overviews of main services with internal links to service pages (reuse [features](../blocks/features.md) or [image-text](../blocks/image-text.md))
7. **Team section** — small [team-grid](../blocks/team-grid.md) row showing 3–6 featured people, photos + names + short credibility-driven bios
8. **Blog / resources strip** — 3 most recent posts as [post cards](../blocks/post-card.md) (only if blog exists and is active)
9. **Final [CTA](../blocks/cta.md)** — one more clear action before the footer
10. **Footer** — full nav, legal, contact, social, [payment-info](../blocks/payment-info.md) if ecom

## Required: 2–3 primary CTAs across the page

Per the SEO framework: header + hero + (mid-page or footer). Same destination, varied framing. Don't bury the CTA only in the hero.

## Recommended (situational) blocks

- **[Image-text](../blocks/image-text.md)** — for "how we work" or "story behind" sections
- **[FAQ](../blocks/faq.md)** — only if the offering genuinely needs explanation
- **Contact form snippet** — small inline form near the bottom for low-friction reach-out
- **Pricing teaser** — only if pricing is part of the conversion flow
- **Search bar** — only for large content-driven or ecommerce sites ([search-bar](../blocks/search-bar.md))
- **Live chat / chatbot** — for high-consideration services where prospects need quick answers
- **Numbers strip** — `years in business / clients served / projects shipped` — 3–4 stat band

## Common variations

- **Service-first home** — features lead after hero, then testimonials. Best when value prop is the service itself.
- **Story-first home** — text-heavy intro after hero, then features. Best for brand-driven / founder-led sites.
- **Product-first home** — feature + screenshot + CTA stacked. Best for SaaS / product-led sites.
- **Ecommerce home** — featured products + categories + new arrivals + testimonials
- **Editorial home** — recent posts grid is the primary content, services secondary

## SEO / schema notes

- H1 on the hero headline (only one H1 per page)
- Schema: `Organization` with `logo`, `sameAs` for social, `address` if local business
- Optional: `WebSite` with `SearchAction` if the site has site-search
- For ecommerce: also include `Store` or `LocalBusiness` schema if applicable
- Internal links: hero CTA → primary service / contact; team strip → team listing; blog teaser → blog archive; service strip → service pages

## Common page-level ACF fields

- `seo_title` — overrides default for SEO (RankMath / Yoast)
- `seo_description`
- `og_image` — fallback Open Graph image
- `hero_override_image` — if home gets seasonal swaps
- `featured_team_members` — relationship (for the team strip)
- `featured_services` — relationship (for the service summary section)
- `show_blog_teaser` — true_false, default true if blog has posts

## Don'ts

- Don't exceed 7–8 sections — visitors won't scroll past 5
- Don't put the primary CTA only in the hero — repeat it mid-page and at bottom
- Don't use carousels for the hero — accessibility, analytics, and conversion all suffer
- Don't lead with awards / certifications — lead with what the user gets
- Don't show 30 team members on home — feature 3–6, link to full [team listing](team-listing.md)
- Don't auto-show a chat widget on page load — invasive; trigger on intent or after dwell
- Don't link the trust-strip logos to themselves (causes confusion) — link to case studies or simply make them non-clickable
- Don't use generic stock photos for the team section — fake authority is worse than no photo
- Don't omit the contact path from the footer — visitors who didn't convert above the fold need it visible somewhere
