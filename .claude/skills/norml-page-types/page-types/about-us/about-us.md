# About Us and people

Family ID: `about-us`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

The organization needs a trust hub and may have public profiles for named people.

**Skip or use another family:** Do not publish a biography for every employee merely because a staff record exists.

## Canonical entity and model

Organization identity plus related people; these are distinct content records.

About Us is the logical archive/hub. It can be a singleton Page querying a team-member collection; it need not be a native CPT archive.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Present the organization and its people in one trust destination; the label can be About Us rather than Team. |
| `single` | [single.md](single.md) | single | Describe one real person, their role, and relevant expertise. |
| `team-archive` | [team-archive.md](team-archive.md) | archive | Help visitors browse people when the About Us page alone is insufficient. |
| `department-archive` | [department-archive.md](department-archive.md) | taxonomy-archive | Browse a meaningful department or practice group. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

About Us → team member; optional dedicated team listing and department listings. Person profiles can also link to authored content, but are not automatically WordPress author archives.
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

External instructors/practitioners belong to [experts](../experts/experts.md) when they are not the operator’s team. Shared person identity may support both roles without duplicating the biography record.
