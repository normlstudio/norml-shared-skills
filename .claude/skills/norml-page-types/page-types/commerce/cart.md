# Cart destination

Family: [Commerce and customer journeys](commerce.md). Member ID: `commerce/cart`.
Logical role: `utility`.

## Purpose and fit

Review a visitor’s current selection before checkout.

## Route, identity and parents

- Illustrative route: `/cart/`. Keep the verified project canonical route.
- Parent(s): Product/shop or selection journey.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Actual cart state; accurate item/availability totals from the platform; empty state; supported onward route.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link canonical product pages and checkout; preserve session ownership.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

An empty-cart response is only evidence for that state. No test additions, quantity mutations or purchases are authorized by catalog research.
Choose include, embed, defer or omit with evidence. Record unavailable counterparts
as embedded-only, disabled, not applicable or unresolved. Do not manufacture routes
to complete an archive/single pair or multiply every possible filter combination.

## Structure and implementation handoff

No exact dedicated `norml-page-structures` member spec was verified for this variant.
Read its nearest matching page/block specs for genuinely shared elements; use the
explicit project brief and record remaining structure gaps. Hand identity, roles,
parents, route, sources and unresolved decisions to `sitemap planning`; actual
backend logic, forms, commerce and tool behavior remain implementation work.

## Pattern provenance

Generalized catalog pattern; verify fit and behavior on the target project.
Read [pattern notes](../../standards/pattern-notes.md) for abstraction limits; verify target content and functional behavior independently.
