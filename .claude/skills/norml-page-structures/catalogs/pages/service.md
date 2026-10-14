# Service page

> One service offering, in depth. The page that converts "interested" into "let's talk."

## Purpose

Explain one service: what it is, who it's for, what the outcome is, how the process works, what it costs (or how to get a quote), and proof it works. Drive to contact / book / quote.

## Required structural elements (top → bottom)

1. **Header** — site nav, logo, primary CTA
2. **[Hero](../blocks/hero.md)** — service-focused: H1 = service name, dek = outcome, CTA = book/contact
3. **Service overview & benefits** — clear explanation of the service + what problem it solves + key buyer benefits ([benefits-grid](../blocks/benefits-grid.md) or [text-content](../blocks/text-content.md))
4. **Target audience identification** — who this service is designed for (so visitors quickly see if it fits)
5. **What you get** — [features](../blocks/features.md) — concrete deliverables, not vague benefits
6. **[Process steps](../blocks/process-steps.md)** — numbered steps, ideally with timeline ("Week 1: discovery, Week 2: build…")
7. **Proof** — [testimonials](../blocks/testimonials.md) specific to this service, or 1–2 case-study teasers
8. **[Pricing](../blocks/pricing.md) or pricing guidance** — if applicable, surface to set expectations
9. **Partner / trust signals** — [logo-cloud](../blocks/logo-cloud.md) variant (partner logos, certifications, affiliations)
10. **Compelling visuals** — relevant images, graphics, or short videos demonstrating the service / process / results
11. **Blog / resources strip** — related articles, guides, or educational resources that support SEO and authority (links to relevant blog posts)
12. **[FAQ](../blocks/faq.md)** — the 5–8 questions every prospect asks; may describe visible Q&A with FAQPage; Google FAQ rich results are retired
13. **Final [CTA](../blocks/cta.md)** — clear next step, single button
14. **Chatbot / Quick contact widget (optional)** — easy way to ask questions without leaving the page
15. **Footer**

## Recommended (situational) blocks

- **Service-specific CTA** mid-page — book a call / request a quote / schedule consultation (in addition to the final CTA)
- **Lead magnet** — downloadable guide / checklist tied to this service
- **Related services** — links to other service pages
- **Service-specific reviews** — [product-reviews](../blocks/product-reviews.md) variant if reviews are public per service
- **Comparison table** — vs alternatives / vs DIY / vs competitors (with care — no badmouthing)
- **Mini-case-study card** — one project specifically using this service

## Common variations

- **Productized service** — strong [pricing](../blocks/pricing.md) block, defined packages (Bronze/Silver/Gold), short FAQ
- **Custom / enterprise service** — no pricing, lots of process detail, case studies prominent, "request a quote" CTA
- **Sprint / engagement service** — timeline-first, deliverables-second
- **Subscription service** — pricing monthly/annual toggle, billing terms FAQ

## SEO / schema notes

- H1 = service name + primary keyword
- Schema: `Service` with `serviceType`, `provider` (your Organization), `areaServed`, `description`, optional `offers` with pricing
- FAQ block emits `FAQPage` schema
- Internal linking: from home → this page, from blog posts → this page (where relevant), from related-services → this page

## Common page-level ACF fields

- `service_name` (canonical, used in nav and breadcrumbs)
- `service_short_description` (used in service-index listings)
- `service_icon`
- `target_audience` — wysiwyg (renders the "who this is for" section)
- `process_overview` — repeater (see [process-steps.md](../blocks/process-steps.md))
- `pricing_visible` (toggle — controls whether pricing block renders)
- `pricing_data` — see [pricing.md](../blocks/pricing.md)
- `partner_logos` — gallery
- `service_specific_testimonials` — repeater or post relationship
- `faq` — repeater
- `related_blog_posts` — relationship (for the resources strip)
- `chatbot_enabled` — true_false
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't list 20 deliverables — pick the 4–6 that matter most
- Don't show generic stock-photo team members
- Don't put the FAQ above the proof (testimonials come first; FAQ resolves last-mile objections)
- Don't have 3 different CTAs ("book a call", "download guide", "watch demo") competing on the same page — pick one primary, demote the rest
- Don't write the target-audience section as "anyone who wants…" — be specific or skip it
- Don't ship a service page without any visible proof (testimonials, case studies, logos) — the page reads as theory, not practice
- Don't pad with awards and badges instead of showing actual outcomes
- Don't auto-show a chatbot popup that interrupts reading
- Don't link "related services" to dead / placeholder pages
- Don't ship pricing that's outdated vs the team's actual rates
