# Connection boundaries

Select accounts by the user's instruction and verify through the provider.
Do not infer identity from an AI login, a local secret label or a browser tab.

Keep actual tokens/passwords in macOS Keychain, Windows Credential Manager or
Linux Secret Service; provider-managed gcloud/gh/MCP OAuth stores are acceptable.
Use secure native entry and an in-process secret-store API. Never put a secret
in shell arguments, logs, screenshots, source code, synced files or chat.
Do not inspect or copy a provider's OAuth database. Non-secret notes may record
account, endpoint, scopes, target IDs, OS-store reference and verification date.

If an existing CLI falls back to plaintext credentials when the native store
is unavailable, stop and configure its documented protected-store route.
Do not simply assume a successful login implies safe storage.

One runtime's MCP login does not authenticate another runtime. Inspect the
requested runtime's current help, registration and credential-storage support.
Register only the selected connector, preserve existing entries, reload it,
then verify a harmless identity call and one intended resource.

Opening the provider sign-in page is a login step. Browser control, screenshots
of private account pages and UI operations require their own authorization.
Prefer supported API/CLI operations for repeatable setup and verification.

Administrator privileges, resource sharing, API enablement, developer approval,
license assignment and billing are separate boundaries. Do not grant broad
Owner roles or change payer merely to fix a 403. Ask only for the verified
missing permission and never request a secret in chat.

Do not send, post, create contracts, launch campaigns, publish deployments,
change DNS or spend generation credits as a verification test. A successful
read does not demonstrate write entitlement; verify writes later inside the
authorized operating workflow. Reconcile uncertain mutations before retry.

If a secret is exposed, stop use, revoke/rotate through the provider, remove
the leak through the owning workflow, securely reconnect and verify again.
