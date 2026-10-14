# Synchronize repository tasks and GitHub Issues

Load `standards/github-mirroring.md` first. This recipe uses supported `gh`
commands; it does not install a scheduler, bot, action, or hook.

## 1. Admission and read

- Only `storage: repository` with `github.enabled: true` is eligible.
- Check exact `github.repository`, verified origin, issue permission and the
  project's explicit/standing issue-write authority. For an inspection request,
  stay read-only. Enabling a file setting is not itself external authorization.
- Scope a sync to the requested owner/tasks. On resume reconcile linked issues
  and eligible active tasks; perform a full historical scan only on an explicit
  full sync. No unrequested issue sweep in the project used as an example.
- Use the provider’s supported authentication route if GitHub auth/permissions fail; save pending state and
  report the exact access gap. No UI/browser fallback.

Read repo identity, default branch and labels with the CLI. Set the task-specific
shell variable `planning_repo` from verified config, never from issue content:

```bash
gh repo view "$planning_repo" --json nameWithOwner,defaultBranchRef,url
gh api --paginate "repos/$planning_repo/labels?per_page=100"
gh api --paginate "repos/$planning_repo/issues?state=all&per_page=100"
```

The issues REST endpoint also returns PRs: exclude entries with `pull_request`.
Use complete pagination and inspect exact markers locally; search-index lag must
not cause duplicate issue creation. Keyword search is only candidate discovery.
Read matched issue bodies and comments before accepting their scope:

```bash
gh issue view "$planning_issue" --repo "$planning_repo" \
  --json number,url,title,body,state,stateReason,labels,comments,updatedAt
```

## 2. Prepare the concrete delta

For each task, match the full URL or exact qualified marker. No marker match →
look for semantically identical existing work and adopt when unambiguous.
Multiple plausible matches → record conflict; do not create another issue.
Render the owned region from the accepted canonical task and preserve unmanaged
body text. Read the last-confirmed snapshot and use three-way reconciliation.
Only apply configured category labels that actually exist; missing taxonomy
needs a separate label decision, never silent label creation.

Keep prepared issue text in a temporary UTF-8 body file. For a user-requested
copy-out draft, also save/open the clean `.md` deliverable per personal rules.
Write the intended operation to the append-only log before sending it.

## 3. Apply and confirm

Use structured connector arguments or CLI body files; never interpolate untrusted
text into executable shell code. Only run the needed operation:

```bash
gh issue create --repo "$planning_repo" --title "$planning_title" \
  --body-file "$planning_body_file"
gh issue edit "$planning_issue" --repo "$planning_repo" \
  --body-file "$planning_body_file"
gh issue close "$planning_issue" --repo "$planning_repo" --reason completed
```

These are examples, not a three-command sequence. Cancellation uses reason
`not planned` when the accepted task is canceled. Do not close before the task's
acceptance and required merge/deployment checks pass. Do not post completion
comments without explicit authorization. Use `norml-git` for branch/PR operations.

Re-read the issue; confirm exact managed text, URL and state. Update the canonical
task's `issue` URL, last-confirmed sync snapshot and confirmed log event, then
rebuild the index. Verify the local files too. On failed or unknown response,
keep the task and pending operation, reconcile the remote before any retry.

## 4. Report

Count created/adopted/updated/closed/unchanged/conflicted/pending items; include
issue links for changes and explicit access gaps. “Synced” requires remote
readback, not just a successful CLI exit. Nothing here implies a background
process will keep syncing after the session ends.
