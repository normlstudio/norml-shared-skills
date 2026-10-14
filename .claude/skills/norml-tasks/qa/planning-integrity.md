# Planning integrity gate

Apply the relevant checks before declaring a capture, plan, sync, upgrade, phase,
or milestone complete. Record failures honestly; structural validity does not
prove that the task outcome was achieved.

## Ownership and discovery

- [ ] Canonical project and owner identities are resolved; correct workspace/repo recipe selected.
- [ ] Both known planning surfaces were read, or unavailable coverage was disclosed.
- [ ] Config maps use verified portable locations; reciprocal identities agree.
- [ ] No duplicate active native/external GSD plan or cross-owner implementation copy.

## Capture and priorities

- [ ] Every new/amended task links the preserved original request or canonical meeting transcript, with original language and author/date; exact wording is separate from interpretation.
- [ ] Later corrections retain previous sources; unavailable historical originals are labelled, never invented.
- [ ] Source intent, decisions, constraints, questions and ideas were distinguished.
- [ ] Every meaningful source item has a task/goal/decision/deferral or unresolved disposition.
- [ ] Existing tasks/issues were checked before creating duplicates.
- [ ] Long-term and short-term goals have observable success checks and sources.
- [ ] The next action is unblocked and its priority/order has a reason.
- [ ] No invented estimates, deadlines, approved decisions or execution authority.

## Records and index

- [ ] Unique stable task IDs and individual canonical task files; no reused retired IDs.
- [ ] Index rows agree with task status, queue, priority, goal and issue links.
- [ ] Dependencies resolve; real task/phase dependency graphs have no cycles.
- [ ] Cross-owner dependencies were actually read; unavailable evidence remains unresolved.
- [ ] Every task has scope, acceptance, steps, next action and source.
- [ ] New/materially amended tasks and phase plans have a bounded provisional skill
  shortlist with reasons/use conditions; actual execution reads the selected contracts.
- [ ] Unused candidates are not treated as missing work; legacy tasks are not bulk-rewritten.
- [ ] Blockers have an unblock action; done/canceled records have evidence/reason.
- [ ] Concurrent changes were re-read/merged rather than overwritten.

## Project depth

- [ ] Distinct milestones retain independent state; config/index identify active ones.
- [ ] Atomic requirements trace to one phase and at least one plan before execution.
- [ ] Plans order canonical task IDs with bounded scope, must-haves, validation and dependencies.
- [ ] State agrees with actual plan/task/summary evidence; resume works without chat history.
- [ ] Locked decisions and explicit revisions win; ordinary links aren't dependency cycles.

## GitHub mirror

- [ ] Correct repository identity and authority, exact qualified markers, full pagination.
- [ ] Existing issue reused; unmanaged body/comments preserved; no invented labels.
- [ ] Last-confirmed snapshots detect remote edits; conflicts remain visible.
- [ ] Create timeout/unknown outcome reconciled before retry; no duplicate create.
- [ ] Post-write remote readback matches canonical accepted scope and intended state.
- [ ] No task completed solely because an issue closed or PR merged.
- [ ] No comments/messages without explicit authorization; no browser fallback.
- [ ] Git inclusion and commits follow `norml-git`; public/private source boundary checked.

## Outcome verification

- [ ] Observable goal, artifacts, integration/wiring and mapped requirements checked.
- [ ] Relevant automated, visual and human acceptance results are recorded.
- [ ] Required merge/deployment state verified when part of acceptance.
- [ ] Gaps create repair work; pending human checks remain pending.
- [ ] Milestone/goal completion derives from success checks, not merely task count.

## Migration

- [ ] Source preserved, every open/closed/partial item mapped, counts/meanings checked.
- [ ] Legacy IDs, links, evidence and issue repository identities preserved or explicitly remapped.
- [ ] External GSD remains unchanged until verified canonical cutover.

## Mechanical helper and scenario QA

`python3 scripts/planning.py check <planning-root>` checks local task metadata,
IDs, local dependency cycles, safe links and index freshness. `index --write`
rebuilds the navigation index after valid canonical edits. Both refuse legacy
stores; neither migrates, synchronizes GitHub, nor verifies domain outcomes.
External refs are reported for separate human/agent resolution.

Run `python3 qa/test-planning.py` for helper regression tests. Also review these
behavior scenarios when changing the skill:

1. Mixed content/design/code dump → split owners, preserve one canonical task each.
2. Quick task grows → milestone plan points to same task ID; no duplicate issue.
3. No workspace mapping / repo offline → partial coverage, no invented owner/status.
4. Remote issue changed while local scope changed → conflict, not last-write-wins.
5. Create timeout → marker enumeration before retry; duplicate match blocks create.
6. PR merged into non-default branch / acceptance pending → inspect, don't infer done.
7. Existing v2 store → read safely; explicit upgrade preserves every open item.
8. Two sessions edit tasks → stale index write refused, re-read and reconcile.

9. One-line or multilingual input → save verbatim source/language; task links its original anchor, translation remains separate.
10. One request creates multiple tasks → all link one capture; a correction appends another source.
11. Meeting-derived work → source links the canonical transcript and available timestamp, with no duplicate full transcript.

12. A content/design dump → suggest only relevant skills with reasons; optional image generation remains conditional and does not authorize paid calls.
13. Scope changes at execution → select a different evidenced skill, update the shortlist and record actual use; unused suggestions do not block completion.
14. No registered skill fits → record no match, never invent a capability or install an external pack.
