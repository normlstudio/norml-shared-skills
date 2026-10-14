# Brands and manufacturers

Family ID: `brands`. The family is the complete set of related destinations.
Member files are flat siblings; project URLs are instances, not new catalog files.

## Purpose and fit

Visitors shop or explore a catalog by the organization behind an item or by a verified manufacturer/brand classification.

**Skip or use another family:** Use providers for organizations with profile/offer relationships beyond a retail brand; do not make every product keyword a brand.

## Canonical entity and model

One verified brand identity and its actual product relationships; manufacturer and brand can be different.

Often product taxonomy terms, with editorial landing content when justified. Reuse existing product-brand data and record uncertain mappings.
Actual WordPress mapping belongs to `WordPress architecture review`; preserve a verified
inherited model and keep logical purpose distinct from native query role.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Find a brand represented in the catalog. |
| `single` | [single.md](single.md) | single | Browse products associated with one verified brand. |

Every member is an option. Projects do not necessarily need every hub
or counterpart; read each member’s provenance and omission conditions. Supported
generalizations are not claims of observed implementation.

## Relationships, depth and combinations

Optional brand index → one-brand landing → product singles/categories. A brand landing may list products without being a provider profile.
Read [architecture principles](../../standards/architecture.md). Native entity
relationships, URL nesting and navigation can differ. Extra public routes need a
distinct purpose and an explicit canonical decision, not only a stored relationship.

## Eligibility and content truth

Keep real records, content sources and operational state in the project. Select
include, embed, defer or omit using its actual evidence, purpose and owners.
Evaluate public hub/detail availability together without forcing useless pairs.
Page presence does not establish integration correctness or factual accuracy.

## Handoff and provenance

Record family/member, source version, identity, disposition/evidence, state,
logical/native roles, parents/route, counterpart availability, source owner,
structure fit and unresolved work in the existing architecture/sitemap artifact.
This family abstracts [generalized patterns](../../standards/pattern-notes.md);
member specifications describe generalized patterns; target observation is required.
