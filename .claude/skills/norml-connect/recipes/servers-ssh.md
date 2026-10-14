# Connect: SSH servers

## 1. What and why

Read-only connection to a known server. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Verified hostname, port, account, host-key fingerprint and authorization to that target. Resolve connection metadata from the user/project, never guess a document root.

## 4. Setup

Reuse the selected SSH alias/key first. Generate a new key only if authorized: `ssh-keygen -t ed25519 -C '<your-email>' -f '<chosen-key-path>'`. The owner adds the public key to the intended server account. Match the server fingerprint to a trusted independent source before first connection. Use `ssh <verified-alias>`; do not disable host-key checking.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

`ssh <verified-alias> true` should succeed. A harmless identity/path read can then verify the exact target account; no deploy or database operation is part of connection setup.

## 7. Obstacles and fixes

Public-key denied: verify authorized_keys and chosen account. Changed host key: stop and verify with the administrator; do not blindly remove known_hosts. Timeout: diagnose network/firewall and endpoint before retries.

## 8. Administrator bootstrap

The server administrator grants the exact account/public-key access and confirms the trusted host fingerprint.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://www.openssh.com/manual.html). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
