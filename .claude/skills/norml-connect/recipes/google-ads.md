# Connect: Google Ads

## 1. What and why

Selected customer read-only API access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Chosen customer ID, developer-token access, supported API version and user OAuth access to that customer. Manager ID is used only when applicable.

## 4. Setup

Reuse an authorized official Google Ads client. Otherwise the owner completes developer-token/app bootstrap, and the agent launches the supported installed-app OAuth flow with the adwords scope and validated state. Store developer token, OAuth client secret and refresh token in the native secret store. Do not use a plaintext google-ads.yaml with embedded credentials. No private campaign helper is required.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read the selected customer identity, currency/timezone and one allowed reporting endpoint. Verify test versus Production access and the optional login-customer ID. Visible account inventory does not justify choosing an unrelated customer.

## 7. Obstacles and fixes

401: wrong/revoked user grant. Developer-token restriction: verify access level/test boundary. Customer denied: account membership/manager mapping. Unsupported version: select a currently supported provider API version.

## 8. Administrator bootstrap

Owner/admin obtains developer-token approval and OAuth app access and grants customer membership. Funding and campaign writes remain separate.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.google.com/google-ads/api/docs/oauth/overview). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
