# Connect: Smartlead

## 1. What and why

Read-only campaign inventory authentication. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

An intended workspace and plan/role with API access. This recipe does not provision mailboxes, configure warm-up or send campaigns.

## 4. Setup

The owner creates a dedicated API key through the provider’s supported API-key management surface and enters it directly into the OS store. Use the official API client with the key resolved in process. Suppress query-string URLs because this provider may authenticate via a key parameter. Preserve other workspaces and existing working keys.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

A successful campaign-inventory read proves authentication; record a sanitized count and separately confirm workspace identity through the account’s supported metadata. A count alone does not prove the intended workspace.

## 7. Obstacles and fixes

401/Invalid API Key: rotate exact credential after confirming intended workspace. Missing key control: role/plan restriction. 429: wait per provider. Timeouts/5xx create no mutation authority.

## 8. Administrator bootstrap

Only an authorized workspace owner grants API management and creates/rotates the dedicated key.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://api.smartlead.ai/). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
