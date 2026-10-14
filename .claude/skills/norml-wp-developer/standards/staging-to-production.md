# Code, content and environment ownership

Code/schema moves local → staging → production. Live content/field values are production-owned
and may move to isolated staging for testing. Never automatically replace an ongoing live
DB with staging just because the request says deploy.

## Inventory before moving state

List code-managed plugins/core/theme, ACF definitions versus values, content/media, payment,
mail, webhooks/queues and environment-only configuration. WordPress core is not inherently a
Sage theme dependency; inspect the actual installation/Bedrock/root Composer setup. Update
only the dependency the project actually owns. Plugin/core changes are tested on staging
first where staging exists, then production with its backup/rollback gate.

## Refresh production content into staging

1. Verify exact site/DB identities and scope; authorize sensitive-data access and destructive
   staging overwrite. Preserve pending staging editor work before it can be lost.
2. Back up staging and obtain a protected production snapshot outside web roots/Git.
3. Disable outbound email, live billing, webhooks and jobs **before** copied data can run.
   Use sandbox endpoints/test keys stored securely; enforce access/noindex for staging.
4. Use serialization-aware WP-CLI export rewrites, preserving GUIDs, for verified URLs:

```bash
wp --path={production-root} search-replace \
  'https://example.com' 'https://staging.example.com' \
  --skip-columns=guid --all-tables-with-prefix --export={private-staging-dump}
```

5. Transfer via a verified single-hop/relay route; import only at the verified staging root.
   Reset/drop is destructive and requires approved scope; inspect the import SQL semantics.
6. Reapply environment settings/test identities, indexing and side-effect restrictions.
7. Sync media incrementally without deleting staging-only files unless a separately reviewed
   deletion manifest is authorized. A shared production bucket must be read-only for staging.
8. Clear applicable caches, read back site URLs, verify frontend/editor/media and isolation.

Minimize personal data where possible. Private snapshots are transient recovery/testing
material; retention and access are project-defined. Do not schedule silent destructive refresh.
A staging restore follows the verified backup/activation route, then must pass isolation checks.

## ACF and schema

Version field definitions in local JSON/PHP; retain existing key conventions and detect
repo-versus-server drift before overwrite. Values remain production content. Deploying JSON
does not fill values or guarantee admin sync happened. Verify schema/Sync notices and editor
save/read-back using the installed supported mechanism. Do not assume `wp acf` extensions.
Durable content model registration lives independently of its visual theme when portability
requires it; record theme/ACF dependencies deliberately.

## Intentional staging-to-production data work

Initial launch can use a fully reviewed replacement with production-only state accounted for.
Ongoing work uses an exact record/field/relationship manifest, stable source-to-target mapping,
conflict policy, protected-data checks and rollback. Never replace shared `wp_posts` tables
for one CPT; WXR imports can duplicate records and need rehearsal/idempotency decisions.
Options never bring live payment/email/user/URL configuration by accident. Code deploys and
editorial content changes remain independently scoped and verified.

## Environment-specific state

Keep wp-config/runtime secrets, server rules, SSL, DNS/CDN/object-cache and provider endpoints
per environment; do not blanket-copy them through theme deployment. Shared security rules
can be versioned infrastructure only under their actual owner and explicit target policy.
Sage/Acorn existence is checked before any framework-specific cache command.

## Recovery

Stop writes/deploys, identify exact last revision/state operation, preserve recovery evidence,
restore known-good scoped state/code, verify integrity and isolation, then replay only the
approved change. Production DB restoration can discard concurrent orders/content and needs
coordination; a code Git rollback does not restore data.
