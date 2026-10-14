# Programs and courses

Family ID: `programs`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

The organization offers structured programs, classes or courses with repeated delivery instances.

**Skip or use another family:** Do not confuse an evergreen program with an event date, or make every calendar slot a public page.

## Canonical entity and model

One program/course and optional session/cohort records.

Collection with separately governed sessions/cohorts; reuse an installed learning or enrollment model if present.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Choose a suitable program or course. |
| `single` | [single.md](single.md) | single | Explain the enduring offering independently from any one delivery date. |
| `session-single` | [session-single.md](session-single.md) | single | Explain one delivery instance when it needs its own shareable destination. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Program archive → program single → optional session/cohort single; sessions can stay embedded.
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

## Matching adjacent patterns

For a directory’s third-party learning offers and host/expert relationships, use [courses](../courses/courses.md). Reuse one canonical offer; do not mirror it into both families. Programs remains the owned recurring delivery/cohort model.
