# Backup provider: `managed-host`

> Hosts with built-in WordPress backup systems: WP Engine, Kinsta, SiteGround Cloud, Cloudways, Flywheel, Pantheon, Pressable.

## Provider capabilities are project-specific

Managed hosts may expose daily/on-demand snapshots and partial or full restores.
Verify current plan retention, environment scope, restore granularity and exact supported
API/CLI before use. Do not treat illustrative routes below as a tested integration.

## Project backup record

Record non-secret provider, verified schedule/retention, destination, completed snapshot ID,
last verification and restore-test evidence in the project contract. Authentication stays
in the OS/provider secret store. The contract never contains secret values.

## How to verify backup is current

Each host has its own check. Common pattern via API or panel:

- **WP Engine:** User Portal → site → Backup Points → check timestamp of latest "Daily" entry
- **Kinsta:** MyKinsta API → `/sites/{site_id}/backups` → check `created_at`
- **SiteGround:** Site Tools → Security → Backups → check Date column
- **Cloudways:** API → `/api/v1/server/{server_id}/backup` → check `last_backup_timestamp`

Document the per-project verification command in the per-project `ci-cd.md` if the host supports CLI / API.

## How to trigger an on-demand backup

When a planned destructive change is imminent, trigger a fresh backup first:

| Host | How |
|---|---|
| WP Engine | Portal → site → "Back up now" button OR `wpe-update` CLI |
| SiteGround | Site Tools → Security → Backups → "Create Backup" |
| Cloudways | Server panel → "Take Backup Now" |

Wait for completion before proceeding. Don't deploy on top of an in-progress backup — restore points can be inconsistent.

## How to restore

Each host has UI-based restore. Document the exact path in per-project `ci-cd.md`. General flow:

1. Identify the target backup (by timestamp, ideally one minute before the breaking change)
2. Click "Restore" in the host's panel
3. Most hosts do atomic restore (files + DB together) — watch for partial-restore options if you only need DB
4. Wait for completion (for the provider-reported interval)
5. Verify the restore landed (timestamp on the site, recent content visible)
6. Cache flush if not automatic

## Cost / limitations

- **Restore takes minutes, not seconds.** Plan accordingly — don't promise zero-downtime if a restore might be needed.
- **Retention is finite.** Verify the actual plan and project's recovery window.
- **Inter-environment restores** (restore prod from a staging backup point) are usually possible but require explicit confirmation in the panel — easy to misclick.
- **Backups aren't always tested.** Schedule a quarterly restore-to-staging test to verify the backup system actually works.

