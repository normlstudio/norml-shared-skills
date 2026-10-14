# Worktree lifecycle

`norml-git` owns worktree creation, inventory, preservation, retirement and
registration repair for its callers. Project build/deploy procedures own their
acceptance checks; the chosen task tracker owns task status. Neither a merged PR nor a
completed task alone authorizes discarding a working directory.

## Select the action and authority

- **Create / resume:** use an existing suitable checkout when safe. Create a
  linked worktree only when isolation is needed; do not create one per trivial
  command or clone the repository for every release.
- **Audit / identify:** inspect and write a reviewable inventory. Do not remove
  worktrees, clones, caches, branches or registrations just to produce a report.
- **Finish current work:** retire a temporary checkout created and owned by this
  task in the same turn once all gates below pass. This is ordinary completion
  housekeeping; no extra permission is needed. Preserve it with an explicit
  owner/reason if work is unmerged, parked, shared or still needed.
- **Clean up existing checkouts:** an explicit cleanup request authorizes the
  qualifying exact-path batch. First prepare the inventory and apply every
  gate; do not ask again for the same safe batch. Ambiguous ownership or unique
  files remain kept, with the concrete unresolved reason.
- **Move / repair / prune:** use the separate procedures below. They are not
  synonyms for deleting old feature work.

Updating this skill, running a disk audit, or publishing a repository is not
permission to delete historical checkouts. Never infer consent to delete
branches. Do not install a scheduled cleanup job, hook or daemon unless asked.

## Git facts that affect disk usage

A linked worktree shares a repository's object database and most refs, but has
its own checkout, HEAD and index. Dependencies, build output, screenshots and
local configuration can grow independently in every checkout. A standalone
clone has its own repository and can itself own linked worktrees. A `.git` file
alone is not enough to distinguish a linked worktree from a submodule or a repo
using a separate Git directory: verify Git's common directory and registry.

Merging does not remove the directory. `git worktree remove` removes an eligible
linked checkout and its registration; it leaves its branch available. `prune`
cleans stale administrative records for missing checkouts, not populated
folders. Neither branch deletion nor Git garbage collection replaces checkout
retirement. APFS clones, hard links and sparse files mean summed directory sizes
are not a promise of recoverable bytes.

## 1. Discover the repository and all consumers

1. Resolve canonical project/repository ownership and read its instructions.
   Identify the main worktree and configured integration/release branch, not
   an assumed `main`. A release clone is not automatically canonical.
2. Inspect these commands in each distinct common Git directory:

   ```bash
   git -C "$task_repo" rev-parse --path-format=absolute --git-common-dir
   git -C "$task_repo" worktree list --porcelain -z
   git -C "$task_repo" remote get-url origin
   ```

   Check installed Git support first. Use NUL-safe parsing where available;
   never split paths on whitespace. A command failure is unknown, not clean.
3. A machine-wide audit searches the explicitly scoped project roots and follows
   worktree registrations into hidden project folders, caches, runtime folders
   and temporary locations. Deduplicate by common-directory identity and exact
   path. Report what was not searched. Do not stop at one folder named Worktrees.
4. Separate linked checkouts, primary clones, bare repositories, submodules,
   missing paths, locked/offline worktrees and broken registrations. A present
   directory with a missing `.git` link is a possible recovery case, not empty.
5. Check live processes and current directories with supported OS inspection;
   inspect project server/runner configuration, task execution claims and
   session ownership. Check inbound symlinks from other checkouts, main repos,
   installed launchers and registered skills. Include shared dependencies,
   node_modules targets, object alternates and clone references. Do not print
   process arguments, configuration values or secret contents unnecessarily.
6. Record observed activity and coverage limits. No process observed, old mtime,
   a stale task claim or a directory named `release` is not proof of abandonment.
   Investigate parked sessions. Recent/uncertain ownership stays kept until
   resolved; do not impose an arbitrary age-based deletion rule.

## 2. Create with an owner and an exit condition

- Fetch the verified authorized Git source and select a specific base commit.
  Preserve unrelated changes; do not reset, stash or change someone else's
  checkout just to create isolation.
- Prefer a linked worktree of a durable canonical repo. Never base durable work
  on a disposable release clone whose deletion would remove its common Git
  directory. Keep worktrees outside each other's directories and off synced
  storage. Follow the project's existing local path convention.
