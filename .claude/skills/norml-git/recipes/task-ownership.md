# Shared task ownership

Owner: `norml-git`. Audience: developers and assistants using a project-enabled
shared ownership protocol across computers. This optional adapter supports GitHub
repositories owned by any authorized user or organization. Python 3.9+, Git and an authenticated GitHub CLI
are required. Existing Git credentials are reused; there is no new service.

## Before implementation — mandatory

1. Resolve the canonical writable GitHub repository and the **actual integration
   branch** from project instructions. Never infer completion from the current
   detached checkout, an issue assignee, a closed source PR, or a local branch.
   Read status and all project instructions without changing existing WIP.
2. Run the audit below. Read issue text, open/merged PRs, issue cross-references,
   integrated `git log`, authors and relevant diffs/code. Search by feature name,
   aliases and developer identities as well as issue number. Work may already
   be integrated by a different PR while the original PR or issue remains open.
   The machine report is evidence to inspect, not a completeness verdict.
3. Classify each requirement as integrated, in an active PR/claim, missing, or
   blocked. Record source commits/PRs and the **remaining delta**. Verify behavior
   if source code alone cannot establish completion. Do not claim an already
   completed task or redo somebody else's active implementation.
4. Agree shared interfaces, literal repository-relative file boundaries and
   acceptance criteria before dispatch. Atomically claim the remaining task.
   A failed, conflicting or ambiguous claim blocks dependent implementation.
5. Use `check` immediately before editing and before staging/committing; supply
   every planned/touched path. Renew at least every 20 minutes and check after
   reconnecting or resuming. Read-only research does not need a claim.

```bash
# Resolve skill-root to this installed package.
python3 "{skill-root}/scripts/task_claims.py" \
  --repo "{project-root}" audit --issue 42 --base develop

# Inspect result.receipt and the report, then use the returned audit path.
python3 "{skill-root}/scripts/task_claims.py" \
  --repo "{project-root}" claim --audit "{audit-receipt}" \
  --owner "Developer One" --session "unique-worker-session" \
  --path src/widget --path tests/widget \
  --remaining "Only the verified missing offline behavior; preserve existing consent fix"

python3 "{skill-root}/scripts/task_claims.py" \
  --repo "{project-root}" check --receipt "{claim-receipt}" --path src/widget/view.js
```

For ClickUp or other tasks without a GitHub issue, use the stable provider ID
with `audit --task clickup-abc123 --keywords "offline widget" --base develop`.
For an internal task use one agreed lowercase slug. The canonical task key is
repository + issue number/provider ID, never title, person, branch or model.
Aliases for the same requirement must resolve to that key before claiming.
Changing the key to get around a conflict is forbidden. Different repositories
have separate ledgers; a cross-repository feature needs claims in every repo
before edits, parked if the full set cannot be acquired.

**One path per flag:** pass several boundaries as `--path src --path tests`.
Never join them as `--path "src,tests"`: a comma inside a scope is invalid,
not a shorthand. The CLI refuses it with instructions to repeat `--path`,
before writing a registry update or saving a lease. This also applies to
`check --path`. Quote a single filename containing spaces, such as
`--path "notes with spaces.txt"`; spaces remain valid. Scopes are literal
paths, not lists to split automatically. Existing ledger records are not
rewritten or released by this validation fix.

## What is shared

The remote branch `norml/task-claims` contains only `claims.json`. Every update
is a commit descended from the observed remote tip and an ordinary fast-forward
push. Simultaneous contenders cannot both replace that tip. The loser refreshes
and rechecks task/path ownership; disjoint updates retry without losing either
record. No force-push, branch replacement, expiry-based stealing or automatic
branch deletion is used.

Each record contains task, human owner, distinct session, file scopes, remaining
work, integration branch/base commit, state, generation and timestamps. Paths
are literal directories/files; `.` reserves the whole repository. Case variants
conflict conservatively across platforms; symlink/nested-checkout paths must
be claimed in their owning repository directly. Equal tasks
or overlapping scopes cannot be acquired by another claim, even in another
worktree, clone or computer. Do not put secrets, client transcripts or large
source documents in descriptions/evidence. The ledger has the repository's
existing visibility and Git write permissions.

