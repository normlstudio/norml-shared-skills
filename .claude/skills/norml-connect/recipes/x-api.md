# Connect: X API

## 1. What and why

Own-account user-context authentication. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

The intended channel/app owner, developer API entitlement, a deliberate OAuth method and approved cost boundary. Consumer Premium access is separate from API access.

## 4. Setup

For the source-derived OAuth 1.0a path, the developer-app owner configures the needed app permissions before generating consumer key/secret and user access-token/secret. Store all four in the OS store; a supported OAuth 1.0a client signs inside the process. Bearer-only app auth and OAuth 2 client IDs are not substitutes for this quartet. Another supported OAuth method must be configured and verified as its own route. Do not fabricate a publishing client from a private sibling skill.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

GET `/2/users/me` through the chosen user-context client must return the exact intended username/ID. Confirm the current billing impact before a paid API check. No temporary post is required.

## 7. Obstacles and fixes

401: mismatched app/user credentials. 403 on writing despite successful identity read: missing app/token permission. If permission changes, reauthorize/regenerate the required user grant. 429: honor provider limits. Wrong username blocks later writes.

## 8. Administrator bootstrap

The app/channel owner controls developer access, user permission, credits and spending limit. A connection request authorizes no posting or credit purchase.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://docs.x.com/fundamentals/authentication/oauth-1-0a/overview). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
