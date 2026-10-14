# Team-member single

Family: [About Us and people](about-us.md). Member ID: `about-us/single`.
Logical role: `single`.

## Purpose and fit

Describe one real person, their role, and relevant expertise.

## Route, identity and parents

- Illustrative route: `/about/{person}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): About Us hub; /team/{person}/ is an approved alternative.
- Identity: One canonical entity, collection query or singleton destination as appropriate to the role; actual project IDs are resolved from evidence.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Stable person identity; current role; approved biography/photo; attributed work or publications when available.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Return to About Us or the selected team directory; link authored work through the same person identity.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Public-profile approval and useful biography required; private staff data stays private.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

Read `the optional installed page-structure catalog`.  This is a fit reference, not permission to change its requirement levels. Read the linked blocks from that sibling before scaffolding.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
