# GitHub mirror contract

Repository task files own scope, steps, priority, status, and acceptance evidence.
Issues make that work visible and discussable by the team. The index is derived
from task files; neither index nor issue is an independent execution master.

## Identity and managed content

One concrete task ↔ at most one issue in its configured repository. The task
frontmatter stores the full issue URL. Issue bodies have one marked region:

```markdown
<!-- norml-task: sample-plugin::TASK-001 -->
## Planning record
.claude/tasks/items/task-001-add-control.md

## Outcome and scope
Approved outcome, relevant constraints, bounded scope.

## Acceptance
- [ ] Observable acceptance criterion.

## Current plan
Task status, queue, priority; link to relevant plan and PR if present.
<!-- /norml-task -->
```

Use the immutable `owner_id::TASK-NNN` marker, never the title, as identity.
Preserve all text outside the region and all comments. The owned region may be
replaced only after comparing it to the last confirmed snapshot. Existing issue
adoption preserves its original body and records the accepted source mapping;
do not erase the original specification just to fit a new format.

Scope excludes confidential workspace notes, credentials, raw private transcripts,
and unapproved commercial commitments. Include the actionable accepted task,
not everything the AI read while planning it. User-written titles/labels stay
unless explicitly reconciled; never replace an issue's entire label set.

## Three-way reconciliation

`sync/github-state.json` maps qualified task ID to repository, issue number/URL,
last confirmed canonical task digest, managed-region text/digest, remote state,
last observed title and labels, and the remote `updatedAt` value. Write it only
after re-reading and confirming a successful remote operation. No secret values.

| Change since last confirmed snapshot | Action |
|---|---|
| Neither side changed | No-op |
| Local only | Re-read remote, then update only owned fields/region |
| Remote only | Read change/comments as team input; apply accepted change to task, regenerate mirror |
| Both changed | Compare field by field; merge disjoint edits, record incompatible changes as sync conflict |
| First sync / snapshot missing | Re-read both; adopt only after semantic match; never assume overwrite permission |
| Remote closed, local open | Inspect reason and PR/evidence; done only if acceptance passes; otherwise conflict |
| Local done, remote open | Verify acceptance and configured merge/deploy condition, then close |
| Remote deleted/transferred | Record missing/moved target; follow verified new identity, do not blindly recreate |

Remote closure might mean duplicate, canceled, or completed. It cannot blindly
check off the local task. Do not auto-reopen a teammate's issue while reconciling
an unresolved difference. Conflicts block dependent execution/completion but
must not stop unrelated ready work.

## Recovery and concurrency

Append operation intent and result to `sync/github-log.jsonl`: operation ID,
qualified task ID, repo, desired change hash, issue URL when known, outcome
(`confirmed`, `failed`, `unknown`, `conflict`) and timestamp. No raw secrets.
On timeout or an uncertain create result, record unknown and enumerate issues
by marker before retry. Wait for full enumeration to succeed; never treat a
failed/partial response as zero matches. More than one matching marker is a
conflict; do not delete duplicates automatically.

Use one writer per task. Before any remote write, re-fetch the issue and verify
its state/managed text still matches the just-reviewed version. If it changed,
reconcile again. CLI writes are not transactional compare-and-swap: post-write
readback is required; concurrent ambiguity must remain visible. Retry after
rate limit/auth/network failure only through supported API/CLI; local planning
remains saved and mirror state remains pending.

## Completion semantics

Record the task's completion definition: acceptance checks plus merge/deploy
only when required. Intermediate PRs reference the issue without closing it.
GitHub closing keywords apply when a PR targets the repository's default branch;
verify the branch and actual issue state after merge. Never assume it is `main`.
Manual issue close does not require a comment. Comments/messages require explicit
authorization even when issue creation/updating itself is authorized.

Primary mechanics checked Sep 7, 2026:
[GitHub CLI issue commands](https://cli.github.com/manual/gh_issue) and
[GitHub PR/issue linking](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
