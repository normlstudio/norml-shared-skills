# Example — connecting a milestone's planning documents

Fictional project-depth example, continuing the onboarding scenario. The design
has now been accepted in a hypothetical source decision. This illustrates
planned work, not work verified or shipped in a real project.

## Milestone

Repository planning owner: `sample-product-plugin`.
Milestone directory: `.claude/tasks/milestones/clear-onboarding/`.
Goal: an installed plugin guides the owner through the accepted setup sequence.

## How each document contributes

| Document | Concrete content in this example |
|---|---|
| `project.md` | Build the accepted onboarding sequence; existing provider connection behavior stays a constraint; analytics remains excluded. |
| `requirements.md` | ONB-01: each step explains its purpose and next action. ONB-02: completed steps reflect persisted setup state. Both link the accepted design and the relevant goal. |
| `roadmap.md` | Phase 01 implements and verifies the sequence. ONB-01 and ONB-02 map to that phase, with plan 01-01. |
| `state.md` | Phase 01 is Planned. Next action: inspect the existing setup state before implementing TASK-001. No completed summary or verification exists. |
| `phases/01-setup/context.md` | The accepted screen order is locked. Provider internals are outside scope. Styling details may follow the existing design system. |
| `phases/01-setup/01-01-plan.md` | Order TASK-001 (wire step state) before TASK-002 (build the step interface), then verify both requirements. Record bounded file scope after inspecting the actual repo. |

There is no `research.md` because this example supplies no consequential unknown
that requires external research. Actual source files and commands would be
resolved from the real project, not invented to make an example look executable.

## Canonical task relationships

Both tasks live in the owner's `items/`, not inside the plan file:

- TASK-001: wire the accepted steps to the existing persisted setup state.
- TASK-002: render those steps and their explanations; depends on TASK-001.

Both identify `milestone: clear-onboarding` and `plan: 01-01`. The plan references
them; the central index links them; GitHub mirrors them only through the configured
repository recipe. No separate issue is created for every heading or checklist step.

## What gets created after execution

`01-01-summary.md` records actual changes, deviations and validation results.
`verification.md` evaluates ONB-01 and ONB-02 against observable behavior and
records any missing acceptance checks. Until that evidence exists, neither file
should contain a fabricated Pass. If persisted state is wrong after reload,
verification reports Gaps found and links a repair task.

The phase is Complete only when the checks pass. A later, unrelated initiative
gets another milestone directory; it does not overwrite this roadmap or state.
