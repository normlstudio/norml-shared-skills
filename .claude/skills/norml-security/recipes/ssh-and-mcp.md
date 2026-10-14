# SSH keys and MCP secret transport

## SSH

Reuse configured alias/key and verify target identity before creating another pair. Private keys
stay in the protected SSH directory with restricted permissions. Generate a new authorized pair
with an interactive passphrase; only the `.pub` key may be displayed/transferred to the server
administrator. Never cat/read private key content into the assistant. Use supported SSH agent or
OS keychain integration for passphrase caching. Host-key changes require verified out-of-band
identity, never `StrictHostKeyChecking=no` to bypass a refusal.

A read-only connection test uses the already configured alias/key and exact target. Do not scan
unknown servers or improvise an installation path. Reference metadata may hold host/user/port/key
path, never private bytes or passwords. Revoking a key means removing its server authorization;
local deletion alone is not revocation.

## MCP

1. Resolve the exact provider identity and intended workspace/resource. Reuse existing authorized
   connection rather than reissuing it because an AI account/runtime changed.
2. Register a reviewed secure launcher through each runtime's supported mechanism. Config holds
   only launcher/non-secret identifiers, not copied token/auth-state values.
3. The launcher retrieves a protected secret in memory and passes it to its client without
   stdout/debug/argv leakage. Keep protocol stdout clean. Never assume JSON expands `${VAR}`
   or that GUI apps inherit the user's interactive shell exports.
4. Verify configuration, handshake, account identity and one intended read independently.
5. Rotation updates the one protected source; restart every affected launcher and reverify.
   Removal first inventories consumers. Removing a runtime entry does not revoke provider access.

Sharing credential references does not share chats, memories, tool approvals or provider permissions.
Other machines need their own authorized setup. Keep distinct provider identities distinct; cloud
chats cannot automatically read a local keychain. If a client lacks supported secure transport,
record that exact limitation instead of writing a literal token to config or decrypting auth stores.
