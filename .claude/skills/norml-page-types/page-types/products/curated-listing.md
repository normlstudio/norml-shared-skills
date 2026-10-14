# Curated merchandising listing

Family: [Products](products.md). Member ID: `products/curated-listing`.
Logical role: `archive`.

## Purpose and fit

Browse a maintained selection such as sale items, new arrivals or gifts.

## Route, identity and parents

- Illustrative route: `/{selection}/`. Keep the verified project canonical route.
- Parent(s): Shop or merchandising navigation.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Defined live predicate or curated members; selection purpose; current products and lifecycle.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link canonical products, relevant categories and any real configurator.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

Sale/new/gift labels are listing variants, not new product entities. Criteria need an owner; do not infer recency from a page label or approve every filter URL as public.
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