- Check whether the branch/path already exists or is checked out. Reuse only
  with verified ownership. Never force-add, reset an existing branch with `-B`,
  or check the same branch out in multiple worktrees to bypass Git's refusal.

  ```bash
  git -C "$task_repo" worktree add -b "$task_branch" "$task_worktree" "$task_base_sha"
  # Reproducible testing of an exact published revision:
  git -C "$task_repo" worktree add --detach "$task_worktree" "$task_base_sha"
  ```

- Record path, common-directory identity, branch/HEAD, base SHA, target branch,
  purpose, task/owner/session, creation time, expected consumers, artifacts to
  preserve and exit condition. Store machine-local records in a canonical
  repo's common Git directory under `norml/worktrees/`; link portable identity
  from the existing task. Do not create a second task/status system or put the
  only record inside the disposable checkout. Never record secret values.
- Install only needed dependencies. Shared dependency links require recorded
  inbound/outbound consumers and compatible versions. Do not copy environment
  secrets into another checkout; use the project's supported secure loader.
- Temporary build scripts clean their exact owned path on success and failure,
  but retain unexpected edits/evidence. Check and report cleanup errors; never
  hide failed removal behind a successful overall report. Kill/crash recovery
  needs reconciliation on the next run; an exit trap is not a guarantee.

## 3. Prove integration and preserve every kind of work

Fetch fresh refs from the verified canonical remote without pulling/resetting
any checkout. Record the target ref and fetched SHA. If fetch fails, mark merge
verification unavailable and do not promote cached evidence to safe removal.
Do not change Git config or migrate remotes as an incidental audit operation.

For each candidate capture a fresh HEAD and inspect:

```bash
git -C "$task_worktree" status --porcelain=v1 -z --untracked-files=all
git -C "$task_worktree" ls-files --others --ignored --exclude-standard -z
git -C "$task_worktree" submodule status --recursive
```

Check index and unstaged edits, untracked files, ignored files, submodule work,
merge/rebase/cherry-pick state, worktree-specific refs and reflogs where they may
hold unfinished work. A published HEAD does not include any of these edits.
A stash is shared repository state; never pop/drop it as housekeeping. Empty
stdout on an error must not count as a clean status.

Test ancestry in an object database that contains both commits:

```bash
git -C "$task_canonical_repo" merge-base --is-ancestor "$task_head_sha" "$task_target_sha"
```

Exit 0 proves ancestry; exit 1 means not an ancestor; other failures are unknown.
A missing object in another clone is not proof of merge or loss. If needed,
fetch the specific authorized ref into an isolated audit namespace without
checking it out or moving the target branch, then re-evaluate.

For rebased, cherry-picked or squash-merged work, inspect PR merge evidence,
`git cherry <target> <head>`, the branch's scoped diff, merge commits and final
integrated behavior. Patch equivalence is supporting evidence, not a universal
proof: squashes and merge commits need separate review, and a later revert may
mean the feature is no longer present. Preserve the branch/commit even when a
review proves the intent integrated. Unresolved unmatched commits stay kept;
never force a merge merely to make cleanup possible.

Classify files separately:

- Tracked/untracked implementation, task state and evidence: keep or preserve at
  the verified canonical home under the applicable Git/planning policy.
- Ignored local configuration, environment material, databases, user uploads,
  QA captures and release provenance: review; ignored does not mean disposable.
  Preserve secrets through the user’s protected credential store, never in a bundle/report/skill repo.
- Reproducible generated dependencies and builds: eligible only after confirming
  they contain no sole copy of required evidence or manually patched work and
  no live/inbound consumer. Never blanket-delete all ignored files.

Before retiring a **standalone clone**, prove that all needed local branches,
tags, stashes, detached/reflog-only commits, Git LFS objects, submodule work and
local-only artifacts survive in a durable verified location. Verify any backup
by reading it back; a Git bundle does not preserve ignored files, LFS payloads or
uncommitted work. Inspect `.git/objects/info/alternates` and consumers of local
`--shared`/`--reference` clones. The clone's HEAD being on remote main is not
sufficient. Never remove its Git storage while any linked checkout depends on it.

## 4. Build a concrete disposition manifest

For each exact path, record type, common directory, owner/task, HEAD/branch,
remote/target SHA and verification time, tracked/untracked/ignored findings,
active consumers, locks, inbound links/alternates, child worktrees, preservation
evidence and measured directory allocation. Report these categories:

