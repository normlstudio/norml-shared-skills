# Brand landing

Family: [Brands and manufacturers](brands.md). Member ID: `brands/single`.
Logical role: `single`.

## Purpose and fit

Browse products associated with one verified brand.

## Route, identity and parents

- Illustrative route: `/brand/{brand}/`. Keep the verified project canonical route.
- Parent(s): Brand index or shop/product navigation.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Brand identity; eligible products; relevant categories/context; sourced manufacturer distinction where needed.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link product singles, catalog categories and equivalent brand navigation destinations.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

A native brand term archive is still one-brand logically. the FAQ example also has /polaroid/ category entry: compare audience/query purpose and avoid duplicate destinations by inference.
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
