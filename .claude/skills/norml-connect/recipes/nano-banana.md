# Connect: Gemini image access

## 1. What and why

Subscription versus API connection boundary. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Explicit selected Google account, requested subscription-web or API route and current model entitlement. A Google login, web subscription and API billing are different states.

## 4. Setup

Honor the requested route. For subscription access open the provider’s own login for the user without extracting cookies; automation needs its own browser authorization. For API access use Google’s supported Gemini client and the selected project/key in the native secret store. Never silently attach API billing to fix web subscription access. Model generation is an operating task, not a default connection test.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Verify account and available model/entitlement through the chosen supported route. Report capability as untested until a separately authorized generation produces the requested model’s downloadable, decodable output. A login badge alone does not prove image capability.

## 7. Obstacles and fixes

Web subscription but depleted API credits: different products. CLI OAuth working while image extension requests key: different auth route. Wrong Google account: select explicitly, preserve other sessions. Model quota: report exact refusal and do not switch payer/model implicitly.

## 8. Administrator bootstrap

Workspace/license and API-billing owners control enablement, license assignment and funding. None is inferred from a connection request.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://ai.google.dev/gemini-api/docs/billing/). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
