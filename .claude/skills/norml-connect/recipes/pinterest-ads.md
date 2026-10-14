# Connect: Pinterest Ads

## 1. What and why

OAuth Ads-account read. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Selected app/business and Ads account, supported access tier, registered exact localhost redirect URI and required read scopes.

## 4. Setup

Use provider OAuth 2 authorization-code flow with state validation and the exact registered redirect URI. Request ads:read, billing:read only when needed, and ads:write only for authorized later mutations. Store app secret/access/refresh grants directly in the OS store. A provider-issued limited token must retain its actual displayed expiry/scopes and be labelled temporary; never assume it can refresh.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

List available Ads accounts using the official API, then read the chosen ID and compare identity, country and currency. Multiple similar names do not justify choosing the first. Do not create or activate an ad to verify.

## 7. Obstacles and fixes

Redirect mismatch: match scheme/host/port/path exactly. 401: refresh or reconnect the selected grant. 403: account permission, scope or access tier. Temporary token expiry needs replacement, not refresh. Billing unavailable means evidence missing, not verified.

## 8. Administrator bootstrap

The app/business owner registers redirect URIs, obtains provider access-tier approval and grants the intended account access.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
