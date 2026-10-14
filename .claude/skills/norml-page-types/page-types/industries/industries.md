# Industries

Family ID: `industries`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Different industries have distinct needs, constraints, vocabulary or buying contexts that the organization can substantiate.

**Skip or use another family:** Historical client tags alone do not justify a public industry family; an audience role is not an industry.

## Canonical entity and model

One canonical industry; optional industry-service and industry-location relationship records.

Industry content can be a collection or substantial taxonomy-term landing pages; reuse existing classification when suitable.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Help visitors find the business sector that matches their context. |
| `single` | [single.md](single.md) | single | Explain the organization’s relevance to one industry and orient visitors within it. |
| `industry-by-service` | [industry-by-service.md](industry-by-service.md) | intersection | Explain one service in the context of one industry, as a child of that industry in the industry-first model. |
| `industry-by-location` | [industry-by-location.md](industry-by-location.md) | intersection | Describe a verified industry context in a particular place when geography changes the visitor’s needs. |
| `subindustry` | [subindustry.md](subindustry.md) | single | Explain a real narrower sector within a broader industry. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Industries → industry single → industry × service or industry × location. A sector/subsector can add depth when it is a real hierarchy. Services link to the same industry-service records, regardless of route orientation.
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
