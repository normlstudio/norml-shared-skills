# Industry × service

Family: [Industries](industries.md). Member ID: `industries/industry-by-service`.
Logical role: `intersection`.

## Purpose and fit

Explain one service in the context of one industry, as a child of that industry in the industry-first model.

## Route, identity and parents

- Illustrative route: `/industries/{industry}/{service}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Industry single; canonical service is the other parent.
- Identity: One unique tuple of the referenced canonical parents; store contextual differences only.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

References to the industry and service; distinct needs/workflows; delivery implications; appropriate proof; next action.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link the industry parent and canonical service; the service page links back to this same record.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

This file owns the unordered industry-service pair. /services/{service}/industries/{industry}/ is an alternative orientation, not another page. Enable only individually eligible pairs.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
