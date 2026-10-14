# Connect: Palmier Pro

## 1. What & why

Palmier Pro is a native macOS video editor with a built-in streamable HTTP MCP
server. Connecting it lets Codex or Claude Code inspect and operate the local
Palmier project through the tools the app advertises.

The server is local-only at `http://127.0.0.1:19789/mcp`. Palmier Pro must be
running whenever a runtime uses the connection.

## 2. Who needs it

Marketing, content, and other teammates who edit video in Palmier Pro. This is
an optional operator connection, not a baseline requirement for every role.

## 3. Prerequisites

- macOS with Palmier Pro installed in `/Applications/PalmierPro.app`
- Palmier Pro running; sign in inside the app when the requested capability
  requires an account or subscription
- Codex or Claude Code installed for the runtime being connected

The direct HTTP path does not require Node. Palmier's bundled Claude Desktop
shim declares Node 18 or newer, but Codex and Claude Code can connect directly
to the app instead.

## 4. Self-serve setup

1. Start Palmier Pro and confirm that its loopback server is listening:

   ```bash
   open -a "Palmier Pro"
   lsof -nP -iTCP:19789 -sTCP:LISTEN
   ```

2. Register the server in Codex if `codex mcp get palmier-pro --json` does not
   already show the exact loopback URL:

   ```bash
   codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp
   ```

3. Register it separately in Claude Code when that runtime also needs access:

   ```bash
   claude mcp add --transport http --scope user \
     palmier-pro http://127.0.0.1:19789/mcp
   ```

4. Start a fresh session in each newly configured runtime. MCP tools are loaded
   when the session starts; changing the config does not retrofit the current
   tool list.

## 5. Where the secret goes

There is no secret. Palmier Pro exposes an unauthenticated loopback endpoint
that is reachable only on the same Mac. Do not create a Keychain entry for it.

Codex and Claude Code store only the local endpoint in their own MCP registries.
Their registrations are separate and must not be assumed to synchronize.

## 6. Verify

With Palmier Pro running, execute the sanitized verifier:

```bash
python3 {skill-root}/scripts/verify-palmier-pro.py
```

It must report an MCP protocol version, the `palmier-pro` server identity, a
non-zero tool count, and `manage_project list: passed`. It never prints project
names or media details.

Also confirm the runtime registration:

```bash
codex mcp get palmier-pro --json
claude mcp get palmier-pro
```

Only run the command for the runtime being verified. In a fresh session, a
read-only end-to-end prompt is: `List my Palmier projects without opening one.`

## 7. Obstacles & fixes

- **Connection refused → Palmier Pro is not running or its MCP listener has not
  started →** open the app, wait for its main window, then rerun the `lsof` and
  verifier commands
- **The registration exists but Palmier tools are missing → The session loaded
  before the MCP entry was added →** start a fresh Codex or Claude Code session
- **The runtime points at a different URL → A stale Palmier entry already exists
  →** inspect it with `codex mcp get palmier-pro --json` or
  `claude mcp get palmier-pro`; remove only that named entry, then add the exact
  loopback URL again
- **The verifier passes but no project is selected → Connection and project
  selection are separate →** use `manage_project` with `action='list'`, then
  explicitly open the intended project
- **Editing works but generation fails → The MCP connection is healthy, while
  Palmier account, subscription, or model access is unavailable →** sign in to
  Palmier Pro, check `list_models`, and do not retry a paid generation without
  user confirmation
- **Palmier's Claude Desktop shim fails under Node 16 → The bundled MCP shim
  declares Node 18 or newer →** use the direct HTTP registration above for
  Codex or Claude Code, or upgrade the Node runtime used by Claude Desktop

## 8. Admin-only bootstrap

No company administrator bootstrap is required. Palmier account access and any
paid subscription are owned by the teammate or account owner using the app.

## 9. Escalation

Share the Palmier Pro app version, sanitized output from the verifier, the
relevant `mcp get` result, and whether port `19789` is listening. Do not share
project names, media, transcripts, or generated content unless needed and
approved for the support request.
