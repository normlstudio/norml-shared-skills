# Norml CI/CD

> Choose and document how a WordPress project deploys, protects live data and recovers from failure.

## The problem

A code deploy, a database promotion and a media sync can affect very different state. Treating them
as one operation can overwrite live work.

This package records topology, data ownership, backups, permissions and exact verification before
another operator ships.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Set up CI/CD for this WordPress project | *"Set up CI/CD for this WordPress project"* |
| Which deployment pattern applies here | *"Which deployment pattern applies here"* |
| Prepare staging-to-production policy | *"Prepare staging-to-production policy"* |
| Create a theme-only local workspace contract | *"Create a theme-only local workspace contract"* |
| Set up the backup and restore strategy | *"Set up the backup and restore strategy"* |
| Put this project in MVP mode | *"Put this project in MVP mode"* |

## A typical run

1. Ask for a policy for the supplied WordPress repository and live URL.
2. The agent reads current instructions, discovers actual theme/site roots and determines whether
local fixtures represent live behavior.
3. It selects the deployment pattern and appropriate database/backup strategy, then writes the
existing contract or `.claude/ci-cd.md`.
4. It records supported deploy/rollback commands, prior authorization and unresolved backup/access
evidence. Deployment remains a separate operation.

---

## Inputs and outputs

Provide the repository, known URLs, existing deployment contract and current scope of authority.
Access is used only through a configured provider/SSH/CLI connection. Unknown values remain
explicit blockers. The output is a non-secret project deployment contract, not copied auth state.

## Deployment patterns in depth

| Pattern | What local work contains | How live state is treated |
|---|---|---|
| `local-github-prod` | Representative source/runtime fixtures | Direct approved deploy; production owns data |
| `direct-prod` | Theme code and optional disposable WP shell | DB/uploads stay live; all real WP-CLI is remote |
| `local-github-staging-prod` | Source and local testing | CI/staging review before protected production release |
| `prod-only-with-git` | Host-side source when local is impossible | Every write has backup, Git record and live verification |
| `prod-only-no-git` | No independent source history | Temporary explicit fallback with tested restore and exit plan |
| `staging-only-no-git` | Builder changes on staging | Reviewed database/media promotion; protected live state preserved |
| `elementor-child-with-git` | Versioned child theme plus editor-owned layouts | Separate code and builder-content tracks |

The names retain the source topology vocabulary. They do not require the publisher's GitHub
organization. A user-owned Git host or provider-native pipeline is valid when its exact
mechanics are recorded. A missing contract supplies a provisional recommendation, not authority.

## Database strategies in depth

- **Single environment:** the live DB is authoritative. Back up and verify writes remotely.
  Local fixture databases do not sync back and never connect to the live database.
- **Full staging replacement:** appropriate at initial launch or a deliberately accepted
  replacement. It can destroy production-only orders/users/submissions/editor work.
- **Selective migration:** identify exact source/target records and eligible fields; retain
  a conflict/idempotency policy, relationships and rollback. Shared post tables are not a slice.
- **Editor ownership:** developers deploy definitions/code; editors manage live content/values.
  A code release never silently imports editorial database state.

WordPress serialized values need serialization-aware rewrites. `sed` on SQL is unsafe.
The full strategy uses `wp search-replace --export` so the source site is not modified.
A WXR import can duplicate existing posts; rehearsal and identifier mapping are required.
Neither an assumed `wp db export --where` nor an assumed ACF CLI extension is a supported contract.

## Backup strategies in depth

| Backup strategy | What must be verified |
|---|---|
| Managed host | Current completed snapshot, exact environment, retention, restore granularity |
| Shared host | Per-site versus account-wide scope, available panel/API route and current snapshot |
| VPS | Private DB/media capture, off-site encrypted storage, failure monitoring and restore test |
| Cloud | Coordinated database/storage/config snapshots, region, retention and on-call runbook |

The package does not promise current provider prices, retention entitlements or restore duration.
Use supported provider interfaces and the actual account plan. Panel-only verification may need
narrow user involvement; an unavailable API is not permission to take over a browser.

## MVP mode

MVP mode is deliberately selected when live feedback is the accepted testing surface and
local/staging parity is optional. The topology stays separate. Exact source revision,
protected secrets, backup/data gates, rollback and live behavior verification remain required.
The project records intentional debt and how to return to standard mode.

## The full CI pipeline

`standards/staging-pipeline.md` includes separate PR validation, staging release and protected
production jobs. It covers dev-tool dependency installation, production-only runtime packaging,
retaining Blade templates, artifact checksums, host verification and deployment concurrency.
It also separates code rollback from data/media recovery and provides inline smoke checks.

## Common scenarios

### Small site with reliable local checks

Select `local-github-prod`, record a current backup and approved exact deploy destination,
commit/push the source revision, then have the authorized operator deploy and verify it.
If local data cannot represent live plugins/content/media, record that limitation or use
`direct-prod`.

### Theme-only fleet workspace

Select `direct-prod`. Clone only theme source and optional disposable fixtures. Production
WP-CLI stays rooted at one verified remote site. Do not download live media/DB as routine work.
Every source fix starts locally and ships as a clean pushed revision; no live hot edits.

### Live builder site with submissions

A template/content export must protect submissions, users and other diverging data. Select
an exact migration path rather than a full DB overwrite. Keep the child-theme code track separate.

## When something breaks

| Finding | Response |
|---|---|
| Deployment root cannot be proved | Continue read-only discovery; block writes |
| Backup is missing or in progress | Block destructive operations until completed recovery evidence |
| Production files drift from source | Reconcile ownership deliberately before overwrite |
| Candidate contains unrelated WIP | Scope the source; never blanket-stage or deploy it |
| Full sync would lose live state | Switch to a reviewed selective/editor-owned path |
| Declared provider command is unsupported | Verify current official route and update the project contract |

## Security and scope

Credential values stay in provider-managed authentication, the OS protected store or CI secrets.
Project docs store only references/metadata. Use exact allowlists and review deletion dry-runs.
The package does not send notifications, install providers, create subscriptions or deploy by
selection.

## Package versus project files

The package supplies catalogs and templates. The user's `.claude/ci-cd.md` is a generated
project artifact. Keep runtime secrets, private dumps, releases and QA evidence under the
project's appropriate protected storage; they are not public package files.

## Install and source

Source collection: [norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
From the collection root, install this complete folder with the local installer:

```bash
python3 scripts/install.py --destination <project>/.claude/skills --skill norml-ci-cd
```

Replace `<project>` with the real project directory. The installer does not overwrite
existing packages by default, mutate runtime settings, fetch credentials or install dependencies.
See the collection README for verified installation/runtime scope. Provider and project
workflows in the skill are instructions; installation is not live-operation verification.

## Inside the installed package

- `SKILL.md` — Runtime selection and policy router.
- `recipes/deployment/` — Seven topology procedures.
- `recipes/database/` — Four data ownership/migration strategies.
- `recipes/backup/` — Managed/shared/VPS/cloud recovery patterns.
- `modes/mvp-mode.md` — Optional live-feedback delivery overlay.
- `templates/ci-cd.md` — Non-secret project contract.
- `standards/staging-pipeline.md` — Self-contained full CI/release/rollback guide.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
