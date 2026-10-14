# Deployment recipes — index

The vibecode/developer/manager skills read this catalog to know which deployment pattern a project uses. Seven patterns total. Each per-project `.claude/ci-cd.md` declares **exactly one** as `pattern:`.

Deployment patterns describe topology. A project may separately declare an
operating overlay such as `mode: mvp-mode`; modes live under `modes/`, never in
this recipe catalog. Load the mode and pattern together, with the mode unable to
relax the pattern's security or data-integrity rules.

## How to use

When the brief says "set up CI/CD for {project}" or "ship this":

1. Read this index to see the seven patterns
2. Open the specific `deployment/{slug}.md` for the project's declared pattern (from `.claude/ci-cd.md`)
3. Follow its rules — environments, workflow, DB strategy reference, backup strategy reference, permissions

If no pattern is declared (no `.claude/ci-cd.md` exists), **default to `local-github-prod`** (the safe single-env pattern) and proceed under its rules — offer to scaffold `ci-cd.md` so the choice is recorded. Don't hard-stop. The permissions matrix still binds: production deploys need human go-ahead.

## Index

| Pattern | File | One-line | When |
|---|---|---|---|
| `local-github-prod` | [deployment/local-github-prod.md](deployment/local-github-prod.md) | Representative local runtime + GitHub + prod-direct deploy, no staging | **Default pattern.** Small internal sites, secondary brands, static mirrors. |
| `direct-prod` | [deployment/direct-prod.md](deployment/direct-prod.md) | Local theme + optional disposable Local WP; live DB/uploads stay on prod | owner-managed fleets/directories where AI works from local code and WP-CLI runs remotely. |
| `local-github-staging-prod` | [deployment/local-github-staging-prod.md](deployment/local-github-staging-prod.md) | GitHub Actions pipeline — staging gates production | Client-facing serious dev. See bundled `standards/staging-pipeline.md`. |
| `prod-only-with-git` | [deployment/prod-only-with-git.md](deployment/prod-only-with-git.md) | One env, git for safety, edits direct on prod with backup-before | Worse than `local-github-prod`; only when local dev isn't viable. |
| `prod-only-no-git` | [deployment/prod-only-no-git.md](deployment/prod-only-no-git.md) | Last resort, throwaway, full reliance on host backups | Avoid. Requires explicit user approval. |
| `staging-only-no-git` | [deployment/staging-only-no-git.md](deployment/staging-only-no-git.md) | Staging is source of truth, promote = staging→prod sync | Rare. Elementor / no-code sites without a theme repo. |
| `elementor-child-with-git` | [deployment/elementor-child-with-git.md](deployment/elementor-child-with-git.md) | Elementor site + a child theme just for `.claude/` | Elementor sites where we still want the deploy contract tracked. |

## How to pick

**Start from the default — `local-github-prod` — and only move off it when an answer below points elsewhere.** Four questions:

1. **Staging?** Yes → `local-github-staging-prod`. No → keep narrowing.
2. **Real theme code (Sage / custom)?** No (Elementor) → keep narrowing. Yes → ask how representative local WordPress is.
3. **What does local contain?**
   - Representative WordPress/data fixtures suitable for pre-deploy checks → `local-github-prod`
   - Theme code + disposable/optional Local WP only; production keeps the real DB/uploads → `direct-prod`
4. **Is a local edit surface viable at all?**
   - Local theme work possible → `elementor-child-with-git` (Elementor), `local-github-prod` (representative local runtime), or `direct-prod` (theme-only runtime)
   - Local dev not viable → `prod-only-with-git` (acceptable) or `prod-only-no-git` (last resort, needs approval)
   - Site lives entirely on staging with no git → `staging-only-no-git` (rare)

When the project is client-facing or revenue-driving, prefer the more conservative pattern (with staging) and write it into `ci-cd.md`. Otherwise the default (`local-github-prod`) stands. Explicit downgrade below the default requires the user to say so.

## Adding a new pattern

1. Copy the closest existing pattern file as a template
2. Fill in: environments, workflow, DB strategy reference, backup strategy reference, permissions matrix, gotchas
3. Add a row to the index above
4. Update `templates/ci-cd.md` if the new pattern needs schema additions
