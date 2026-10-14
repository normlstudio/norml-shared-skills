# Policy/document single

Family: [Policies and legal information](legal.md). Member ID: `legal/policy-single`.
Logical role: `singleton`.

## Purpose and fit

Present one authoritative approved document.

## Route, identity and parents

- Illustrative route: `/legal/{policy}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Legal hub or footer.
- Identity: One canonical entity, collection query or singleton destination as appropriate to the role; actual project IDs are resolved from evidence.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Approved exact policy text; responsible organization; revision/effective date when provided.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link relevant policies and organization contact as authorized.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Legal content comes from its approved owner; architecture decisions do not authorize legal edits.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
