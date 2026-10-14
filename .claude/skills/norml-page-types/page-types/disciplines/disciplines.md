# Disciplines and subject catalogs

Family ID: `disciplines`. The family is the complete set of related destinations.
Member files are flat siblings; project URLs are instances, not new catalog files.

## Purpose and fit

Visitors browse offerings by a broad subject or practice, with meaningful higher-level category groupings.

**Skip or use another family:** An organization’s sellable service belongs to services. A customer’s business sector belongs to industries. A subject grouping is neither by default.

## Canonical entity and model

A discipline/subject entity, related category entities and matching catalog offers. Category membership can be many-to-many.

Often rich taxonomy-term pages, but actual category/discipline storage and public status must be verified. Editorial text plus listings do not automatically make a CPT.
Actual WordPress mapping belongs to `WordPress architecture review`; preserve a verified
inherited model and keep logical purpose distinct from native query role.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Orient visitors across subjects. |
| `category-hub` | [category-hub.md](category-hub.md) | taxonomy-archive | Browse a broader subject category and its disciplines/offers. |
| `single` | [single.md](single.md) | single | Explain one subject and browse its related offerings. |

Every member is an option. Projects do not necessarily need every hub
or counterpart; read each member’s provenance and omission conditions. Supported
generalizations are not claims of observed implementation.

## Relationships, depth and combinations

Subject hub → category hub → discipline landing; discipline can list courses, providers, experts and specialties. Navigation hierarchy need not equal native term parent.
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
