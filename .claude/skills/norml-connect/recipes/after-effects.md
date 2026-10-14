# Connect: After Effects MCP

## 1. What & why
Use the third-party MIT-licensed `@kumoproductions/mcp-aftereffects` bridge for local After Effects project inspection, atomic edits, saving and preview frames. Adobe does not maintain this connector. Source: https://github.com/kumoproductions/mcp-aftereffects (reviewed version 0.2.0).

## 2. Who needs it
Designers and marketers producing editable motion projects; for an explicitly chosen editing workflow.

## 3. Prerequisites
Licensed After Effects 2024–2026 on macOS or Windows; Node.js 24 or newer; intended runtime installed. Review the pinned package and its install scripts first. Existing Adobe subscription and app login remain user-owned.

## 4. Self-serve setup
1. Resolve the installed AE application and Node binary. Keep an existing runtime default unchanged; install Node 24 alongside it if required.
2. Install the pinned package in an isolated local directory outside Drive and Git:
   `npm install --prefix "{local-tool-root}/after-effects-mcp" --ignore-scripts --no-audit --no-fund @kumoproductions/mcp-aftereffects@0.2.0`
3. Register the exact absolute Node and `node_modules/@kumoproductions/mcp-aftereffects/dist/index.js` paths with each requested runtime. Claude Code: `claude mcp add --scope user aftereffects -- {node-path} {server-path}`. Codex: `codex mcp add aftereffects -- {node-path} {server-path}`. Inspect existing names first; back up configuration before replacing an existing entry. No generic eval flag is required for normal operations.
4. Open After Effects. Enable Preferences → Scripting & Expressions → Allow Scripts to Write Files and Access Network. Prefer an AE scripting preference query/update if supported; otherwise the teammate sets this control.
5. Allow the provider-owned macOS Automation prompt for the calling app to control After Effects. Never change TCC databases, bypass denial, or force-quit an occupied editor.
6. Reload the runtime to expose the new tool menu. A direct MCP SDK client can verify the same stdio server in the current session.

## 5. Where the secret goes
This local connector needs no API key. Store only non-secret version/paths/status in local private notes; OS consent remains user-owned. Never place Adobe login state in the bridge or synced storage.

## 6. Verify
Initialize MCP, list tools, then call `ae_version_info` and `ae_project_info`. Tool discovery alone does not prove AE access. Discover operation schemas with `ae_catalog`; test create/keyframe/save/render on a dedicated scratch composition only when editing is authorized. Inspect the resulting PNG and confirm the saved AEP exists. Distinguish installed, registered, connected and edit/render verified.

## 7. Obstacles & fixes
- Node below 24 → engine mismatch → use an isolated Node 24 binary, not a global default switch.
- Automation denied (-1743) → macOS consent absent → teammate permits the calling app; do not bypass.
- Automation permission absent → inspect the actual calling process and supported native consent. Do not alter TCC or use a relay to bypass denied permission.
- Dispatcher cannot write → AE scripting preference disabled → enable the documented preference and retry once.
- Timeout → AE may show a modal dialog or another script may hold its lock → inspect status and resolve the dialog; never replay a mutation until checking whether it applied.
- Wrong app path → set `AE_MCP_EXE` to the verified application bundle.
- Active unrelated project → inspect dirty state, save it only if authorized, and use a separate scratch project or stop before replacing it.

## 8. Admin-only bootstrap
No server, Adobe organization admin or paid MCP subscription is required. Managed Macs may require their administrator to allow Automation. Installation does not authorize changing any production website or purchasing templates/music.

## 9. Escalation
Report package version, AE version, tool name and sanitized error. Ask the teammate only for an unresolved OS consent or occupied-project decision. Preserve existing projects and disclose unverified edit/render status.
