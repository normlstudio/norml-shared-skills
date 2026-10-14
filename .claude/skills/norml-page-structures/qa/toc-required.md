# Required blog table of contents

Source: Norml Studio, Oct 10, 2026. Blog contents navigation is required by the
shared blog structure, including short posts. This explicit update supersedes
historical source defaults captured by the unchanged migration hash manifest.

## Acceptance

- No word-count or minimum-heading gate in the page, block, entry point or guide.
- No per-post visibility opt-out for required blog navigation.
- H2 links preserve authored section titles; H3-only legacy posts use real H3s.
- Unsectioned posts use one body anchor labelled “Article”, without invented headings.
- Desktop TOC is left of the article and begins at the body, below the full-width intro.
- Record `centered-pair` or `left-edge-toc`; no silent right-side default.
- `centered-pair`: measured outside left/right whitespace matches within rounding tolerance.
- `left-edge-toc`: article center matches the remaining pane's center, not the viewport.
- Check actual coordinates at narrow/normal/wide desktop widths; readable measure,
  adjacent deliberate gap, aligned body tops and no horizontal overflow.
- Prose text stays left aligned. Centering the text is not a layout correction.
- Sidebar precedes the article in DOM order; mobile keyboard and visual order agree.
- Grid, sticky CSS and collapse JavaScript share the project's recorded breakpoint.
- Exactly one sticky owner; sidebar stretch gives it scroll room within the body.
- Mobile TOC moves above the left-aligned prose and collapses instead of disappearing.
- Every link resolves to exactly one rendered target; active section updates on scroll.
- Keyboard expansion and navigation work; reduced motion is respected.
- Exercise a short post, one/two headings, legacy H3s, unsectioned content and
  repeated/generated anchors. An empty TOC or an empty placeholder does not pass.

The page and block specifications are the runtime source; this file checks their
agreement. Project-specific screenshots and client content stay in the project.
