# Pattern: `local-github-prod`

> Representative local development → the configured Git repository → production via
> an explicit deploy command. **No staging.** GitHub is canonical; local has
> enough fixtures/runtime coverage to validate changes before they go live.

## When to use

- Small or secondary sites with one production environment
- Low-risk, occasional code changes
- Staging is unavailable and local verification is sufficient
- The local site/static mirror is representative enough to validate the affected behavior
- A maintained Git repository is still required as the safety record

## When NOT to use

- Client-critical or revenue-driving site → `local-github-staging-prod`
- Multiple active developers → `local-github-staging-prod`
- Local contains only the theme/disposable fixtures while the real DB and uploads remain production-only → `direct-prod`
- No local development is possible → `prod-only-with-git`

## Environments

| Environment | Where | Source of truth | Deploy owner |
|---|---|---|---|
| Local | Teammate's clone | Source code | n/a |
| Production | Live host | Built code + live DB | Human-approved deploy |
| Staging | None | — | — |

## Workflow

1. Clone from `git@github.com:{owner}/{repo}.git`.
2. Install dependencies and develop locally.
3. Run the build and project checks.
4. Verify a current backup.
5. Commit and push only the intended source; verify the exact remote revision.
6. Deploy that clean revision with the approved command in the project contract.
7. Run cache/smoke checks and confirm deployed revision parity.

## Database strategy

`single-env`. Content changes happen in production through the approved content
path. Every destructive DB operation requires the declared backup checkpoint.

## Backup strategy

Read the project deployment contract `backup` block and the matching strategy
reference. `provider: none` blocks destructive operations.

## Permissions matrix

| Action | Autonomous | Human go-ahead |
|---|---|---|
| Edit/build/test locally | ✅ | — |
| Commit + push feature work to GitHub | ✅ | — |
| Deploy code to production | — | ✅ |
| Post-deploy cache/smoke checks | ✅ | — |
| Destructive production DB or plugin operation | — | ✅ |

## Required hooks

Before deploy: successful build/checks + current backup verification.

After deploy: application/theme cache clear, WordPress cache flush when
applicable, production smoke test, and exact-source commit/push verification.

## Gotchas

- No staging means visual/runtime changes become public at deployment; preserve
  before-state evidence and verify immediately after.
- If local WordPress cannot represent the production content/plugin/media state,
  declare `direct-prod` instead of overstating local QA coverage.
- A legacy `bitbucket-pipelines.yml` may remain for history but is never active.
- A Bitbucket remote may remain only as fetch-only `bitbucket-archive` with a
  disabled push URL; GitHub must be `origin`.

