# Norml Changelog

> Record verified changes and decisions so future developers can understand the current project
state.

## The problem

Recent commits and chat context do not automatically preserve why a decision was made.

The package updates existing project records and compresses older routine entries while retaining
durable decisions, security fixes and breaking changes.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Log this development change | *"Log this development change"* |
| Update the changelog | *"Update the changelog"* |
| Record this architecture decision | *"Record this architecture decision"* |
| What changed in this session | *"What changed in this session"* |
| Update integration documentation | *"Update integration documentation"* |
| Compress the older routine changelog entries | *"Compress the older routine changelog entries"* |

## A typical run

1. Ask to log the verified block implementation and its registration decision.
2. The agent reads existing docs and relevant Git/session evidence, separating actual changes from
pending deployment.
3. It merges one same-day section in `docs/changelog.md` and updates the existing architecture
decision with rationale.
4. It confirms the files changed and records any unresolved migration state without claiming
production acceptance.

---

## Inputs and outputs

The package needs verified change/decision evidence and a project path. Existing project
instructions decide document locations; defaults are `docs/changelog.md` and
`docs/target-architecture.md` only when no convention exists. It updates applicable
architecture/infrastructure/content documentation and an existing migration map when affected.

## Evidence and ownership

Read actual diff/log and session scope. Recent commits can belong to another developer;
do not attribute every recent author's work to this session. Use a known baseline rather
than assuming `HEAD~5` exists. Without Git, supplied conversation/source evidence is enough.
Read immediately before writing and use scoped patches to preserve parallel-session changes.
Stop on conflicting concurrent edits instead of replacing the whole file.

## Entry format

Merge one section per date, group by area, write implemented changes in past tense and include
non-obvious rationale. `[DECISION]` tags durable architecture choices; `[INTEGRATION]` tags
external dependency/data ownership. Connected/verified, proposed and pending states differ.
Never put credentials, private dumps or fabricated acceptance into a changelog.

## Compression

After 50 date sections, summarize eligible routine work older than 30 days into weekly entries.
Keep at least the latest 20 date sections detailed. Preserve decisions, integration entries,
security fixes and breaking changes verbatim. Blend repetitive repairs into the true final state
without erasing why choices were made or promoting unfinished work to complete.

## Architecture updates

Read the existing target, merge into the matching section and add a current update marker.
Integrations record purpose, non-secret identity, data owner, sync direction and verified method.
If a new choice replaces an old one, retain a dated Superseded note and rationale. Migration
status changes only when evidence supports them; no new map for unrelated work.

## When something breaks

| Situation | Response |
|---|---|
| No docs exist | Create only the minimal changelog/architecture skeleton |
| No durable change/decision | Skip logging and say so |
| Decision contradicts previous choice | Keep a superseded record, then write the accepted current choice |
| Another session changed the file | Reread and scoped-merge, or stop on a real conflict |
| Planned work appears in a diff summary | Separate it from implemented and accepted work |

## Scope

Writing a log does not send messages, commit source or publish documentation. Optional Git
execution can follow existing authorization; the logging workflow itself uses only standard
read-only Git evidence and project Markdown.

## Install and source

Source collection: [norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
From the collection root, install this complete folder with the local installer:

```bash
python3 scripts/install.py --destination <project>/.claude/skills --skill norml-changelog
```

Replace `<project>` with the real project directory. The installer does not overwrite
existing packages by default, mutate runtime settings, fetch credentials or install dependencies.
See the collection README for verified installation/runtime scope. Provider and project
workflows in the skill are instructions; installation is not live-operation verification.

## Inside the installed package

- `SKILL.md` — Gather/log/reconcile procedure.
- `templates/changelog-format.md` — Entry examples and compression rules.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
