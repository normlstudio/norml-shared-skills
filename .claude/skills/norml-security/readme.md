# norml-security

> Keep secret values outside model-visible text and handle storage, exposure and local scanning
through explicit scope.

## The problem

Secrets can persist in command arguments, transcripts, config and backups even after a visible
copy disappears.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Api key | *"API key"* |
| Keychain | *"Keychain"* |
| Credential manager | *"Credential Manager"* |
| Ssh key | *"SSH key"* |
| Mcp credentials | *"MCP credentials"* |
| Secret exposure | *"secret exposure"* |
| Leak check | *"leak check"* |
| Browser password migration | *"browser password migration"* |

## A typical run

1. Verify provider, resource, existing store and allowed effects.
2. Use a masked native prompt or supported provider auth.
3. Confirm identity and intended read without showing secret values.
4. Rotate/revoke and reconcile actual consumers when required.
5. Report privately; redact only under reviewed opt-in scope.

---

## Details

### Inputs

- Exact provider account/resource and authorized credential reference.
- Existing protected store or supported provider-managed authentication.
- Swift and logged-in GUI for the macOS helper; Python 3.10+ for selected-file scanning.

### What it creates or changes

- Protected store entries without secret values in assistant output.
- Sanitized identity/resource verification status.
- Restricted scanner reports and explicit unresolved coverage.
- Opt-in redacted files; original backups stay in a separate private OS temporary root
  or an explicitly selected private, non-synced `--backup-dir`, never beside source files.
  `--report-dir` controls reports only; backups remain until cleanup is authorized.

### Commands in depth

#### Api key

*"API key"* — Resolve provider identity and least privilege, then use protected native entry
rather than chat.

#### Keychain

*"Keychain"* — Use a masked macOS dialog and native Security calls; existing entries require
explicit replacement.

#### Credential manager

*"Credential Manager"* — Use the reviewed Windows module and masked prompt; module installation
and execution are separate.

#### Ssh key

*"SSH key"* — Keep private bytes out of model input; transfer only a verified public key and test
the configured target.

#### Mcp credentials

*"MCP credentials"* — Register a reviewed secret-resolving launcher; verify handshake, identity
and one intended resource.

#### Secret exposure

*"secret exposure"* — Stop propagation, use provider-supported rotation/revocation, and update
actual consumers.

#### Leak check

*"leak check"* — Scan only explicitly selected paths, review restricted report and choose
redaction separately.

#### Browser password migration

*"browser password migration"* — Use the selected supported human autofill store and verify exact
domain/account; preserve conflicts.

### Inside the package

- [SKILL.md](SKILL.md)
  Secret boundaries and workflow selection
- [secure-entry-and-use.md](recipes/secure-entry-and-use.md)
  macOS/Windows entry and in-memory use
- [ssh-and-mcp.md](recipes/ssh-and-mcp.md)
  Private-key and transport boundaries
- [exposure-response.md](recipes/exposure-response.md)
  Revocation, consumer update and cleanup
- [add-secret-macos.swift](scripts/add-secret-macos.swift)
  Masked dialog plus native Keychain APIs
- [secrets-sweep.py](scripts/secrets-sweep.py)
  Explicit-path scanner and opt-in redaction
- [test-sweep.py](qa/test-sweep.py)
  Disposable input/preservation/CLI tests

### Limits

- No Linux secret-store helper is shipped.
- Windows helper needs an explicitly installed reviewed CredentialManager module and verification
  on Windows.
- Scanner patterns do not cover every secret format, Git history, browser stores or cloud logs.
- Private-key header findings are report-only; local deletion does not revoke credentials.

### When something breaks

- **Secret appears in chat or source.** Stop propagating it and follow exposure response.
- **Protected entry already exists.** Check consumers before an explicitly authorized replacement.
- **Scanner exits nonzero.** Read its restricted report; findings/errors remain unresolved.
- **Native prompt or supported transfer is unavailable.** Report the exact prerequisite; use a
  user-approved native/provider route.

### Source of truth

[SKILL.md](SKILL.md) routes runtime operations. The linked procedures provide the full operational
checks. This guide explains the public package and does not add authority or claim live access.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
