# Case studies page (compare / proof / before-after)

> A standalone proof page that compares N (typically 2–4) anonymized client stories side-by-side or in sequence. Sells the methodology, not a single project. Differs from `case-study.md`, which is one client per page.

## Purpose

Show that the same methodology produces results across different industries / company stages. Used for service businesses where one diagnostic / playbook gets re-run against different verticals — readers see "this approach worked here AND here, so it'll work for us." Metrics-first; narrative is supporting evidence.

## Required structural elements (top → bottom)

1. **Header** (site chrome)
2. **Page hero / heading band** — H1 + one-line subhead. Plain panel, not a media-heavy hero. The cards below are the visual interest.
3. **Intro paragraph** (optional, short) — one sentence framing what the reader is about to see ("Two anonymized stories. Same 30-day audit. Different industries, same kind of result.")
4. **N × [case-study-card](../blocks/case-study-card.md)** — one per anonymized story. Each card carries: industry / stage label, challenge, approach, key findings, outcome narrative, and the metric strip (1–4 numbers).
5. **Closing media** — video, embedded testimonial, or trust strip. Often a personal invite video (founder / principal) since the cards already do the heavy lifting.
6. **Closing [CTA](../blocks/cta.md)** — dual button: primary (book / contact) + secondary (pricing / next step).
7. **Footer** (site chrome)

## Recommended (situational) blocks

- [testimonials](../blocks/testimonials.md) — strip of 2–3 short pull-quotes between cards if cards are quote-light
- [logo-cloud](../blocks/logo-cloud.md) — "industries we've worked with" above the cards (only if the cards are anonymized and the logos are real)
- [faq](../blocks/faq.md) — "common questions about results" if buyers tend to push back on the numbers
- [process-steps](../blocks/process-steps.md) — collapsed view of the methodology that produced the results, if not shown elsewhere

## Common variations

- **2-card before/after** — most common; pair contrasting industries (SaaS + Manufacturing, B2B + B2C, etc.) to show methodology range
- **Grid of 4** — agency-style proof grid; cards become tighter, less prose, more metric-forward
- **Sequence of 3 (timeline)** — Series A → Growth → Scale, same playbook at different stages

## SEO / schema notes

- **H1 = the methodology framing**, not "case studies." Example: "See the Difference Alignment Can Make" (proves a thesis), not "Our Case Studies" (generic). Page title in the head tag can be more literal ("How it works | Tom Opp Consulting").
- Slug: `/comparison/`, `/results/`, `/proof/`, or `/case-studies/`. Avoid `/work/` (implies portfolio, not proof).
- Schema: each card can emit `Article` or `CaseStudy` JSON-LD with `about` set to the industry. Page itself = `CollectionPage` linking to the cards.
- Open Graph image: the strongest metric strip rendered as a card image, NOT a hero photo.

## Common page-level ACF fields

- `page_heading` (H1)
- `page_intro` (optional one-line subhead)
- `closing_video_url` (string, full URL — accept VideoPress mp4 or YouTube/Vimeo embed)
- `closing_video_poster` (image)
- `closing_cta_primary_label`, `closing_cta_primary_url`
- `closing_cta_secondary_label`, `closing_cta_secondary_url`
- The cards themselves are NOT page-level fields — they live as ACF block instances in the post content (Gutenberg) so they're reusable on the homepage and elsewhere.

## Don'ts

- **Don't ship the raw source-capture scrape.** If the page is being built from a `00-source-capture/*.md` dump, the dump contains template scaffolding (`### Media`, `(none)`, `Page-level summary`, parenthetical section labels like `Continuous Improvement (hero)`) that MUST be stripped before publish. The published page should never contain `(none)`, never show a `<h3>Media</h3>` heading, never expose page-level meta. This is the #1 failure mode of an AI-built proof page.
- **Don't dump the impact stats as a `<ul><li>`.** Metrics on a proof page are the headline; render them as an emphasized strip (number + label) inside each card, not as 4-bullet prose lists. The case-study-card block enforces this.
- **Don't make every metric look equal.** If one card has 3 numbers and the other has 4, that's fine — let each card's strip wrap naturally. Don't pad to match.
- **Don't put metrics behind a click.** The whole reason a buyer is on this page is to see the numbers. Above-the-card-fold, in big mono-tabular type.
- **Don't reveal client names if anonymized.** The label should be the industry + stage ("B2B SaaS — Series A"), not a redacted name. Anonymization disclaimer goes in italics under the card title, not as a footer.
- **Don't auto-rotate or carousel the cards.** Visitor scrolls; cards are stacked vertically. Carousels hide content that exists to be compared.
- **Don't put the closing video above the cards.** The cards are the proof; the video is the personal close. Order matters.
- **Don't write H1 as "Case Studies."** Sell the thesis the cards prove, not the format.
