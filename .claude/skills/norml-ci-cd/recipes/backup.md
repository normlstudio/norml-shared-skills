# Backup strategy catalog

Read the project's non-secret deployment contract for provider, current completed backup,
scope, freshness, retention and tested restore route. Authentication uses the OS protected
store or provider-managed credentials. Missing/unverified recovery blocks destructive work.

| Strategy | Procedure | Use |
|---|---|---|
| `managed-host` | [Managed host](backup/managed-host.md) | Provider owns snapshot/restore service |
| `shared-host` | [Shared host](backup/shared-host.md) | Panel-based files/database recovery |
| `vps-no-builtin` | [VPS](backup/vps-no-builtin.md) | Owner builds monitored off-site backups |
| `cloud-aws-custom` | [Cloud](backup/cloud-aws-custom.md) | Multiple cloud storage/database components |

Verify provider interfaces and actual entitlements before operations. Prefer API/CLI where
supported. Panel-only work needs user-authorized UI operation or narrow human verification;
a disconnected API does not authorize browser takeover. Do not promise restore timings.
