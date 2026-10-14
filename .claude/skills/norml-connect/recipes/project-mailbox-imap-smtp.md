# Connect: Project mailbox

## 1. What and why

TLS IMAP/SMTP authentication without sending. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

An existing authorized mailbox, exact username, documented provider client endpoints/ports and an owner-approved secure credential handoff or supported OAuth route.

## 4. Setup

Resolve the provider’s IMAP/SMTP settings; an MX record is mail routing, not a client endpoint. Store passwords/app passwords in the native secret store, or use provider OAuth in its managed store. Use an in-process IMAP/SMTP client with certificate-validated TLS. Ports 993/465 are common implicit TLS examples, not universal defaults. For STARTTLS, negotiate before authentication and fail if unavailable.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Authenticate to IMAP and SMTP and disconnect without selecting private mail content or sending a message. Verify certificate hostname and chosen address. Reachable ports or a desktop client’s saved settings are insufficient.

## 7. Obstacles and fixes

Webmail works but API auth fails: verify full username, app-password/OAuth policy and endpoint. TLS failure: stop; never disable validation. Password rotation affects every authorized consumer and requires an explicit coordinated change.

## 8. Administrator bootstrap

The mailbox/domain owner creates the mailbox, enables approved authentication and grants access. No shared password is stored in a project note or public package.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://docs.python.org/3/library/imaplib.html). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
