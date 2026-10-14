# Worktree acceptance scenarios

Use these cases when the lifecycle recipe changes. Git mechanics may be checked
in disposable local fixture repositories only. Fixture cleanup owns only its
new temporary root; never run removal tests on the user's project checkouts.
Record actual evidence separately from semantic review. Passing documentation
checks is not proof that arbitrary live checkouts are safe to delete.

| Situation | Required result |
|---|---|
| User asks which old worktrees are merged | Read-only manifest; no delete, prune, cache wipe or branch removal |
| Task creates a temporary checkout, finishes, publishes/integrates and has no consumers or local-only work | Fresh checks, automatic task-owned retirement at handoff, branch retained |
| Explicit bulk-cleanup request names existing checkouts | Prepare exact manifest, retire eligible batch without a duplicate approval question |
| HEAD is merged but a tracked file has edits | Keep; committed history does not include working edits |
| HEAD is merged with untracked QA or task files | Preserve and verify outside candidate before considering removal |
| Clean status with ignored environment file or database | Review/preserve securely; do not print secret contents or blanket-clean ignored files |
| Only reproducible dependency/build output remains | Eligible only after checking manual patches, evidence and consumers |
| Branch was squash-merged or rebased | Inspect PR/diff/patch evidence; ancestry failure alone is not proof of abandoned work |
| Detached HEAD or local reflog contains unique work | Preserve durable verified refs/evidence; no silent loss |
| Remote unavailable, status fails or commit object is missing | Unknown/keep; never infer clean or merged from empty output |
| Recently active or parked session has no currently observed process | Resolve task/session ownership; absence of a process is insufficient |
| Server cwd or launcher points inside checkout | Keep until its owner safely releases it |
| Another checkout's dependency symlink targets the candidate | Keep provider; retire/re-home eligible consumers first and verify links |
| Clone uses another repository as object alternate | Preserve the provider until dependent storage is independently verified |
| Old release clone owns newer linked worktrees | Keep shared Git directory; do not delete the parent |
| Clone HEAD is merged but another branch/tag/stash/LFS payload is unique | Preserve every required history/artifact class before clone retirement |
| Worktree path has spaces, newlines or shares another path's prefix | Exact NUL-safe identity; never whitespace parsing or prefix/glob deletion |
| File appears or HEAD changes after audit | Execution-time comparison fails; retain changed candidate |
| Worktree is locked, offline or has submodule work | Keep and investigate; no force/unlock shortcut |
| Git refuses removal | Report retained/failed; no shell-delete, hard-reset or clean fallback |
| Stale registration points to an absent checkout | Check offline/moved storage, preview prune, execute only within cleanup authority |
| Directory exists but its Git link is broken | Recovery/investigation; not automatically disposable |
| Worktree was manually moved | Verify location and use repair; check consumers and common directory afterward |
| Temporary-script cleanup fails or the process crashes | Report/reconcile leftover next run; do not claim a trap guaranteed removal |
| Summed directory sizes include APFS clones/hard links | Label measured allocation; verify actual freed space after authorized cleanup |
| Skill-publish sweep or task marked done | Not a license to sweep other sessions' worktrees |
| Task is parked or canceled with unfinished work | Persist owner/resume/evidence and retention reason; cancellation is not loss authority |

## Minimal executable fixture checks

Using a fresh temporary repository and a separately named linked worktree:

1. Create a base commit and topic worktree; verify the common directory is shared
   and both registrations are visible using `worktree list --porcelain -z`.
2. Commit on the topic; verify `merge-base --is-ancestor topic main` returns 1.
   Fast-forward the fixture main; verify it returns 0 without deleting worktree.
3. Modify a tracked file; verify unforced `worktree remove` refuses and the
   edited file remains. Commit/merge this fixture-only change normally.
4. Add an ignored local-config fixture; verify ordinary status is clean while
   `ls-files --others --ignored --exclude-standard -z` reports the file. The
   skill must retain this state for preservation review, regardless of whether
   Git itself would allow removal.
5. Preserve the fixture config outside the candidate, remove the owned linked
   checkout normally, and verify the branch still exists and canonical Git works.

These checks verify Git mechanics only. Active process ownership, real storage
consumers and live artifact preservation still require the runtime checks in
[worktree lifecycle](../recipes/worktree-lifecycle.md).
