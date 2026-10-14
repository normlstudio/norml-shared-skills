# Plan and execute a milestone

Read `schemas/milestone-documents.md` for the document definitions and
`examples/planning-a-milestone.md` for a worked illustration.

Available for both workspace and repository planning. GSD supplies the discipline:
bounded context, explicit requirements, small executable plans, evidence, and
resume state. Domain skills supply actual execution and validation.

## 1. Initialize or ingest

Read the current context and both planning stores. Reuse an existing matching
milestone; otherwise create `milestones/{slug}/`. Derive `project.md` from source
intent: outcome, current reality, constraints, scope, exclusions, locked choices.
Separate accepted requirements from proposals using source precedence. Write
atomic observable requirements in `requirements.md`, each with source and goal.
Map each active requirement to one phase in `roadmap.md`, order real dependencies,
and state the observable phase goal. Write `state.md`; update config's active
milestone list and index links. Do not copy an overall workspace roadmap into a repo:
create a narrower implementation milestone linked to the relevant parent goal.

## 2. Discuss the selected phase

In `phases/01-slug/context.md`, capture locked decisions, preferences, constraints,
deferred ideas, agent-discretion areas and material unresolved questions. Do not
reopen accepted decisions without contradictory evidence. Resolve necessary
questions while continuing unrelated planning where possible.

## 3. Resolve uncertainty only when needed

Create phase `research.md` only when unstable external facts, an unfamiliar
integration, or a consequential unknown affects the plan. Browse current primary
sources when required; retain source links and planning implications. Existing
code and context may already answer the question. No ritual research deliverable.

## 4. Build an executable plan

Create one or more `01-01-plan.md` files using the milestone document definition. Each specifies an
observable outcome, goal/requirements, must-haves, real dependencies, bounded file
scope, ordered canonical task links, verification, risks and preservation.
Every independently actionable unit receives an owner-wide task file in `items/`.
The plan orders those IDs and explains integration; implementation steps/status
live in the task, not another full copy inside the plan. Record each task's
`milestone` and `plan`; no duplicate issue for the plan itself.

Include a provisional Suggested skills section using
[skill selection](../standards/skill-selection.md). Reference each task’s shortlist
and add only plan-level integration/validation candidates; do not mandate every match.

Check before execution: every requirement is covered; prerequisites exist; steps
are concrete; dependencies are acyclic; each plan can fit a fresh session by
loading only its scoped context. If too broad, split at independently verifiable
outcomes. Don't measure a plan by fabricated time/effort.

## 5. Execute through domain skills

Execution must be requested/authorized. Read state, selected plan, task and its
prerequisites; record the worker/branch claim. Use the relevant domain skill,
validate proportionally and preserve other work. If new evidence changes scope,
record the deviation and update requirements/plan before dependent work proceeds.
On interruption save exact progress and next action. On plan completion write the
matching summary with result, evidence, deviations and remaining work. Route Git
checkpoints through `norml-git`; mirror eligible task changes through the issue recipe.

## 6. Verify from the goal

Use `qa/planning-integrity.md` and the verification definition in `schemas/milestone-documents.md`. Check observable
truths, artifacts, actual integration/wiring, relevant regressions, and each
mapped requirement. For workspace work, acceptance evidence can be a reviewed design,
approved copy, validated source packet, or live Google artifact via its domain
skill. “A file exists” is insufficient in either storage recipe.

Gaps create linked repair tasks/plans and leave the phase incomplete. Human-only
checks stay pending until the required person's evidence is available. Never
turn pending acceptance into a pass to unblock the roadmap.

## 7. Complete and select next

Only after verification passes: update requirements and roadmap phase state,
canonical tasks and central index; update `state.md`; reconcile repository
issues; log meaningful outcomes through `the project changelog procedure`. When the milestone's
whole goal passes, mark it complete and remove it from active config selection,
leaving its folder and task links intact. Assess parent goal success separately.
Choose the next unblocked task/phase. Starting another milestone creates a new
folder; it never replaces the old brief or roadmap.
