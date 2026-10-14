# Connect: Notion

## 1. What and why

Connection identity and exact content access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

A Notion account/workspace plus a supported OAuth connector or owner-approved internal connection with read capability and access to the exact source resource.

## 4. Setup

Reuse the intended connector. For an internal connection the workspace owner creates it with minimum capabilities and shares the original page/database to it. Enter its token into a native secret store; the selected SDK loads it inside the process. Set a supported, deliberately chosen Notion-Version header and migrate endpoint/resource IDs together when changing API version.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read the connection identity via `/v1/users/me`, then retrieve the exact page/database/data source. A successful user call with 404 on content is authenticated but not authorized. Pin the intended resource type; modern database containers and data sources differ.

## 7. Obstacles and fixes

401: credential revoked. 404: resource ID/type wrong or source not shared. 403: missing content capability. Working MCP auth does not authenticate an unrelated local token client.

## 8. Administrator bootstrap

The workspace owner controls integration capabilities and content sharing. No user should borrow another person’s token.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.notion.com/docs/authorization). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
