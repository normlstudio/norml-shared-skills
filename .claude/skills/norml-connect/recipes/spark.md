# Connect: Spark

## 1. What & why

Expose the teammate's chosen Spark Desktop accounts to the local CLI. Mailbox operations use the installed vendor command contract.

## 2. Who needs it

People using Spark on macOS who want interactive email/calendar access. Optional;
not the automation contract for project provisioning mailboxes.

## 3. Prerequisites

The user's running Spark Desktop app, their intended account already added,
and its supported `spark` CLI. The app-provided use-spark skill is the command
source. This reviewed contract covers the macOS IPC interface, not Windows.

## 4. Self-serve setup

1. Check `command -v spark` and the installed vendor-provided command documentation. Reuse existing installation.
2. If the app is closed, ask the teammate to launch Spark Desktop.
3. In Spark Desktop → Settings → AI Agents, the teammate enables only the
   intended account/shared inbox at the access needed: read-only for reading,
   triage only when draft or mailbox mutation is requested.
4. If the CLI or its skill is missing, use the installed app's AI Agents setup
   instructions. `spark skill` emits the vendor skill once the CLI is available;
   preserve its provenance and use the runtime’s supported registration route.
   Do not guess an npm package, brew formula or unsupported installer command.

## 5. Where the secret goes

Spark's own app retains its account authentication. Do not extract, copy or
re-store mailbox passwords/cookies. The CLI uses IPC, not a second auth token.
No separate credential is created for the IPC route.
No mailbox inventory belongs in the shared catalog.

## 6. Verify

Run `spark accounts`; confirm the exact intended account and its reported access
level. Report only the relevant account status, not all mailbox/calendar names.
A successful list verifies account exposure, not draft or send permission. Use
read-only checks; do not create a draft or post a team comment as a smoke test.

## 7. Obstacles & fixes

- IPC connection fails → run in the person's real Mac desktop session and have
  them launch the app. Containers and headless servers cannot provide it.
- Intended mailbox absent → enable that specific account in Settings → AI Agents.
- Write denied → current access is read-only. Keep requested reading operational;
  changing permission is a separate user choice.
- Unknown command → follow use-spark's version/embedded-skill refresh procedure.

## 8. Admin-only bootstrap

None for a person's already connected mailbox. Shared inbox/team permission may
need the workspace owner; request only the specific missing resource permission.

## 9. Escalation

Report the missing binary, app connection or account access level. No browser
fallback or mailbox-secret export. Route headless project mail to the documented
project-mailbox-imap-smtp recipe instead.
