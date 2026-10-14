# Naming, ownership and storage

Resolve `{skill-root}` to the canonical installed package, `{source-repo}` to its actual owner,
`{project-root}` to context/data, and `{runtime-root}` to the user’s selected runtime skill directory.
These are independent anchors. Quote resolved paths containing spaces; never use arbitrary cwd.

## Placement

| Audience | Canonical source | Boundary |
|---|---|---|
| Reusable across projects | Existing user-owned collection | Generic method, no client facts |
| Internal organization | Its authorized private source repository | Access-restricted process |
| Client-specific | Its authorized private client collection | Verified client prefix and scope |
| Product-local | Existing product repository | Project-scoped discovery by default |
| Public/shareable | Separate sanitized package/collection | No private source dependencies |

Reuse the verified owner. No company slug, organization host or mandatory repository per category
is required. New repository creation needs authority; existing visibility remains unchanged.
Sharing and installation are separate decisions. One client collection can contain several related
skills; splitting it per capability is rarely needed without a reason.

Skill slugs match `^[a-z0-9]+(?:-[a-z0-9]+)*$`; folder name equals frontmatter `name`.
Check installed names and target directories before registration. Existing valid identities are
preserved unless a rename is requested. Prefix client/product names when needed to avoid ambiguity.
For Norml-branded public editions, use `norml-` and credit `Norml Studio`; this is branding only.

Markdown basenames use lowercase kebab-case, with reserved `SKILL.md` and existing canonical
runtime instruction filenames retaining required casing. No `[`, `]` or `|` in Markdown basenames.
Use verb-led procedure names and descriptive nouns for contracts. Exact upstream-required casing
stays in explicitly tool-owned namespaces. Package folder changes do not rename project data paths.

Secrets/auth state never belong in either a package or project prose. Use protected credential
stores/provider-supported auth with reference-only local settings. Current people/client data,
reports and screenshots stay at the verified data owner, outside reusable distribution.
