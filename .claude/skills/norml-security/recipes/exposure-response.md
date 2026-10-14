# Exposure response

1. Stop using/propagating the exposed credential. Refer to it by type/reference, never its value.
2. State the concrete observed exposure and affected provider/account. A scanner match alone is
   a candidate needing private confirmation; do not rotate another user's legitimate fixture.
3. Inventory consumers and obtain required provider/action authority. Use supported revocation
   and replacement flows; the human performs unavoidable login/MFA/consent/native secret entry.
4. Store the replacement directly in the protected store. Revoke the exposed credential and verify
   revocation/new identity as supported; do not claim revocation from a local deletion.
5. Update authorized consumers, restart them and verify intended resources without secret output.
6. Remove exposed copies only under reviewed exact scope; retain non-secret incident evidence.
   Git/chat/file/cloud history may preserve earlier values. Never force-push/delete history as
   an automatic incident shortcut. Rotation is required even if an exposed copy disappears.
7. Offer an explicitly scoped local sweep. Report-only scanning and actual redaction are separate
   effects. Local cleanup cannot touch provider logs, remote chat storage or earlier replicas.
8. Report sanitized actions, verification, outstanding consumers/exposure surfaces and blockers.

Private-key replacement includes installing/verifying the new public authorization before removing
old server authorization, within the approved target scope. Shared credentials need consumer
coordination; account recovery codes and signing keys may have provider-specific consequences.
Use current official provider guidance rather than guessing token-issuance UI/API support.
