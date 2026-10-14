# Search results

Family: [Search and journey states](utility.md). Member ID: `utility/search`.
Logical role: `utility`.

## Purpose and fit

Find existing content by a visitor query.

## Route, identity and parents

- Illustrative route: `/search/?q={query}`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Site-wide search entry.
- Identity: One system/query/journey state; no invented editorial record.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Query state; real results; useful empty/error state; supported destinations.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link canonical content records rather than duplicate search URLs.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

A search result is not a new editorial archive. Verify query behavior during implementation.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
