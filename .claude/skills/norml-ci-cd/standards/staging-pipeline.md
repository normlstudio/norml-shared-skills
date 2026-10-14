# Staging pipeline, release packaging and rollback

Use existing project automation when verified. A new serious-project baseline is short-lived
branches → PR validation → integration branch/staging → immutable production release.
GitHub Actions is an example provider; user-owned Git hosts/CI and managed-host pipelines
remain valid. The project contract declares actual branch, environments and commands.

## Three workflows

| Workflow | Trigger | Acceptance |
|---|---|---|
| PR validate | Pull request changes | Dependency install, syntax/lint/build/relevant tests, secret scan |
| Staging deploy | Accepted integration revision | Exact source/artifact deployment and smoke validation |
| Production deploy | Reviewed immutable tag/release | Protected authorization, backup, exact revision and rollback |

Separate environments, least-privilege credentials and provider-supported authentication.
Actions versions in examples must be checked against current official releases and preferably
pinned by audited commit. Untrusted fork PRs receive no deployment secrets. Use permissions
at job scope, artifact provenance/checksums, reviewed deploy inputs and concurrency controls
so simultaneous release jobs cannot swap a target out of order.

## Validation/build

1. Checkout exact source; install compatible PHP/Node with lockfile caching.
2. Install Composer development dependencies for Pint/PHPUnit and use `npm ci`.
3. Run actual configured checks; absent tests are reported, not falsely passing.
4. Build production assets and inspect manifest/entries.
5. Create a separate runtime artifact with production-only Composer dependencies.
6. Retain runtime Blade `resources/views` and any directly consumed resources. Never
   discard all `resources/` just because some source assets are build-only.
7. Include PHP/bootstrap, production vendor, built assets and required metadata. Exclude
   Git/node_modules/tests/secrets/dumps/uploads and local runtime cache/log state.

## Deployment

Read exact site/release/theme root, permission scope and recovery evidence from the contract.
Verify SSH host identity through a reviewed known-hosts record. Never disable host-key checking.
Transfer to a unique release directory, validate runtime/dependency/filesystem readiness,
then atomically activate its symlink where the host supports that mechanism. Do not assume
WordPress/theme paths are symlink-aware without testing. For a host-specific deploy use the
supported native interface and document equivalent immutable revision/rollback proof.

`rsync --delete` is allowed only against a fresh/bounded release with reviewed exclusions
and dry-run. Never sync an entire WordPress/content root. Standard rsync has one local/one
remote endpoint; remote-to-remote transfer needs execution on one host or an explicit relay.
Keep writable runtime storage persistent and deploy secrets outside the release artifact.

## Production gate

The user may already authorize the exact deployment. Otherwise obtain scope-specific approval
only after the candidate and target are concrete. A declared protected CI environment enforces
its required reviewers; selecting this package cannot override provider rules. Data-changing
operations need exact destructive scope authorization, recoverable backup and live-write plan.
Tag inputs must resolve to the reviewed source SHA. Never publish dirty/untracked WIP.

## Post-deploy

Verify runtime PHP version matches the build, required plugins/ACF/schema load, changed pages
render and interactions work. Run applicable cache hooks only; with Acorn use supported
`optimize:clear`/`view:clear` then `view:cache`, verified against installed commands.
Do not run an invented `wp acorn cache:clear` namespace. Flush rewrite rules only when routing
changes; do not do it on every request. Confirm production indexing, canonical URLs, protected
content and analytics/consent behavior when affected. Record exact deployed SHA/checksum.

## Rollback

Record a known-good previous revision and independent data/media recovery point. Keep an
appropriate project-defined release history. Code rollback swaps/redeploys immutable source;
it does not undo DB migrations, orders, content or uploads. A full DB restore can lose new
live writes and needs coordinated scope approval. Verify the rollback path before release.
On a materially broken live state execute the approved recovery, verify it, then repair
through another reviewed revision. Never hot-edit production to conceal source drift.

## Smoke checks without another skill

Use authorized HTTP/API/browser testing for changed pages and representative home/archive/
detail/contact routes. Check status, TLS, redirects, assets, console/page/network errors,
responsive dimensions, keyboard interactions and editor field save/read-back. Inspect actual
robots/sitemap routes for environment-appropriate indexing and plugin/schema integrity.
Do not submit real email/payment actions without specific test authorization and cleanup.
