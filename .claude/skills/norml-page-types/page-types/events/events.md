# Events

Family ID: `events`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors need to discover and understand real scheduled occurrences.

**Skip or use another family:** A recurring offering/program is distinct from a dated occurrence; a physical venue is a location.

## Canonical entity and model

One event occurrence or explicitly modeled series with occurrence records.

Collection with date/status and venue relationships; recurring series must avoid ambiguous duplicate identities.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Browse upcoming and past events with truthful availability. |
| `single` | [single.md](single.md) | single | Understand and attend/register for one actual occurrence. |
| `category-archive` | [category-archive.md](category-archive.md) | taxonomy-archive | Browse events of a meaningful type. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Event archive → event single; optional event-type archive.
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
