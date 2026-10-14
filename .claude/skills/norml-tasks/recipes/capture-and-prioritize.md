# Capture a dump and prioritize it

Read `schemas/planning-workspace.md` and `schemas/task-record.md` for the output
requirements. For an illustration, see `examples/organizing-a-thought-dump.md`.

1. Resolve the owner(s) and read goals/indexes on both known surfaces. In a
   repository follow its freshness and issue lookup procedure first.
2. Save each original request before refining it, including one-line requests.
   Follow `standards/source-provenance.md`: verbatim original language, author,
   source/date, available message URL, and a disposition table under `captures/`.
   Meetings route to the configured canonical meeting archive first; link its canonical transcript instead
   of copying it. Every resulting or amended task links the original request
   anchor in its Source section. Append later requests without rewriting history.
3. Extract goals, decisions, constraints, ideas, questions, and actions using
   `standards/prioritization.md`. Preserve nuance; never turn assumptions into
   approved requirements. Record relevant decisions in the existing project or
   milestone context, with source links.
4. Search existing task files and mapped GitHub issues for the same outcome.
   Amend the existing task when it is the same work; retain both sources.
   For overlaps, split acceptance boundaries and link dependencies explicitly.
5. Write/update `goals.md`: long-term outcomes and a short-term focus linked to
   its parent. If no goal can be grounded, capture the task with `goals: []`
   and record that gap; don't fabricate a strategy just to fill a field.
6. Allocate a stable task ID after re-reading the store. Create one
   `items/task-nnn-slug.md` per independently executable outcome using
   `schemas/task-record.md`: source, why, scope, acceptance, bounded steps,
   dependencies, next action. Titles start with a concrete verb.
   Add `## Suggested skills` using [skill selection](../standards/skill-selection.md):
   exact candidates, reason and use condition, explicitly provisional.
7. Separate workspace coordination from repo implementation. Cross-link outcomes;
   do not duplicate implementation checklists in both places.
8. Select queue, status, priority, and rank with a short reason. Use Now, Next,
   Someday, Blocked, Done. Research and unknowns do not make a task executable;
   put a blocking decision before dependent implementation.
9. Promote substantial work into `recipes/plan-milestone.md`, retaining the task
   identity and pointing at the milestone. Phases reference task files.
10. Rebuild `tasks.md`, run the integrity gate, and mirror eligible repository
    tasks with `recipes/sync-github-issues.md`. Report the focus, first/next
    actions, routed locations, and unresolved questions. Capturing work does
    not start its implementation.
