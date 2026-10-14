---
name: norml-wp-developer
version: 1.0.0
description: >
  Develop WordPress themes through two paths: new Sage/Acorn/Blade/Tailwind/Vite projects and inherited themes that retain their existing stack. Includes content-model pre-check, section/component separation, ACF block previews, three-layer CSS, Git/CI review gates and code-versus-data deployment rules. Use for new themes, inherited WordPress work, blocks/components/templates, WP CI/CD or staging-to-production engineering.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml WordPress Developer


Build within the project's verified architecture. This public package contains its own
engineering standards; no private skill, shared drive, company account or bootstrap is needed.
All sample commands are project-adapted patterns, not an executed installer/deployer.

## Scope and preflight

Read project instructions, existing architecture and deployment policy. Find the actual
code repository/root, theme, WordPress root, builder, dependency versions/lockfiles,
registered types/taxonomies, ACF registration style and current editing workflow.
No exact target or access evidence means read-only research, not invented operations.

Keep tooling/context inside the actual repository (usually the active custom/child theme).
A Local WP installation directory is not automatically the source repository. Do not scatter
new tool folders outside the project or create a second maintained instruction copy.
Authentication uses supported provider flows and the OS protected credential store;
CI uses protected environment secrets. Never commit/print secrets, database dumps or auth state.
Prefer API/CLI for services; a disconnected connector grants no browser authority.

### Content-model pre-check

Decide the WordPress primitive before scaffolding:

- A true singleton → Page; chronological editorial content → Post.
- A distinct repeatable collection → CPT, with deliberately selected archive/single behavior.
- A shared filter/browse vocabulary → taxonomy; displayed attribute → typed custom field.
- Site-wide singleton values → options; reusable layout → patterns/components.
- Persistent behavior/model registration → plugin; presentation → theme/child theme.

Read existing registrations before creating parallel models. Explain a wrong-primitive
tradeoff and resolve it before building; honor an already agreed architecture or deliberate
override. Record routes, fields, ownership and permalink flush requirements.
Optional `norml-wp-architecture` supplies a deeper specification; these baseline decisions
remain usable independently.

### Choose project mode

1. **Inherited/non-Sage/uncertain:** read [inherited projects](standards/inherited-projects.md)
   first. Match existing layout, compiler, templating, ACF/native block style and editor.
   No silent Sage/Blade/Vite/Tailwind/Alpine or builder migration.
2. **New or already Sage-based:** read [Sage foundation](standards/sage-framework.md),
   [theme architecture](standards/theme-architecture.md) and
   [file structure](standards/file-structure.md). Verify supported stable versions from
   official framework docs and existing manifests before installation. The examples are
   a Sage 11/Acorn 5/Tailwind 4 baseline, not a promise that latest versions are compatible.

## Task routing

| Work | Read before editing |
|---|---|
| Sage bootstrap, templates and assets | [Sage framework](standards/sage-framework.md), [theme architecture](standards/theme-architecture.md) |
| Create a Sage file | [File structure](standards/file-structure.md) |
| Sections/Blade components/Alpine | [Component system](standards/component-system.md) |
| Native or ACF blocks and previews | [Blocks](standards/acf-blocks.md), inherited project's actual registration style |
| Tokens, responsive rules and block CSS | [CSS system](standards/css-design-system.md) and inherited guide §7 |
| JavaScript behavior | [JavaScript](standards/javascript-architecture.md) |
| Vite/environment setup | [Assets](standards/asset-pipeline.md), [setup](standards/environment-setup.md) |
| PRs/release tags | [Git workflow](standards/git-workflow.md) |
| CI/package/deploy/rollback | [CI/CD](standards/ci-cd.md) and project deployment contract |
| Acceptance | [QA gates](standards/qa-gates.md), [antipattern catalog](standards/antipatterns/readme.md) |
| Data refresh/code-versus-content | [Staging/production](standards/staging-to-production.md) |

Read only relevant standards but in full before their operation. Preserve the approved page
composition and conditional requirements. Record required element → implementation → editing
source → rendered evidence. Missing content/integration, a hidden empty slot or a substitute
CTA is unresolved. An optional `norml-page-structures` package can supply composition;
without it use the user's approved page specification, never an invented private catalog.

## Authoring rules

### PHP and templates

For Sage use Composer PSR-4 namespaces, boot-only `functions.php`, Blade layouts/sections
and typed props. In inherited themes match current includes and pass component arguments
through `get_template_part(..., null, $args)` when supported. Sections fetch content;
components receive data; loop partials compose posts. Escape every output in context,
sanitize input and verify capability/nonces for mutating endpoints. Avoid unbounded queries,
queries per card and synchronous provider calls while rendering.

