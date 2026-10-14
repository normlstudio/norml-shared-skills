# Skill package anatomy

Keep one runtime entry point and descriptive support folders:

```text
{collection}/.claude/skills/{slug}/
├── SKILL.md
├── changelog.md
├── readme.md
└── {semantic folders only when useful}/
```

`SKILL.md` frontmatter includes matching `name`, semantic `version` and grounded `description`
with real triggers and disambiguation. New editions start at 1.0.0; updates retain history and
use patch/minor/major according to compatibility, not file count. The body routes purpose,
inputs, procedures, outputs/effects, validation and hard stops. Link required files from the
exact consuming step; a procedure unreachable from the router is not discoverable behavior.

## Folder roles

| Folder | Contents |
|---|---|
| `recipes/` | Bounded selectable procedures |
| `processes/` | Ordered composed workflows |
| `actions/` | Single action runbooks |
| `modes/` | Policies controlling autonomy |
| `standards/` | Rules/decision criteria |
| `schemas/` | Record/interface definitions |
| `templates/` | Concrete output templates |
| `providers/` | Provider-specific adapters |
| `catalogs/` | Named inventories |
| `examples/` | Sanitized fictional fixtures |
| `qa/` | Acceptance/regression contracts |
| `scripts/` | Executable deterministic helpers |
| `renderer/` | Optional included documentation renderer |
| `research/` | Source-backed static background |

Create only populated folders that accurately describe their contents. Avoid `references/`,
`reference/`, `knowledge/`, `supporting-material/`, `playbooks/`, `workflows/`, `docs/`, `misc/`,
`other/`, `notes/`, `files/` as skill drawers. Project context and `.github/workflows/` are different
namespaces. Do not manufacture empty structure or pad atomic skills with unnecessary support files.

A collection root lists actual packages, boundaries, license and validation/install procedures.
Keep existing canonical project instructions; never create competing maintained runtime copies.
Ignore credentials, auth sessions, caches, live datasets and generated operational logs.

Human docs derive from the actual source, with useful first-run inputs, outputs and honest limits.
If HTML is wanted, include/reuse an available deterministic renderer with its real inputs; do not
claim a renderer or private documentation skill exists. This creator works with Markdown alone.
A missing requested HTML surface remains pending, not a reason to invent a tool dependency.

Per-person onboarding, if needed, has Why, Prerequisites, Steps, Verification, Troubleshooting,
and Rotation/revoke. Use supported provider auth. Scaffold-only can identify missing content,
but cannot claim operational readiness. Runtime installation is separate opt-in work.
