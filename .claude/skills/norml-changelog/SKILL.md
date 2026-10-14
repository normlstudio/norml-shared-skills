---
name: norml-changelog
version: 1.0.0
description: >
  Record verified development changes, architectural decisions and integrations in project Markdown. Use for log this, update changelog, record this decision, what changed, or session-end logging required by project instructions. Preserves decisions and security/breaking changes while compressing older routine entries.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml Changelog


Keep future developers and parallel sessions informed without relying on chat history.
This package operates local project Markdown and read-only Git evidence; it needs no service.

## 1. Gather verified changes

Resolve the project's existing changelog and architecture docs before creating alternatives.
Default to `docs/changelog.md` and `docs/target-architecture.md` only when no convention exists.
Read existing docs, relevant diff and recent log. For Git repositories use `git status`,
`git diff --stat`, `git diff` and `git log --oneline -10`; inspect actual commits rather than
assuming every recent author's work belongs to this session. Use a known baseline when
available; do not assume `HEAD~5` exists. Without Git, use supplied session evidence.

Separate implemented changes from approved decisions, discoveries and unfinished work.
Never mark a planned change as complete, invent acceptance, estimate effort, or publish secrets.

## 2. Write the changelog

Use [format and examples](templates/changelog-format.md). Merge into one section per date,
group changes by area, use past tense and explain non-obvious reasons. Tag architectural
choices `[DECISION]` and external dependencies `[INTEGRATION]`. Blend repeated repair rounds
into an accurate final-state entry while retaining important evidence/history.

When there are more than 50 date sections, compress routine entries older than 30 days into
Monday-to-Sunday weekly summaries, retaining at least the most recent 20 date sections in full.
Never compress away decisions, integration details, security fixes or breaking changes.
Reread the file immediately before updating so another session's newly written entry survives.
Use a scoped patch rather than replacing the whole file. Stop on concurrent conflicting edits.

## 3. Update current architecture

For a verified decision, read the target file and merge into its matching section.
Integrations record purpose, data owner, non-secret resource identity, sync direction,
supported method and added date. State whether it is connected/verified or only proposed.
Tool choices belong in the existing tooling section; data ownership in Data Sources;
conventions in Conventions; infrastructure/theme/content changes in their existing docs.

If a decision supersedes an earlier one, retain a dated Superseded note and rationale.
Do not silently overwrite history. Add an update marker using the project's established
format (default `Updated: Oct 13, 2026`, with the actual current date).

## 4. Update migration status when applicable

Read the existing migration map; update only affected components with verified state.
Keep incomplete/blocked statuses honest. Do not create a migration map for unrelated work.

## Edge cases and completion

If docs are absent, create a minimal changelog and architecture skeleton. If nothing changed
or was decided/discovered that future sessions need, skip logging. Do not send, commit or
publish simply because a log was written; follow the user's existing Git permissions.
Confirm which files changed and whether compression occurred. The full log stays in files.

Optional `norml-git` can handle commits; logging works independently through standard Git reads.
