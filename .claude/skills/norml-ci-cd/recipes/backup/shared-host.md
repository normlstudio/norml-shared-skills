# Backup provider: `shared-host`

> Shared hosting with panel-based daily snapshots. Covers panel-based shared hosts; verify the exact provider capabilities.

## What you get

- **Daily automatic snapshots** of files + DB
- **Retention:** typically 7-14 days (varies by plan)
- **Panel-based restore UI** (Beget panel, cPanel, Plesk, ISPmanager)
- **Manual snapshot triggers** usually available with limits (e.g., 1 manual per day)

## Project backup record

Record non-secret provider, verified schedule/retention, destination, completed snapshot ID,
last verification and restore-test evidence in the project contract. Authentication stays
in the OS/provider secret store. The contract never contains secret values.

## How to verify backup is current

For Beget-style hosts (no API):
- Log into the hosting panel
- Navigate to Backups / Снимки / Backup section
- Confirm a snapshot dated within the last 24 hours exists

For cPanel hosts:
- cPanel → JetBackup or built-in Backups → check latest backup timestamp

There's typically **no CLI or API** for this. Verification is manual via panel. The per-project `ci-cd.md` should note "verification requires logging into the hosting panel" so Claude can flag this and ask the user to confirm.

## How to trigger an on-demand backup

For Beget:
- Panel → Backups → "Create backup" / "Создать копию" button (if available — some plans limit manual triggers)

For cPanel + JetBackup:
- JetBackup → Manage → "Generate Backup"

If manual triggers aren't available, the daily auto-backup IS the only safety net — plan destructive changes for shortly after the daily backup window (typically early morning) so the freshest snapshot is recent.

## How to restore

1. Log into the hosting panel
2. Navigate to Backups
3. Pick the target snapshot (by timestamp)
4. Choose what to restore:
   - **Full site** (files + DB) — easiest, most common
   - **Files only** (preserves current DB)
   - **DB only** (preserves current files)
5. Click Restore
6. Wait for the host's process to complete (for the provider-reported interval)
7. Verify the site
8. Flush caches if not automatic

**Account-wide restore warning:** the panel restore overwrites the entire account state to that snapshot. There is no "preview" — once you click Restore, the change is committed. Take a manual snapshot RIGHT BEFORE the restore so you can undo the restore if needed.

## How to download a backup for off-site storage

For Beget:
- Panel → Backups → pick snapshot → Download (some plans only)
- Or SSH in and copy the backup directory to local

For cPanel:
- Files → Backup Wizard → Download Full / Partial backup

Useful before a known-risky change — download the latest backup as a local insurance policy.

## Cost / limitations

- **No API.** Most operations are panel-only. Claude can't auto-verify backups; must ask the user.
- **Retention is short** (7 days is common). Bugs that take longer than a week to surface have no easy restore path.
- **Restore is account-wide, not per-site** on some hosts. If one account hosts multiple sites, a restore affects all of them. Check the host's granularity.
- **Manual trigger limits.** You may not be able to take 5 backups in 5 hours.
- **Snapshots include `wp-content/uploads/`** — good for media restore, but means dumps can be large and slow to restore.

## Operational protocol

1. Before any destructive change, **ask the user to confirm a recent backup exists** (since Claude can't verify via API)
2. If the user can't confirm, ask them to take a manual snapshot via the panel before proceeding
3. Note the snapshot timestamp in the session record so a restore target is unambiguous

