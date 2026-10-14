# Blog and editorial articles

Family ID: `blog`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

The organization publishes substantive editorial articles with a maintainable author/topic system.

**Skip or use another family:** Do not use a blog post to stand in for a canonical service, product or legal document.

## Canonical entity and model

One editorial article plus topic and author relationships.

WordPress posts or an existing editorial collection; author records and public team profiles may be distinct.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Browse current and historical editorial work. |
| `single` | [single.md](single.md) | single | Deliver one editorial article with traceable authorship and useful onward reading. |
| `topic-archive` | [topic-archive.md](topic-archive.md) | taxonomy-archive | Browse articles about one stable topic. |
| `author-archive` | [author-archive.md](author-archive.md) | archive | Browse articles credited to one author. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Blog archive → article single; optional topic and author archives. News can be a distinct lifecycle or a section in this collection.
Read [architecture principles](../../standards/architecture.md) before selecting
depth, classifications or combinations. Parent URLs do not dictate CMS storage.
Intersections reference canonical entities and have one owner and canonical route.

## Eligibility and content truth

Use the brief/SMC, actual inventory and approved records to decide include,
embed, defer or omit. Read each member’s distinct evidence/omission requirements.
This family does not fabricate client entities or authorize page generation.
Real facts and relationship-specific differences need maintained source owners.

## Handoff

Record family/member IDs, source version, entity/tuple, disposition/evidence,
observed/planned/proposed state, logical/native roles, parent(s), route, hub/single
availability, relationships/depth, content owner/source and unresolved work in
the project’s existing architecture record. Read each selected member’s exact
structure fit or gap; `norml-page-structures` owns blocks and elements.
