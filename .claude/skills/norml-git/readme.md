# norml-git

> Make clear commits, preserve shared work, synchronize authorized remotes, and manage worktrees
safely.

## The problem

A shared working tree can contain several people’s unfinished changes. A blanket commit or cleanup
can lose ownership and local-only work.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Commit this | *"commit this"* |
| Push my changes | *"push my changes"* |
| Pull latest | *"pull latest"* |
| Audit worktrees | *"audit worktrees"* |
| Create an isolated checkout | *"create an isolated checkout"* |
| Clean up merged worktrees | *"clean up merged worktrees"* |
| Claim task | *"claim task"* |
| Resolve a git conflict | *"resolve a Git conflict"* |

## A typical run

1. Read instructions, status, history, remote identity and permissions.
2. Identify owned files and group commits by rationale.
3. Scan actual staged content and run applicable checks.
4. Apply only requested effects and verify the resulting SHA.
5. Retire a checkout only after history, file and consumer gates.

---

## Details

### Inputs

- An authorized repository and its actual integration branch.
- Git; optional claims/issue reads need Python 3.9+ and authenticated GitHub CLI.
- The requested operation and current user/task ownership.

### What it creates or changes

- Reviewed Conventional Commits and status evidence.
- Authorized synchronization with verified remote commit.
- Exact worktree disposition/preservation records.
- Optional remote claims with local receipts outside source.

### Commands in depth

#### Commit this

*"commit this"* — Inspect the actual diff, stage exact owned paths, and create rationale-based
Conventional Commits.

#### Push my changes

*"push my changes"* — Verify destination, outgoing commits and authority; push normally and verify
the resulting remote SHA.

#### Pull latest

*"pull latest"* — Fetch and inspect divergence first; fast-forward safely rather than pulling
blindly over local changes.

#### Audit worktrees

*"audit worktrees"* — Produce a read-only exact-path inventory including integration, local files
and active consumers.

#### Create an isolated checkout

*"create an isolated checkout"* — Resolve task owner, base commit and exit condition; create an
isolated linked worktree only when needed.

#### Clean up merged worktrees

*"clean up merged worktrees"* — Check history, ignored/local files, submodules and consumers
before retiring the authorized exact paths.

#### Claim task

*"claim task"* — Use the optional project-enabled remote ledger after auditing already integrated
and active work.

#### Resolve a git conflict

*"resolve a Git conflict"* — Diagnose repository state, preserve local/incoming work and resolve
the actual competing change.

### Inside the package

- [SKILL.md](SKILL.md)
  Operation router and authorization boundaries
- [project-repositories.md](recipes/project-repositories.md)
  Commit and synchronize workflow
- [worktree-lifecycle.md](recipes/worktree-lifecycle.md)
  Local-file/history/consumer preservation
- [task-ownership.md](recipes/task-ownership.md)
  Optional shared-claim protocol
- [task_claims.py](scripts/task_claims.py)
  Fast-forward remote coordination helper
- [test_task_claims.py](qa/test_task_claims.py)
  Real disposable-remote race checks

### Limits

- No automatic push, deployment or repository sweep.
- The shared-claim adapter supports GitHub and isolated local test remotes; core Git/worktree
  procedures support other Git hosts.
- Claims are cooperative bookkeeping, not editor or filesystem enforcement.
- Merged history alone does not make a checkout disposable.

### When something breaks

- **Push fails.** Check identity, permissions and divergence; preserve local commits, never
  force-push.
- **Another worker’s files are staged.** Coordinate index ownership before committing; preserve
  that staged work.
- **Worktree has ignored files.** Inventory local config/evidence and consumers before retirement.
- **Claim ledger unavailable or busy.** Stop claimed implementation and resolve access/ownership;
  never assume expiration means free.

### Source of truth

[SKILL.md](SKILL.md) routes runtime operations. The linked procedures provide the full operational
checks. This guide explains the public package and does not add authority or claim live access.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
