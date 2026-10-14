# Search and journey states

Family ID: `utility`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors need system navigation or a clear response to a journey outcome.

**Skip or use another family:** Do not force search, 404, thank-you or login into archive/single pairs or public content collections.

## Canonical entity and model

A system query/state or journey result, not an editorial entity.

System routes or singleton states; an informational-site catalog does not own account-app architecture.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `search` | [search.md](search.md) | utility | Find existing content by a visitor query. |
| `not-found` | [not-found.md](not-found.md) | utility | Recover from a missing destination. |
| `thank-you` | [thank-you.md](thank-you.md) | utility | Acknowledge a verified completed submission and explain the supported next step. |
| `communication-preferences` | [communication-preferences.md](communication-preferences.md) | utility | View or control supported subscription/communication choices. |
| `newsletter-signup` | [newsletter-signup.md](newsletter-signup.md) | singleton | Subscribe to a maintained publication through a real supported route. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Search → canonical result; 404 → recovery routes; thank-you → verified successful enquiry.
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

View or control supported subscription/communication choices. Subscribe to a maintained publication through a real supported route.
Read [pattern notes](../../standards/pattern-notes.md) and the new
member files for their exact matching, model and omission distinctions.

## Matching adjacent patterns

Transactional customer/cart/selection states are in [commerce](../commerce/commerce.md). This catalog identifies companion page roles; it does not own a full authenticated account application.
