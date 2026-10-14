# Backup provider: `cloud-aws-custom`


## When this applies

- WordPress runs on EC2 / GCE / Azure VM with attached storage
- Or on a managed-K8s cluster
- Or on a Lightsail / equivalent without `lightsail-snapshot` configured
- Compliance / regulatory needs may add requirements (HIPAA, GDPR, SOC2) — restore must be auditable

## The hard truth

This is the most expensive and most failure-prone backup pattern. Custom backup systems break silently more often than they work. **If at all possible, use a managed WP host** (`managed-host`) or a VPS with built-in snapshots (`vps-no-builtin` + provider add-on).

When you're stuck with this pattern (often because the client mandated AWS / GCP / Azure for compliance), proceed with maximum rigor.

## What needs to be designed

### 1. Backup orchestration

- **EBS snapshots** (AWS) or **Persistent Disk snapshots** (GCP) for full-disk capture
- **Database backup:** if RDS / Cloud SQL, use the managed snapshot system; if MySQL on EC2, `mysqldump` + S3 upload
- **Uploads:** if on S3 already (recommended), use S3 versioning; if on EBS, snapshot is sufficient
- **Configuration:** if Ansible / Terraform managed, the IaC IS the config backup; if not, capture `/etc/nginx`, `/etc/php`, etc.

### 2. Storage

- **S3 / GCS / Azure Blob** in a different region than primary
- **Lifecycle policies** for retention (e.g., 30 days standard, then Glacier for monthly archives)
- **Encryption at rest** (S3 default or customer-managed key per compliance)

### 3. Cron / scheduling

- **AWS:** EventBridge → Lambda → backup operation
- **GCP:** Cloud Scheduler → Cloud Function → backup
- **Azure:** Azure Automation runbook → backup
- **OR a cron job on the WP VM** — simpler but less auditable

### 4. Monitoring

- CloudWatch / Stackdriver alarm if a backup misses its window
- Daily summary email or Slack notification
- Failure paging via OpsGenie / PagerDuty

### 5. Documented restore

- A runbook for the on-call engineer: every command, every confirmation prompt, every "verify this before proceeding"
- Test restores quarterly
- Record the test result in the project's `ci-cd.md`

## Project backup record

Record non-secret provider, verified schedule/retention, destination, completed snapshot ID,
last verification and restore-test evidence in the project contract. Authentication stays
in the OS/provider secret store. The contract never contains secret values.

## Per-project `ci-cd.md` requirements

For projects with this backup provider, the per-project `ci-cd.md` MUST include:

1. **Backup architecture diagram** (ASCII or linked Lucidchart) — show every component
2. **Backup verification command** — how to check the latest snapshot is fresh and uncorrupted
3. **Restore runbook** — full step-by-step, written for a person on-call who hasn't done it before
4. **Who to escalate to** — DBA, infra lead, on-call rotation
5. **Compliance notes** — what data retention rules apply, when can backups be deleted

This is the LONGEST `ci-cd.md` of any pattern. That's appropriate — the operational complexity demands it.

## How to verify backup is current

Project-specific. Examples:

**AWS RDS:**
```bash
aws rds describe-db-snapshots \
  --db-instance-identifier {instance} \
  --query 'reverse(sort_by(DBSnapshots,&SnapshotCreateTime))[0]' \
  | jq '{id: .DBSnapshotIdentifier, time: .SnapshotCreateTime, status: .Status}'
```
Confirm `time` is recent and `status` is `available`.

**EBS:**
```bash
aws ec2 describe-snapshots \
  --filters Name=tag:Project,Values={project-slug} \
  --query 'reverse(sort_by(Snapshots,&StartTime))[0]' \
  | jq '{id: .SnapshotId, time: .StartTime, state: .State}'
```

**GCP Persistent Disk:**
```bash
gcloud compute snapshots list --filter="labels.project={project-slug}" --sort-by=~creationTimestamp --limit=1
```

## How to trigger on-demand backup

Document the project-specific command. For RDS:
```bash
aws rds create-db-snapshot --db-instance-identifier {instance} --db-snapshot-identifier manual-pre-deploy-$(date +%Y%m%d-%H%M)
```
Wait for `status: available` before proceeding.

## How to restore

**This is project-specific and lives in the per-project `ci-cd.md` restore runbook.** Generic shape:

1. Verify the target snapshot is healthy (`describe-snapshots` / `describe-db-snapshots`)
2. Coordinate with infra / DBA — restore requires console access and may have compliance review
3. **DB restore:**
   - RDS: restore snapshot to a new instance, point WP at the new instance, decommission old
   - MySQL-on-EC2: `mysql < dump.sql` after stopping WP
4. **File restore:**
   - EBS snapshot: create volume from snapshot, mount, rsync to target
   - S3 versioning: restore to specific version
5. Smoke test
6. Document the incident: what triggered the restore, what was restored, lessons

## Cost / limitations

- **The most expensive backup pattern operationally.** Engineering time + storage + tooling.
- **The most failure-prone.** Custom backup logic breaks silently. Monitoring is critical.
- **The most documentation-heavy.** Every step needs to be explicit because restoring under pressure is when mistakes happen.
- **Compliance overhead is real.** GDPR right-to-erasure, retention max-age, audit logs.

## When to refuse operations

- If `last_verified` is older than 24 hours → refuse, ask the user to verify
- If `last_restore_test` is older than 90 days → flag loudly; consider refusing
- If backup architecture is undocumented in per-project `ci-cd.md` → refuse all destructive ops until documented

