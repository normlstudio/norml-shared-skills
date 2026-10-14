# Connect: Figma MCP

## 1. What and why

First-party remote MCP and intended-frame read. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

A Figma account with access to the exact file/frame and a runtime supporting remote HTTP MCP/OAuth. Seat/plan capabilities must be checked on the current account.

## 4. Setup

Inspect the intended runtime’s current MCP help. Register the official endpoint `https://mcp.figma.com/mcp` only if absent, then complete its provider-owned OAuth. Claude Code example: `claude mcp add --transport http Figma https://mcp.figma.com/mcp`. Register other runtimes separately using their current supported command. Preserve existing connections. Community canvas-write bridges are separate third-party installations, not silently bundled here.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Initialize/list tools, then read or request design context for the intended frame link. Confirm actual file visibility, account and feature capability. Server registration alone proves no target access.

## 7. Obstacles and fixes

403: file or plan/seat boundary. Tools absent: runtime registration/reload. Wrong frame: resolve URL/file/node ID. OAuth in one runtime does not authenticate another. A canvas write is a separate user action.

## 8. Administrator bootstrap

Workspace/file owners grant narrow file access and any necessary existing seat capability. No seat purchase is implied.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://developers.figma.com/docs/figma-mcp-server/). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
