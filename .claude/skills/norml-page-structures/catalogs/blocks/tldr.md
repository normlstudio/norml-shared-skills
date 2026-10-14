# TL;DR block

> A one-paragraph plain-prose summary of the article. Sits between post header and TOC (or body) on long-form pieces.

## Purpose

Give the skimming reader a 2–3 sentence summary of the whole article without making them scan a bulleted list (that's [key-takeaways.md](key-takeaways.md)'s job). TL;DR fits when the article has a single thesis that compresses naturally to a sentence or two. Key takeaways fits when the article has 3–7 independent points.

## Required elements

- **Label** — "TL;DR" — short prefix in distinct typography
- **Summary paragraph** — 2–3 sentences, max ~60 words

## Optional elements

- Link to "skip to full article" anchor — helpful if TL;DR sits above the TOC
- Different label variants by region/voice — "Short version" / "In one paragraph" / "The gist"

## Gutenberg + ACF default (primary)

**Block name:** `acf/tldr`
**ACF field group:** `TL;DR`

Fields:
- `label` — text, default `"TL;DR"`
- `summary` — textarea, required, max 60 words
- `style` — radio: `inline-prefix | boxed-callout | sidebar`, default `boxed-callout`

**Post-level override:**
- `show_tldr` — true_false, default false (off by default; opt-in per long post)

**Blade template:** `resources/views/blocks/tldr.blade.php`

Render the summary with the label inline-bold-prefixed in the "inline-prefix" variant; as a tinted card in "boxed-callout."

## Elementor fallback

Use a Heading widget for the label and a Text Editor widget for the summary, wrapped in a Container with tinted background.

## Variations

- **Inline prefix** — `**TL;DR —** summary text here.` Single paragraph, no card
- **Boxed callout** — bordered/tinted card with TL;DR label on its own line
- **Sidebar TL;DR** — narrow column alongside opening paragraph (desktop only, falls back to inline on mobile)

## Used on

- Blog post (long-form, opt-in per post, default off)
- Investigative / deep-dive content (mandatory)
- News article (mandatory)
- Case study (variant: "Outcome in one sentence")

## Don'ts

- Don't ship a TL;DR longer than 60 words — defeats the purpose
- Don't render TL;DR on a 600-word post — the post IS the TL;DR
- Don't pair with Key Takeaways unless the article is genuinely long-form (>2500 words) and benefits from both
- Don't write TL;DR as "This article discusses…" — write the actual thesis ("Most teams underprice SEO; here's the math.")
- Don't auto-generate the TL;DR with an LLM at render time — too unpredictable; have a human write it as a field
- Don't put TL;DR after the body (it's not a recap; that's Key Takeaways) — TL;DR is for the reader who hasn't started reading yet
