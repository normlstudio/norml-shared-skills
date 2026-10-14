# Pattern: `direct-prod`

> Production-direct WordPress with a thin local code workspace. The theme is
> cloned locally and tracked in GitHub; the production database and uploads
> stay on production. Local WP is the preferred disposable shell, not a data
> mirror. All real database work uses remote WP-CLI against the verified live
> site path.

## When to use

- A owner-managed fleet, directory, or thematic site ships directly to production
- Many sites must remain available locally without downloading large uploads or databases
- AI needs a complete local theme tree for inspection, editing, builds, and git history
- Production is the only representative runtime/data environment
- A current backup and verified SSH/WP-CLI access exist

Local WP is preferred because it provides a stable PHP/WordPress shell when a
developer wants to lint, activate the theme, or render fixture pages. The site
does not need to be running for ordinary source inspection, editing, git, or
frontend builds; start only the one currently being checked.

## When NOT to use

- A staging environment exists or the site is client-critical/revenue-driving → `local-github-staging-prod`
- A representative local database/media copy is required for reliable pre-deploy QA → `local-github-prod`
- The project is Elementor/page-builder-first with little theme code → `elementor-child-with-git`
- Theme code can only be edited on the host and no local source workspace is viable → `prod-only-with-git`
- Production backup, exact document root, or SSH/WP-CLI access cannot be verified

## Source-of-truth split

| Concern | Source of truth | Explicitly not the source of truth |
|---|---|---|
| Theme source, `.claude/`, lockfiles | the configured Git repository | Production filesystem |
| Current working copy | Local theme clone | A server-side editor |
| Live content, options, users, plugin state | Production database | Local WP's disposable DB |
| Media library | Production `wp-content/uploads/` | Local uploads |
| Runtime truth | Production URL | Fixture-only local pages |

The local clone may live directly at the Local WP theme path or in another local
folder linked into it. Both are one pattern. Record `Mode: local-wp-thin`
(preferred) or `Mode: theme-only` in the project `ci-cd.md`.

## Non-negotiable boundaries

1. **Never point local `wp-config.php` at the production database.** Remote DB access from a laptop bypasses the production application boundary, makes local plugins/code capable of live writes, and usually fails because of host network restrictions and environment-specific URLs.
2. **Never routinely download or sync production DB/uploads.** The thin clone is intentionally code-only. A separately approved migration or incident workflow is outside this pattern.
3. **Never inspect or edit production theme files as the working copy.** AI analyzes and changes the local repository. Production SSH is limited to scoped deploy, integrity/drift checks, remote WP-CLI, cache work, and verification.
4. **Never hot-fix the production theme.** Every code change follows local → GitHub → production, including urgent follow-ups.
5. **Never deploy an unpushed or dirty worktree.** Production must map to a clean revision already present in GitHub.

## One-time setup

1. Resolve the non-secret project deployment contract, then verify the exact production site root, theme root, SSH target, WP-CLI PHP binary, and backup provider. Do not infer a broad account path.
2. Create or resolve a user-owned Git repository with the `wordpress-website` topic. GitHub is canonical.
3. Seed the local repository from GitHub or a supplied theme source. If production is the only existing copy, retrieving that exact theme folder is a separate, explicitly authorized bootstrap step; never crawl or copy the full hosting account, `wp-content`, uploads, or database.
4. Preferred: create a stopped-by-default Local WP site and place/clone the repository at `app/public/wp-content/themes/{theme-slug}`. Give it a clean disposable local database; do not import production data.
5. Fallback: keep a theme-only clone anywhere on disk. PHP syntax checks and frontend builds still work, but WordPress rendering/local WP-CLI do not.
6. Keep local `wp-content/uploads/` empty and ignored. Keep DB dumps, `.env`, Local configuration, logs, caches, `node_modules/`, and secrets out of git.
7. Record the exact allowlisted deploy source/destination, excludes, remote WP-CLI prefix, cache hooks, backup check, and rollback command in `.claude/ci-cd.md`.
8. Run a deploy dry-run and a read-only remote WP-CLI check. Do not ship until the destination is proven to be the exact production theme path.

## Per-change workflow

1. **Sync locally.** Pull with fast-forward only and inspect the local theme tree. If the working tree contains unrelated changes, preserve them and scope this change separately.
2. **Check production drift without adopting production as the workspace.** Use the project's declared commit/checksum or scoped deploy dry-run. If production contains unexpected theme changes, stop; reconcile deliberately before overwriting anything.
3. **Edit locally.** Change only the theme repository. Use local static analysis, PHP lint, tests, and frontend builds. Start Local WP only when its disposable fixture site adds useful coverage.
4. **Inspect live data narrowly when needed.** Run read-only WP-CLI through SSH against the verified production site root. Return only the rows/fields needed for the task; do not export the DB as routine analysis.
5. **Prepare production.** Obtain human go-ahead for the deploy, verify the declared backup checkpoint, run the build/checks, and confirm the worktree contains only the intended change.
6. **Publish the revision.** Create the Conventional Commit and push it to GitHub before deployment. Confirm local `HEAD` equals its upstream revision.
7. **Deploy that revision only.** Use the exact project command: preferably a production fast-forward pull with a read-only deploy key, or a theme-scoped rsync/SFTP release from the clean local revision. A destructive sync requires a reviewed dry-run and explicit excludes/allowlist.
8. **Run production-side follow-ups.** Execute cache commands and any approved WP-CLI changes remotely. Every production DB write uses the `single-env` backup/verify process; never run it through local WP-CLI.
9. **Verify.** Smoke-test the changed live URLs and confirm the deployed commit/checksum matches the pushed revision. If a fix is needed, repeat the workflow from the local clone.

