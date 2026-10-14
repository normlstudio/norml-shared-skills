# Connect: Airtable

## 1. What and why

Base-schema read using scoped PAT/OAuth. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

A supported OAuth connector or personal access token with schema.bases:read and the selected base resource grant. Record writes need separately authorized data.records:write.

## 4. Setup

Reuse the intended connector. Otherwise the owner creates a PAT scoped to that base, enters it directly into the native secret store, and the approved API client retrieves it only in memory. Do not use retired API keys or paste the PAT into command arguments.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

GET `/v0/meta/bases/<base-id>/tables` through the official Web API must return the expected base schema. Verify selected table/field identities without dumping records. A schema read does not prove record-write permission.

## 7. Obstacles and fixes

401: revoked/wrong credential. 403: scope or resource grant missing. 404: wrong/invisible base. 429: respect retry guidance. Repair API access instead of browser takeover.

## 8. Administrator bootstrap

Workspace/base owners grant base access and token scopes. Schema creation and actual record mutations are separate operations.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://airtable.com/developers/web/guides/personal-access-tokens). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
