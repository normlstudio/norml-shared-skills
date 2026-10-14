# Milestone documents — planning and verification records

A milestone is a bounded initiative under `.claude/tasks/milestones/{slug}/`.
This document defines the related records together so the AI understands their
relationships. It replaces separate blank outlines for every project/phase file.
Create each document from actual project evidence, following
[the milestone recipe](../recipes/plan-milestone.md).

## Milestone-level records

| File | Required content | Responsibility |
|---|---|---|
| `project.md` | Current reality, core value, validated facts, active scope, exclusions, sourced constraints, locked decisions/rationale, source links and update event | Defines this initiative, not a second whole-product strategy |
| `requirements.md` | Atomic requirement ID, observable outcome, goal, source, status, owning phase; deferred requirements with reason; traceability table to plans | Says what must be true |
| `roadmap.md` | Milestone outcome; phases with ID, goal, requirements, dependencies, status and plan links; coverage table | Orders phase outcomes |
| `state.md` | Current phase/plan/task/status; last completed event/evidence; one next action; blockers; recent decisions; links to active context, plan, summary and verification | Resumes the work without the original chat |

Each active requirement belongs to exactly one phase and at least one plan
before execution. IDs are scoped to the milestone and never reused. Phase
statuses: Not started, Discussing, Ready to plan, Planned, In progress,
Needs verification, Blocked, Complete, Deferred. Requirement statuses:
Pending, In progress, Blocked, Complete, Deferred.

## Phase records

All phase records live inside `phases/01-phase-slug/` under that milestone.

| File | Required content | Create/update when |
|---|---|---|
| `context.md` | Goal boundary, locked decisions, preferences/constraints, deferred ideas, agent discretion, material open questions, sources | Discussing the phase |
| `research.md` | Consequential questions, sourced findings, planning implications, decisions enabled, remaining uncertainty | Only when existing evidence cannot answer a material question |
| `01-01-plan.md` | Objective, requirement IDs, dependencies, must-haves, bounded file scope, ordered canonical task links, provisional suggested skills (or task-shortlist links), validation, risks/preservation, non-goals and Git policy pointer | Planning a bounded piece of the phase |
| `01-01-summary.md` | Observed result, requirements advanced with evidence, meaningful changes/paths, validation results, decisions/deviations, remaining work and Git status | After execution, or as an explicitly partial interruption summary |
| `verification.md` | Verdict, phase goal, must-have/evidence/results table, requirement/plan/evidence/results table, regression checks, gaps/repair links, completion decision | Verifying actual outcomes |

## Task and plan relationship

Plans order owner-wide `TASK-NNN` records and explain which requirement each
advances. Scope and integration expectations are appropriate in a plan; task
steps/status/evidence remain in their canonical item files. A plan's link to an
item from its phase directory has the shape
`../../../../items/task-001-describe-action.md`. Root roadmap links include the
phase path, e.g. `phases/01-onboarding/01-01-plan.md`. Resolve links from the
actual file location; do not copy paths blindly from an example.

## Evidence and completion

Verification verdicts are Passed, Gaps found, or Blocked. No result defaults to
Pass. Pending checks, unresolved questions and missing human acceptance remain
explicit. Every failed must-have creates linked repair work and prevents phase
completion. A summary may say what changed; verification decides whether the
intended outcome is supported by evidence.

Completing a milestone retains its folder and task identities, updates active
selection in config, and evaluates the parent goal separately. A new milestone
gets a new folder. See the [worked milestone](../examples/planning-a-milestone.md)
for how the records connect; its illustrative state is not completion evidence.
