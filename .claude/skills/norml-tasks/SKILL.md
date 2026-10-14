---
name: norml-tasks
version: 1.0.0
description: >
  Turn thought dumps into sourced goals, prioritized task files, executable milestone plans and verified resume state in the user’s own workspace or repository. Use for organize these thoughts, capture tasks, prioritize, plan a project, resume, park, verify phase, or synchronize GitHub issues. Works file-native with optional user-configured GitHub mirroring.
metadata:
  author: Norml Studio
---


# Norml Tasks

A standalone Markdown planning system. Task files own scope, status, steps and evidence; the
index supplies navigation. Planning does not authorize implementation, publication or spending.

## First-run discovery

Resolve the project, actual owner and authorized filesystem root from the request and current
project instructions. Read existing `.claude/tasks/config.json`, goals, index and relevant tasks.
Search all mapped workspace/repository planning homes and any active tool-owned `.planning/`
before creating another store. An unavailable counterpart is partial coverage, not an empty backlog.

Choose [workspace planning](recipes/workspace-planning.md) for general coordination/content/design
in any user-configured folder; choose [repository planning](recipes/repository-planning.md) for code.
The local filesystem is sufficient. Python 3.10+ runs the bundled structural helper. Optional GitHub
mirroring needs authenticated `gh`, a verified owner/repository and explicit issue-write authority.
It is disabled by default, including repository stores, until those requirements are met.

Read [layering](standards/layering.md), [planning model](standards/planning-model.md), and the
[workspace](schemas/planning-workspace.md), [task](schemas/task-record.md), and
[milestone definitions](schemas/milestone-documents.md) as the operation requires.

## Routing

| Request | Procedure |
|---|---|
| Capture, organize, prioritize | [Capture and prioritize](recipes/capture-and-prioritize.md) |
| General coordination/workspace | [Workspace planning](recipes/workspace-planning.md) |
| Development/repository planning | [Repository planning](recipes/repository-planning.md) |
| Discuss, plan, execute, verify phase | [Milestone planning](recipes/plan-milestone.md) |
| List, next, progress, resume, park, block, done | [Review and resume](recipes/review-and-resume.md) |
| Explicit GitHub mirror/sync | [Issue reconciliation](recipes/sync-github-issues.md) |
| Requested legacy upgrade | [Preserving upgrade](migrations/upgrade-v2.md) |

Storage choice and depth are independent. Quick tasks use config, goals, `items/`, a linked index
and source captures. Substantial initiatives add distinct `milestones/{slug}/` with requirements,
roadmap, persistent state, phase context/plans/summaries/verification. Create folders only for actual
content; never overwrite an old initiative to begin a new one.

## Operating loop

1. Locate and read current owner/context, mapped surfaces and selected dependencies.
2. Preserve the exact request in `captures/` before refining it. Original language, author/date,
   known source identity and later corrections remain separate from interpretation. Existing
   canonical transcripts are linked rather than copied. Redact any exposed secret.
3. Classify outcomes, accepted decisions, constraints, questions, ideas and actionable work.
   Deduplicate by intended outcome across mapped tasks and configured remote issues.
4. Write one canonical task per independently verifiable outcome with a stable owner-wide ID.
   Link its source, goals, bounded scope, acceptance checks, ordered steps and next action.
5. Select Now/Next/Someday/Blocked/Done and P0–P3 with qualitative reasons. Dependencies and
   explicit user priority determine ordering; no guessed effort scores or delivery forecasts.
6. Plan phases when needed. Suggest only a small provisional set of actually available skills;
   execution reads their current contracts. No matching skill is a valid finding.
7. Execute only when requested. Preserve ownership and current state; scope changes stay explicit.
8. Verify observable outcomes and regressions. Gaps create linked repair work. A checked box,
   closed issue, merged PR or created file does not prove acceptance.
9. Update canonical tasks first, derive index/state second, reconcile optional mirrors last.
   Leave exact resume state and disclose partial access, conflicts and pending checks.

## Boundaries and optional handoffs

One canonical task; indexes/issues/plans point to it. Cross-owner IDs are `owner-id::TASK-NNN`.
Retain completed/canceled IDs. Cancellation does not satisfy a dependency. Preserve concurrent
changes by re-reading before writing and refusing stale index replacement.

`planning.commit_docs` controls inclusion, never Git authority. Use project Git policy, preserving
unrelated work and hooks; optional bundled `norml-git` provides full mechanics. Worktrees must
pass local-file/history/consumer preservation before removal. A parked claim remains owned until
explicit protocol handoff/release; never clear a shared remote lease merely because local work stops.

No company tool registry, cloud drive, billing tracker or external planning runtime is required.
Do not invent time/cost estimates, people assignments, deadlines or approved decisions. External
tracker adapters are optional, opt-in and subordinate to the chosen canonical task file. Issue
creation does not authorize comments/messages or changing repository visibility.

## Validation

Run [planning integrity](qa/planning-integrity.md). The helper checks structure and local
references; it does not perform domain acceptance, sync GitHub or migrate old stores:

```bash
python3 "{skill-root}/scripts/planning.py" index "{planning-root}" --write
python3 "{skill-root}/scripts/planning.py" check "{planning-root}"
python3 "{skill-root}/qa/test-planning.py"
```

Resolve placeholder anchors before executing. Examples are fictional. An existing external GSD
namespace remains canonical until an explicitly verified cutover; no competing execution state.