Local audit and ownership receipts live under the common Git directory in
`norml/task-claims/`; they are never committed into the application. Git objects
are added, but application HEAD, index, working files and Git configuration
are untouched. Plumbing creates metadata commits without implementation commit
hooks; normal push hooks remain in effect. A receipt is cooperative bookkeeping,
not protection against a repository writer deliberately bypassing the protocol.

**Enablement gate:** before the first claim in a project, inspect branch rules,
CI/deploy triggers and external automation. Reserve this branch for coordination,
exclude it from application deployment and mirror automation, and confirm the
team has write access. Refused hooks/policies stop the claim; do not bypass them.
Service-ledger writes are the scoped coordination operation authorized by task
ownership; they do not authorize publishing an implementation branch.

## Running, review, handoff and integration

The script has global `--repo` and `--remote` options before the command. Results
are JSON; refusals exit 2. All ownership checks read the remote; no cached/offline
fallback grants editing rights.

| Command | Meaning |
|---|---|
| `list` | Read shared records, including retained history and parked tasks |
| `renew --receipt …` | Current owner refreshes heartbeat and resumes active work |
| `park --receipt … --evidence "PR URL or concrete blocker"` | Retain ownership in review/blocked state; stop edits |
| `handoff --receipt … --owner "Developer Two" --session "new-unique-session"` | Explicit transfer; increment generation and invalidate previous receipts |
| `adopt --id {claim-id} --session {assigned-session}` | New computer creates a local receipt for its explicitly assigned live claim |
| `release --receipt … --integrated-commit {full-sha}` | Close after a related implementation commit is verified in the actual remote integration branch |

A 30-minute stale heartbeat blocks the current owner's edits until renewal.
It **never** makes the task available to somebody else. Missing connectivity,
closed terminals, worker completion or elapsed time do not prove abandonment.
If a push outcome is unknown, a pending receipt is printed: reconnect and check
that receipt or explicitly adopt the recorded session. Never create a second
claim on the assumption the first push failed.

An unmerged PR stays owned. Release requires a new commit touching the claimed
scope and reachable from the shared integration branch; the original baseline
commit cannot be used. After squash integration, supply the squash commit and
verify it actually contains this work. Commit reachability is necessary evidence,
not a substitute for acceptance checks. For cancelled work or an unavailable
owner, this initial version intentionally has **no automatic steal/cancel**:
park/retain the claim and arrange a documented explicit handoff with the owner.
Do not manually rewrite the branch to clear an inconvenient lock.

## Coordinators and shared files

The coordinator owns the top-level issue claim. Workers receive its ID, agreed
subtask, allowed files, interface contract and completion checks. They check the
coordinator's live claim with their paths; only the coordinator changes ownership
or releases it. Do not launch a second independent claim for the same issue.
For separate issues, workers may own separate claims with unique session IDs.

Use independent worktrees when changes can intersect. Worktrees isolate files;
the shared claim prevents duplicate task ownership. If two workers need one
common interface file, the coordinator owns that edit and dispatches dependent
implementation only after the contract is fixed. A worker asking to leave its
file boundary must stop until the coordinator updates the plan and resolves
scope ownership. There is no scope-expansion shortcut in the initial CLI.

## Enablement and limits

Before writing a first ledger, obtain explicit authority for coordination-branch writes and
review remote branch protection, CI/deploy triggers and write access. Reserve `norml/task-claims`
for this metadata; no application deployments or mirror triggers may consume it. This package
name is a protocol namespace, not a company ownership requirement. No ledger is created by
installation alone. Core Git operations remain standalone when project policy does not enable it.

All participating developers must adopt the same protocol. The tool cannot discover arbitrary
unpushed work, enforce editor access, steal abandoned tasks or automatically cancel claims.
Existing work needs its actual owner's explicit enrollment. Keep unknown claims and arrange
an explicit handoff. Do not manually edit the ledger to clear inconvenient ownership.

## Verification

Run `python3 qa/test_task_claims.py` from this package. Actual temporary bare remotes and
independent clones test rejected races, disjoint retries, overlap, network failure, WIP
preservation, explicit handoff and integration release. GitHub API reads are mocked in that
suite; live authentication and the user's branch-trigger policy are verified separately.

Protocol basis: [Git push](https://git-scm.com/docs/git-push),
[Git commit-tree](https://git-scm.com/docs/git-commit-tree), and GitHub CLI issue/PR reads.
The script's JSON audit is evidence to inspect, not a semantic completion verdict.
