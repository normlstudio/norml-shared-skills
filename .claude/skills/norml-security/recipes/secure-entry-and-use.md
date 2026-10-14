# Secure credential entry and runtime use

Resolve intended provider account, credential scope and existing consumers first. Reuse a working
protected reference. Entry names are user-selected non-secret identifiers, such as `project-api`.
Native secure entry is human interaction; never ask the user to paste a value into conversation.

## macOS

Run the bundled helper with resolved package root and user-selected identifiers:

```bash
swift "{skill-root}/scripts/add-secret-macos.swift" "{service}" "{account}"
```

Swift/AppKit/Security are prerequisites; do not auto-install a compiler to store one credential.
A masked native field passes bytes directly to Keychain APIs. Cancel/empty entry fails closed;
existing service/account entries are refused. For an explicitly authorized replacement append
`--replace`; inventory shared consumers before updating. The helper reads back and compares bytes
without revealing value or length. Native Keychain consent/unlock may be required.

If Swift or GUI is unavailable, open the native Keychain Access create-password flow and let the
user enter it directly. Do not use scripted secret argv or unsupported stdin tricks. Terminal
interactive `security ... -w` may have platform/token-length pitfalls, so it is not presented as a
universal secure long-token importer. Verify the consumer instead of guessing storage correctness.

## Windows

An explicitly installed reviewed `CredentialManager` PowerShell module is required. If missing,
report the prerequisite and arrange authorized installation through supported PowerShell Gallery
mechanisms; the helper does not silently install it.

```powershell
& "{skill-root}\scripts\add-secret-windows.ps1" -Service "{service}" -Account "{account}"
```

The masked `Get-Credential` prompt stores directly in the current user's Credential Manager.
An existing target is refused unless `-ReplaceExisting` is explicitly authorized. The account
label is non-secret; actual provider identity still requires read-only resource verification.
Never use `cmdkey /pass:VALUE`, shell-profile exports or a plaintext file as a fallback.

## Using the value

Prefer provider CLI-managed OAuth or a vetted in-process protected-store client. When a local
consumer needs a token, retrieve it inside that process and set its HTTP authorization in memory.
Disable request/response/body tracing; sanitize errors. Do not insert secrets into curl flags,
subprocess argv, tool-call JSON, generated config or persistent environment exports. If a reviewed
launcher requires a child-only environment variable, document its OS/process visibility and keep
it confined to that child; do not imply environment variables are a vault.

Test the exact intended identity/resource with a least-privilege read-only call and return only
sanitized status/account/resource facts. Secret-store metadata presence alone proves no API access.
On rotation, replace the exact authorized entry, restart consumers and reverify. Never claim
connected from a tool listing or local entry existence. Clipboard history can retain pasted values;
when used, clear through the chosen manager, not only the current clipboard.
