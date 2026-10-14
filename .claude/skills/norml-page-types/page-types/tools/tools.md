# Interactive tools and calculators

Family ID: `tools`. The family is the complete set of related destinations.
Member files are flat siblings; project URLs are instances, not new catalog files.

## Purpose and fit

A visitor can perform a bounded task on a public page: calculate, answer a quiz or run a timer/practice utility.

**Skip or use another family:** A tool is not an article with an embedded screenshot, a product configurator or a transactional checkout. Use a parent-page embed when no distinct destination is useful.

## Canonical entity and model

One maintained interactive tool with a defined input, operation and result/state contract.

Collection for several tools, or standalone routes for a small set. Tool state is not a published post by default; implementation is delegated.
Actual WordPress mapping belongs to `WordPress architecture review`; preserve a verified
inherited model and keep logical purpose distinct from native query role.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Choose a tool by the task it helps perform. |
| `calculator` | [calculator.md](calculator.md) | single | Explore an output from stated inputs and a maintained calculation method. |
| `quiz` | [quiz.md](quiz.md) | single | Answer a bounded set of questions and receive a supported category or recommendation. |
| `practice-tool` | [practice-tool.md](practice-tool.md) | single | Use a time/state-based utility such as a timer or guided sequence. |

Every member is an option. Projects do not necessarily need every hub
or counterpart; read each member’s provenance and omission conditions. Supported
generalizations are not claims of observed implementation.

## Relationships, depth and combinations

Optional tools index → calculator, quiz or practice-tool destination; informative copy supports the task. Result states stay within the tool unless a separate shareable result contract is approved.
Read [architecture principles](../../standards/architecture.md). Native entity
relationships, URL nesting and navigation can differ. Extra public routes need a
distinct purpose and an explicit canonical decision, not only a stored relationship.

## Eligibility and content truth

Keep real records, content sources and operational state in the project. Select
include, embed, defer or omit using its actual evidence, purpose and owners.
Evaluate public hub/detail availability together without forcing useless pairs.
Page presence does not establish integration correctness or factual accuracy.

## Handoff and provenance

Record family/member, source version, identity, disposition/evidence, state,
logical/native roles, parents/route, counterpart availability, source owner,
structure fit and unresolved work in the existing architecture/sitemap artifact.
This family abstracts [generalized patterns](../../standards/pattern-notes.md);
member specifications describe generalized patterns; target observation is required.
