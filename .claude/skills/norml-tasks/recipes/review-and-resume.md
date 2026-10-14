# Review, resume, and maintain planning

## List / next / review

Resolve both stores. Read config, goals and indexes; inspect selected tasks,
dependencies and active milestone state. Report coverage explicitly if a store
is unavailable. Reconcile configured issues before claiming current repo
status. Apply the prioritization standard, not task-file timestamps. Output one
current goal, one next unblocked action, why it comes first, and what's blocked.

## Resume

Reconstruct from task files, active state, plan/summary pairs, acceptance
results, Git and verified issue links. Load only the selected task/phase and its
prerequisites. A later session should not need the original chat. If summaries,
indexes and actual evidence disagree, repair the stale projection; unresolved
contradictions block dependent execution. Reconfirm that an old plan still fits
current code and locked decisions before starting.

## Block / unblock

Record the exact blocking condition, checked evidence and next unblock action
in the task. Set blocked status/queue and update milestone state. On resolution,
attach evidence and return to open/next unless explicitly selected for Now.
Unavailable external dependency evidence is a blocker, not a completed prerequisite.

## Park / freeze

Keep a precise resume point: last completed step, current files/state, unresolved
questions, next action, and reason parked. Park/retain the execution claim; remote ownership follows its explicit protocol. Set open/
someday for deliberate deferral, or blocked/blocked for a real obstacle. Pause
the milestone in its state and remove it from active selection when appropriate.
Never delete the task or move it to a personal board.

## Done / cancel

Done requires acceptance evidence plus any configured merge/deploy requirement.
Check goal/requirement coverage rather than inferring it from issue closure.
Write the task result; rebuild the index, update state/requirements/roadmap,
then reconcile the mirror. A failed check creates linked repair work. Explicit
cancellation uses canceled/done with a reason; it never counts as verified
completion of dependent work. Graduate durable outcomes through `the project changelog procedure`.

## Concurrent workers

Follow the repo's named integrator/worktree convention. Record an execution
claim in the task (`Worker`, branch/worktree identity, start event) when starting;
transfer or park it explicitly at handoff. A stale claim is investigated, not automatically stolen.
Before each write re-read changed files. One owner updates an index at a time;
rebuild from the merged canonical task files after branch merges. The helper
checks stale-index writes; it is not a distributed lock across workspace machines.

## Worktree handoff

At resume, verify the recorded checkout still exists and matches its Git identity
through `norml-git/recipes/worktree-lifecycle.md`; do not silently recreate or
replace a missing worktree. At done/cancel/park, persist task and evidence first,
then let norml-git retire an eligible task-owned temporary checkout or record an
explicit retention reason. Parking is not deletion authorization. Preserve or explicitly transfer the
execution claim without losing the branch, owner or resume pointer.
