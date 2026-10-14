# FAQ and answers

Family ID: `faq`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors have recurring questions that deserve a navigable answer system; some answers may need their own URLs.

**Skip or use another family:** A short accordion in a service page does not require an FAQ collection or public answer singles.

## Canonical entity and model

One maintained question-answer record; optional topics.

FAQ Page with embedded answers, or a question collection with hub/topic/single routes when individual answers justify them.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Help visitors find verified answers to recurring questions. |
| `single` | [single.md](single.md) | single | Answer one question fully when a distinct destination improves navigation or sharing. |
| `topic-archive` | [topic-archive.md](topic-archive.md) | taxonomy-archive | Group related questions into a coherent browsing destination. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

FAQ archive → topic archive → answer single. Public singles are optional; explicitly record embedded-only questions rather than creating empty detail pages.
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

Product/model support topics are a topic-archive variant: keep the same question-answer records across topic listings. the FAQ example demonstrates hub → model topic → answer; no extra FAQ family is needed.
