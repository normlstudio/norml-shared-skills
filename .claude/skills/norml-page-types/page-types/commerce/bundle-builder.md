# Bundle/quantity-set builder

Family: [Commerce and customer journeys](commerce.md). Member ID: `commerce/bundle-builder`.
Logical role: `utility`.

## Purpose and fit

Choose multiple eligible products as one supported bundle/cart selection.

## Route, identity and parents

- Illustrative route: `/sets/`. Keep the verified project canonical route.
- Parent(s): Product catalog or related product category.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Canonical products; eligible selection rules; maintained promotion/quantity logic; platform-owned pricing/cart handoff.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link product records and actual cart; saved presets are states of this same builder unless separately contracted.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

Source shows a selectable sets page, not proof that cart discounts calculate correctly. No hardcoded copied promotion figures in the reusable specification.
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
