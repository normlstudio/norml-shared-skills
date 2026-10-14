# Connect: Slack

## 1. What and why

Workspace identity and read-only channel access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Membership in the target Slack workspace and an approved OAuth app/connector. Determine whether the task needs user identity or a bot; do not infer posting authority.

## 4. Setup

Reuse an existing supported connector or owner-approved Slack app. Request only required read scopes for channel/history/search; chat:write is separate. The user completes OAuth, and the client stores the grant in its native protected store. For a token-based reviewed MCP launcher, load the token from the OS store into memory/environment at process start; never embed it in MCP config. Register each chosen runtime separately.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

`auth.test` must return the expected team/user identity. Read one intended channel via `conversations.info`/a permitted history read. Do not send a test message. Tool presence verifies discovery, not access to all channels.

## 7. Obstacles and fixes

invalid_auth/token_revoked: reconnect exact installation. missing_scope: request only the missing scope. channel_not_found: verify membership and ID. One runtime working says nothing about another runtime’s registration.

## 8. Administrator bootstrap

Workspace/app admins approve the app and narrow scopes; private-channel membership remains a separate resource grant.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://docs.slack.dev/authentication/). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