| Disposition | Requirement |
|---|---|
| Retire linked worktree | Integrated, preserved, clean, unused, unlocked, authorized |
| Retire standalone clone | Same gates plus all-ref/local-history/storage dependency checks |
| Preserve local files first | Integrated but local configuration/evidence needs retention |
| Keep active / unfinished / dependent | Unique work, active consumer, ownership or dependency blocker |
| Investigate / repair registration | Missing, offline, invalid or unavailable verification |

Use exact paths, not basenames, prefix globs or age cutoffs. Keep historical
branch names by default. State that disk allocation totals may double-count
shared storage; distinguish measured before/after free space from estimates.
This skill does not supply time or cost estimates.

## 5. Retire and verify

1. Re-read the exact candidate immediately before mutation. Confirm its
   canonical path and common directory, HEAD, full status, ignored inventory,
   target SHA, locks, consumers and ownership still match the manifest. Abort
   changed candidates individually; do not overwrite concurrent edits. Arrange
   a quiet ownership handoff; a filesystem snapshot is not a concurrency lock.
2. Save required artifacts and task resume/completion records outside the
   candidate first. Move the agent's own cwd to a surviving repository. Stop
   only services owned by this task and covered by its authority; shared or
   unknown processes remain blockers. Remove consumer worktrees before a
   dependency provider only if every consumer is independently eligible.
3. For an eligible linked worktree, from the surviving repo:

   ```bash
   git -C "$task_repo" worktree remove "$task_worktree"
   ```

   No `--force`, `git clean`, hard reset or shell deletion fallback when Git
   refuses. Diagnose dirty/locked/submodule state and retain it. Submodule
   worktrees need a separate reviewed preservation/removal path; do not
   silently force them. A primary clone is not removable with this command.
4. For an authorized standalone clone, verify the extra preservation gates and
   all children are gone/re-homed. Use exact-path filesystem removal through
   the approved local cleanup route, never recursive parent/glob deletion.
   Do not delete a main/bare repository merely because it looks unused.
5. Confirm path absence, surviving registrations and canonical repository
   health. Verify preserved branches/commits and local artifacts are accessible,
   inbound links are intact, and surviving worktrees can still resolve Git.
   Record actual before/after free space with concurrent-disk-change caveats.
6. Mark lifecycle record removed with evidence, or kept with a specific owner,
   reason and next condition. Report removed/kept/failed paths; never report
   cleanup complete when a removal failed. Do not delete branches, expire
   reflogs, prune objects or run aggressive GC as a side effect.

## Move, lock, repair and prune

- Use `git worktree move` for eligible linked checkouts. Verify consumer paths
  and lifecycle records afterward. Main worktrees and worktrees with submodules
  have restrictions; do not bypass them with an unreviewed filesystem move.
- Use `git worktree lock --reason <reason>` for deliberate offline/removable
  storage or an explicit retention need. Record why. Never automatically unlock
  another session's worktree to remove it; a lock is not proof of active process
  ownership and is not a general write mutex.
- After a verified manual relocation, use `git worktree repair` from the
  surviving repository to repair Git links; verify both common directory and
  checkout after repair. Never prune before investigating missing storage.
- Preview with `git worktree prune --dry-run --verbose`. Execute `prune` only
  when cleanup authority covers the verified stale registrations and storage
  is not merely offline. Do not shorten expiration to force disappearance.
  Metadata pruning usually recovers little space; report it separately.

## Caller handoff and completion

Every operation using this skill’s worktree workflow loads this recipe before creation
and invokes it again at task finish, cancellation, parking or resume. Planning
records link the checkout identity; they do not implement their own removal
logic. Publishing skill drafts does not authorize removing their unmerged or
actively used worktrees. A temporary checkout is not fully handed off until it
is removed or retained with a durable reason. Legacy bulk cleanup remains a
separate scoped action, not an automatic sweep after every commit.

## Sources and behavioral verification

Grounded in the local disk/worktree audit and Git's official contracts; local
project names, live paths and measurements remain outside this shared skill.

- [Git worktree](https://git-scm.com/docs/git-worktree): lifecycle commands,
  shared/per-worktree state, locks, porcelain output and submodule limitations.
- [Git merge-base](https://git-scm.com/docs/git-merge-base): ancestry exit codes.
- [Git cherry](https://git-scm.com/docs/git-cherry): patch-equivalence semantics.

Run [worktree scenarios](../qa/worktree-scenarios.md) when changing this recipe.
