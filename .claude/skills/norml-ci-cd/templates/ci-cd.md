# Deployment contract — {project}

## Identity and topology

- Pattern: {selected catalog slug or custom with rationale}
- Mode: {standard or deliberately chosen mvp-mode}
- Canonical repository / branch: {user-owned repository and actual integration branch}
- Source revision: {commit SHA or release}
- Contract owner: {verified responsible person}
- Approved scope: {exact authorization; none if absent}

## Environments

| Environment | URL | Exact WordPress root | Exact theme root | Authentication reference |
|---|---|---|---|---|
| Production | {verified URL} | {verified root} | {verified theme root} | {OS/provider reference only} |
| Staging | {verified URL or none} | {verified root or none} | {verified root or none} | {reference or none} |
| Local | {URL or none} | {fixture root or none} | {repo root} | {reference or none} |

- Local mode: {representative-local / disposable-local / theme-only / none}
- Local DB/media: {fixtures / representative authorized copy / none}
- Remote WP-CLI prefix: {verified SSH alias + exact site path + correct PHP/WP binary}
- Runtime requirements and confirmed CLI/FPM parity: {actual versions}
- No secret values in this contract. No local connection to the live DB in a thin workspace.

## Database

- Strategy: {single-env / staging-to-prod-full / staging-to-prod-selective / content-via-wp-admin-only}
- Eligible records/options: {exact identifiers and source-to-target mapping; none by default}
- Protected data: {users, orders, submissions, comments, editor work and other live state}
- URL rewrites: {exact source/target and serialization-aware dry-run}
- Staging side effects disabled: {email, payments, webhooks, scheduled jobs}

## Backup and recovery

- Provider: {managed-host / shared-host / vps-no-builtin / cloud-aws-custom / none}
- Scope, timestamp and completed backup ID: {evidence}
- Frequency / retention / freshness requirement: {verified project values}
- Storage and credential reference: {non-secret destination/reference}
- Restore test and owner: {actual last test, result and verified person}
- Data restore command/process: {tested exact procedure; blocker if absent}
- Code rollback unit/command: {known-good revision and exact restore command}
- Backup verification command: {provider-supported read-only command or verified manual route}

## Permissions

| Action | Existing authorization | Conditions |
|---|---|---|
| Read/build/test local source | {scope} | Preserve unrelated WIP |
| Read production narrowly | {scope} | Exact verified site root |
| Write staging | {scope or required} | Appropriate backup and no external side effects |
| Merge/release | {scope or required} | Approved review and passing checks |
| Deploy production code | {scope or required} | Exact pushed revision and recovery |
| Write production data | {scope or required} | Backup and read-back verification |
| Destructive data/state change | {scope or required} | Explicit exact operation authorization and recovery |

## Commands and hooks

### Build / checks

{Exact commands supported by existing lockfiles and tool versions}

### Staging deployment

{Exact approved command and endpoints, or none}

### Production deployment

{Exact approved immutable artifact command, or blocker}

### Dry-run and exclusions

{Theme/release allowlist; no DB, media, secrets or runtime storage overwrites; review deletions}

### Post-deploy verification

1. Confirm revision/artifact checksums match the pushed source.
2. Run declared application/WordPress/cache hooks only where applicable.
3. Verify changed URLs, editor rendering and interactions; record actual evidence.
4. Confirm content and protected records survived; verify indexing and analytics if affected.
5. If failed, execute the recorded recovery process; verify recovery too.

## Known constraints and policy changes

{Dated decisions, migration history, intentional MVP debt, current blockers}
