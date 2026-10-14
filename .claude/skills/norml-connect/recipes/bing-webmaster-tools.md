# Connect: Bing Webmaster Tools

## 1. What and why

User-scoped JSON API authentication. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

An intended Bing Webmaster identity, API access and a generated user-scoped API key. A first verified site may be an account prerequisite.

## 4. Setup

Store the provider-generated key in the native secret store. Use Bing’s supported JSON REST API; retrieve the key in process. The GetUserSites request contains an apikey query parameter, so suppress request URLs, debug logs and raw exception payloads. Never pass that URL to a visible shell argument. No site/DNS/sitemap mutation belongs to connection setup.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read GetUserSites and reduce output to expected site URL plus verification boolean. Do not expose ownership verification codes. An empty list authenticates but gives no target authorization; verify the exact site before using it.

## 7. Obstacles and fixes

InvalidApiKey: revoked/incorrect/wrong-user key. Expected site missing: wrong account or not shared. No API option: account/API terms or first-site prerequisite. Avoid obsolete SOAP/POX integration routes.

## 8. Administrator bootstrap

The account owner enables API access, rotates the key and grants/establishes intended site ownership through separately authorized website operations.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://learn.microsoft.com/en-us/bingwebmaster/getting-access). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
