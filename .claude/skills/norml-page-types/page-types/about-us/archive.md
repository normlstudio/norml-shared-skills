# About Us archive/hub

Family: [About Us and people](about-us.md). Member ID: `about-us/archive`.
Logical role: `archive`.

## Purpose and fit

Present the organization and its people in one trust destination; the label can be About Us rather than Team.

## Route, identity and parents

- Illustrative route: `/about/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Site root.
- Identity: One canonical entity, collection query or singleton destination as appropriate to the role; actual project IDs are resolved from evidence.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Organization story and identity; verified people selected for the hub; links to public profiles when those exist.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link each public person to the team-member single; use team-archive only if a separate directory helps visitors.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Record logical_role: archive and the actual technical role separately. An organization with no public people may use About Us as a singleton.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

Read `the optional installed page-structure catalog`.  This is a fit reference, not permission to change its requirement levels. Read the linked blocks from that sibling before scaffolding.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
