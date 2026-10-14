# Checkout destination

Family: [Commerce and customer journeys](commerce.md). Member ID: `commerce/checkout`.
Logical role: `utility`.

## Purpose and fit

Complete the platform’s actual order journey.

## Route, identity and parents

- Illustrative route: `/checkout/`. Keep the verified project canonical route.
- Parent(s): Cart or supported direct purchase journey.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Eligibility/session prerequisites; platform-owned checkout state; actual delivery/payment integration boundaries.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link cart/recovery and authoritative order status after verified completion.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

Observed checkout request redirected to cart with an empty session. Full checkout/payment behavior remains unverified; do not claim a working form or place an order to prove this type.
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
