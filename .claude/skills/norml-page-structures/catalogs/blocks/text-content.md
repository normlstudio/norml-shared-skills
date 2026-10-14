# Text content block

> Rich-text body — paragraphs, headings, lists, blockquotes, inline images, links.

## Purpose

The workhorse for long-form content. Blog post bodies, about-page copy, legal pages, case-study narratives — anywhere the content is primarily prose.

## Required elements

- **Body content** — wysiwyg / rich-text editor field
- Proper heading hierarchy (H2 / H3 / H4) following the page's H1
- Sensible typography (line length 60–80ch, paragraph spacing, list indentation)

## Optional elements

- **Pull quotes** — visual blockquotes that break up long sections
- **Inline images** — captioned, with proper alt text
- **Code blocks** (for technical content) — with syntax highlighting
- **Callout / info boxes** — colored banners for tips, warnings, notes
- **Embedded media** — video, tweet, Loom, CodePen via oEmbed
- **Footnotes / endnotes**

## Gutenberg + ACF default (primary)

**Block name:** `acf/text-content`
**ACF field group:** `Text Content`

Fields:
- `content` — wysiwyg, required (allows full HTML via Gutenberg editor)
- `width` — radio: `narrow | default | wide | full` (default: `default`, ~70ch)
- `align` — radio: `left | center | justified` (default: `left`)
- `lead_paragraph` — toggle: makes the first paragraph larger (for article intros)

**Blade template:** `resources/views/blocks/text-content.blade.php`

**Note:** for most cases on a blog post, the body should be the WordPress post content (native Gutenberg) — not this block. Use this block when text content appears INSIDE another page (about, case study, service page), not as the main article body.

## Elementor fallback

Use Elementor's Text Editor widget. Set max-width to match the project's content column width.

## Variations

- **Narrow column** — for long-form reading (60–70ch); default for blog post body
- **Two-column** — for legal pages or comparison content
- **Wide column** — for design-heavy text sections (about page hero copy)
- **Lead-paragraph variant** — larger first paragraph (article intros, executive summaries)

## Used on

Blog post (article body or sections), about, case study (narrative sections), legal (privacy, terms), help docs.

## Typography hygiene

- **Line length** — 60–80 characters per line for readability
- **Paragraph spacing** — generous (1.5× line-height between paragraphs)
- **Heading hierarchy** — never skip levels (H2 → H4 with no H3 is bad)
- **Link styles** — distinct from body text (underline + color), accessible contrast
- **Lists** — use `<ul>` and `<ol>`, not paragraphs with dashes
- **Inline emphasis** — `<strong>` for importance, `<em>` for tone, not all-caps or styled `<b>`

## Don'ts

- Don't center long-form text — left-align is more readable
- Don't use H1 inside this block — the page already has its H1
- Don't fill it with stock-photo inline images
- Don't use bold for entire paragraphs ("important info!") — write it as a callout if it's important
- Don't write 800-word paragraphs — break into 3–5 sentence chunks
- Don't paste from Google Docs without cleaning the inline styles
