# Membership/loyalty program single

Family: [Memberships and loyalty programs](memberships.md). Member ID: `memberships/single`.
Logical role: `single`.

## Purpose and fit

Explain one program’s real benefits and how someone joins.

## Route, identity and parents

- Illustrative route: `/club/ or /memberships/{program}/`. Keep the verified project canonical route.
- Parent(s): Site root or optional membership hub.
- Identity: reuse the family’s entity/query/state and its canonical relationships.
- Native role/model: delegate WordPress mapping to `WordPress architecture review`; a logical single can query a related collection.

## Content responsibility

Approved benefits; eligibility; sourced tier/progression rules; supported joining/account route.
The project owns real facts and runtime state. Keep shared entity facts canonical
and member-specific context separate. These are information responsibilities,
not a visual block prescription.

## Relationships and navigation

Link account/join and relevant terms; keep public explanation separate from private member balances.
Record navigation, URL and CMS hierarchy independently.

## Eligibility, omission and variants

Architecture review does not verify reward accrual, discounts or eligibility enforcement. Never infer actual membership status from a visit to the public page.
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
