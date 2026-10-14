# Pattern: `prod-only-with-git`

> One environment (production). Git as a safety net for source code. Edits happen directly on production with a backup-before for every change.

## When to use

- Local dev is genuinely not viable (host is non-portable, vendor lock-in, can't run the stack locally)
- Site is too small to justify staging
- Site lives on a VPS where running git on the server is acceptable (and the user has agreed)
- Backups are solid (host-builtin or scripted-to-cloud) — non-negotiable for this pattern

## When NOT to use

- A local theme edit surface is viable, even without production DB/uploads → `direct-prod`
- A representative full local environment is viable → `local-github-prod`
- Site is client-facing and revenue-generating → `local-github-staging-prod` (set up local + staging first)
- No backup system at all → set up backups first; refuse to operate in this pattern without them

## Environments

| Env | Where | Source of truth | Who deploys |
|---|---|---|---|
| **Production** | The live hosted site, with `.git/` on the server | Code on server (synced to GitHub) + DB | Teammate via SSH; commits push from server to GitHub |
| Local | **None** (or read-only clone for reference) | — | — |
| Staging | **None** | — | — |

## Workflow

1. **One-time setup:**
   - SSH to production
   - `git init` in the theme folder (or `git clone` from GitHub if repo exists)
   - Add the GitHub remote with a deploy key (read+write)
   - Run `git config core.sshCommand "ssh -i {protected-private-key-path} -o IdentitiesOnly=yes"` per-repo
   - Confirm `.gitignore` excludes `node_modules/`, `vendor/`, compiled output, `.env`
2. **Per change:**
   - **Pre-deploy:** trigger a backup, verify it landed (see `recipes/backup/{provider}.md`)
   - SSH into production
   - Edit theme files directly (or via vibecode through SSH)
   - If Vite is needed: requires Node installed on the server (acceptable trade-off for this pattern; otherwise restrict to changes that don't need a build)
   - Run any post-edit step (cache flush, `wp acorn view:cache`)
   - Smoke test the change live
3. **Commit on the server:**
   ```bash
   git add -- {owned-paths}
git commit -m "fix(theme): explain the verified change"
git push origin {branch}
   ```
   - This is the safety net — if the change breaks something, `git revert HEAD` rolls back the source instantly
4. **DB changes:** backup-before, then edit. Always.

## Database strategy

`single-env`. There's only production. All DB writes are direct + backup-before.

## Backup strategy

Must be a real provider — `managed-host`, `shared-host`, `vps-no-builtin` (with a working cloud-backup script), or `cloud-aws-custom` (with a working custom flow). **`provider: "none"` is incompatible with this pattern.**

## Permissions matrix (default — override in per-project `ci-cd.md`)

| Action | Claude can do autonomously | Requires human go-ahead |
|---|---|---|
| Edit source files on production via SSH | — | ✅ |
| Trigger a backup before any change | ✅ (REQUIRED before any other action) | — |
| Run post-deploy hooks (cache flush, view cache) | ✅ | — |
| `git add` + commit + push on the server | ✅ | — |
| `git revert HEAD` to roll back | ✅ | — |
| Plugin install/activate/deactivate | — | ✅ |
| Theme switch | — | ✅ |
| `wp db` destructive commands | — | ✅ |
| `wp eval` / arbitrary PHP | — | ✅ |

## Pre-deploy hooks

1. **Mandatory:** verify backup is recent (≤ 24h), and trigger a fresh one if older
2. Note the current `git rev-parse HEAD` so you know the rollback target
3. (Optional) Snapshot the home page (Playwright) for before/after comparison

## Post-deploy hooks

1. Cache flush (`wp cache flush`, `wp acorn view:clear`, etc.)
2. Smoke test the changed URL
3. (Optional) Visual diff against pre-deploy snapshot

## Gotchas

- **You're editing live code.** Every save changes the running site. A typo can take the site down.
- **Backups are the only safety net.** If a backup isn't recent or doesn't work, this pattern is unsafe.
- **Vite on the server is a security trade-off.** Adds Node + npm + a dev server to a production host. Only justifiable if local dev is truly impossible.
- **Don't drift from GitHub.** Commit every change on the server. Otherwise the repo decays and the next dev's pull will conflict catastrophically.
- **`wp db` operations are extra dangerous.** Always backup-before. Always.

## What this pattern is NOT

- Not the same as `prod-only-no-git`. Git IS present here; that's the whole point. Without git, this pattern collapses into the no-git variant and loses its safety net.
- Not an excuse to skip a local source workspace. If a theme-only clone becomes viable, upgrade to `direct-prod`; if a representative local runtime becomes viable, upgrade to `local-github-prod`.

