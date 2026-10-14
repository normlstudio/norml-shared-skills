# Services

Family ID: `services`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

The business offers identifiable services that visitors need to compare or understand individually.

**Skip or use another family:** A single undifferentiated offering may live on one page; a packaged product is not automatically another service.

## Canonical entity and model

One canonical service, with optional category and contextual relationship records.

Repeatable services suggest a collection; one-off services may be Pages. WordPress mapping is decided by WordPress architecture review.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Make the service range understandable and route visitors to the relevant offer. |
| `single` | [single.md](single.md) | single | Explain one service and its scope so a visitor can decide whether it fits. |
| `category-archive` | [category-archive.md](category-archive.md) | taxonomy-archive | Explain and browse a meaningful subset of services. |
| `service-by-location` | [service-by-location.md](service-by-location.md) | intersection | Explain how one real service is available in one verified service area. |
| `subservice-single` | [subservice-single.md](subservice-single.md) | single | Understand a narrower supported scope within a broader service. |
| `contextual-archive` | [contextual-archive.md](contextual-archive.md) | archive | Find eligible contextual service destinations across places or other approved axes. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Services → service category → service single. Service × location lives here. Industry × service lives in industries/industry-by-service.md; do not create a second specification or URL for the same pair.
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

## Additional project patterns

Understand a narrower supported scope within a broader service. Find eligible contextual service destinations across places or other approved axes.
Read [pattern notes](../../standards/pattern-notes.md) and the new
member files for their exact matching, model and omission distinctions.
