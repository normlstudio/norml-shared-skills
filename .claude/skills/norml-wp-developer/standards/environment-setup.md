# Environment setup

Discover existing environment before provisioning. Use the project's chosen supported
WordPress host/local shell and verified paths. New Sage setup requires compatible PHP,
WordPress, Composer, Node and licensed ACF only if the requested feature uses ACF.
Verify current official version compatibility, then choose a stable release or pinned
project version. Never install an unreviewed `dev-main` by default.

```bash
# Run from the verified WordPress themes directory for a newly authorized Sage project.
composer create-project roots/sage {theme-slug}
cd {theme-slug}
npm install
npm run build
```

Inspect and commit source manifests/lockfiles, set the actual project metadata, confirm the
Vite base/local URL/HTTPS configuration, and activate only on the authorized environment.
Reuse existing `wp-config.php`; secret values stay in runtime/provider/OS protected stores,
never prompts or committed project instructions. Theme working docs belong in the repository.

Use a disposable local DB/fixtures for theme-only work; never point local WordPress at a live
database. If a representative data copy is authorized, handle it privately, minimize personal
records, disable external side effects and verify the destination before importing.

Confirm frontend, editor and assets with actual rendered evidence. Document what local fixtures
cannot represent. Record a deployment/backup/rollback policy before any live operation;
[CI/CD](ci-cd.md) and [staging/production](staging-to-production.md) supply the bundled rules.
