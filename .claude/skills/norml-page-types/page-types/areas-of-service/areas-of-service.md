# Areas of service

Family ID: `areas-of-service`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

The business serves multiple verified geographic areas and visitors need to understand coverage.

**Skip or use another family:** A service area is not a branch address, office, or license jurisdiction by default.

## Canonical entity and model

One area (country, region, city, neighborhood or another real coverage unit).

Collection or geography taxonomy with substantive term pages; entity and route hierarchy are separate decisions.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Show where services are actually available. |
| `single` | [single.md](single.md) | single | Explain coverage and how visitors in one area can obtain the applicable offers. |
| `child-area` | [child-area.md](child-area.md) | single | Describe a narrower area within a genuine coverage hierarchy. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Coverage archive → area single → optional child area. Service × location remains in services/service-by-location.md, even if its canonical route is nested here.
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
