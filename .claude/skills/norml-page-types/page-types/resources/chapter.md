# Guide/documentation chapter

Family: [Resources, guides and downloads](resources.md). Member ID: `resources/chapter`.
Logical role: `single`.

## Purpose and fit

Read one coherent section of a genuinely hierarchical guide.

## Route, identity and parents

- Illustrative route: `/resources/{guide}/{chapter}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Parent guide resource.
- Identity: One canonical entity, collection query or singleton destination as appropriate to the role; actual project IDs are resolved from evidence.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Chapter content; verified guide membership; ordering/navigation when appropriate.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link parent guide and adjacent chapters without duplicating the full guide body.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Split for navigation and maintainability, not arbitrary URL depth; documentation may warrant its own future family.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
