# Upgrade an existing planning store without losing work

Run only when a structure upgrade/import is requested. A v3 skill can read and
update legacy quick/project planning without forcing a migration. It must not
write a v3 index over an unmigrated v2 backlog.

1. Inventory config, goals, all backlog sections, root project/requirements/
   roadmap/state, phases, existing issue links, and external planning systems.
   Record counts of open/completed/deferred tasks and source paths.
2. Read live project/WIP rules. Save a preserved snapshot under the owning
   `.claude/tasks/migration-backup/{dated-slug}/` before edits; never delete it.
3. Propose a source-to-destination mapping. Existing v2 `TASK-NNN` IDs are
   preserved. Items lacking IDs receive new IDs plus their exact original
   line/issue reference as provenance. Keep nested unresolved work, source
   qualifiers, and completion notes; don't simplify a partial completion to done.
4. Convert backlog bodies to `items/task-nnn-slug.md`. Map queue/status/priority;
   acceptance or evidence not present stays explicitly unresolved. Completed
   historical records retain their claimed state and source evidence, marked
   historically reported rather than retroactively verified.
5. Move root project-lane files/phases into one named `milestones/{slug}/` and
   repair every relative link. Map plan-local IDs to canonical task IDs; plans
   reference tasks rather than duplicating full bodies. Keep source ID aliases.
6. Create the v3 config with verified dual-location map. Reuse existing issue
   URLs only after checking exact repository identity (forks may share old
   issue numbers). Do not copy issue identity between unrelated repositories.
7. Build the index only after every source item has a destination. Compare
   before/after counts and all open task meanings, check traceability, links,
   statuses and issue identity. Run `qa/planning-integrity.md`.
8. Record the mapping and cutover in `migration-backup/{dated-slug}/mapping.md`.
   Mark the source snapshot historical; select the v3 destination as the only
   active native plan. Roll back if verification fails, preserving new work too.

## External GSD

Preserve the external `.planning/` source unchanged. Map its project,
requirements, roadmap, states, plans and summaries into native records only
on an explicit migration request. Keep its tool-required casing inside that
source namespace. Verify first, then record canonical cutover; never run both
execution systems for the same milestone. Historical source systems remain read-only during a requested import.
