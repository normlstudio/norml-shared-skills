# Table of contents block

> Auto-generated jump links to H2/H3 sections in a blog post or long-form page. Blog default: left of the article body, sticky on desktop, collapsible above the article on mobile.

## Purpose

Help a reader scan the article structure before committing to a full read, and let them jump to the section that matters. Improves dwell time on long-form, supports SEO (Google sometimes shows TOC anchors as sitelinks), and signals editorial quality.

## Required elements

- **Heading** — "Contents" / "In this article" / "Table of contents"
- **List of links** — generated from H2s in the post body (optionally H3s as nested children); use existing H3s if a legacy article has no H2s
- **Blog visibility** — required on every post regardless of length or heading count. For unsectioned content, use one body anchor labelled "Article"; never invent headings or ship empty navigation
- Each item: anchor link (`#section-slug`), display text matches its authored heading (or the explicit "Article" body fallback), current section highlighted on scroll

## Optional elements

- **Sticky position on desktop** — TOC follows the viewport as the user scrolls (left or right sidebar)
- **Collapsible on mobile** — single tap to expand/collapse, collapsed by default
- **Progress indicator** — thin progress bar showing reading position
- **Estimated read time per section** — only useful for very long pieces (~5000+ words)
- **Auto-skip empty H2s** — when an H2 has no body content beneath it before the next H2

## Gutenberg + ACF default (primary)

**Block name:** `acf/toc`
**ACF field group:** `Table of contents`

Fields:
- `heading` — text, default `"In this article"`
- `depth` — radio: `h2-only | h2-h3 | h2-h3-h4`, default `h2-only`
- `position` — radio: `inline | sticky-left | sticky-right`, default `sticky-left` (falls back to inline on mobile)
- `show_progress_bar` — true_false, default false
- `collapsible_mobile` — true_false, default true
- `expanded_mobile_default` — true_false, default false (start collapsed on mobile)

**Blog visibility is template-owned:** no `show_toc` opt-out and no word-count or
minimum-heading threshold. Legacy visibility metadata must not suppress the
required navigation. Other page types retain their own TOC applicability.

**Blade template:** `resources/views/blocks/toc.blade.php`

Build the link list in PHP at render time by parsing post content for real headings (DOMDocument or regex on `the_content()`), assigning a slug if the H2 doesn't have an `id`, injecting the `id` back into the body output, and emitting the link list.

Sticky behavior: pure CSS with a project-owned top offset. Use the same recorded
project breakpoint for the two-column grid, sticky state and mobile collapse.
For blogs, select `centered-pair` or `left-edge-toc` from the
[blog composition contract](../pages/blog-post.md#two-permitted-desktop-compositions).
The sidebar comes first in DOM order. Keep exactly one sticky owner and stretch
the sidebar to the body height. Verify centering by actual coordinates.

Active-section highlight: small IntersectionObserver script, no library.

## Elementor fallback

Use a third-party Elementor TOC widget (Elementor Pro has one, or "Table of Contents Plus" plugin). Configure to mirror the spec: H2-only by default, sticky on desktop. The native Gutenberg `core/table-of-contents` block also works (Gutenberg ≥6.3) if the project is happy with default styling.

## Variations

- **Inline TOC** — at the top of the post body, between header and first H2; non-sticky
- **Sticky-left sidebar (blog default)** — TOC left, article right; center their combined group or center the article within the remaining pane, as specified by the blog page contract
- **Sticky-right sidebar** — available for other page types or an explicit recorded blog override; never silently use it as the blog default
- **Floating button (mobile)** — small FAB that expands the TOC as an overlay
- **Top-banner TOC** — full-width strip between hero and body, horizontal scroll of anchor pills (for visually-led pieces with short H2s)

## Used on

- Blog post (required for every length, including news and short posts)
- Service page (long-form variant, when content reads like an article)
- Knowledge base / docs
- Legal pages (terms, privacy) — even short ones benefit from a TOC

## Don'ts

- Don't mistake left-aligned text or lack of overflow for correctly centered desktop composition
- Don't suppress a blog TOC for 1–2 headings or fewer than 800 words; no length gates
- Don't invent section headings for an unsectioned body; use the single truthful article-body anchor
- Don't include H1 in the TOC — the title is already the headline
- Don't go deeper than H3 in most cases — H4+ creates a visually noisy nested list
- Don't use page anchors that conflict with named WordPress anchors (`#main`, `#content`, `#comments`)
- Don't auto-scroll smoothly without `prefers-reduced-motion` check — motion sickness
- Don't hide the TOC entirely on mobile — collapse, don't remove (users still want scannability)
- Don't write H2s like "Section 1" — they'll show up as TOC items and look lazy
- Don't ship a TOC that doesn't update its active-section highlight on scroll — half the point is the orientation signal
