# Case study page

> One project, told as a story: problem → approach → outcome. Proof artifact for service pages.

## Purpose

Show how the work actually plays out. Specific client, specific problem, specific solution, specific result. Used as proof on service pages, in proposals, and in sales conversations.

## Required structural elements (top → bottom)

1. **Header**
2. **[Hero](../blocks/hero.md)** — case-study variant: client name, project title, key metric or outcome line, featured visual (hero image / video / screenshot)
3. **Meta strip** — client, industry, services delivered, timeline, role. One row, scannable.
4. **The problem** — [text-content](../blocks/text-content.md) — what the client was dealing with, in their words where possible
5. **The approach** — [text-content](../blocks/text-content.md) or [image-text](../blocks/image-text.md) sequence — what you did, with visuals (mockups, process diagrams, before/after)
6. **The outcome** — metrics-first if available (conversion lift, time saved, $$ moved); narrative if not
7. **Client [testimonial](../blocks/testimonials.md)** — full quote from the person you worked with
8. **Related case studies / next project** — keep them clicking
9. **Final [CTA](../blocks/cta.md)** — "want results like this?" → contact
10. **Footer**

## Recommended (situational) blocks

- Image gallery / screenshots — design-heavy projects benefit from 3–6 visuals
- Embedded video — client testimonial video, walkthrough, or demo
- [logo-cloud](../blocks/logo-cloud.md) — "other clients we've helped" if portfolio is light
- Tech stack chip row — for technical projects, list tools used

## Common variations

- **Metrics-led case study** — outcome up top under hero, then unpack how. Best for performance / growth wins.
- **Story-led case study** — narrative top-to-bottom, outcome at the end. Best for brand / design / strategic work.
- **Process-led case study** — heavy on the "how we did it," lighter on the why. Best for technical / engineering showcases.

## SEO / schema notes

- H1 = project name or one-line outcome ("How [Client] grew X by Y%")
- Schema: `CreativeWork` or `CaseStudy` (custom); `author` = your Organization
- Slug should include client name, not just a generic project name

## Common page-level ACF fields

- `client_name`
- `client_logo`
- `client_industry`
- `services_delivered` (taxonomy or repeater linking to service pages)
- `project_timeline` (e.g., "8 weeks, Mar–May 2026")
- `headline_metric` (e.g., "+248% conversion rate")
- `featured_image`, `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't write case studies in first-person plural ("we did X, we built Y") for the whole page — vary with quotes and client voice
- Don't make every project sound equally amazing — readers tune out
- Don't omit the problem — without it, the outcome means nothing
- Don't bury the metric — if you have one, it goes above the fold
