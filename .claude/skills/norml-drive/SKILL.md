---
name: norml-drive
version: 1.0.0
description: >
  Operate native Google Sheets and Docs through their live file IDs: pull,
  inspect, plan, apply and verify. Covers formulas, tables, formatting,
  document structure, tabs and UTF-16 indices with explicit account selection,
  protected local caches and destructive-operation safeguards.
license: MIT
---

# Norml Drive

Keep the live native Google file canonical. This public edition works with
your own Google account and target files; no company Drive mount or sibling
skill is needed. The bundled [authentication guide](standards/authentication.md)
and credential broker make it usable by itself.

## Workflow

1. Resolve the exact file ID from its native URL or .gsheet/.gdoc pointer JSON.
   Stop if a name matches several files. Do not substitute an Office export.
2. Confirm the intended account, target type and required read/edit capability.
   Follow [authentication](standards/authentication.md). Do not read tokens.
3. Sheets: follow [Sheets operations](recipes/gsheet.md). Pull a fresh snapshot,
   inspect locally, find rows/tables by identity, plan bounded requests and
   check the live modifiedTime again immediately before applying.
4. Docs: follow [Docs operations](recipes/gdoc.md). Read tabs/content/revision,
   select the exact tab, build UTF-16 ranges and use an appropriate revision
   write control. Re-read table indices after structure changes.
5. Apply only the authorized changes and read back the exact values, formulas,
   formatting and structure. Refresh caches and report target IDs/results.

## Destructive operations

Never permanently delete files or empty Trash through this skill. Trashing a
file, deleting a sheet/tab, clearing existing values, deleting dimensions or
content and recreating table wrappers require explicit authorization for exact
targets and a rollback plan. Existing task instructions can supply that
authorization; do not invent blanket deletion permission from a cleanup request.
Separate destructive calls from additive batches. Preserve comments and prior
content; a copied Google Doc does not preserve its comment threads.

## Source and cache boundaries

Local caches are rebuildable inspection snapshots, never write authority or
canonical documents. Use a user-private machine-local path outside Git/synced
storage. The snapshot may include personal data: restrict directory/file
permissions and do not print the whole cache into chat. Raw formulas and typed
values are retained separately from displayed text. See
[cache schema](standards/cache-schema.md) and [styling](standards/styling.md).

## Helpers and verification

`scripts/sheets.py` provides correct arbitrary A1 column labels and bounded
snapshot extraction. `scripts/doc_builder.py` builds text/style requests using
UTF-16 offsets and an explicit tab. Both are library helpers; they do not
provide an unattended mutation CLI. Run `python3 -m unittest discover -s qa`.

API login, Editor permission and an applied change are different verification
states. Missing access blocks dependent writes. Use supported API/MCP/CLI
connections; browser takeover and credential extraction are not fallbacks.
