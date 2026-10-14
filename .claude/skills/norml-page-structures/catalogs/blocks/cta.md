# CTA block

> End-of-section / end-of-page call-to-action band. One clear action.

## Purpose

Convert the engaged reader. The visitor has consumed enough — give them the obvious next step before they bounce.

## Required elements

- **Headline** — short, action-oriented ("Ready to talk?" / "Get started today" / "See it in action")
- **CTA button** — single primary action, URL + label
- Visual treatment that makes the band feel distinct from surrounding content (background color, illustration, accent)

## Optional elements

- Sub-headline (one supporting sentence)
- Secondary action (lower-emphasis text link, e.g., "or see how it works →")
- Trust micro-copy under the button ("No credit card required" / "30-day free trial" / "Reply within 1 business day")
- Visual / illustration to the side
- Stats or proof in the band ("Join 500+ teams who...")

## Gutenberg + ACF default (primary)

**Block name:** `acf/cta`
**ACF field group:** `CTA`

Fields:
- `headline` — text, required
- `sub_headline` — textarea, optional
- `primary_cta` — link, required (URL + label + new tab toggle)
- `secondary_cta` — link, optional (rendered as text link)
- `trust_microcopy` — text, optional
- `layout` — radio: `centered | split | left-aligned | full-width-band` (default: `centered`)
- `background` — radio: `accent | dark | light | gradient | image` (project's design tokens)
- `background_image` — image, shown when background = image
- `illustration` — image, optional (for split layout)

**Blade template:** `resources/views/blocks/cta.blade.php`

## Elementor fallback

Use Elementor's Call to Action widget. Match background and button styles to project design tokens.

## Variations

- **Centered band** — full-width section, headline + button stacked center; default for most cases
- **Split band** — headline left, button right; works mid-page
- **Inline mid-article CTA** — for blog posts; smaller, narrower, less visual weight
- **Sticky bottom bar** — for landing pages; persists as user scrolls (with dismiss button)
- **Newsletter signup CTA** — replaces button with email input + subscribe button

## Used on

Almost every page — at minimum: end of home, end of service, end of case study, end of blog post, end of landing.

## Don'ts

- Don't have 3 different CTAs in one band — pick one primary action
- Don't use vague labels like "Submit" / "Click here" / "Learn more" — use action-specific verbs ("Book a call", "Download the guide", "Start free trial")
- Don't make the CTA disappear into the page — it should pop visually (contrast with surrounding content)
- Don't put a CTA without a destination set — wire it up before shipping
- Don't add 5 fields to a CTA "form" — if it's that long, it's a form section, not a CTA
- Don't repeat the exact same CTA copy 4 times on the same page — vary the framing while keeping the action consistent
