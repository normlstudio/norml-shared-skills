# Locate the planning owner and mapped surfaces

Resolve the user’s configured workspace root and named project/area. Read its existing context
and applicable agent instructions. Code belongs in the actual repository, often a custom theme
or plugin rather than the full CMS installation. General coordination belongs in its established
workspace. Never infer ownership from cwd, one matching folder name or a company taxonomy.

1. Look for existing `.claude/tasks/config.json` and any active `.planning/` system.
2. Read its verified `locations.workspace` and `locations.repositories` maps. Resolve each
   portable workspace-relative or repo-relative path against the user’s local configured root.
3. Inspect all declared counterparts before creating new task state. Bound searches to approved
   roots; verify project context and repository remote. Missing access remains unresolved.
4. Record stable project/owner IDs; the map links stores without duplicating task bodies.
5. Workspace-wide list/next/resume reads each mapped index, follows cross-owner dependencies and
   reports coverage. Unread stores are never silently treated as having no tasks.

For a single standalone workspace, its own location may be `.claude/tasks` relative to the chosen
project root. Another workspace path is relative to the same user-configured workspace anchor.
A repository location carries its repo-relative `planning_path`; the hosted `owner/repository`
identity is optional for local-only planning and required when GitHub mirroring is enabled.
Do not commit machine-specific absolute paths, secret configuration or a global mutable registry.

Split outcomes across owners, not copies: a design approval task can precede a repository
implementation task through `coordination-owner::TASK-001`. The coordinator does not repeat
implementation steps/status. An unavailable true owner leaves a preserved unresolved capture;
it does not justify a falsely canonical replacement backlog. Keep source and runtime artifacts
separate from the reusable installed skill package.
