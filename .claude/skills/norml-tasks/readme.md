# norml-tasks

> Turn original requests into prioritized task files, executable milestone plans and verified
resume state.

## The problem

Thought dumps mix outcomes, ideas, decisions and work. A long index can hide the original request
and make later sessions repeat or misread it.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Organize these thoughts | *"organize these thoughts"* |
| Capture tasks | *"capture tasks"* |
| Prioritize | *"prioritize"* |
| Plan a project | *"plan a project"* |
| Resume | *"resume"* |
| Park | *"park"* |
| Verify phase | *"verify phase"* |
| Synchronize github issues | *"synchronize GitHub issues"* |

## A typical run

1. Read owner context and every known mapped planning surface.
2. Capture exact wording, language, identity and later corrections.
3. Deduplicate, connect goals and rank bounded actions.
4. Use quick tasks or phases; execute only requested work.
5. Record evidence, rebuild index and leave one next action.

---

## Details

### Inputs

- An authorized project/workspace root and source request.
- Existing task/context maps when present. A local repository needs no hosted identity
  when GitHub mirroring is disabled; enabling it requires a verified `owner/repository`.
- Python 3.10+ for the helper; optional issue sync needs authenticated gh.

### What it creates or changes

- .claude/tasks/config.json, goals.md and a linked tasks.md index.
- One canonical items/task-nnn-slug.md per independent outcome.
- Verbatim source captures and correction pointers.
- Optional milestone requirements, roadmap, phase plans, evidence and state.

### Commands in depth

#### Organize these thoughts

*"organize these thoughts"* — Preserve original wording, separate goals/decisions/ideas/actions,
and deduplicate against mapped work.

#### Capture tasks

*"capture tasks"* — Create or amend one stable task record with source, scope, acceptance, steps
and next action.

#### Prioritize

*"prioritize"* — Use explicit user priority and real dependencies; explain ordering without
made-up effort scores.

#### Plan a project

*"plan a project"* — Choose quick tasks or milestone requirements, phases and plans according to
the actual outcome.

#### Resume

*"resume"* — Read current state, selected task, prerequisites and verification evidence before
continuing.

#### Park

*"park"* — Save exact resume state and reason; retain ownership according to its explicit
coordination protocol.

#### Verify phase

*"verify phase"* — Check observable requirements and regressions; pending human checks stay pending.

#### Synchronize github issues

*"synchronize GitHub issues"* — Use opt-in configured GitHub CLI reconciliation with managed
regions and post-write readback.

### Inside the package

- [SKILL.md](SKILL.md)
  Storage/depth/action router
- [capture-and-prioritize.md](recipes/capture-and-prioritize.md)
  Source-backed capture and ordering
- [plan-milestone.md](recipes/plan-milestone.md)
  Phase plan, execution and verification
- [task-record.md](schemas/task-record.md)
  Stable task identity and required sections
- [github-mirroring.md](standards/github-mirroring.md)
  Optional conflict-aware issue reconciliation
- [planning.py](scripts/planning.py)
  Structural validator and derived index
- [test-planning.py](qa/test-planning.py)
  Isolated integrity and stale-write checks

### Limits

- Capture/priority does not authorize implementation, publishing or spending.
- The structural helper does not verify domain acceptance or synchronize GitHub.
- GitHub is optional and disabled until configured and authorized.
- Cross-owner dependencies require current evidence from their actual owner.

### When something breaks

- **Index is stale.** Change canonical task files first, then run index --write.
- **Mapped store is unavailable.** Disclose partial coverage; do not infer no tasks or completed
  dependencies.
- **Remote issue and local task both changed.** Reconcile against the last-confirmed snapshot and
  retain conflicts.
- **Phase checks fail.** Create linked repair work; keep completion pending.

### Source of truth

[SKILL.md](SKILL.md) routes runtime operations. The linked procedures provide the full operational
checks. This guide explains the public package and does not add authority or claim live access.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
