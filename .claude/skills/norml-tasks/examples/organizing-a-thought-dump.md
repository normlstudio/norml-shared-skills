# Example — organizing a thought dump

Fictional worked example. It shows the distinction between original input,
goals and a task. It is not real client work or a default plan to copy.

## Original request

> Setup is confusing. First, write a clearer onboarding outline. Once we've
> agreed on it, implement it in the plugin. Maybe explore analytics later.

The product has a verified workspace planning owner `sample-product-coordination`
and a linked repository owner `sample-product-plugin`.

## What the AI extracts

| Input | Meaning | Destination |
|---|---|---|
| Setup is confusing | Desired outcome: customers understand setup | workspace long-term GOAL-01 |
| First write the outline | Selected next outcome: an agreed onboarding outline | workspace short-term GOAL-02, parent GOAL-01 |
| Write the outline | Concrete action | workspace TASK-001 |
| Once agreed, implement | Code work with an approval prerequisite | Repository task linked to the accepted outline; keep blocked until then |
| Maybe explore analytics | Uncommitted idea | Capture disposition; no active implementation commitment |

Save this exact request and its disposition in `captures/yyyy-mm-dd-onboarding.md`;
the task links that original source. Later corrections become new captures.

## Resulting goals

The workspace `goals.md` declares:

- GOAL-01: customers can understand the setup journey; success requires evidence
  from the project's agreed usability/acceptance check, not just a written outline.
- GOAL-02: an onboarding outline is accepted for implementation; its parent is
  GOAL-01 and its success check is the recorded review decision.

GOAL-02 is the current focus. Both goals remain active; neither has evidence of
achievement yet. “First” is an ordering instruction, not a fabricated due date.

## Resulting task file

Destination: `.claude/tasks/items/task-001-draft-onboarding-outline.md` on workspace.
This filled example is also parsed by the isolated QA tests. Its source anchor refers
to this illustration; an actual task links its saved project capture instead.

```markdown
---
id: "TASK-001"
title: "Draft a clearer onboarding outline"
status: "open"
queue: "now"
priority: "P1"
rank: 1
goals: ["GOAL-02"]
depends_on: []
milestone: null
plan: null
issue: null
---

## Outcome

A concrete onboarding outline is ready for the product owner's review.

## Source

Fictional request: [original request](#original-request),
English; author/date unresolved in this illustration. The original is preserved before refinement.

## Scope

Describe the screens, sequence and user-facing explanations in a reviewable draft.
Plugin code and analytics are outside this task.

## Acceptance

- [ ] The draft describes the purpose and next action for each proposed screen.
- [ ] Open product decisions are listed rather than silently resolved.
- [ ] A reviewable draft is saved in the product's human-facing design workspace.

## Steps

1. Read the existing onboarding material and the product's locked decisions.
2. Draft the proposed screen sequence through the appropriate content/design skill.
3. Check every screen for a clear purpose and next action; save the review draft.

## Priority reason

The user explicitly selected the outline first; implementation depends on its approval.

## Blocker

None

## Next action

Read the existing onboarding material linked from the product context.

## Evidence

Not yet executed. No acceptance check has passed.

## Execution claim

None

## Decisions and changes

Draft preparation is this task's outcome. Approval remains the short-term goal's
success check and must be recorded before repository implementation can proceed.
```

## What appears in the index

`tasks.md` shows one Now row linking TASK-001, P1, open, GOAL-02 and no issue.
It does not repeat the task body. Finishing this draft task does not automatically
achieve GOAL-02: that goal still needs the recorded approval. The repository's
implementation task stays blocked on approval rather than assuming that a
completed draft means an accepted design.
