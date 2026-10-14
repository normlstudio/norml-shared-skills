# Connect: Google Sheets

## 1. What and why

Native sheets API access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

The intended Google identity and an exact native file ID; choose read versus edit explicitly.

## 4. Setup

Follow [Google Workspace](google-workspace-automation.md). There is no separate sheets key. Build the relevant client using scripts/google_auth.py and load_credentials(account). Do not read an Office export or hardcode a company file ID.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read the exact file using the native API and check Drive metadata canEdit only if writing is needed. Authentication, target read and write permission are separate results.

## 7. Obstacles and fixes

403: wrong identity/resource/scopes/API enablement. canEdit=False: Viewer/Commenter works for reading but not editing. .gdoc/.gsheet is a pointer: resolve its ID rather than parsing document content from it.

## 8. Administrator bootstrap

Owner/admin grants the exact file permission and approves required OAuth/app policy. No service-account key distribution is included.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.google.com/workspace/sheets/api/scopes). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
