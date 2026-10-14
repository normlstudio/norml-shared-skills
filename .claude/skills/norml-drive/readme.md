# Norml Drive

> Edit native Google files from live IDs with fresh state and verified changes.

## What it does

Read [SKILL.md](SKILL.md) for the runtime workflow and
[the recipes](recipes/) for the operating steps. All identity and resource
values come from your own request. This public edition requires no company
credentials, private data, internal repository or company Drive mount.

## When to use it

- Update this Google Sheet.
- Create a native Google Doc.
- Inspect this document’s tabs.

## Install and first run

Install this folder through the collection's root installation instructions.
The package carries its own entry point, helpers and procedures. Installing
instructions does not authorize an account login or live mutation. Start by
naming the exact account and resource. Reuse existing provider authentication.

## How it works

The runtime router selects a procedure. The agent resolves identity and target,
reads the current state, checks authorization, performs only the requested
operation and verifies the result. Secrets stay in the OS/provider store;
local inspection snapshots stay outside Git and synced storage.

## Inside the skill

- `SKILL.md` selects the bounded workflow.
- `recipes/` contains concrete setup or document-operation procedures.
- `standards/` defines account, storage and safety boundaries.
- `scripts/` contains packaged helpers, with no embedded account values.
- `requirements.txt` names the optional Google Python client dependencies.

## Capabilities and limits

Google helper scripts use Python and gcloud with explicit account selection.
Install dependencies into an isolated virtualenv. Other connected APIs/MCPs
may be reused if they support the required native operation and identity.
There is no blanket write grant, paid verification or browser takeover.
Missing provider access remains a precise blocker, not a successful connection.

## Verification

Helper logic, syntax, links and package boundaries are checked locally. No
recipient account has been authenticated or mutated during packaging. Run
the selected recipe's exact-resource read on your machine before relying on
account access. See the collection's validation command for package checks.

Covers SKILL.md v1.0.0. Generated Oct 13, 2026.
