# Product-category archive

Family: [Products](products.md). Member ID: `products/category-archive`.
Logical role: `taxonomy-archive`.

## Purpose and fit

Browse products sharing a meaningful selection criterion.

## Route, identity and parents

- Illustrative route: `/products/category/{category}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Products archive.
- Identity: One canonical entity, collection query or singleton destination as appropriate to the role; actual project IDs are resolved from evidence.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Canonical category; eligible products; context supporting comparison.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link contained product singles and product archive.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

A category with no visitor purpose can remain a filter; a service category is a different family.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

Read `the optional installed page-structure catalog`. (commerce only) This is a fit reference, not permission to change its requirement levels. Read the linked blocks from that sibling before scaffolding.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
