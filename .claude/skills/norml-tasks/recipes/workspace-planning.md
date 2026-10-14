# General planning in a user-configured workspace

1. Resolve the authorized project/area directory and read its context/instructions.
2. Use [location discovery](../standards/layering.md) to find all known counterpart planning.
3. Initialize `.claude/tasks/` only when none owns the same scope. Use schema version 3,
   `storage: workspace`, a verified `locations.workspace` map, `commit_docs: false`, and
   `github.enabled: false`. See [workspace definition](../schemas/planning-workspace.md).
4. Capture/prioritize through [the capture recipe](capture-and-prioritize.md). Larger initiatives
   use the same milestone/phase method as repository work; acceptance fits the actual artifact.
5. Link implementation outcomes in their code repository; never duplicate their editable task.
6. Update canonical task, index and resume state; run integrity checks and report coverage.

Filesystem Markdown/JSON is sufficient; no cloud account or company folder tree is required.
For native externally hosted artifacts, retain authorized IDs/links rather than inventing a
second content master. This recipe sends no messages or remote tracker writes implicitly.
