# QA gates

What we check, and when, before code lands in production on a serious The project. Three checkpoints — none of them optional.

The aim: bugs and regressions get caught before clients see them. "It looked fine on my machine" is not a QA gate.

---

## Three checkpoints

| Gate | Runs when | Blocks what |
|---|---|---|
| **Pre-merge** | Before merging a PR into `main` | The PR landing |
| **Pre-deploy** | After staging is updated, before tagging a production release | The production tag |
| **Post-deploy** | Immediately after a production deploy lands | Calling the deploy "done" |

A change that doesn't pass all three doesn't ship.

---

## Pre-merge gate

Runs automatically on every PR via `.github/workflows/pr-validate.yml` (see `ci-cd.md`). Plus manual review by another teammate.

### Automated checks (CI must pass)

- **PHP lint** — `vendor/bin/pint --test` clean
- **JS/CSS lint** — `npm run lint` clean (ESLint + Stylelint if configured)
- **Build** — `npm run build` (Vite production build) succeeds without errors
- **Tests** — `vendor/bin/phpunit` if `tests/` exists; all green
- **Secrets scan** — no `wp-config.php`, `.env`, key files, or `password = "..."`-shaped strings added (use `gitleaks` or `trufflehog` in the workflow)

### Manual reviewer checks

The reviewer (a teammate other than the author) goes through the [pull request review gates in `git-workflow.md`](git-workflow.md#review-gates). For QA specifically:

- **Correctness** — does the PR description match the diff? Are the test-plan boxes plausibly true?
- **Package conventions** — file paths, naming, Blade components, ACF JSON, Tailwind utilities follow `norml-wp-developer` (`file-structure.md`, `component-system.md`, `acf-blocks.md`)
- **Security smell test** — escaped output (`esc_html`, `esc_attr`, `wp_kses`), sanitized input, capability checks, nonces on POST endpoints, no concatenated SQL
- **Performance smell test** — no queries in loops, transients for expensive lookups, bounded `WP_Query` results, no synchronous calls to external APIs in render path
- **Accessibility smell test** — semantic HTML, `alt` on images, keyboard nav on interactive components, focus styles preserved

If the reviewer can't verify a claim from the diff alone, they ask for a screenshot or a staging URL — don't approve on faith.

---

## Pre-deploy gate

Runs after `main` deploys to staging (auto, via `deploy-staging.yml`) and before tagging a production release.

This is the **manual QA pass** on the staging environment. It is the most important gate. Skipping it is how production breaks.

### Required checks on staging

1. **Smoke checks** — run the checks described in `ci-cd.md` against staging. Verifies HTTP codes, SSL, redirects, wp-admin reachable, REST API responsive, no broken internal links on top 20 pages. Must pass.

2. **Visual sweep** — open each new/modified page and section in a browser. Check at three viewports: 375px (mobile), 768px (tablet), 1280px+ (desktop). Look for:
   - Layout shifts (CLS)
   - Missing images
   - Broken icons or fonts
   - Text overflowing containers
   - Stacking-order bugs (z-index)
   - Dark text on dark backgrounds (the classic vibe-coded regression)

3. **Interaction smoke** — for every new interactive element (button, accordion, modal, slider, filter), actually click/tap/submit and verify behavior. Watch the browser console for errors during the interaction.

4. **ACF field check** — if new ACF fields were added:
   - Open the relevant post type in wp-admin and verify fields render in the editor
   - Fill them in, save, reload the front end, verify values appear
   - Verify JSON synced correctly from `acf-json/` (check the `Sync available` notice in wp-admin's Custom Fields page is empty)

5. **Performance pass** — if the PR touches a heavy page (landing, blog index, search), run the bundled performance checks (or optional `norml-performance-audit`) and confirm Core Web Vitals didn't regress. Tolerable bands:
   - **LCP** ≤ 2.5s (good)
   - **CLS** < 0.1
   - **INP** ≤ 200ms
   - Score degradation > 10 points vs main = investigate before tagging

6. **Client review** — for content/design changes that are user-visible, prepare the staging review evidence and require the project-approved sign-off before release; do not send messages without authorization.

### Optional checks (project-dependent)

- **Cross-browser** — Safari, Firefox, Chrome at least. WebKit-specific bugs are real.
- **WP admin smoke** — log into wp-admin on staging, open the Pages/Posts list, edit one. If the editor doesn't load, ship-blocker.
- **Email** — if any form was changed, submit a test entry and confirm the email arrived (use a real address, not `test@test.com`).

### When to fail the gate

Failing the pre-deploy gate is **not** a personal failing — it's the gate doing its job. Tag a new PR with the fix and re-run staging. Don't skip.

---

## Post-deploy gate

Runs in the minutes after a production deploy. Confirms the deploy actually worked.

### Required checks on production

1. **Smoke checks** against the production URL. Same as staging but the URL is real.

2. **Visit the top 5 pages** by traffic (home + 4 — for most projects that's home, primary service page, blog index, contact, plus one). Confirm they render correctly.

3. **DB integrity check** — log into wp-admin, open the most-edited post type, confirm the list loads and a sample post opens for editing. (Catches `acf_get_field_groups()` errors and ACF JSON sync issues.)

4. **Search index** — if the site has a search feature, run a search for a known term and confirm hits. Catches index-corruption or DB-prefix mismatches.

5. **Sitemap and robots** — `curl /sitemap.xml` returns valid XML, `/robots.txt` matches the env (production should NOT have `Disallow: /`).

6. **Analytics + tag manager** — load a page and confirm GA4 / GTM / Plausible / whatever fires. Use the browser devtools Network tab.

### Failed live verification

Rollback a materially broken live state using the verified recovery path. A forward fix
requires a proven bounded change, new exact source revision and renewed verification.

## Hotfix QA

Hotfixes bypass the normal cycle but **not** the gates. A hotfix still:

- Passes pre-merge (CI + reviewer)
- Passes pre-deploy on staging (yes, even a hotfix — verify it on staging first)
- Passes post-deploy on production

The temptation to "just push it, it's one line" is how production gets worse, not better. Five extra minutes of staging verification beats a 3am rollback.

---

## Common bugs the gates catch

These are the recurring categories Projects have hit. Train yourself to scan for them during QA.

- **Wrong env in `wp-config.php`** — staging deploys with `WP_ENV=production` accidentally. Catch via the environment/indexing check (it'll find indexing on robots.txt).
- **ACF JSON not synced** — fields exist in code but `Sync available` notice in wp-admin shows pending. Author forgot to re-sync.
- **Image URLs hardcoded to staging** — Gutenberg blocks pasted with full URLs from staging. Run search-replace or the smoke checks in this package broken-link scan.
- **Form mailer using old domain** — moved from a staging contact form to production but the from-address is still `noreply@staging.example.com`. Test the form on production.
- **Plugin update missed on production** — Composer-managed plugins deployed but a manually-installed plugin is out of date. Catch via wp-admin's update notices.
- **Caching layer not flushed** — old assets served because Cloudflare/Litespeed/WPRocket cached aggressively. Always purge the edge cache after a production deploy.

---

