# Banned: per-page CSS shadow design system

A page stylesheet recreating buttons, cards, headings, colors and fonts in parallel with
global components causes design drift and duplicate maintenance. Examples include
`css/blocks-{page}-page.css`, `assets/css/page-{name}.css`, and page-specific palette tokens.

## Detect

```bash
rg --files resources/css css assets/css 2>/dev/null | rg '(^|/)(page-[^/]+|blocks-[^/]+-page|[^/]+-page)\.css$'
rg -n 'blocks-.*-page|page-.*\.css' app resources inc 2>/dev/null
```

Inspect matches; missing directories are simply absent, while unreadable directories are
reported. Do not treat every filename containing `page` as a defect (for example a reusable
pagination component). Confirm that the file creates page-level visual primitives or is
actually shipped to one page. Review compiled chunk names and conditional enqueue routes.

## Fix

Move semantic tokens into the global token layer, reusable visual primitives into globally
available components, and genuinely unique composition into a block layout. Reuse fonts and
buttons; no hex palette, font override or bespoke buttons in block layout files.
Existing debt needs an explicitly scoped refactor; do not silently rewrite unrelated pages.

See [CSS system](../css-design-system.md) and [inherited guide](../inherited-projects.md).
