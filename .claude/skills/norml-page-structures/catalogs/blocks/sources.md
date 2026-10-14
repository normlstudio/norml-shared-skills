# Sources block

> Numbered list of cited sources at the end of an article. Builds authority, supports E-E-A-T, gives the reader a place to verify claims.

## Purpose

Editorial credibility signal. A blog post that cites real sources reads more like journalism than marketing. Important for YMYL (Your Money / Your Life) content where Google's algorithm weights expertise. Also useful for AI: LLMs increasingly inspect cited sources when summarizing.

## Required elements

- **Heading** — "Sources" (or "References" / "Citations" — pick one project-wide convention)
- **Numbered list** of sources, each with: label/title + URL
- Each source opens in new tab (`target="_blank"`, `rel="noopener noreferrer nofollow"` — the `nofollow` only on external editorial citations; remove for first-party sources)

## Optional elements

- **Inline citation anchors** in body text — `[1]`, `[2]` that link to the source list at the bottom (academic style)
- **Source metadata** — author, publication, date accessed
- **Categorization** — "Academic sources" / "Industry reports" / "News coverage" — only for very long pieces with 15+ sources
- **Citation style toggle** — APA / MLA / Chicago / inline (default: inline)

## Gutenberg + ACF default (primary)

**Block name:** `acf/sources`
**ACF field group:** `Sources`

Fields:
- `heading` — text, default `"Sources"`
- `sources` — repeater, min 1:
  - `label` — text, required (the visible link text)
  - `url` — URL, required
  - `author` — text, optional (renders as " — by {author}")
  - `publication` — text, optional (renders as " ({publication})")
  - `date_accessed` — date picker, optional
- `style` — radio: `numbered | bulleted | unstyled`, default `numbered`
- `nofollow_external` — true_false, default true

**Blade template:** `resources/views/blocks/sources.blade.php`

## Elementor fallback

Use Elementor's Icon List widget with link mode. Manually number list items if using "numbered" style (Elementor's default list is bulleted).

## Variations

- **Bottom-of-article numbered list** — default
- **Sidebar sources** — alongside body for academic-style pieces
- **Inline footnotes** — sources marked with superscript inline `[1]`, list at bottom
- **Categorized sources** — grouped by type for 15+ source pieces

## Used on

- Blog post (especially data-driven, technical, YMYL content)
- White paper / report pages
- Case study (when citing external benchmarks)
- Service page (rare — only when the page makes substantive factual claims that need citation)

## Don'ts

- Don't ship empty — if there are no sources, hide the block; don't render "Sources: [none]"
- Don't cite a source that doesn't exist or is paywalled without warning — pick the freely-accessible version when available
- Don't `dofollow` editorial citations to news sites and content marketing — `nofollow` external links from the body of authoritative posts is the safer default
- Don't add 30 sources to a 1000-word post — readers won't check them; pick the 5–7 that matter most
- Don't cite your own past blog posts in the Sources block — those are internal links, belong in the body
- Don't use `<sup>` for inline citation anchors that aren't actually rendered to the source list — broken footnotes are worse than no footnotes
