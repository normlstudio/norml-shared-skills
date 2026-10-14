# Connect: Google Drive

## 1. What and why

Mounted-file navigation and native API access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

The chosen account and exact authorized folder. Google Drive for Desktop is optional for mounted Markdown/local assets; it does not authenticate an API client.

## 4. Setup

If a mount is requested, use Google’s supported Drive for Desktop installation/login and resolve the actual mount path rather than hardcoding an email or drive letter. Native Docs/Sheets pointers contain IDs, not document text. For API access use [Google Workspace](google-workspace-automation.md).

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read a known local ordinary file for mount verification. Separately verify API identity and the exact native file. A mount listing does not establish API edit access.

## 7. Obstacles and fixes

Wrong/missing mount: inspect selected Drive account and localized folder/shortcut path. Permission denied: target sharing missing. Native pointer empty: read live content through the API, not an export.

## 8. Administrator bootstrap

The folder/shared-drive owner grants only the necessary target access. Group inheritance and limited-access children must be checked for that real target.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://support.google.com/drive/answer/10838124). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
