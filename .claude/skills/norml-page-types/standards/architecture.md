# Page-family architecture principles

## Vocabulary

| Term | Meaning in this catalog |
|---|---|
| Family / page type | A named set of related destinations with a content model and purpose |
| Member | A reusable page contract within a family; one file per kind of destination |
| Instance | One real page, e.g. one industry or one person; never a new catalog file |
| Archive/hub | A destination organizing access to a collection; may contain substantial narrative |
| Single | A destination about one member entity or relationship record |
| Taxonomy archive | A listing restricted to a meaningful classification |
| Singleton | A one-off destination, such as home or Contact |
| Intersection | A destination for one eligible tuple of canonical entities |
| Utility | A system/query/journey state rather than editorial content |

An intersection normally has a single-record detail role technically, but its
logical role is `intersection` so its eligibility and two parents remain visible.
An industry single implemented as a substantial taxonomy-term page may technically
be a taxonomy route; logical purpose and native query role must remain separate.

## Family, label, hierarchy and storage are independent

Archive/single thinking describes the visitor’s relationship to a collection.
It does not require every family to be a WordPress CPT or every archive to use
`archive-{post_type}`. About Us can organize people while WordPress renders it as
a Page; team-member singles can come from a separate collection. The archive label
can be About Us, Journal, Work or another project-approved term.

The native WordPress template follows the actual query type. A built-in posts
index, a Page, a CPT archive and a taxonomy route have different template paths.
Do not decide these from labels or sibling URL counts. Delegate verified mapping
to `WordPress architecture review`; preserve inherited models unless a change is authorized.
See the official [template hierarchy](https://developer.wordpress.org/themes/classic-themes/basics/template-hierarchy/)
and [post-type registration](https://developer.wordpress.org/plugins/post-types/registering-custom-post-types/).

There are four different relationships to record:

1. **Navigation parent:** where a visitor enters and returns.
2. **URL parent:** which path, if any, contains the route.
3. **Entity relation:** which records the page references.
4. **CMS hierarchy:** whether storage actually uses parent/child records.

They need not coincide. `/team/{person}/` can return to `/about/`.
A `/services/{service}/{area}/` record can reference two independent collections
without either collection being a native parent of the other.

## Archive and single decisions

For a collection, evaluate the hub and detail destinations together. Explicitly
record each as public, embedded-only, disabled, not applicable or unresolved.
A short FAQ answer/testimonial can be embedded-only. Do not publish useless
singles just to satisfy a pair. Home, Contact and system states do not need pairs.
When singles exist, provide a coherent return/browse destination; explain an
intentional omission rather than inventing an archive. Never infer that an absent
route has been implemented.

## Multiplication and canonical ownership

Supported intersections are **options**, never an instruction to generate all
combinations. A catalog member is one reusable specification, not one file per
service, industry or area. Twenty services × thirty areas gives 600 possible
pairs mathematically; it proves neither eligibility nor approval of 600 pages.

For each proposed tuple verify:

- Both canonical entities exist or are explicitly approved-planned.
- The relationship is real: availability, relevance or compatibility is evidenced.
- The visitor’s question and action differ enough to justify a destination.
- Distinct useful content/proof can be maintained; removing entity labels still
  leaves meaningful differences. Name substitution alone fails this gate.
- One owner can keep relationship-specific facts accurate as parents change.
- One canonical route and identity are selected; overlapping existing pages are
  reconciled. Navigation/internal links make both parents discoverable.
- The project’s claim, publication and implementation gates can be met.

Disposition: include only eligible pairs; embed limited contextual information
in a parent when sufficient; defer evidence-dependent work; omit unsupported pairs.
This is a product/navigation/content gate; SEO validation can add checks but is
not the sole reason for this catalog or for a page’s existence.

Canonical homes for seed combinations:

| Pair | Member owner | Alternative route orientation |
|---|---|---|
| industry × service | industries/industry-by-service.md | Industry-first or service-first, one canonical route |
| service × location | services/service-by-location.md | Service-first or service-area-first, one canonical route |
| industry × location | industries/industry-by-location.md | Industry-first default; another orientation needs an explicit decision |
| product × industry | products/product-by-industry.md | Product-first default; no duplicate industry-first copy |

Here `location` in service/industry combinations means a verified **service area**
unless the project explicitly selects a physical location relationship. Resolve
the entity kind first; coverage and offices are different facts.
The same unordered pair has one relationship identity even when its path changes.
Reverse references point to its owning file; do not clone a member into two folders.

More dimensions or deeper branches are allowed only after explicit matching,
eligibility and a member contract. No universal maximum exists. A particular
project can forbid industry × service × location; a shared two-axis catalog
never overrides that constraint or implicitly authorizes a third axis.

## Content truth and minimum handoff

Canonical service/product facts live on their entity records. Industry/area facts
live on their entity records. The relationship owns only contextual differences
and references. Classification listings query those relationships, not copied
content. A category, a filter, a rich term page and a nested detail page are
different decisions; do not add public URLs simply because the CMS permits them.

Persist chosen family/member, source version, disposition/evidence, state,
logical/native roles, identity, parent(s), route, hub/single availability,
relationships/depth, content owner/source, structure reference and unresolved work.
`sitemap planning` owns the complete site inventory, not this file. Reuse its
existing artifact and the project’s task system.
