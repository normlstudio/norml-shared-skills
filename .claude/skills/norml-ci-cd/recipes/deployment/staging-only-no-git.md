# Pattern: `staging-only-no-git`

> Staging is the source of truth. Site is edited on staging (via WP admin / Elementor / page builder). Promote = copy staging → production.

## When to use

- Elementor / Divi / Bricks / page-builder-only site with no real theme code
- Site is built by a designer / non-dev editing in WP admin
- Code-side maintenance is minimal — most "changes" are content + layout in the builder
- The team isn't going to write Blade or PHP for this project

## When NOT to use

- Theme has real code (Sage / custom PHP / Blade) → use one of the git-based patterns
- Editor / content team will manage production directly → `single-env` patterns
- Site needs version control on code → `elementor-child-with-git` (the upgrade)

## Environments

| Env | Where | Source of truth | Who deploys |
|---|---|---|---|
| **Staging** | `staging.{domain}` or similar | Files + DB (builder content) | Editor via WP admin |
| **Production** | The live hosted site | Mirror of staging at last promote | Teammate via staging→prod sync |
| Local | **None** | — | — |
| GitHub | **None** | — | — |

## Workflow

1. **Edit on staging:**
   - Designer / editor goes to staging URL
   - Logs into wp-admin
   - Edits pages via Elementor or whatever page builder
2. **Visual review on staging** by the team / client
3. **Promote staging → production:** read the bundled full/ selective DB strategy,
   verify recovery and production-only state, apply serialization-aware export rewrites
   without mutating staging, import only the approved target and sync approved media
   incrementally through a valid one-hop/relay transfer. Clear appropriate caches and verify.
4. **No git involvement** — there is no code repo to commit to

## Database strategy

`staging-to-prod-full` only when replacement is explicitly approved and production has no
protected divergent state. Builder templates/content are database-backed, but that does not
make full DB replacement the only promotion mechanism. Use a scoped migration/export
workflow for an ongoing live site.

**Exception:** if the editor team is also managing prod-side options (e.g., form submissions, post comments, RankMath data), use `staging-to-prod-selective` to avoid clobbering those. Define exactly which tables / options sync in the per-project `ci-cd.md`.

## Backup strategy

Real provider, verified-working. Same as `prod-only-with-git` — the DB IS the site, so backups are the only undo.

## Permissions matrix (default — override in per-project `ci-cd.md`)

| Action | Claude can do autonomously | Requires human go-ahead |
|---|---|---|
| Edit content on staging via WP admin / REST | ✅ | — |
| Trigger staging backup | ✅ | — |
| Trigger production backup before promote | ✅ (REQUIRED) | — |
| Run staging→prod DB sync | — | ✅ |
| Run staging→prod uploads rsync | — | ✅ |
| Plugin / theme changes on prod | — | ✅ |
| `wp db` destructive commands on prod | — | ✅ |

## Pre-promote hooks (staging → prod)

1. Backup production DB → verify the dump file is non-empty and recent
2. Backup production `wp-content/uploads/` (or confirm host backup is current)
3. Take a Playwright snapshot of the production home page (for visual diff after)

## Post-promote hooks

1. Cache flush on production
2. Smoke test
3. Visual diff against pre-promote snapshot of home + 2-3 key pages
4. If anything looks broken, restore from the pre-promote backup

## Gotchas

- **DB sync is destructive by nature.** Every promote replaces production DB with staging's. Anything entered on production after the last promote (form submissions, comments, RankMath analytics) is gone unless protected by selective sync.
- **Serialized data in WP options** breaks with `sed`. ALWAYS use `wp search-replace`, never `sed -i`.
- **Page builder caches** (Elementor CSS, Divi static files) need explicit regeneration after promote. Add to post-promote hooks if relevant.
- **No code rollback.** A bad promote can only be reverted by restoring the pre-promote DB backup.
- **No commit history of changes.** Editor changes are visible in the builder's revision system at best, but there's no audit trail of "what changed in the last 30 days."

## Migration path

The cleaner upgrade is `elementor-child-with-git`:
1. Create a child theme of Hello Elementor (or whichever parent)
2. Push to the configured Git repository
3. Use the child theme's `.claude/` to track deploy contracts and project notes
4. Editing still happens in Elementor on staging — but now there's a git home

This pattern (`staging-only-no-git`) should only exist when even a child theme can't be installed (extreme legacy / managed-host limitations).

## What this pattern is NOT

- Not the right choice when ANY code-side work is expected — that's `elementor-child-with-git` or better
- Not safe for client-critical sites without strong backups
- Not "vibecode-able" — vibecode requires git

