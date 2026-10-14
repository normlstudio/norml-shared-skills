# Task record — required fields and sections

Defines a single canonical task under `{owner}/.claude/tasks/items/`. This is a
contract for creating task records from real input, not a blank task to copy.
A [filled task example](../examples/organizing-a-thought-dump.md#resulting-task-file)
shows the result in context.

## Identity and location

Filename: `task-nnn-describe-action.md`. Its number matches the stable
`TASK-NNN` ID; the owner config supplies the namespace. Reordering and completion
do not change identity. Fully qualified cross-owner refs use `owner-id::TASK-NNN`.

## Metadata

Use flat YAML frontmatter between `---` lines. Values must be JSON literals:
quoted strings, numeric rank, JSON arrays, `null`. No multiline/nested YAML.
All fields below must be present; optional links use null or an empty array.

| Field | Type | Meaning / constraints |
|---|---|---|
| `id` | string | `TASK-001` or next unused owner-wide ID |
| `title` | string | Concrete action, not an abstract topic |
| `status` | string | open / in-progress / blocked / done / canceled |
| `queue` | string | now / next / someday / blocked / done |
| `priority` | string | P0 / P1 / P2 / P3; definitions in the priority standard |
| `rank` | positive integer | Order inside its queue, with a prose reason |
| `goals` | string array | Existing local or qualified goal IDs; empty when not yet grounded |
| `depends_on` | string array | Real task prerequisites, local or qualified; empty for none |
| `milestone` | string or null | Existing milestone folder slug |
| `plan` | string or null | Existing phase-plan ID such as 01-01; requires a milestone |
| `issue` | string or null | Verified full GitHub issue URL in this owner's repository |

Blocked status and blocked queue go together. Done/canceled use Done queue.
In-progress requires Now. Tasks in Now must have satisfied local prerequisites;
external prerequisites require separate current evidence. Cancellation does not
satisfy a dependency. An issue URL is identity, not proof of completion.

## Required prose sections

Use these H2 names so the validator can check structure. Fill them with actual
context. For a tiny task, a sentence per section is enough; never pad with generic
steps. None/not yet is honest for unavailable evidence, not for known requirements.

| Heading | Question the content answers |
|---|---|
| Outcome | What will become true, and why does it matter? |
| Source | Clickable original-request/archive pointer, original language and author/date; preserve all later correction sources. Which decisions are accepted? |
| Scope | Which behavior/artifacts/paths are included and excluded? |
| Acceptance | What observable checks determine done? Include merge/deploy only if required. |
| Steps | What concrete actions, in order, should the next session take? |
| Priority reason | Why this queue and rank, relative to the current goal/dependencies? |
| Blocker | What exact condition prevents progress, or None? |
| Next action | What is the first executable step now? |
| Evidence | What was actually checked, with result/pointer, or Not yet? |
| Execution claim | Which worker/branch owns execution, or None? |
| Decisions and changes | What changed in scope/priority; cancellation reason; old IDs if imported? |

New or materially amended records also include `## Suggested skills`, following
[skill selection](../standards/skill-selection.md). Record candidate names, reasons
and use conditions; the set is provisional. Older records need no bulk backfill.

Acceptance starts unchecked until evidence exists. Steps describe the task's
execution, not the whole project's roadmap. Time/effort/cost forecasts require
a separately authorized evidence-backed estimation workflow; preserve source figures without inventing new ones.

## Related definitions

- [Planning workspace](planning-workspace.md) — owner config, goals and index.
- [Planning model](../standards/planning-model.md) — lifecycle and authority.
- [Prioritization](../standards/prioritization.md) — selection and ordering.
- [Issue mirror](../standards/github-mirroring.md) — remote identity/reconciliation.

Source records follow [source provenance](../standards/source-provenance.md). A refined task, source label without a link, or inaccessible chat-memory reference is not the original request. Legacy sources must be marked unavailable when unrecoverable; never reconstruct invented verbatim text.
