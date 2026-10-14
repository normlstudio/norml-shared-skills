# Key takeaways block

> A short bulleted summary of the article's main points. Usually sits between the post header and the body, or at the very end as a wrap-up.

## Purpose

Give the skimming reader the gist in 5 seconds without making them scroll. AI-overview-friendly (LLMs cite bulleted summaries more often than buried paragraphs). Often paired with a [TL;DR](tldr.md) block — they serve overlapping but distinct purposes: TL;DR = one-paragraph summary in plain prose; Key takeaways = 3–5 enumerated bullets.

## Required elements

- **Heading** — "Key takeaways" (or "TL;DR — key points" if the project uses takeaways instead of a separate TL;DR)
- **Bulleted list** — 3–7 bullets, each a complete sentence
- Visual treatment that sets the block apart from regular body content (tinted background, accent border, icon)

## Optional elements

- Section dek (one supporting sentence above the bullets)
- Icon per bullet (small SVG checkmark / arrow / dot) — purely visual
- Numbered variant instead of bulleted — when sequence matters

## Gutenberg + ACF default (primary)

**Block name:** `acf/key-takeaways`
**ACF field group:** `Key takeaways`

Fields:
- `heading` — text, default `"Key takeaways"`
- `dek` — textarea, optional
- `bullets` — repeater, min 3, max 7:
  - `text` — wysiwyg (allows bold + links inside bullets, no headings)
- `style` — radio: `boxed | bordered | minimal`, default `boxed`
- `icon` — radio: `none | check | arrow | dot`, default `check`

**Blade template:** `resources/views/blocks/key-takeaways.blade.php`

Schema: emit `ItemList` (or extend the parent `BlogPosting` with `mainEntity`) — useful for AI-overview citations. Optional; not required for the block to function.

## Elementor fallback

Use Elementor's Icon List widget with a tinted Container background. Match icon and spacing to the project's design tokens.

## Variations

- **Top-of-article boxed callout** — sits between post header and body, default
- **End-of-article wrap-up** — sits between body and FAQ, framed as "What we covered"
- **Sidebar version** — sticky alongside body, narrower column
- **Numbered variant** — when the takeaways are sequenced steps

## Used on

- Blog post (long-form default)
- Service page (variant: "Why this matters" at the top)
- Resource / guide pages
- Case study (variant: "What we learned")

## Don'ts

- Don't have fewer than 3 bullets — block looks broken
- Don't have more than 7 bullets — block stops being a summary; just becomes another body section
- Don't write bullets longer than 25 words — they stop scanning at that length
- Don't repeat the same bullet verbatim in the body — readers feel patronized
- Don't put Key Takeaways AND TL;DR right next to each other unless one is plain prose and the other is bullets (and even then, default to picking one)
- Don't render Key Takeaways on a 300-word post — there's nothing to take away
- Don't write bullets that lead with "We" or "Our" — write reader-first ("You can…" / "Search ranks reward…" / "Most teams overlook…")
