# CSS system and responsive contract

Actual typography, spacing, palette and container values come from the approved project
design. Preserve existing inherited tokens before adding a parallel framework or palette.
Resolve absent design choices before styling. New Sage may use Tailwind 4 `@theme` and
`@layer components`; inherited plain CSS/SCSS uses its existing compiler and conventions.

## Three layers

1. Tokens: semantic colors/fonts/type/spacing/radii in one global source.
2. Shared components: global button/card/heading/container/accordion primitives.
3. Individual block layout: grid/flex/position/decorative composition only.

No stylesheet scoped to a single page that redefines shared primitives. Before writing a
block file inspect the global components; promote a reusable primitive there. A block needs
no CSS file when utilities/shared components already express its layout. No hex palette,
`font-family` override or parallel buttons inside block layouts. In inherited BEM/SCSS use
flat `block__element--modifier`, semantic variables, `@use`/`@forward`, and shallow nesting.

## Loading

Keep tokens/components available globally and in the editor. Block-specific CSS may be
conditional only if discovery covers the actual rendering route. `has_block()` on the current
post alone can miss template-part, reusable/synced, archive-controlled and nested content.
Use supported block asset metadata or a verified traversal/manifest; missing CSS is not
acceptable optimization. Do not duplicate editor/frontend style systems.

## Responsive/accessibility acceptance

Honor approved containers and gutters; avoid accidental narrow boxing or stretched hollow
sections at wide widths. Grid children need `min-width: 0`; media needs correct bounds and
aspect ratio; text wraps naturally. Structural breakpoints follow the project contract.
Test 375, 768, 1024, 1440 and 1900 pixels and any feature-specific breakpoint.

Check no horizontal scrolling, readable type, appropriate stack/order, touch targets,
visible focus, keyboard controls, contrast, reduced motion and print when relevant.
Use `text-wrap: balance/pretty` only when supported and justified. Never `transition: all`.
Do not suppress overflow to conceal a broken child layout. Record measurements/screenshots.

Use the [antipattern detector](antipatterns/per-page-css-files.md) before closing code work.
