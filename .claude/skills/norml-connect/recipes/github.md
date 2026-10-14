# Connect: GitHub

## 1. What and why

Git and repository/API access. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

Git, GitHub CLI and access to the exact repository. Choose the intended owner/repository; no organization is imposed.

## 4. Setup

Inspect `gh auth status` first. If needed run `gh auth login --hostname github.com --git-protocol ssh --web` and `gh auth setup-git`. Let the user complete provider login and any SSO approval. Reuse an existing SSH key; register only its public key. Never rotate or replace working authentication without a reason.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

`gh repo view <owner>/<repo> --json nameWithOwner,url` must return the selected target. For SSH run `ssh -T git@github.com`; GitHub may return exit 1 even for its successful no-shell greeting. Do not interpret that exit alone as failed authentication.

## 7. Obstacles and fixes

404 may mean no repository permission, not absence. Confirm owner, account and SSO. SSH denial means check public-key registration and agent state. Never read a private key into chat.

## 8. Administrator bootstrap

Repository/organization owners grant narrow team/repository access and SSO authority. They alone approve policy changes.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://cli.github.com/manual/gh_auth_login). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
