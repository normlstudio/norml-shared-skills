# Social share block

> Horizontal row of share buttons after a blog post body. LinkedIn / X / Facebook / Pinterest / Email / copy-link.

## Purpose

Let engaged readers share the post to their network. Distinct from [Share with AI](share-ai.md), which pipes the article into an LLM, and [Google Preferred Source](preferred-source.md), which stores a reader's publication preference in Google. On blog singles the locked order is Share with AI → Google Preferred Source → social sharing.

## Required elements

- **Section heading** (optional) — "Share this article" or simply omit if visual is self-evident
- **Share targets** — minimum 3, default 4–5
- Each share target has: icon (SVG), accessible label, click destination (intent URL or `navigator.share` for mobile)

## Optional elements

- Vertical sidebar variant (sticky alongside body on desktop)
- "Copy link" button — `navigator.clipboard.writeText(window.location.href)` with toast feedback
- Share count (e.g., "Shared 47×") — only if real share data is available (most platforms killed share counts; skip unless project has Buffer/SharedCount integration)
- "Email a friend" — opens `mailto:?subject=…&body=…`

## Gutenberg + ACF default (primary)

**Block name:** `acf/share-social`
**ACF field group:** `Social share`

Fields:
- `heading` — text, optional, default empty
- `targets` — checkbox group (multi-select):
  - `linkedin`, `x`, `facebook`, `pinterest`, `whatsapp`, `email`, `copy_link`
  - default: `linkedin`, `x`, `facebook`, `pinterest`, `copy_link`
- `layout` — radio: `horizontal | vertical-sidebar | sticky-sidebar`, default `horizontal`
- `pinterest_image_field` — image (only when Pinterest is enabled — Pinterest's intent URL needs a media URL; fallback to featured image if empty)

**Theme Options page:**
- `default_targets` — same multi-select, sets the per-post default

**Blade template:** `resources/views/blocks/share-social.blade.php`

Share URL patterns (all `target="_blank"`):
- LinkedIn: `https://www.linkedin.com/sharing/share-offsite/?url={URL}`
- X/Twitter: `https://x.com/intent/post?text={TITLE}&url={URL}`
- Facebook: `https://www.facebook.com/sharer/sharer.php?u={URL}`
- Pinterest: `https://pinterest.com/pin/create/button/?url={URL}&media={IMAGE_URL}&description={TITLE}`
- WhatsApp: `https://wa.me/?text={TITLE}%20{URL}`
- Email: `mailto:?subject={TITLE}&body={URL}`
- Copy link: JS click handler, no URL

## Elementor fallback

Elementor's Social Icons / Share Buttons widget. Native. Configure target list to match the spec defaults.

## Variations

- **Horizontal row** — default, below post body
- **Vertical sticky sidebar** — left or right of post body, sticks on scroll, hides on mobile
- **Floating bottom bar (mobile)** — fixed to bottom of viewport, only on mobile
- **Inline mid-article** — small text "Share this" + 3 inline icons after a pull-quote or callout

## Used on

- Blog post (default)
- Case study (sometimes)
- Long-form service page (sometimes)
- Resource / guide pages

## Don'ts

- Don't show 7+ share targets — picks 4–5, the rest is decoration
- Don't include Reddit / Hacker News / Mastodon unless the audience genuinely uses them (most B2B / consumer brands don't)
- Don't ship without a fallback Pinterest image — if `pinterest_image_field` is empty AND there's no featured image, hide the Pinterest button rather than passing an empty `media=` URL
- Don't auto-open the share dialog when the page loads — invasive
- Don't track shares without a privacy banner if the project is in EU
- Don't put share buttons above the article — readers haven't decided to share yet; surfaces them after they read
- Don't pair with the WordPress core "Share" block (Jetpack-flavored) AND a custom share-social block at once — pick one source-of-truth
