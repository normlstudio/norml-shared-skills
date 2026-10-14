# Solutions, use cases and audiences

Family ID: `solutions`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors begin with a problem, use case or audience need that spans one or more offers.

**Skip or use another family:** Do not relabel identical service pages as solutions; a job role, industry and business problem are different axes.

## Canonical entity and model

One controlled solution/use-case/audience entity, with its kind recorded.

Collection or classified Pages; choose whether kinds share a collection or require separate collections from their editorial lifecycle.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Route visitors by the problem or use case they recognize. |
| `single` | [single.md](single.md) | single | Explain how one problem or use case is addressed across relevant offers. |
| `audience-archive` | [audience-archive.md](audience-archive.md) | archive | Help different visitor roles find relevant guidance. |
| `audience-single` | [audience-single.md](audience-single.md) | single | Explain relevance for one role or customer group. |
| `application-archive` | [application-archive.md](application-archive.md) | archive | Find products by the job or application they are suitable for. |
| `application-single` | [application-single.md](application-single.md) | single | Understand one application and browse suitable products. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Solutions archive → solution single; optional audience archive/single. Services and products are referenced offers, not duplicated as new entities.
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

Find products by the job or application they are suitable for. Understand one application and browse suitable products.
Read [pattern notes](../../standards/pattern-notes.md) and the new
member files for their exact matching, model and omission distinctions.
