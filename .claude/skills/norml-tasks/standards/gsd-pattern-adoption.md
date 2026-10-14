# GSD pattern adoption

The v2 foundation of `norml-tasks` is informed by the project-planning model evaluated from the
external `open-gsd/gsd-core` workflow in the source planning method. This note
records the design decisions; it is not a vendored copy of that runtime.

## Adopted patterns

- A living project definition before implementation
- Atomic requirements with stable IDs and phase traceability
- A roadmap organized by observable phase outcomes
- Phase discussion/context before detailed plans
- Research only where uncertainty materially affects the plan
- Small executable plans paired with outcome summaries
- Goal-backward verification that can block phase completion
- A persistent state document that makes resumption independent of chat history
- A `commit_docs` switch that expresses whether planning belongs in Git

## Public adaptations

- Planning is layered beside the thing it is about, not centralized in one tool.
- native filenames are lowercase kebab-case.
- `norml-git` exclusively owns staging, commit structure, hooks, branches, and
  pushes; `commit_docs` is only an inclusion policy.
- Planning never contains model-generated time, effort, hour, or cost estimates.
- Source precedence applies to individual statements and explicit revisions.
- Ordinary document cross-links do not create dependency cycles.
- Existing domain skills remain responsible for implementation and QA.

## Rejected dependencies

- No external GSD runtime is required for native planning.
- No automatic generic commits from a planning tool.
- No parallel canonical task state across external tools, GSD, and `.claude/tasks/`.
- No requirement that research or discussion artifacts exist when they add no
  decision value.

External GSD can still be used as a project-scoped pilot. Its `.planning/`
namespace remains visibly tool-owned, and migration happens only through an
explicit source mapping and canonical cutover.


## v3 design decisions

GSD is the phase-execution discipline inside the wider file planning system.
workspace and repository storage share one task contract; quick and project depth
remain independent of that storage choice. Canonical task files, index, goal
horizons, multiple milestone folders, dual-location discovery, and GitHub
mirroring are planning additions. No external runtime installation is required.

The current upstream documents discuss → plan → execute → verify → ship, bounded
context, and persistent state. This skill adopts that loop without forcing a research
artifact or requiring parallel agents for ordinary captures. When delegation is
explicitly requested, scoped task/phase files supply bounded context; absent
such a request, one agent can run the same lifecycle sequentially.

Primary source checked Sep 7, 2026:
[GSD Core](https://github.com/open-gsd/gsd-core).
The earlier [GSD repository](https://github.com/gsd-build/get-shit-done) redirects
to that current project. This skill implements its own file contract rather than
vendoring upstream instructions.
