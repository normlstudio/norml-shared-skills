# Connect: Runway generation MCP

## 1. What & why

Connect the owner’s media account to Codex through the official OAuth MCP. Source: [provider connection guide](https://help.runwayml.com/hc/en-us/articles/51931843164691-Connecting-to-Runway-MCP).

## 2. Who needs it

Authorized Marketing and Design operators, when explicitly requested.

## 3. Prerequisites

The correct provider account/workspace and supported Codex CLI. Uses Runway app credits. Explore Mode is not supported. This is distinct from the Developer Portal MCP at dev.runwayml.com/mcp.

## 4. Self-serve setup

The agent checks the existing named Codex server and reuses a correct URL. If missing, add it with `codex mcp add runway --url https://mcp.runwayml.com/mcp`. Initiate account authorization with `codex -c 'mcp_oauth_credentials_store="keyring"' mcp login runway`. For new registration, apply the same keyring override to the add command if it initiates OAuth. The agent opens the provider URL; the account owner completes sign-in, MFA and consent. Do not automate consent or invent scopes.

## 5. Where the secret goes

Codex manages OAuth in the native OS keyring, through the runtime’s native protected OAuth store. Never copy tokens to headers, environment variables, chat or synced files. Keep only non-secret identity/scopes/verification notes outside Git and synced folders. Preserve other runtime connections.

## 6. Verify

Confirm OAuth completion, then discover the live tools and make the provider’s available read-only account/credit lookup. Report the returned identity/workspace and available entitlement. Registration alone is not proof. If this session cannot reload new tools, report login status separately and reopen/resume in a runtime that loads the connector. Never spend credits as an authentication test.

## 7. Obstacles & fixes

URL saved but no account access → missing OAuth → start provider sign-in. Browser already logged in → it may still need consent for the connector. Wrong subscription → verify the selected provider account/workspace; do not purchase another plan. Tools absent after successful OAuth → reload the MCP in the runtime; another app’s connector does not authenticate Codex. API-key fields empty → normal for this OAuth route. `whoami` reports a Free personal workspace with no video models → authentication works, but that workspace lacks video entitlement. Check the intended paid login; if multipleWorkspacesAvailable is true, use list_workspaces and reconnect to the chosen workspace. Never infer a paid plan from a successful sign-in.

## 8. Admin-only bootstrap

Workspace admins may need to allow custom connectors or grant access to the paid workspace. No subscription purchase, plan change or credit purchase is authorized by connection setup.

## 9. Escalation

Capture only server URL, client version, HTTP/error code and the failed stage. Ask for the narrow account/admin approval required by the provider; never request a secret in chat or silently substitute browser automation or a paid API.

Source-derived connection route; recheck provider/client compatibility before first use. No account or entitlement was verified during public packaging.
