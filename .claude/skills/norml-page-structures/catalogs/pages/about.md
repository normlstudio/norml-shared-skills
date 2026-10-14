# About page

> The "who are you?" page. Mission, story, team, proof — but no sales pitch. Visitor came here to vet the brand before deciding to trust it.

## Purpose

Build trust by showing the human and organizational substance behind the brand. Cover: what you do, why you do it, who's behind it, what you've achieved, where you work. Less about converting; more about removing the "is this a real company?" doubt.

## Required structural elements (top → bottom)

1. **Header**
2. **Page hero** — H1 ("About us" / "Our story" / "Who we are") + one-line dek
3. **Mission and values** — short statement of the core mission and 3–4 values, structurally similar to a [features](../blocks/features.md) block but values-themed
4. **Company history / age indicator** — brief overview of the company's history; can be a timeline or a paragraph with "Founded in YYYY"
5. **Services / products overview** — brief summary of what the company offers, with internal links to the relevant service / product pages (reuse [features](../blocks/features.md) or [image-text](../blocks/image-text.md))
6. **Team section** — [team-grid](../blocks/team-grid.md) or photo + bio — see [team-listing.md](team-listing.md) for the full team page
7. **Awards / recognitions** — small section, reuse [logo-cloud](../blocks/logo-cloud.md) shape with award logos or text list
8. **Office photos / behind-the-scenes** — small gallery to humanize the brand (optional but high-value)
9. **Top management** — photos + bios of leadership (or use [team-grid](../blocks/team-grid.md) with a `leadership` filter)
10. **Final [CTA](../blocks/cta.md)** — book a call / contact / learn more
11. **Footer**

## Recommended (situational) blocks

- **[Testimonials](../blocks/testimonials.md)** — short proof strip mid-page
- **[Logo cloud](../blocks/logo-cloud.md)** — for client/partner logos (separate from awards)
- **Press / media mentions** — small section if the brand has been in the press
- **Career link** — small CTA to "we're hiring" if applicable
- **Founding story** — long-form variant of company history (only if the story is genuinely compelling)
- **Numbers strip** — `years in business / clients served / countries / team size` (4-stat band)
- **Values cards** — alternative to mission paragraph: 3–4 value cards with icon + name + description

## Common variations

- **Founder-led brand** — story-first, prominent founder bio, less corporate-team focus
- **Established firm** — history-first, leadership team prominent, awards visible
- **Agency / studio** — team-grid front and center, mission paragraph, light on history
- **Local business** — office photos prominent, team grid optional, hours and address surfaced

## SEO / schema notes

- H1 on the page title
- Schema: `Organization` with `foundingDate`, `founder`, `numberOfEmployees`, `address`, `logo`, `sameAs` for social links
- Internal links: from About → key service pages, About → contact, About → blog (if blog exists)

## Common page-level ACF fields

- `intro_dek` — paragraph under H1
- `mission_statement` — textarea
- `values` — repeater (icon, name, description), min 3
- `founding_year` — number
- `founding_story` — wysiwyg, optional
- `team_section_mode` — radio: `featured-leadership | full-team | linked-only`, default `featured-leadership`
- `awards` — repeater (logo or text + label), optional
- `office_photos` — gallery, optional
- `numbers_strip` — repeater (number, label), optional
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't write the mission like a corporate cliché ("Our mission is to empower…") — write it like a human would say it out loud
- Don't show 30 team members on the About page — link to a [team-listing](team-listing.md) page; About teases the team, doesn't list it
- Don't list 12 values — 3–4 max; more dilutes them
- Don't claim awards you don't have or that nobody recognizes
- Don't put a high-friction CTA on About — visitors aren't ready to convert here; offer a soft action (read blog / see team / contact)
- Don't use stock photos for team members — fake authority is worse than no photo
- Don't ship office photos that look corporate-stock ("two people at a whiteboard smiling") — use real, candid shots
- Don't bury the founding year — it's a credibility signal, surface it
- Don't pad the page to feel "big" — a sparse About page reads as confidence; a bloated one as overcompensation
