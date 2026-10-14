# Commit and synchronize a repository

1. Read the repository instructions, actual integration branch and operation authority.
2. Inspect status, staged/unstaged diff, untracked files and remote identity without printing secrets.
3. Fetch authorized refs and inspect divergence; preserve another worker's changes and index.
4. If the optional shared ledger is enabled, check the current lease for every changed path.
5. Resolve planning inclusion, group by rationale, inspect artifacts/secrets, stage exact paths.
6. Run applicable checks and create Conventional Commits with meaningful rationale.
7. Push only when requested or covered by an explicit project policy; verify the remote SHA.
8. Record status, subjects, verification and remaining work. A commit is not a deployment.

A pull request or review branch follows the project's policy. Check the real default branch.
Use supported host CLI/API, and body files for untrusted multiline text. Issue/PR comments and
messages require authorization. Authentication failures never justify browser takeover or secrets
in config. Use an installed supported connector or user-approved provider login.

For worktree creation and handoff, consume [the lifecycle](worktree-lifecycle.md). Save task
state/evidence outside a disposable checkout before retiring it. Publication does not authorize
cleaning other workers' checkouts.
