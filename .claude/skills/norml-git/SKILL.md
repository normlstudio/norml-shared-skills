---
name: norml-git
version: 1.0.0
description: >
  Inspect repository history, preserve shared work, make rationale-based Conventional Commits, synchronize authorized remotes, manage worktrees safely, and coordinate shared tasks through an optional GitHub claim ledger. Use for commit this, push my changes, pull latest, audit worktrees, create an isolated checkout, clean up merged worktrees, claim task, or resolve a Git conflict.
metadata:
  author: Norml Studio
---


# Norml Git

A portable Git operating skill for developers and AI assistants. Discover the user's repository,
integration branch, hosting policy, identity and permissions before changing it. Every repository
uses the same preservation rules; skill repositories carry no automatic publishing exception.

## First-run inputs

Resolve `{repo}` from the requested project and `git rev-parse --show-toplevel`, `{skill-root}`
from this installed folder, the authorized remote name/URL, integration branch, task owner/session,
and the user's requested effects. Read project instructions and deployment policy. Do not assume
GitHub, a company organization, `main`, a commit email or permission to create a remote.

Git is required. The optional shared-claim and issue/PR adapters additionally need Python 3.9+
and authenticated GitHub CLI (`gh`). The core commit and worktree workflows work on other Git hosts.
Use existing supported authentication. Provider sign-in/MFA/consent is handled by the user when
unavoidable; never request secrets in chat or print credential-bearing remote URLs.

## Choose the operation

| Request | Procedure |
|---|---|
| Commit current task | [Commit and synchronize](recipes/project-repositories.md) |
| Pull/latest | Fetch and inspect first; fast-forward only when safe |
| Push/publish | Verify authorized destination, review exact outgoing changes, then push |
| Conflict/failure | Diagnose state; preserve both sides; resolve the actual conflict |
| Worktree create/resume/audit/retire/move/repair | [Worktree lifecycle](recipes/worktree-lifecycle.md) |
| Shared implementation ownership | [Shared task ownership](recipes/task-ownership.md) |

An audit is read-only. A commit request is permission to create the requested commit; it does not
by itself authorize pushing, deploying, sweeping other repositories, or changing remote visibility.
A publish request authorizes its concrete reviewed scope. Honor explicit standing project policy
when it exists; never infer it from a folder name or the presence of `.claude/skills/`.

## Commit grouping

Split by logical rationale. A feature, an unrelated fix and a cross-cutting convention change
normally form different commits. Bundle synchronized renames, dependent interface changes and
one uniform cleanup when they share one reason. Explicit user bundling wins; describe the scopes
honestly in the body. Do not repeatedly seek approval for routine grouping within authorized work.

1. Inspect `git status --porcelain`, `git diff --stat`, `git diff` and `git diff --cached`.
2. Identify current-task changes and preserve other workers' staged/unstaged work. If an index
   contains another worker's changes, coordinate before committing; a commit includes the index.
3. Group candidate files/hunks by rationale; prepare specific subjects.
4. Scan the actual staged diff and newly added files for secrets and inappropriate artifacts.
5. Stage exact paths with `git add -- path1 path2`. Use interactive hunk staging only when needed.
   Never use blanket `git add .` or `git add -A` in shared work.
6. Run meaningful applicable checks; fix failing hooks instead of bypassing them.
7. Commit the reviewed group, then verify the resulting commit and remaining status.

## Conventional Commits

Format: `<type>(<scope>): <imperative description>`; optional `!` marks a breaking change.
Keep the subject at most 72 characters. Types: `feat`, `fix`, `docs`, `style`, `refactor`,
`perf`, `test`, `build`, `ci`, `chore`, `revert`. Scope identifies the actual affected module.

Good subjects identify the behavior: `fix(checkout): preserve selected shipping method`;
`refactor(auth): isolate token refresh from request transport`. Avoid `updates`, `WIP` and
`various fixes`. A future reader should understand the change and reason without rereading its diff.

Use a body when the reason, compatibility boundary, preservation requirement or validation would
otherwise be unclear. Include what changed, why, notable decisions and relevant issue IDs. Preserve
source numbers exactly; do not invent estimates or deadlines. For multiline text, create an exact
UTF-8 message file and run `git commit -F "$message_file"`; do not interpolate untrusted text into
shell code. `BREAKING CHANGE:` footers describe incompatible behavior.

## Remote freshness and repair

Fetch the configured destination without changing the worktree, then inspect divergence. Never
pull blindly over someone else's edits. A clean branch may fast-forward with `git pull --ff-only`.
If local commits diverge, use the project's agreed merge/rebase policy; never rewrite published
history without explicit authority. Preserve WIP through an agreed snapshot or owned stash only.
A stash is shared repository state; never pop or drop an unknown stash.

For a conflict, inspect status, base, local and incoming versions. Merge compatible changes and
keep ownership/history clear. Material competing product intent needs a decision; an auth failure
needs a supported reconnect. Never switch to a guessed branch or discard files to silence an error.
After repair, run relevant checks and verify the operation completed. Report unresolved conflicts.

Before an authorized push, verify remote fetch/push destinations, outgoing commits and the actual
branch. Push normally; verify the remote commit afterward. Never force-push, bypass hooks, alter
Git config, delete branches, hard-reset, or clean files merely as a repair shortcut.

## Planning checkpoints

Read `.claude/tasks/config.json` or the active tool-owned `.planning/config.json` when present.
`planning.commit_docs` is inclusion policy, not commit/push authorization. `false` keeps planning
local; `true` allows exact-path staging under normal rules. Ignore rules win for untracked files;
do not force-add ignored planning. Existing tracked history is not silently removed.

One execution system owns each milestone. Baseline planning, executable phase plan, implementation,
and completion evidence are distinct historical rationales. Keep stable plan/task/requirement IDs
in commit bodies when available. Summaries do not replace observable outcome verification.

## Worktree and collaboration boundaries

Read the complete lifecycle recipe before creation or removal. An integrated commit is only one
cleanup gate: local/ignored files, submodules, reflogs, active processes, symlinks and object storage
consumers also matter. Retain unknown ownership and unique work. Never delete branches implicitly.

Shared teams may enable the bundled remote ledger after checking branch/CI/deploy policy.
It prevents cooperative duplicate task/path claims; it is not filesystem enforcement. Research
is exempt. If enabled by project policy, claim verified remaining work before implementation and
check it before edits/commits. Unavailable/conflicting ledgers block claimed implementation.

## Verification and limits

[Claim tests](qa/test_task_claims.py) exercise real disposable bare remotes and independent clones.
[Worktree scenarios](qa/worktree-scenarios.md) supply preservation cases. No live repository cleanup
or remote publication is a test fixture. Optional bundled `norml-tasks` supplies planning records;
all Git mechanics above remain usable alone.
