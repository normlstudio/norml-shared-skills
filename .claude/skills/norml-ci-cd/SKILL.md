---
name: norml-ci-cd
version: 1.0.0
description: >
  Select and document a portable WordPress deployment topology, database ownership strategy, backup strategy and optional MVP delivery mode. Use for pipeline setup, deployment policy, staging promotion planning, theme-only local workspaces, or backup/restore design. Creates a project deployment contract; does not deploy or issue credentials.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml CI/CD


This package defines how a project ships. It does not execute deployment. It works with a
user-owned Git repository, any supported WordPress host, and the tools already selected by
the project. No shared drive, company account, private skill or internal service is required.

## Inputs and authority

Read existing project instructions and the deployment contract before changing policy.
Discover the actual code repository, staging/production targets, active theme, WordPress
root, runtime versions, current backup and authorized deployment method. Never guess an SSH
host, path or environment from a name. Read-only discovery may continue when a write gate
is unresolved. Secrets belong in provider-managed authentication, the OS protected store,
or a CI environment secret store; record references and non-secret metadata only.

A user instruction already authorizing a specific deploy satisfies its approval gate.
Choosing a topology does not authorize a production deploy or destructive database sync.

## Select the topology

Read [the catalog](recipes/deployment.md) and the selected recipe in full.

| Pattern | Appropriate use |
|---|---|
| `local-github-prod` | Representative local verification; source in a Git remote; direct production deploy |
| `direct-prod` | Theme-only local clone with optional disposable WordPress fixtures; live DB/media stay remote |
| `local-github-staging-prod` | Pull requests and CI; staging validation before protected production deployment |
| `prod-only-with-git` | Explicitly accepted legacy constraint: source changes on the host with Git and backups |
| `prod-only-no-git` | Explicitly accepted temporary fallback with tested backups and a migration plan |
| `staging-only-no-git` | Builder-managed staging; carefully bounded data promotion |
| `elementor-child-with-git` | Builder content and a versioned child theme follow separate tracks |

The historical `github` names identify the example topology, not a mandatory company
organization. Use the user's supported Git host and document different CI mechanics.
If no contract exists, treat `local-github-prod` as a provisional recommendation. Verify
that local checks are representative before selecting it. A missing contract grants no
production authority. Real staging usually selects the staging pattern; disposable local
fixtures select `direct-prod`; a builder usually selects the child-theme pattern.

## Database ownership

Read [database strategies](recipes/database.md), then the selected strategy.

- `single-env`: production is the only real data source; backup and read-back every write.
- `staging-to-prod-full`: initial launch or explicitly reviewed replacement; protect live data.
- `staging-to-prod-selective`: explicitly identified records/options; never replace shared post tables.
- `content-via-wp-admin-only`: developers ship code; editors own live values/content.

Do not combine an ongoing production service with routine full staging DB replacement.
ACF field definitions are versioned schema; field values are live data. WordPress data
and database dumps never go into Git. Production-only records must survive promotion.

## Backups

Read [backup strategies](recipes/backup.md). Select `managed-host`, `shared-host`,
`vps-no-builtin`, or `cloud-aws-custom`. Record actual retention, freshness, granularity,
storage, credential references and tested restore commands. Do not infer a provider's
current API, plan entitlement, timing or price from examples in this package. Verify its
current official interface before operating it. A declared backup without evidence is
not a verified recovery point. Missing/unusable backups block destructive operations.

## Operating mode

[Optional MVP mode](modes/mvp-mode.md) changes delivery ceremony, not deployment topology.
Use only when the user deliberately selects live feedback and optional staging/local parity.
Keep exact source revision, protected secrets, data gates, rollback and live smoke verification.
A standard project uses its normal pattern gates. Do not silently infer MVP mode from age.

## Write the project contract

Use [the template](templates/ci-cd.md) at the existing project contract location, or default
`{project-root}/.claude/ci-cd.md`. Preserve an existing approved topology and instructions.
Record verified environment roots, local mode, database/backup strategy, permission matrix,
exact deployment/rollback commands, pre/post hooks, review gates and known constraints.
Link it from the existing project instructions. Replace every unresolved field with an
explicit blocker rather than plausible commands. Document consent only for verified scope.

## Consumption before a deploy

The operator reads contract → pattern → database recipe → backup recipe → selected mode.
The operator then checks authorization, performs backup/build checks, publishes exact source,
deploys that revision, clears appropriate caches and verifies live behavior and revision.
For a staging CI setup, [the bundled pipeline guide](standards/staging-pipeline.md) provides
PR validation, release packaging, protected environments and rollback detail.

## Hard boundaries

- A thin local site never connects to production's DB or routinely downloads DB/media.
- Under `direct-prod`, edit locally, publish to Git, then deploy; never hot-edit live source.
- Stage only owned paths; preserve other sessions' work and unexpected server drift.
- A destructive sync requires a reviewed dry-run where supported, exact allowlists and recovery.
- Keep deployment metadata separate from secret values; never print or commit secrets.
- Use purpose-built API/CLI operations. A disconnected connector is not browser authority.
- Report policy preparation separately from executed/verified deployment.

Optional sibling `norml-wp-developer` can execute the resulting engineering workflow,
but everything needed to select and document the policy is bundled here.
