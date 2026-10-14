# Database strategy: `single-env`

> One authoritative data environment (production). No sync. All real DB changes are direct on prod with backup-before.

## When this applies

- Patterns: `local-github-prod`, `direct-prod`, `prod-only-with-git`, `prod-only-no-git`
- Any project where staging doesn't exist (or staging is purely a code preview, not a DB mirror)
- A thin Local WP shell may have a disposable fixture DB, but it is never synced and never treated as project data

## The core rule

**Backup before every destructive DB operation.** No exceptions. "Destructive" means anything that writes, updates, deletes, or restructures — not just `DROP`. Plugin uninstall with "delete data" is destructive. `wp search-replace` is destructive. `wp option update` is destructive (for the row being updated).

## Tools

| Action | Command |
|---|---|
| Full DB dump | `wp db export {project-slug}-{YYYY-MM-DD-HHmm}.sql` |
| Single-table dump | `wp db export --tables={prefix}_{table} {table}-{date}.sql` |
| Verify dump non-empty | Check success, size/checksum and SQL structure privately; prove an isolated restore. Do not print private rows. |
| Search-replace (URL changes, value changes) | `wp search-replace 'old' 'new' --skip-columns=guid --all-tables-with-prefix` |
| Cache flush after content change | `wp cache flush && wp transient delete --all` |
| Restore from dump | `wp db import {dump-file}` |

**Never** use `sed` or `awk` on a `.sql` dump containing WordPress data. Serialized PHP in `wp_options` and post meta will break and the data will corrupt silently. `wp search-replace` understands serialization; `sed` doesn't.

## Process for any DB write

1. **Take backup:** `wp db export pre-{change-name}-{date}.sql`
2. **Verify backup:** successful exit and valid SQL/private checksum; isolated restore evidence
3. **Execute the change** (via `wp` command, REST API, or WP admin)
4. **Verify the change** (read back the affected row / option / post)
5. **If something looks wrong:** `wp db import pre-{change-name}-{date}.sql`
6. **Keep the backup file** until you're confident the change is stable (according to the project recovery/retention policy)
7. Then archive or delete the dump

## What goes in git

**Nothing DB-related.** No `.sql` dumps in git, ever. They contain user data, get huge fast, and merge conflicts on dumps are catastrophic.

ACF JSON files (`acf-json/*.json`) ARE source — they're schema, not data — and DO go in git. They define schema; verify supported ACF loading/sync behavior on the target explicitly.

## Gotchas

- **`guid` should never be search-replaced.** Always `--skip-columns=guid`. WordPress treats `guid` as a permanent identifier; rewriting it breaks RSS readers and other consumers.
- **Plugin-specific tables** sometimes use their own serialization. Common offenders: WooCommerce, BuddyPress, BookingCalendar. Test search-replace results carefully.
- **Multisite has `wp_blogs` + per-blog tables.** `wp search-replace --all-tables-with-prefix` handles them; verify the exact network/table scope against installed WP-CLI help before execution.
- **Large sites:** a full export of 1GB+ DBs takes minutes. Schedule destructive changes during low-traffic windows.
- **Foreign-character escaping:** non-UTF-8 dumps can corrupt. Always run with `--default-character-set=utf8mb4`.

## When to refuse the operation

If the backup step fails or the dump is suspiciously small, **refuse the change**. A change without a verified backup is not a change you can recover from. Tell the user; let them investigate the backup issue first.

