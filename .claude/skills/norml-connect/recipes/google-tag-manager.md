# Connect: Google Tag Manager

## 1. What and why

Read-only API identity and target visibility. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

A selected Google identity with access to the exact GTM-XXXXXXX public container ID, supported API clients and appropriate app/project policy.

## 4. Setup

Reuse a verified connector with the requested read scope. For a new ADC route,
choose a new private provider configuration directory outside Git/synced
storage and use it consistently for login and verification. Do not override a
working default ADC. On POSIX:

```sh
export CLOUDSDK_CONFIG="$HOME/.local/share/google-api-profiles/google-tag-manager"
mkdir -p "$CLOUDSDK_CONFIG"
chmod 700 "$CLOUDSDK_CONFIG"
gcloud auth application-default login user@example.com \
  --scopes='openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/tagmanager.readonly'
```

On Windows set the same process-scoped CLOUDSDK_CONFIG in a user-private
application-data directory; apply a user-only ACL. Provider consent is the
human step. Non-Cloud OAuth scopes may be blocked by the installed SDK client
or organization policy. Use the provider-supported authorized OAuth client or
existing connector if required; the agent does not claim every OAuth client
can be issued through an API. Stop at the exact missing admin approval.
Set a quota project only if needed by observed API policy; the intended account
must have service-usage permission there. Never borrow another account’s grant.

Run `scripts/verify-google-read.py` with the same CLOUDSDK_CONFIG, explicit
profile/account/target and optional quota project. It reads identity and target
resources without printing tokens. Add required Python packages from requirements.txt
in an isolated virtualenv before running it.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

The API must verify user identity and return the exact GTM-XXXXXXX public container ID. No properties means authenticated without target access. Editing/publishing scopes are not requested.

## 7. Obstacles and fixes

403/API disabled: verify API enablement and exact resource grant. Insufficient scopes: repair only this isolated profile. Wrong identity: stop before reads. Policy-blocked consent: request narrow admin access; never disable issuer/TLS validation.

## 8. Administrator bootstrap

Resource owner grants read access. Cloud/project administrators enable required APIs and any necessary quota-project permission. GTM publishing, Analytics editing and GSC ownership remain separate.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.google.com/tag-platform/tag-manager/api/v2/authorization). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
