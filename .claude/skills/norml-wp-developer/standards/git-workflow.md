# Git workflow

This is the Package standard for Git on serious WordPress dev projects. Apply on any project that has a real client, a real staging environment, and a real dev team — not on throwaway/vibe-coded sites (those use the project build workflow, which short-circuits most of this).

The aim: any engineer can pick up the repo, understand history, and ship without breaking production. Commits read well in `git log` six months later. Reviews catch real issues, not nits.

---

## Branch model

**GitHub Flow.** One long-lived branch (`main`), short-lived feature/fix branches off of it. No `develop`, no `release/*`, no GitFlow. Reasons:
- Small teams don't need GitFlow's overhead
- `main` is always deployable to staging
- Production deploys come from tagged commits on `main`, not a separate branch

**Long-lived branch:** `main`. Always green. Always deployable to staging.

**Short-lived branches** (always cut from `main`, always PR back to `main`):
- `feat/{short-description}` — new feature or section
- `fix/{short-description}` — bug fix
- `chore/{short-description}` — refactor, dep bump, build config
- `docs/{short-description}` — README or theme docs
- `style/{short-description}` — formatting, naming-only changes

Use kebab-case. Keep names short — 3–5 words max. Examples: `feat/case-study-block`, `fix/footer-mobile-spacing`, `chore/composer-update`.

**Delete branches after merge.** Use GitHub's auto-delete-on-merge setting.

---

## Commit conventions

**Conventional Commits**, using standard Git. Every commit gets:

- A subject line: `type(scope): summary` — present-tense, lowercase, no period
- A body explaining *why* (not what — the diff shows what)
- Trailers for cross-references (`Refs: #123`, `Closes: #456`)

Types: `feat`, `fix`, `chore`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`.

Scope is optional but encouraged for WP themes — use the theme area: `feat(blocks): add case-study block`, `fix(acf): correct field key for hero title`, `chore(vite): bump to 7.0.4`.

**Never commit:**
- Anything from `node_modules/`, `vendor/`, `public/build/`
- `wp-config.php` or any file containing secrets
- Personal paths or absolute paths to your local machine
- Database dumps, uploads, or anything from `wp-content/uploads/`
- `.DS_Store`, IDE config (use a global `.gitignore`)

**Always commit:**
- `acf-json/*.json` — ACF field group sync (this is source of truth, not the DB)
- `composer.json` + `composer.lock`
- `package.json` + `package-lock.json` (or `pnpm-lock.yaml` etc.)
- `vite.config.js` and any build config
- All `app/`, `resources/`, `config/` files

Use scoped staging and Conventional Commits; inspect the staged diff for unrelated work and secrets.

---

## Pull requests

Every change to `main` goes through a PR. No direct pushes to `main` on serious projects (configure branch protection: require PRs + 1 approval + green CI).

### PR title

Same format as the commit subject. If the PR has multiple logical commits, the title summarizes the whole.

### PR description

Use this template (the GitHub `.github/PULL_REQUEST_TEMPLATE.md` ships it):

```markdown
## What
<one paragraph — what this PR does>

## Why
<one paragraph — the user-facing reason, ticket reference, or context>

## How
<bullets — the implementation approach, only if non-obvious>

## Test plan
- [ ] Local: ran `npm run dev`, verified the change renders
- [ ] Staging: deployed, ran the smoke checks in this package, confirmed the change
- [ ] ACF: if new fields added, verified JSON synced and loaded
- [ ] Mobile: checked at 375px (sm) and 768px (md)
- [ ] No console errors / network errors in browser devtools

## Screenshots / video
<if UI work — before/after or new component shown>

## Risk
<what could break, what to roll back if it does>
```

Keep it tight. Two paragraphs + a checked checklist beats a wall of text.

### Review gates

A PR can merge when **all** of these are true:

1. **CI is green** — lint, build, tests, deploy-to-preview all passed
2. **At least one approval** from a teammate who didn't write the code
3. **No merge conflicts** with `main`
4. **No unaddressed reviewer comments** — every comment is either resolved, replied to, or dismissed with a reason
5. **Test plan boxes are checked** — at minimum local + staging + relevant device checks

Reviewers focus on:
- **Correctness** — does the code do what the description claims?
- **Package conventions** — file structure, naming, Blade components, ACF JSON, Tailwind utilities (read `norml-wp-developer/SKILL.md`)
- **Security** — escaped output, sanitized input, capability checks, nonces on POST
- **Performance** — queries in loops, missing transients, unbounded data fetches
- **Accessibility** — semantic HTML, alt text, keyboard nav for interactive components

Nits (formatting, naming preferences without functional impact) are caught by lint, not by reviewers. If lint missed something, fix lint — don't fight in PR comments.

---

## Merge strategy

**Squash and merge** by default for feature branches. One commit per logical change on `main`. Keeps `git log` readable.

**Merge commit** only when the PR genuinely has multiple distinct atomic commits worth preserving (rare — most feature branches don't need this).

**Rebase and merge** is forbidden — it rewrites history and breaks teammates who pulled the branch.

After merge, GitHub auto-deletes the branch and the cycle is done.

---

## Tagging and releases

Production deploys are driven by **annotated Git tags**, not by direct deploys to a `production` branch.

**Tag format:** `vMAJOR.MINOR.PATCH` (semver), e.g., `v1.4.2`.

**Tagging cadence:** tag on `main` whenever you're ready to promote staging → production. The CI/CD pipeline (`standards/ci-cd.md`) listens for tag pushes and runs the production deploy.

**Tag message:** one paragraph describing what changed since the last tag. This becomes the GitHub Release notes.

```bash
git tag -a v1.4.2 -m "Add case-study block + fix footer mobile spacing. Refs PR #87, #91."
git push origin v1.4.2
```

**Never** tag a commit that hasn't been on `main` and verified on staging. Treat released tags as immutable; create a corrected version instead of force-pushing.

---

## Hotfixes

A hotfix is a production-only fix that can't wait for a normal feature cycle. The workflow:

1. Branch from the **last tag** (not `main`) — `git checkout -b fix/{description} v1.4.2`
2. Make the minimal change. Resist scope creep.
3. PR to `main` — same gates apply (CI green, approval, no conflicts)
4. Merge to `main`
5. Tag a new patch release on `main` — `v1.4.3`
6. CI/CD pipeline deploys to production from the tag

With this branch model, dedicated `hotfix/*` branches and back-merging to a `develop` branch aren't needed — GitHub Flow + tagging handles hotfixes cleanly.

If the fix on `main` would carry unrelated work, **don't** tag straight from `main`. Cherry-pick the hotfix commits to a hotfix branch off the last tag, deploy that.

---

## Repository hygiene

- **`.gitignore`** must exclude `node_modules/`, `vendor/`, `public/build/`, `dist/`, `.env`, `.env.*`, `*.log`, `.DS_Store`, IDE folders.
- **Branch protection on `main`** — require PR, require approvals, require CI green, restrict force-push.
- **No long-lived dependency branches** — bump deps in a PR, merge, move on.
- **Squash old branches** — if a branch has been around for >2 weeks without a PR, close or finish.
- **No "WIP" commits on `main`** — squash them into the merge commit.

---

