---
name: norml-connect
version: 1.0.0
description: >
  Set up and repair provider API, CLI and MCP connections outside any company
  ecosystem. Resolve the requested account and resource, reuse authorized
  access, launch provider login, separate administrator bootstrap, store secrets
  securely and verify the exact target without sending or changing live data.
license: MIT
---

# Norml Connect

Connect an explicitly chosen tool to an explicitly chosen account. This public
edition has no company Drive root, employee domain, central password hub,
credential registry or mandatory sibling skill.

## Workflow

1. Identify provider, operating system, runtime and exact account/resource.
   Read project instructions and reuse a working authorized connection first.
2. Open the matching recipe in [the connection index](recipes/index.md).
   Each recipe separates setup, secret storage, verification and admin work.
3. Prefer supported API/CLI/MCP setup. Launch login and continue after the user
   completes sign-in, MFA and consent. Do not operate the browser as a fallback
   for a disconnected API without explicit user authorization.
4. Keep secrets in the OS secret store or the provider's managed OAuth store.
   Read [connection boundaries](standards/connection-boundaries.md).
5. Perform a read-only identity check and an exact-resource read. Report
   installed, registered, authenticated, authorized and verified separately.
   Never test a connection by posting, sending, purchasing or generating media.
6. On failure use that recipe's obstacles. Capture only sanitized status,
   identity, resource ID, version and time; do not log headers or raw payloads.

## Google Workspace helper

The bundled Python helpers support Google Cloud CLI user OAuth for Drive,
Sheets and Docs on macOS, Linux and Windows where gcloud and Python work.
There is no domain restriction or embedded file ID. Use the selected account
and explicit existing native Sheet/Doc IDs. Follow
[Google Workspace](recipes/google-workspace-automation.md).

The helper does not configure Cloud IAM, generate OAuth clients, grant file
access, create DWD keys, or bypass an organization's app policy. Existing
ADC is a separately selected route; it must have the appropriate scopes.
Third-party recipes document provider setup, not bundled publishing clients.

## Outputs and limits

Produces verified connection status and optional non-secret local notes. It
does not authorize operating changes, share permissions, send messages or
install every service merely because a person has a role. MCP registrations
remain runtime-specific. Paid entitlement is separate from authentication.

## Maintain a recipe

Use [the recipe template](templates/connection-recipe.md). Ground commands in
current provider documentation; preserve observed failures as dated evidence,
not universal facts. Test against a read-only known resource before claiming
the route works. An unavailable supported setup is an explicit blocker.
