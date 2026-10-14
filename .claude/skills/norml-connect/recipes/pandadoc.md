# Connect: PandaDoc

## 1. What and why

Sandbox/Production API authentication. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

The intended workspace, owner-approved Dev Center access and current API entitlement for the chosen environment. Verify current plan terms instead of assuming a subscription includes Production API.

## 4. Setup

Choose Sandbox or Production explicitly. Reuse a working connector or create a dedicated API key under the owner’s Dev Center authority. Store it in the OS store and send it only inside the process’s API-key header. Do not copy agreement data or recipient credentials into setup notes.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read the document list with at most one result and expose only a count/status, not document names or recipients. Confirm workspace/environment from the provider setup metadata. An empty list can authenticate; it does not prove workspace identity by itself.

## 7. Obstacles and fixes

Missing Dev Center: role or API entitlement. 401: key mismatch/revocation. 403: environment/endpoint restriction. Sandbox success does not establish Production access. No real contract is created or sent as a test.

## 8. Administrator bootstrap

The owner/admin enables API access and the correct environment under the provider’s current policy. Signing/sending remain separate explicit actions.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.pandadoc.com/reference/auth-overview). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
