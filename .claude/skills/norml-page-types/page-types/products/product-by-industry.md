# Product × industry

Family: [Products](products.md). Member ID: `products/product-by-industry`.
Logical role: `intersection`.

## Purpose and fit

Explain a product in a distinct industry context.

## Route, identity and parents

- Illustrative route: `/products/{product}/industries/{industry}/`. Preserve an existing canonical route unless change is authorized.
- Parent(s): Product single; industry single is the other parent.
- Identity: One unique tuple of the referenced canonical parents; store contextual differences only.
- Native role/model: resolve with `WordPress architecture review` for WordPress. Logical role does not force a native query or CPT.

## Content responsibility

Product/industry references; industry-specific use and constraints; relevant product proof.
Use verified project sources. Shared entity facts remain canonical; this member
owns only its purpose-specific information. These are information responsibilities,
not a prescribed visual block sequence.

## Relationships and navigation

Link both parents and approved product resources.
Record navigation parents, URL parents and record relationships separately.

## Eligibility, omission and variants

Create only when the product-context page has a job separate from the industry hub and industry-service pages.
Select include, embed, defer or omit with evidence. Any public-route omission
needs an explicit availability state in the project handoff; never create an empty
page to fill this contract. Intersections also pass the per-pair gate in
[architecture principles](../../standards/architecture.md).

## Structure and implementation handoff

No exact catalog match; use the explicit project brief and record the structure gap.
Hand family/member, source version, evidence/disposition, state, identity, logical
and native roles, parents/route, content source and unresolved work to
`sitemap planning`. Actual CMS decisions and code remain downstream.
