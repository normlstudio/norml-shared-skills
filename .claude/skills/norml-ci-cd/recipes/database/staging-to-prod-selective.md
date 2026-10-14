# Database strategy: staging-to-prod-selective

Move only approved records/options while preserving production-owned content and user state.
This is a record migration, not a shortened full-database replacement.

## Define the migration

Declare exact source identifiers, target identifier mapping, eligible fields/options,
relationships, media, URL transformations, conflict policy, protected state and rollback.
Match by stable identity/slug plus post type when IDs differ across environments. Back up
production, review the manifest and prove the importer on an isolated copy before writing.

**Do not export/import `wp_posts` and `wp_postmeta` tables to migrate one CPT.** These tables
also hold pages, attachments, revisions and other post types. A full table dump overwrites
unrelated live records. Do not advertise `wp db export --where` as a portable WP-CLI option.

## Safe paths

### Targeted posts

WP-CLI WXR export can select exact approved post IDs. Confirm flags with the installed
`wp help export`, ensure the WordPress importer command is installed/authorized, and inspect
what meta, terms and attachments actually travel.

```bash
wp --path={staging-root} export --post__in={approved-source-ids} --dir={private-export-dir}
```

WXR import is not an idempotent update mechanism. Rehearse duplicate/slug behavior and a
stable source-to-target mapping before it reaches production. Updating existing records
usually requires a reviewed API/CLI migration with explicit field and relationship mapping.
Do not assume `--authors=skip` prevents duplicate posts.

### Options/settings

Read only the allowlisted option from staging, record the existing production value in
protected recovery storage, review the replacement and update that exact target option.
Use a serialization-aware JSON API/CLI route. Never carry `siteurl`, `home`, identities,
payment/webhook/email configuration, or unrelated options by convenience.

### Schema

Prefer versioned ACF local JSON/PHP definitions through code. On the target verify detected
schema and deliberately perform supported ACF UI sync when necessary. Neither
`wp acf sync --all` nor `wp acf import` is assumed to be bundled with ACF PRO; discover any
installed extension before invoking its namespace. Field definitions do not transport values.

### Taxonomies/media

Map terms by taxonomy + slug and preserve parent/relationship semantics. Copy only approved
attachments and rewrite approved URLs; ensure existing destination media remains intact.
Never sync commerce/user/form plugin tables as ordinary content.

## Acceptance and recovery

Read back changed records/fields/relationships. Check rendered URLs and editor values.
Verify protected orders, users, submissions, comments and production-only content survived.
Run appropriate cache/routing/smoke checks. A missing field or hidden slot is unresolved.
On failure, roll back the exact changed records using the reviewed recovery mapping;
full DB restore can discard concurrent live writes and needs separate coordination.

See [editor-owned strategy](content-via-wp-admin-only.md) if code deploys should carry no data,
and [full replacement](staging-to-prod-full.md) for deliberately destructive initial launch.
