# Connect: Telegram bot

## 1. What and why

Exact bot/chat identity check. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Owner-approved bot token and selected destination. Bot identity and chat permission are separate.

## 4. Setup

The owner creates a bot using BotFather if needed and enters the token directly into the OS store. The recipient starts the bot or adds it to the intended group. Use the official Bot API through an in-process client; token-bearing URLs must never enter logs or command arguments. Do not enumerate unrelated private updates to guess a destination.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Read `getMe` and, for the approved destination, `getChat`. Confirm expected bot username and chat ID. Send nothing during connection setup; an actual alert requires separate authorization.

## 7. Obstacles and fixes

401: wrong/revoked bot token. Chat not found: wrong ID or absent membership. 403: bot blocked/removed. Timeout after a later send has uncertain outcome and must be reconciled before retry.

## 8. Administrator bootstrap

Bot owner creates/rotates through BotFather and grants only the rights needed in the selected chat.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://core.telegram.org/bots/api). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