ACF field reads use explicit safe empty/default values. Do not invent production copy or
hide a required section because input is missing. Missing ACF/plugin APIs fail gracefully
and become explicit editor/verification blockers when they are required.

### Blocks/editor

Use the project's existing native `block.json` or ACF registration mechanism. For new ACF
work prefer supported metadata registration; retain legacy PHP callbacks where that is the
project's established compatible route. Each block has a dedicated render file, accessible
editor-facing title/category, supported anchor and preview. Live examples use realistic
sample data in an explicit preview-only branch; heavy/API-backed blocks may use a scoped
screenshot fallback. No invented example claims on live pages. Match editor styles to frontend.

ACF local JSON versions definitions, not values. Match existing key conventions. Put durable
CPT/taxonomy registration in a site-core plugin when content should survive a theme switch;
choose theme-bound ACF registration only with its dependency/portability tradeoff recorded.

### CSS and responsive behavior

Use tokens → globally shared components → layout for an individual block. Audit shared
components before adding a new rule. No per-page shadow design system, hex palette or
font overrides inside block layouts, and no bespoke parallel button styling. Apply
[CSS system](standards/css-design-system.md). Inherited BEM/SCSS keeps flat component names,
semantic tokens, bounded nesting and `@use`/`@forward`; do not bolt in utilities by stealth.

The approved project design controls actual spacing/type/container values. When no design
contract exists, define the relevant choices before visual implementation. Verify 375,
768, 1024, 1440 and 1900 pixel widths; check overflow, stacking, readable type and keyboard/focus.

### JavaScript, links and media

Sage examples use Alpine; inherited themes retain their existing framework. Keep modules
scoped and imported once, pass data safely (`@js` in Blade), destroy event/widget state when
needed, honor reduced motion and maintain keyboard/focus/ARIA state. Install sliders or
animation libraries only when the feature needs them and existing approvals cover them.

Internal links keep same-tab navigation. External new-tab behavior follows project UX;
when using `_blank`, add `rel="noopener noreferrer"`. Determine host from `home_url()`,
normalize relative links, and do not apply `_blank` to `mailto:`/`tel:`. AReusable button
must not hardcode all links as external. Use responsive WP attachment images, meaningful alt,
dimensions/aspect ratio, and non-lazy LCP images; static assets go through the verified manifest.

## Common implementation loops

### Section/component

1. Confirm model and approved element coverage; inspect existing reusable pieces.
2. Create section under the actual section folder; fetch/normalize content at its boundary.
3. Pass props/arguments to reusable components; compose tokens/shared styles and layout.
4. Add one scoped JS module only for needed behavior, import through the existing entry.
5. Verify editor/content behavior and responsive interactions before completion.

### New ACF block

1. Discover active ACF/version and registration style; read the bundled block guide.
2. Register block metadata/callback and create a dedicated render file.
3. Define typed editor fields using the existing JSON/PHP/admin workflow.
4. Add live example data or a maintained screenshot fallback, with correct frontend/editor CSS.
5. Save/reload fields, render actual content, exercise interactions and review blank/error states.

## Engineering pipeline

Use the project's existing pipeline. For a new serious project the default is GitHub Flow:
short-lived branches → reviewed PR → passing CI → staging → approved immutable production
release. The actual integration branch is discovered, not guessed. Tag only an accepted
revision. Publish/stage only owned files; preserve unrelated WIP and server-side drift.

Read the project deployment contract before any deploy. Optional `norml-ci-cd` can prepare
that policy, but [CI/CD](standards/ci-cd.md) includes the necessary full pipeline locally.
Keep PR validation, staging deployment and protected production release as separate jobs.
Build from lockfiles; retain runtime Blade templates and production Composer dependencies.
Use atomic release activation where supported; record exact target/revision and rollback.

Code/schema flows toward production. Live content/field values flow to isolated staging
for testing. Refresh must disable outgoing mail, real billing, webhooks and scheduled jobs
before copied state can trigger them. No full staging DB replacement of ongoing live data.
Backups and rollback are distinct for code, database and media.

## Completion evidence

Run relevant checks from the three QA gates, plus every bundled antipattern detector.
Record PASS/FAIL/WAIVED with technically grounded reason and actual evidence; unresolved
failures block completion. UI work needs actual rendered states and interaction checks,
not HTTP status alone. Do not automatically submit email/payment forms in production.
Report implemented versus deployed versus verified status accurately, source revision,
changed paths, evidence and material limitations. Optional sibling performance/changelog
packages can help; local measurement and dated project logging suffice independently.
