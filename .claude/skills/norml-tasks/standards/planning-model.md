# Planning records and hierarchy

## Authority by artifact

| Artifact | Owns |
|---|---|
| `config.json` | Project/owner identity, verified locations, active milestone, Git/GitHub policy |
| `goals.md` | Long-term outcomes, short-term outcomes, explicit priority rationale |
| `items/task-nnn-slug.md` | One task's source, objective, status, queue, priority, dependencies, steps, evidence |
| `tasks.md` | Derived navigation index grouped by queue; links and short summaries only |
| `captures/yyyy-mm-dd-topic.md` | Original requests in their original language, or canonical archive pointers, with disposition mapping; source, never a second backlog |
| `milestones/{slug}/` | One bounded initiative's brief, requirements, roadmap, phase plans, evidence, resume state |
| `sync/github-state.json` | Last confirmed values needed to detect concurrent local/remote edits |
| `sync/github-log.jsonl` | Intent/result audit for issue mutations and ambiguous retries |

Task files are canonical. Editing an index row means first applying the change
to the corresponding task, then rebuilding the row. Prefer separate task files
over accumulating long descriptions in an index. Keep completed items in place;
filter the index for visibility, never delete historical IDs to tidy it.

## Identity

- `project_id`: stable project slug shared by its workspace and repository owners.
- `owner_id`: stable unique scope, e.g. `sample-product-coordination` and
  `sample-product-plugin`. Renaming a folder does not rename this ID.
- Goal IDs: `GOAL-01`; a short-term goal names its parent long-term goal.
- Task IDs: `TASK-001`; increase across all items at this owner, including closed
  records. Never reuse an ID; detect collision after fetch/re-read and before
  writes. Concurrent allocation conflicts must be repaired with explicit links.
- Requirement IDs: `AUTH-01`; scoped to a milestone.
- Phase/plan IDs: `01`, `01-01`; scoped to a milestone.
- Cross-owner tasks/goals: `owner_id::TASK-001` / `owner_id::GOAL-01`.
- Plan references: `milestone-slug/01-01`; execution tasks always have owner-wide
  `TASK-NNN` IDs. Legacy plan-local `01-01-T03` IDs remain import aliases.

## Status, queue, priority

These are separate dimensions:

- Status: `open`, `in-progress`, `blocked`, `done`, `canceled`.
- Queue: `now`, `next`, `someday`, `blocked`, `done`.
- Priority: `P0` active breakage/critical blocker; `P1` committed current outcome;
  `P2` valuable uncommitted work; `P3` speculative/lower priority.
- `rank`: positive integer ordering within a queue, selected with a reason.

Blocked status requires a concrete blocker and queue `blocked`. Done/canceled
use queue `done` (the index distinguishes them); completion needs evidence,
cancellation needs an explicit reason. In-progress requires `now`. Deferred
ideas are open/someday with a reason, not falsely completed tasks. Unblocking
returns to open/next or the explicitly selected now queue.

## Goal and milestone depth

Goals describe observable outcomes, a success check, current evidence, source,
and status (`active`, `achieved`, `deferred`, `canceled`). Separate long-term and
short-term sections in `goals.md`; short-term means the next outcome, not an
invented deadline. Pick one current short-term focus unless the user explicitly
maintains concurrent workstreams. Preserve exact source dates with provenance.

Quick tasks may link directly to goals. Project-depth work adds a milestone
whose atomic requirements map to one phase each and at least one plan before
execution. Plans reference canonical task files, not parallel editable task
bodies. Small task-local checklists are steps, not extra issue/task identities.
Multiple milestone folders may coexist; config identifies the active one(s),
and the index links their states. Never overwrite a previous roadmap to start
another initiative. A goal is achieved only when its stated success check passes;
a closed milestone does not automatically achieve the parent long-term goal.

## Source precedence

Resolve statements, not entire documents: explicit user corrections and locked
accepted decisions → newer explicitly superseding decisions → current
requirements/architecture → proposals/roadmaps → background. Keep incompatible
sources and ask the smallest unresolved decision. New prose is not automatically
an accepted decision. Navigation links do not form dependency cycles.

## Partial access and concurrency

Use existing project worktree/integrator rules via `norml-git`. Before replacing
an index or task, compare its content to what was read; changed → re-read and
merge. Cross-owner dependencies need current evidence from the referenced
canonical file. If unavailable, their satisfaction is unknown, not assumed.
Do not mark dependent work ready/complete based on a stale mirror.
