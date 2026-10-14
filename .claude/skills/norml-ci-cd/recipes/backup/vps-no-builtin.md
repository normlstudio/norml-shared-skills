# Backup provider: `vps-no-builtin`

> VPS hosts with no built-in backup: Vultr, DigitalOcean, Hetzner, Linode, OVH. You write the backup script. You own the restore.

## What you DON'T get (the default state)

VPS providers offer the server. They do NOT offer:
- Automatic WordPress backups
- Restore UI
- Snapshot diff / point-in-time recovery (without paid add-ons)

Providers may offer paid disk snapshots. Verify the current plan and restore scope;
disk snapshots do not replace a tested, application-consistent database/media backup.

## What you need to build

A working backup for a `vps-no-builtin` project requires:

1. **A nightly cron job** that:
   - `wp db export` to a `.sql` file
   - `tar` `wp-content/uploads/` (and any other writable dirs)
   - Optionally rsync the theme + plugins (or trust git for those)
2. **Off-site storage** for the backup files:
   - S3 / Backblaze B2 / Wasabi / Cloudflare R2
   - NOT another folder on the same VPS (a VPS failure takes both down)
3. **A retention policy** — typically 7-30 days of dailies, plus monthly archives
4. **A documented restore process** — exactly what commands to run from a fresh VPS to restore
5. **A periodic restore test** — quarterly, to verify the backup actually works

## Project backup record

Record non-secret provider, verified schedule/retention, destination, completed snapshot ID,
last verification and restore-test evidence in the project contract. Authentication stays
in the OS/provider secret store. The contract never contains secret values.

## Backup implementation contract

Implement the job with the provider CLI version already verified for the project:

1. Create a private temporary directory with `umask 077` and a cleanup trap.
2. Export the DB with WP-CLI into it; do not print rows or credentials.
3. Archive uploads/configuration that source control cannot reproduce.
4. Upload to an off-site encrypted destination with least-privilege provider auth.
5. Verify objects, checksums and completion before deleting temporary originals.
6. Use bucket lifecycle rules for retention; never parse a listing into bulk deletion
   commands without a reviewed manifest and dry-run.
7. Emit only sanitized completion metadata and alert when the job fails or goes stale.
8. Test full recovery into an isolated destination and record the evidence.

The project owns exact commands, scheduler, storage region and retention. No paid storage
or provider setup is performed implicitly by selecting this recipe.

## How to verify backup is current

1. SSH to the VPS
2. `tail -50 /var/log/backup-{project-slug}.log` — check last line is "complete" or similar
3. List the B2 bucket: `{verified-provider-cli} {read-only-object-list-command} | tail -5`
4. Confirm latest entry is within the last 24 hours

Can be automated via a cron job that fires an alert if the backup is older than 26 hours.

## How to trigger an on-demand backup

Just run the script manually:
```bash
ssh {vps} '{verified-backup-script-path}'
```

Wait for completion before proceeding.

## How to restore

Document the exact sequence in per-project `ci-cd.md`. Generic shape:

1. Spin up a fresh VPS (or wipe the current one)
2. Install LEMP stack + WP-CLI
3. Pull latest theme code from GitHub
4. Download the target backup from B2:
   ```bash
   {verified-provider-cli} {download-approved-backup-to-private-restore-directory}
   ```
5. Import DB:
   ```bash
   wp db reset --yes
   wp db import /tmp/restore/{project-slug}-db-{date}.sql
   ```
6. Extract uploads:
   ```bash
   tar xzf /tmp/restore/{project-slug}-uploads-{date}.tar.gz -C /var/www/{project-slug}/wp-content/
   ```
7. Fix permissions, flush caches, smoke test

## Cost / limitations

- **You own the script.** If it breaks, no one is going to notice except you.
- **You own the bucket.** Pay for storage; rotate credentials; monitor for unexpected egress.
- **No granular restore.** Single-file recovery is possible by extracting from the `.tar.gz`, but tedious.
- **Restore time is longer** than managed hosts because you're recreating the environment, not clicking a button.
- **Quarterly restore tests are mandatory.** A backup that hasn't been tested is theatre.

## When to refuse operations

If `last_verified` is older than 7 days, or `last_restore_test` is older than 90 days → flag this to the user before any destructive operation. The backup may not work when you need it.

