# Contact and enquiries

Family ID: `contact`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors need a verified way to reach the organization or make an enquiry.

**Skip or use another family:** Different form states are utility pages; branch directories belong to locations.

## Canonical entity and model

Organization contact routes, optionally qualified by real enquiry intent.

Usually singleton Page with shared contact data; separate enquiry pages only when the journey differs.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `contact-hub` | [contact-hub.md](contact-hub.md) | singleton | Reach the right real person, channel or enquiry flow. |
| `enquiry` | [enquiry.md](enquiry.md) | singleton | Collect information for one materially different enquiry purpose. |
| `listing-submission` | [listing-submission.md](listing-submission.md) | singleton | Supply an external offer or organization for a defined review process. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Contact hub → optional enquiry destination; locations can link to it.
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

Supply an external offer or organization for a defined review process.
Read [pattern notes](../../standards/pattern-notes.md) and the new
member files for their exact matching, model and omission distinctions.
