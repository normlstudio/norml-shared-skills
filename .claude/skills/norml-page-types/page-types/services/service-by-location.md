# Service × location

Family: [Services](services.md). Member ID: `services/service-by-location`.
Logical role: `intersection`.

## Purpose and fit

Explain how one real service is available in one verified service area.

## Route, identity and parents

- Illustrative route: `/services/{service}/{location}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Service single; location-first /areas-of-service/{location}/{service}/ is an alternative.
- Identity: One unique tuple of the referenced canonical parents; store contextual differences only.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

References to service and area entities; availability and delivery differences; local evidence; appropriate action.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link both canonical parents, relevant local proof, and nearby eligible alternatives.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Evaluate only verified available pairs. Choose one route orientation; do not publish both orientations as duplicate pages. Do not claim a physical office from a service-area relationship.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

Read `the optional installed page-structure catalog`.  This is a fit reference, not permission to change its requirement levels. Read the linked blocks from that sibling before scaffolding.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
