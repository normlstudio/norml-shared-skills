# Connect: Google Cloud

## 1. What and why

Known-project CLI authentication. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Google Cloud CLI and an intended account/project with the needed IAM role. IAM, resource access and user login are separate.

## 4. Setup

Reuse existing authorization. If needed launch `gcloud auth login user@example.com --no-activate`. Pass `--account` and `--project` explicitly on target operations; do not change global defaults or update ADC just to inspect one project.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

`gcloud projects describe <project-id> --account user@example.com --format="value(projectId)"` must return the exact target. Project listing alone does not establish access to the selected project.

## 7. Obstacles and fixes

PERMISSION_DENIED: identify exact missing IAM permission. Wrong project: pass it per command. Token revoked: reconnect selected account. USER_PROJECT_DENIED: verify quota-project service usage role, not Owner permission.

## 8. Administrator bootstrap

An authorized Cloud administrator grants narrow predefined roles at the lowest suitable project/folder scope and enables only required APIs.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://docs.cloud.google.com/sdk/docs/authorizing). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
