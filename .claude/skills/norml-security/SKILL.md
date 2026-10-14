---
name: norml-security
version: 1.0.0
description: >
  Keep automation secrets out of model-visible text, arguments, files and logs.
  Store credentials in protected OS stores or supported provider-managed auth,
  use them through reviewed local consumers, handle exposure/rotation, and scan
  explicitly selected local files with safe reporting and opt-in redaction.
  Use for API key, token, credentials, Keychain, Credential Manager, SSH key,
  MCP credentials, secret exposure, leak check, or browser password migration.
metadata:
  author: Norml Studio
---

# Norml Security

Operational secret handling for individuals, teams and assistants. The central rule is that
secret values bypass the language model. This edition has no company credential namespace,
team wiki password exception, cloud-drive dependency or mandatory account schema.

## First-run inputs

Resolve the exact provider identity, intended resource/action, existing protected authentication,
operating system and authorized credential reference. User/project choices take precedence.
Prefer existing provider-managed OAuth/keyless access when it fits. Use a supported secure store;
macOS Keychain and Windows Credential Manager procedures are bundled. Linux/cloud runners use
an explicitly selected supported secret backend; this package supplies no Linux storage helper.

`{skill-root}` is this installed folder. `{service}` and `{account}` are the user's non-secret
entry identifiers; they are not proof of provider identity. A local reference-only settings file
may describe endpoint/store reference/account and verification status using the user's own schema.
Keep private metadata outside shared/synced source. No secret values, credential-bearing URLs or
copied auth caches belong in those references.

## Choose the workflow

| Situation | Read next |
|---|---|
| New API token/password | [Secure entry and use](recipes/secure-entry-and-use.md) |
| SSH key or MCP transport | [SSH and MCP](recipes/ssh-and-mcp.md) |
| Secret pasted/exposed | [Exposure response](recipes/exposure-response.md) immediately |
| Local leak scan/redaction | [Local sweep](recipes/local-sweep.md) |
| Human browser login/autofill | [Browser passwords](recipes/browser-autofill.md) |

## Required boundaries

- Never request, repeat, print, screenshot or write a secret in chat, tool arguments, project files,
  committed files, tickets or messages. A fake credential-looking example is unnecessary; use
  unmistakable placeholders or synthetic construction in isolated tests.
- Never read private key/auth-cache contents into the model. Provider CLI owns its login/use/revoke
  storage; use supported commands, not direct cache/database edits or copies between runtimes.
- A credential retrieved inside a reviewed local process stays in memory and flows directly to
  the authorized consumer. No debug payloads, shell tracing, secret command-line flags or dumps.
- Human website passwords and API/app passwords are different credentials. Use the user's chosen
  protected autofill manager for humans, and verify the exact website/account. Generic Keychain
  entries do not prove browser autofill works.
- No hardcoded organization identity, service/account label, secret-manager preference or global
  credentials schema is imposed. Do not silently switch a working backend or rotate shared
  credentials without resolving actual consumers and authorized scope.
- Credential possession does not authorize writes, charges, deployments or message sending.
  Resolve intended access and least-privilege scope; verify account/resource through a read-only call.
- Secret exposure requires revocation/rotation through provider-supported mechanisms. Deleting
  a local copy does not invalidate copies in logs, version history or other systems.
- Local scanning defaults to report-only and requires explicit paths. Redaction and backup cleanup
  require separate reviewed scope; a scanner finding is a candidate, not perfect leak detection.

## Shipped helpers and limits

The macOS Swift helper uses a masked native dialog and Security framework calls in memory. It
never passes the value through `security -w VALUE` argv. It requires Apple command-line developer
 tools/Swift and a logged-in GUI; user unlock/consent remains unavoidable. Its non-secret identifiers
are arguments. It refuses overwriting an existing entry without `--replace` and verifies stored bytes.

The Windows helper uses `Get-Credential` and the explicitly installed `CredentialManager` module.
It does not install modules, print values or test arbitrary endpoints. Actual Windows execution
must be verified on the user's machine; availability on a Mac is not a Windows PASS.

The Python 3.10+ sweep detects prefixed keys, suspicious auth text and private-key shapes. It
supports explicit text files/directories, report-only/dry-run, opt-in redaction, JSON/JSONL integrity,
backups in a separate private OS temporary root or explicitly private non-synced directory,
symlink refusal and pre-write content recheck. It does not scan Git history,
cloud logs, browser stores or hidden remote revisions, and cannot certify absence of all secrets.
Private-key header findings stay report-only because partial redaction would leave key material.

Optional bundled `norml-connect` may handle provider setup; the procedures here also work standalone
using official supported provider auth. Verify static scripts in [isolated QA](qa/test-sweep.py).
No real credential insertion, rotation or user-file redaction is a package-verification fixture.
