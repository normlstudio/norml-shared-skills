# Connect: SolidTime

## 1. What and why

Selected-instance time-tracking API read. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Your own user in the intended instance/organization, project-read authority and personal-token support enabled by the instance administrator.

## 4. Setup

Open the selected instance’s Profile Settings and create a personal API token only if needed. Name it for the approved purpose and enter it directly into the OS store. Use your instance’s documented API base and organization IDs; no company hostname is hardcoded. The selected API client authenticates in memory.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read current-user/organization identity and one intended project through the instance’s documented REST API. Keep raw time entries private. Authentication does not authorize merging imported historical totals or writing billing records.

## 7. Obstacles and fixes

Token UI absent: personal-access client not enabled on self-hosted instance. 401: wrong instance/revoked token. Missing project: organization/resource membership. Imported history requires entry-level deduplication before totaling.

## 8. Administrator bootstrap

For a self-hosted instance, its admin follows the installed-version deployment guide to enable personal access tokens. Never run server Passport bootstrap just because a user wants to connect.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://docs.solidtime.io/user-guide/access-api). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
