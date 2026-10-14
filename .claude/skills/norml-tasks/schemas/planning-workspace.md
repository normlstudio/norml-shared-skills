# Planning workspace — which files exist and what they contain

This is a definition for the AI creating a project's planning workspace. It is
not a blank project document. Create project files from their actual context;
never copy this entire document into a project.

The workspace is `{owner}/.claude/tasks/`. Ownership and placement rules live in
[the location resolver](../standards/layering.md); the lifecycle and status rules
live in [the planning model](../standards/planning-model.md).

## Minimum workspace

| File/directory | Required content | When to create |
|---|---|---|
| `config.json` | Owner identity, location map and policy defined below | First task |
| `goals.md` | Sourced outcomes and current focus | First task; explicitly say if no goal is established |
| `items/` | One canonical file per task; see [task definition](task-record.md) | First task |
| `tasks.md` | Linked navigation generated from task files | First task |
| `captures/` | Original requests and language, canonical meeting pointers, and disposition mapping | For each new request or correction; one capture may source several tasks |
| `milestones/` | Bounded initiatives; see [milestone documents](milestone-documents.md) | Only when project depth is needed |
| `sync/` | Confirmed issue snapshots and operation log | Only when repository issue mirroring is enabled |

## Configuration fields

| Key | Contract |
|---|---|
| `schema_version` | `3`; older/missing version is a legacy store, never silently overwritten |
| `project_id` | Stable project slug shared by all its owners |
| `owner_id` | Unique immutable owner slug, e.g. `sample-product-plugin` |
| `storage` | `workspace` or `repository` |
| `locations.workspace` | Null if unresolved/not applicable, otherwise `{owner_id, path}` relative to the user-configured workspace root, ending in `.claude/tasks` |
| `locations.repositories` | Array of `{owner_id, repository, planning_path}`; repo-relative path ending in `.claude/tasks`. `repository` may be omitted or null for local-only planning; a verified GitHub `owner/repository` is required only when mirroring is enabled |
| `planning.lane` | `quick` or `project`; project depth can also keep quick tasks |
| `planning.active_milestones` | Array of existing milestone folder slugs; one by default, more only for explicit concurrent streams |
| `planning.canonical_system` | `norml-tasks`; external GSD remains untouched until explicit cutover |
| `planning.commit_docs` | Boolean inclusion policy; repository default true, workspace false; existing false requires explicit policy change |
| `github.enabled` | Boolean; true only for repository storage with a verified repository map |
| `github.repository` | Exact repository identity or null when disabled |
| `github.task_scope` | `all-concrete` by default; project-specific narrower policy must be documented and honored |
| `github.category_labels` | Optional category-to-existing-label mapping; never invent remote labels |
| `workflow` | Research when useful, verification mandatory, no unsolicited auto-advance |

A repository store works without any hosted remote or GitHub account. When issue mirroring is
disabled, its location needs only the owner ID and portable planning path; `repository` may be
omitted or null. Enabling GitHub mirroring requires the verified `owner/repository` identity
in both the owning location and `github.repository`. No machine-specific paths, connection config or secrets. Document unresolved
counterparts in the project context; null is not a declaration that no other
store exists. The same project's reciprocal maps must agree on owner IDs and
paths. workspace/repository task namespaces stay distinct.



For a new workspace owner: use `storage: workspace`, `commit_docs: false`,
`github.enabled: false`. For a verified repository owner: default to repository
storage, tracked planning and disabled issues until explicit opt-in, subject to the existing project
policy. Start with `lane: quick`, `active_milestones: []`, no category labels,
`research_when_needed: true`, `verify_before_complete: true`, `auto_advance: false`.
These booleans belong under `workflow`; `commit_docs`, `lane`, active milestones
and canonical system belong under `planning`. Use actual verified project and
owner IDs. An unresolved value stays null with an explanation, never a plausible
placeholder presented as configured.

## Goal document

`goals.md` has four sections: Current focus, Long-term outcomes, Short-term
outcomes, and Deferred or achieved outcomes. A goal declaration is an H3 starting
with its stable ID, such as `### GOAL-01 — Customers can finish setup`.

Each goal states its source, observable success check, current evidence and
status (`active`, `achieved`, `deferred`, `canceled`). A short-term goal names its
parent goal and supporting tasks. Keep the ID when the outcome's wording changes.
If no goal is grounded yet, say so; an empty task goal list is allowed. Do not
invent goals, commitments or deadlines just to populate a document.

## Central task index

`tasks.md` contains owner identity, links to goals/config and active milestone
states, then Now / Next / Someday / Blocked / Done tables. Each row links a task
file and shows priority, status, goal IDs, dependency IDs and its optional issue.
Order by rank then stable ID within the queue. Task files own those values;
update the task first and rebuild using `scripts/planning.py index --write`.
Never insert full task instructions into the index.

## Preserving a thought dump

A capture is source material, not a task. Its destination is
`captures/yyyy-mm-dd-topic.md`, not a generic `capture.md` in the project root.
It contains source/date, original wording, organized meaning, and a disposition
table mapping each meaningful part to a goal, task, decision, deferred idea or
unresolved question. Original meeting dialogue is a pointer to the configured canonical meeting archive'
archive, not another transcript copy. Even one-line input receives a capture with its source and original language.

See [organizing a thought dump](../examples/organizing-a-thought-dump.md) for a
filled example. The example is illustrative, not a default product plan.
