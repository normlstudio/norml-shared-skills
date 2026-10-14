# Pattern: `local-github-staging-prod`

> Canonical full pipeline. Local development → GitHub pull request → GitHub
> Actions → staging → human review → protected production deploy.

## When to use

- Client-facing or revenue-driving site
- Multiple developers contribute
- Long-running maintenance or regulated work
- Any paid production build with a real staging environment

## When NOT to use

- Small, single-environment project → `local-github-prod`
- Elementor-only site with no meaningful theme code → `elementor-child-with-git`

## Canonical detail

Follow [the bundled full pipeline](../../standards/staging-pipeline.md) for PR validation,
release packaging, protected production deployment, smoke checks and rollback.

## Environments

| Environment | Source of truth | Deploy trigger |
|---|---|---|
| Local | GitHub branch clone | n/a |
| Staging | GitHub code + staging DB | Protected staging workflow after merge/push to the declared staging branch |
| Production | GitHub code + production DB | Protected manual approval in GitHub Actions |

## Workflow

1. Branch from the declared integration branch.
2. Develop and verify locally.
3. Open a GitHub pull request; Actions validates lint/build/tests.
4. Human review and merge.
5. GitHub Actions deploys the declared staging branch.
6. QA staging and resolve failures through new commits.
7. Trigger the protected production workflow only with human approval.
8. Smoke-test production and verify the deployed commit SHA.

## Database strategy

Default: `staging-to-prod-selective`. Initial launches may use
`staging-to-prod-full`; mature editorial sites may use
`content-via-wp-admin-only`. The project contract declares the choice.

## Backup strategy

The project deployment contract must name a real backup provider. A missing backup
blocks production database operations and deployment steps that could destroy
state.

## Permissions matrix

| Action | Autonomous | Human go-ahead |
|---|---|---|
| Edit/build/test locally | ✅ | — |
| Open GitHub pull request | ✅ | — |
| Merge pull request | — | ✅ |
| Deploy staging after approved merge | Per project | Per project |
| Approve/trigger production deploy | — | ✅ |
| Production DB write | — | ✅ |

## Gotchas

- GitHub Actions environments must separate staging and production secrets.
- Production requires a protected manual approval gate.
- A legacy Bitbucket pipeline may remain in history but cannot be called,
  mirrored, or treated as a fallback.
- GitHub is `origin`; any Bitbucket archive remote is fetch-only.