## Local WP operating contract

- Local WP is a **shell and preview convenience**, not a production mirror.
- Its database may contain minimal disposable fixtures. Those fixtures never sync to production.
- Its uploads may stay empty. Missing live images are expected; visual truth is checked on production after deploy.
- Local-only admin users, URLs, plugin state, and options are not evidence of production state.
- Local WP can remain stopped while AI reads files or runs git/frontend tooling, so a 30-site fleet does not require 30 running WordPress instances.
- Use local WP-CLI only against the disposable local site. Production WP-CLI is always an SSH command rooted at the verified live site.

## Remote WP-CLI shape

The project contract stores the exact prefix so every command reaches one
verified site rather than whichever WordPress install the SSH account happens
to default to:

```bash
ssh {ssh_alias} 'cd {production_site_path} && {wp_cli_php} {wp_binary} --path={production_site_path} theme status'
```

Replace only the trailing WP-CLI subcommand. Read-only commands may run under
the permissions matrix; writes first pass the production backup and approval
gate. Never reuse the local site's `wp` wrapper for production.

## Deployment implementations

Pick one per project and write the exact command in `.claude/ci-cd.md`.

### A. Production pulls the pushed revision

Preferred when the host permits git and the repository checkout is protected
from web access. The production deploy key is read-only.

```bash
# Local: prove the revision is clean and published.
test -z "$(git status --porcelain)"
test "$(git rev-parse HEAD)" = "$(git rev-parse '@{upstream}')"

# Production: exact paths/revision come from ci-cd.md.
ssh {ssh_alias} 'cd {production_theme_path} && \
  test -z "$(git status --porcelain)" && \
  git switch {branch} && \
  git fetch origin {branch} && \
  git merge --ff-only {deploy_sha} && \
  test "$(git rev-parse HEAD)" = "{deploy_sha}"'
ssh {ssh_alias} 'cd {production_theme_path} && git rev-parse HEAD'
```

Hard stop if the production checkout is dirty or cannot fast-forward. Never
discard server changes to make the pull pass.

### B. Local pushes a theme-scoped release

Use when the host cannot pull GitHub. The project contract owns the exact
source, destination, `.deployignore`, and whether deletion is allowed.

```bash
# Review first. Never rsync a WordPress root or wp-content root.
rsync {flags} --dry-run --itemize-changes --exclude-from=.deployignore \
  {local_theme_path}/ {ssh_alias}:{production_theme_path}/

# Run only after the dry-run matches the intended theme-only change.
rsync {flags} --itemize-changes --exclude-from=.deployignore \
  {local_theme_path}/ {ssh_alias}:{production_theme_path}/
```

Do not assume `--delete` is safe. If stale-file deletion is required, the
project contract must explicitly allow it and the dry-run must show every
deletion before execution.

## Database strategy

`single-env`. Production is the only authoritative data environment. The
disposable Local WP database is test scaffolding and has no sync path.

- Read-only production queries: scoped remote WP-CLI against the verified site root
- Production writes: explicit task scope + verified backup + read-back verification
- Destructive production writes: human go-ahead + verified recoverable backup
- DB dumps: backup destination only; never git and never retained as the routine local workspace

## Backup strategy

Read the project deployment contract `backup` block and its provider reference.
`provider: none` blocks production DB writes and any deploy capable of deleting
or overwriting unrecoverable state.

## Permissions matrix

| Action | Autonomous | Human go-ahead | Prohibited in this pattern |
|---|---|---|---|
| Inspect/edit/build/test the local theme | ✅ | — | — |
| Start/stop Local WP; change disposable fixtures | ✅ | — | — |
| Commit + push the intended theme change | ✅ | — | — |
| Read-only production WP-CLI query | ✅ | — | — |
| Scoped production drift/checksum check | ✅ | — | — |
| Deploy theme code to production | — | ✅ | — |
| Non-destructive production content/option write | — | ✅ | — |
| Destructive production DB/plugin/theme operation | — | ✅ + backup | — |
| Edit production theme files directly | — | — | ✅ |
| Point Local WP at the production DB | — | — | ✅ |
| Routine download of production DB/uploads | — | — | ✅ |

## Required hooks

Before deploy:

1. GitHub remote/upstream verified; intended revision pushed
2. Production drift check clean or explicitly reconciled
3. Build/lint/tests successful
4. Human production go-ahead recorded
5. Current backup verified according to the provider strategy
6. Deploy dry-run reviewed when the method supports it

After deploy:

1. Production commit/checksum matches the pushed revision
2. Theme/application cache clear and WordPress cache flush as declared
3. Approved remote WP-CLI changes read back and verified
4. Production smoke test of the changed URLs
5. Rollback readiness retained until verification passes

## Rollback

- **Code only:** redeploy the previously known-good GitHub revision, clear caches, and smoke-test. Do not repair by editing production files.
- **Database change:** use the verified pre-change backup or the provider restore method. A git rollback does not roll back WordPress data.
- **Both:** restore data and deploy the corresponding known-good code revision as one coordinated recovery.

## Gotchas

- A fixture-only Local WP site cannot prove production content, plugin state, URLs, or media rendering. Treat it as partial verification.
- ACF JSON and code-owned schema belong in git; ACF field values and ordinary content remain in production DB.
- A server-side file editor, automatic updater, or another operator can create production drift. Detect it before every deploy and never overwrite it silently.
- A broad rsync path can delete uploads or plugins. Both endpoints must resolve to the exact theme folder before any write.
- Git protects source code, not the database or uploads. The backup strategy remains mandatory.

