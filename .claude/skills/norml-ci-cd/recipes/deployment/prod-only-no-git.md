# Pattern: `prod-only-no-git`

> One environment (production). No git. Edits happen directly. Full reliance on host backups as the only undo mechanism. **Avoid.**

## When to use

- **Almost never.** This pattern exists to be named so we can refuse it.
- Acceptable cases (require explicit user approval):
  - Truly throwaway site (single-use landing page, demo for one meeting)
  - Client owns the site entirely and refuses any tooling overhead
  - Host doesn't support git at all (extremely rare, mostly legacy shared hosting)
- All cases require:
  - Solid host backups (`provider` NOT `none`)
  - Explicit user acknowledgement that this pattern is fragile
  - Documented exit plan to upgrade to `prod-only-with-git` or better

## When NOT to use

- Any other pattern is achievable. Use it.

## Environments

| Env | Where | Source of truth | Who deploys |
|---|---|---|---|
| **Production** | The live hosted site | Files on disk + DB (no other copies) | Whoever edits via FTP / WP admin / host file manager |

## Workflow

1. **Backup-before EVERY change.** No exceptions.
2. Edit via WP admin, FTP, host file manager, or SSH if available
3. Verify the change
4. Record exactly what changed and verify the recovery path.

## Database strategy

`single-env`. Direct DB writes only via WP admin or `wp` CLI (with backup-before).

## Backup strategy

Must be a real provider with verified-working backups. Test the restore process on day one. **`provider: "none"` is hard-incompatible with this pattern — refuse to operate.**

If the backup system is the host's panel-based snapshot system, document the restore steps in the per-project `ci-cd.md` so anyone can execute them under pressure.

## Permissions matrix (default — override in per-project `ci-cd.md`)

| Action | Claude can do autonomously | Requires human go-ahead |
|---|---|---|
| Trigger a backup | ✅ (REQUIRED before any other action) | — |
| Verify backup landed | ✅ (REQUIRED) | — |
| Any other write action | — | ✅ |

**Essentially everything except backups requires human go-ahead.** This is intentional — the safety budget is zero, so every action gets reviewed.

## Pre-deploy hooks

1. **Mandatory:** trigger backup, verify it landed
2. Capture the home page (Playwright screenshot) for before/after diff
3. Note exactly which files / DB tables you're about to touch

## Post-deploy hooks

1. Cache flush
2. Smoke test on the live site
3. Visual diff against pre-deploy snapshot
4. If anything looks off, restore from the backup taken in pre-deploy hook

## Gotchas

- **No commit history.** You cannot answer "what changed last Tuesday."
- **No code review.** Mistakes go live instantly.
- **No revert.** Only restore from backup, and only if the backup is current.
- **Concurrent editing destroys work.** If two people FTP'd the same file 5 minutes apart, the second overwrites the first with no warning.
- **Plugin updates are roulette.** A WP admin "update plugin" click can break the site with nowhere to roll back code from.

## Migration path

This pattern is a temporary state, not a destination. The migration to `prod-only-with-git` is:

1. Use verified access to retrieve only the authorized theme source; media is separate backup data
2. `git init` in the theme folder
3. Create a the configured Git repository repo, push the initial commit
4. Add `.gitignore` (node_modules, vendor, compiled output, .env)
5. Document the change in the per-project `ci-cd.md` — `pattern:` flips from `prod-only-no-git` to `prod-only-with-git`

Do this as soon as the project is no longer truly throwaway.

## What this pattern is NOT

- Not a normal way to operate. It's a documented worst case so we can refuse it explicitly.
- Not compatible with vibecode. the project build workflow requires git (per its description) — pair with `prod-only-with-git` or better.

