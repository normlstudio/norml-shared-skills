# Development planning in the repository and GitHub Issues

Output definitions: `schemas/planning-workspace.md` and `schemas/task-record.md`.

1. Follow `standards/layering.md`. Identify the actual Git root and planning
   owner. For WordPress it is often the custom theme/plugin repository, not
   the installation. Verify `origin` is the intended configured `owner/repository`.
2. Use `norml-git` to inspect branch, worktrees, pending changes, and remote
   freshness. Fetch/read relevant shared task changes before allocation. Do
   not check off another worker's task from a stale checkout.
3. Read project agent/context instructions, `.claude/ci-cd.md` when deployment
   is involved, existing native planning and any external `.planning/` pilot.
   Discover the mapped workspace home and read its goals/index as well.
4. For a new native store, initialize the common hierarchy with `storage:
   repository`, `planning.commit_docs: true`, and GitHub mirroring disabled until explicitly enabled for
   concrete task records. Config holds exact repository identity and planning
   path. Respect an existing explicit `commit_docs: false`; do not silently
   flip it or force-add ignored planning. Record that the requested Git-tracked
   mirror is unavailable until the project policy changes.
5. Run capture/prioritization or milestone planning. A task file owns its
   requirements, steps, scope, status and evidence; the central index links it.
   Every concrete task is eligible for an issue, including small fixes.
   Speculative capture fragments, goals, and individual checklist steps are
   not separate issues. Existing project's explicit narrower policy remains
   until a policy update is authorized.
6. Reconcile issues through `sync-github-issues.md`: reuse existing matches,
   then create/update the mirror under standing or explicit project authority.
   This is a CLI/API recipe performed when invoked, not an installed background
   daemon or hook. Do not claim automatic sync between sessions.
7. When execution is requested, use the domain skill and repository worktree/
   branch policy. Link branch/PR to the task and issue. Partial PRs use
   `Part of #N`; the last implementation PR can use `Closes #N`. Check the
   actual default branch and completion definition before relying on auto-close.
8. Validate the task's acceptance criteria and required merge/deployment state.
   Save evidence, update canonical status/index, then reconcile issue state.
   A merge or closed issue is insufficient if required runtime checks remain.
9. Route commits/pushes/PRs through `norml-git`. In code repos stage only task
   paths and related implementation; keep unrelated WIP intact. Follow the project’s explicit release and Git policy. No repository has automatic publication solely because it contains skills.

Before putting repository planning in a public repo, inspect its contents for
private client context. Keep private source detail at its authorized home and
publish only the approved actionable task scope. Never change repo visibility.

## Worktree ownership

Before task isolation and at execution handoff, load
`{optional-git-skill}/recipes/worktree-lifecycle.md`. Link its checkout
identity and owner to the task. Save task/evidence outside a disposable checkout
before retirement. A done task or merged PR alone does not prove the directory
is disposable; norml-git owns the local-file, integration and consumer checks.
