# Industry × location

Family: [Industries](industries.md). Member ID: `industries/industry-by-location`.
Logical role: `intersection`.

## Purpose and fit

Describe a verified industry context in a particular place when geography changes the visitor’s needs.

## Route, identity and parents

- Illustrative route: `/industries/{industry}/locations/{location}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Industry single; canonical service-area single is the other parent.
- Identity: One unique tuple of the referenced canonical parents; store contextual differences only.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Industry and area references; relevant local context; actual reach/capability; sourced contextual claims.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link both parents and locally relevant resources or proof.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Optional; a place name alone adds no purpose. Do not imply industry × service × location approval; that needs its own explicit contract.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
