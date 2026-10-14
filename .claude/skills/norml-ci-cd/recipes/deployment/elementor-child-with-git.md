# Pattern: `elementor-child-with-git`

> Elementor (or other page-builder) site, BUT a child theme exists purely as a git home for `.claude/` and any minor code additions (functions.php tweaks, custom CSS, hooks).

## When to use

- Page-builder is the primary build tool (Elementor / Divi / Bricks)
- We still want `.claude/` (deploy contract, project notes, project-specific skills) tracked in git
- We want a place to drop small PHP / CSS additions when the builder isn't enough
- The team wants a clean handoff path if the project ever grows into "real" theme work

## When NOT to use

- Full custom theme (Sage / hand-built) → `local-github-*` patterns
- No `.claude/` tracking needed and site is truly editor-managed → `staging-only-no-git` (rarer, less ideal)
- Real theme code work is happening — move to `local-github-prod` and stop pretending it's Elementor-only

## Environments

| Env | Where | Source of truth | Who deploys |
|---|---|---|---|
| **Local (optional)** | Teammate's clone of the child theme | `.claude/` + any PHP/CSS additions | n/a |
| **Staging (optional)** | `staging.{domain}` if host supports | Files + DB | Teammate or CI |
| **Production** | The live site | Files + DB | Teammate via host deploy or rsync |

Often the local + staging + production setup mirrors `local-github-prod` or `local-github-staging-prod` for the **child theme**, even though most actual site changes happen in Elementor on staging or prod via WP admin.

## Workflow

### Two parallel tracks

**Track 1 — Elementor / content (editor-driven):**
- Edits happen in Elementor on staging (or directly on prod if no staging)
- Promotes via `staging-to-prod-*` DB strategy when staging exists
- See `staging-only-no-git.md` for the editor-side workflow

**Track 2 — Child theme code (dev-driven):**
- Child theme cloned locally
- Edit `functions.php`, custom CSS files, hooks
- Commit + push to the configured Git repository
- Deploy to staging / prod per whichever git-pattern the child theme uses
- This track is where `.claude/ci-cd.md` lives and gets read

## Initial setup

1. **Create the child theme:**
   ```php
   // style.css
   /*
    Theme Name: {Project} Child
    Template: hello-elementor
    Version: 1.0.0
   */
   ```
   ```php
   // functions.php
   <?php
   add_action('wp_enqueue_scripts', function () {
     wp_enqueue_style('parent-style', get_template_directory_uri() . '/style.css');
   });
   ```
2. **Init the the configured Git repository repo** in the child theme folder
3. **Scaffold `.claude/`** via read-only project discovery (it'll detect the child theme via `Template:` header)
4. **Write `ci-cd.md`** — declare `pattern: elementor-child-with-git`
5. **Activate the child theme** on staging + production
6. **Document the Elementor side** in `ci-cd.md` notes — which builder, what plugins, where templates live

## Database strategy

Driven by the Elementor / content side. Usually `staging-to-prod-full` for initial launches, `staging-to-prod-selective` after that.

## Backup strategy

Same as any pattern — read deployment contract. Must be real.

## Permissions matrix

Hybrid of the relevant patterns:

| Action | Claude can do autonomously | Requires human go-ahead |
|---|---|---|
| Edit child theme code locally | ✅ | — |
| Commit + push to GitHub | ✅ | — |
| Deploy child theme to staging | ✅ | — |
| Deploy child theme to prod | — | ✅ |
| Edit Elementor templates on staging via WP admin | ✅ | — |
| Edit Elementor templates on prod via WP admin | — | ✅ |
| DB sync staging → prod | — | ✅ |
| Plugin install/activate on any env | — | ✅ |

## Pre-deploy hooks

For code-side: standard git + build + lint. For Elementor-side: backup-before per `staging-only-no-git`.

## Post-deploy hooks

Code-side: cache flush, `wp acorn view:cache` if Acorn applies, smoke test. Elementor-side: regenerate Elementor CSS (Elementor → Tools → Regenerate CSS).

## Gotchas

- **The child theme is mostly empty.** That's the point. It exists so we have a git home — most content lives in Elementor (DB).
- **Plugin updates can break Elementor templates** in non-obvious ways. Always test plugin updates on staging first if staging exists.
- **`functions.php` is the temptation to grow.** Resist. If real theme code starts piling up, migrate to `local-github-prod` and stop pretending this is "just Elementor."
- **Elementor caches generated CSS per page.** Promote a layout change → regenerate CSS on the target env, otherwise the change won't render.
- **Don't confuse this with `staging-only-no-git`.** The difference is the child theme + git. If the child theme exists, this pattern applies. If not, `staging-only-no-git`.

## What this pattern is NOT

- Not a substitute for real theme code. If you find yourself writing 200 lines of `functions.php`, migrate.
- Not git-tracking Elementor templates. Elementor templates live in the DB; git only tracks the child theme + `.claude/`.

