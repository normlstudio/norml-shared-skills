# Norml WordPress Developer

> Build WordPress themes with explicit content architecture, reusable components, editor previews
and verified releases.

## The problem

A new stack needs a coherent authoring and release workflow. An inherited theme needs changes that
respect its existing architecture.

The package supplies both paths and separates code/schema deployment from live content ownership.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Create a new WordPress theme | *"Create a new WordPress theme"* |
| Work on this inherited non-Sage theme | *"Work on this inherited non-Sage theme"* |
| Add a block with an editor preview | *"Add a block with an editor preview"* |
| Build a reusable Blade component | *"Build a reusable Blade component"* |
| Review the CSS architecture | *"Review the CSS architecture"* |
| Set up WordPress CI and staging-to-production gates | *"Set up WordPress CI and staging-to-production gates"* |

## A typical run

1. Ask to add an editor-facing benefits block to the supplied inherited theme.
2. The agent reads project instructions, discovers current rendering/compiler/ACF style and resolves
its content-model role.
3. It creates a section in the existing folder, passes data into components, registers the block in
the current compatible mechanism and adds preview data.
4. It composes existing CSS tokens/components, verifies editor save/read-back and frontend behavior
at relevant widths.
5. It records implemented versus deployed status; an approved release follows exact-source CI,
backup and live verification gates.

---

## Inputs and outputs

Provide repository, requested change, existing page/content requirements, design rules, authorized
environments and access scope. The package reads existing project instructions and source before
editing. The output can include PHP/Blade/native or ACF blocks, components, styles/modules,
versioned schema and release policy changes. Actual changes depend on the user's request.

The package is not a stock theme ZIP. Its source files are operating guidance. It does not
bundle WordPress, PHP, Composer, Node, Roots Sage or an ACF PRO license.

## First decide the content model

A one-off Page, chronological Post and repeatable CPT solve different content needs.
Shared filter vocabulary is a taxonomy; a displayed value is a typed field; site-wide settings
are options. Persistent model/functionality generally belongs in a plugin, presentation in a theme.
Read existing registrations first. A required archive/single relationship cannot be passed by
creating several unrelated Pages. Knowing project/user overrides remain valid and are recorded.

Optional `norml-wp-architecture` expands this pre-check. It is not an installation prerequisite;
the core model decisions are included in `SKILL.md`.

## New Sage path

Read `standards/sage-framework.md`, then the relevant architecture/file/component guides.
The source baseline uses Sage 11, Acorn 5, Blade, Tailwind 4, Vite and an explicit Alpine choice.
Check the current official compatibility and project lockfiles before selecting versions.
Use stable/pinned compatible versions; development branches are not the default.

- `functions.php` boots autoload/container and topic files; it is not the feature drawer.
- PHP uses Composer PSR-4 `App` namespaces and the actual supported PHP version.
- Blade hierarchy views extend the base layout; reusable components receive explicit props.
- Source assets use the verified build entries and manifest, never hand-edited generated assets.
- Runtime Blade files and production Composer dependencies remain in the deploy artifact.
- ACF is optional to the framework and required only when the feature uses licensed ACF APIs.

A new compatible scaffold can begin with `composer create-project roots/sage {theme-slug}`.
Run it only in a verified authorized theme directory. The project handles activation and runtime
config separately; installing this skill does not execute that command.

## Inherited path

Read `standards/inherited-projects.md` first. Inventory entry/bootstrap, template parts, compiler,
ACF/native block style, editor/builder, registrations and existing design tokens.
Default to inherited behavior when uncertain. Match current directories and naming.
Do not add Sage/Blade/Vite/Tailwind/Alpine, swap ACF/native blocks or remove a builder silently.

A requested refactor is separate from an incidental feature. Its phases are snapshot/recovery,
parity implementation, controlled cutover/QA and removal of old paths. Preserve accepted behavior
before redesigning anything. Record deferred debt instead of claiming cleanup was accepted.

## Template data boundaries

| Layer | Responsibility | Typical place |
|---|---|---|
| Section | Fetch/normalize content and compose the page block | Sage `resources/views/sections/` or existing PHP section folder |
| Component | Render reusable UI from explicit arguments | Blade components or inherited template components |
| Loop partial | Render WordPress loop content | Existing `partials/` or `template-parts/` |

In vanilla WordPress use the supported template-part argument mechanism. In Blade declare
props and safe serialization. A component should not read arbitrary page ACF data itself.
Keep escaping/sanitization/capability/nonce requirements at the right input/output boundary.

## Blocks and previews

Read `standards/acf-blocks.md` before registering a block. New compatible ACF work can use
metadata registration. Inherited projects retain their existing legacy callback style unless
a migration is authorized. Native Gutenberg stays native when that is the established path.

Each block has a dedicated render file and a useful editor category/title/anchor.
Live example data sits in an explicit preview-only branch. Heavy/API-backed blocks may use
a current scoped screenshot fallback; a registered `acf/name` string must not become an unsafe
file path. Example data never substitutes for missing required production content.

Confirm block discovery, insertion, field edit/save/reload, JSON loading/sync when used,
frontend rendering and editor style parity. Empty data/error cases remain visible blockers
when content is required. Discover CLI extensions rather than assuming `wp acf sync` exists.

## CSS system

Use tokens → shared global components → individual block layout. Audit components before
writing CSS. Reuse the site's buttons/fonts/palette instead of importing a mockup's parallel system.
A unique composition gets block layout; it does not justify a whole per-page visual vocabulary.

Inherited BEM/SCSS retains flat component naming, semantic tokens, shallow nesting and modern
module conventions within its existing compiler. New Sage may express the same layers through
Tailwind `@theme` and `@layer components` plus utilities.

Conditional CSS discovery must cover actual nested/synced/template/archive block routes.
`has_block()` on the current post alone is not proof that all rendered blocks were discovered.
Use supported metadata/enqueue mechanisms and verify editor/front-end behavior.

## Responsive and accessibility acceptance

The approved project design controls real gutter/type/container values. Don't force a new
universal palette or width into an inherited project. Resolve missing design choices first.
Test 375, 768, 1024, 1440 and 1900 pixels and feature-specific widths when relevant.

Check overflow, stacking/order, readable type, image dimensions, focus/keyboard behavior,
ARIA state, touch targets, contrast, reduced motion and print when applicable. Suppressing
horizontal overflow is not a repair when the child layout remains broken.

## JavaScript, media and links

Keep one module per needed behavior and the existing import pipeline. For Alpine, register
data before starting one instance; pass PHP values safely and preserve cleanup/lifecycle.
Don't install slider/animation frameworks because the package mentions them.

Use WordPress responsive attachment APIs where appropriate, explicit dimensions/aspect ratio
and meaningful alt. Do not lazy-load the main LCP image. Static asset helpers/custom components
must actually exist in the project or be implemented; stock Sage does not guarantee them.

Internal links preserve same-tab history. External new-tab behavior follows approved UX;
`_blank` needs safe relationship attributes. Normalize hosts relative to `home_url()` and
keep `mailto:`/`tel:` from receiving blanket new-tab behavior.

## Git and review

Use the actual integration branch and project ownership rules. The new serious-project baseline
is GitHub Flow with short feature branches and a reviewed green integration branch.
Commits use Conventional Commits and explain rationale; stage only this change's paths.
Preserve unrelated WIP and server drift. Tags identify accepted immutable source revisions.
Do not move published tags or bypass a protected review environment.

Optional `norml-git` can execute the Git workflow. Standard Git guidance is included here.

## CI and artifacts

`standards/ci-cd.md` describes PR validation, staging and protected production jobs.
PR lint/tests need development tools installed; final runtime artifacts use production-only
Composer dependencies. Build from lockfiles. Keep runtime templates, production vendor and
built manifest/assets. Exclude Git/node_modules/tests/secrets/dumps/uploads/local cache state.

Use a verified atomic release mechanism when supported. Check SSH identity, reviewed targets,
deployment concurrency, artifact checksums and exact source revision. Broad content/root
rsync and silent deletion are prohibited. Code rollback is separate from DB/media recovery.
A deployment policy helper is optional; the necessary rules remain in this package.

## Code versus data

Code and field definitions flow toward production. Production content/field values may refresh
isolated staging. Before copying, disable outgoing mail, live payment, webhooks and jobs.
Minimize personal data and retain snapshots privately under the project's recovery policy.
Don't treat WordPress core as a dependency of every Sage theme; inspect the actual installation.

No routine full staging database replacement after launch. Exact selective migrations need
record/field/relationship mapping, conflict handling and protected-state verification.
A WXR import may duplicate records and shared `wp_posts` tables are never a one-CPT slice.

## Three QA gates

| Gate | Proof |
|---|---|
| Pre-merge | Configured checks, build/relevant tests, secret scan and independent review |
| Pre-deploy | Staging render/interaction/editor/performance evidence and approved scope |
| Post-deploy | Changed live routes, assets, content integrity, environment/indexing and source parity |

Run the antipattern catalog too. Record PASS/FAIL/WAIVED with actual detector output and a
technical waiver rationale. No silent unresolved failures. Do not submit real email/payment
forms during production QA without specific test authorization and cleanup.

## When something breaks

| Finding | First response |
|---|---|
| Manifest absent | Run the existing supported build and inspect actual manifest config |
| ACF fields missing | Inspect local JSON/PHP definition, keys, plugin state and supported sync |
| Editor preview wrong | Check preview flag, assets/iframe context and data return format |
| Stale Blade view | Use supported cache clear then view-cache commands on the verified target |
| Unexplained live files | Stop overwrite and reconcile production drift |
| Deploy lost content | Treat as data incident; code rollback alone is insufficient |
| Existing framework cannot support task | Propose a separately scoped refactor instead of adding a second stack |

## Honest completion

Report implemented, deployed and verified states separately. Include changed paths, exact source
revision, meaningful test evidence and remaining limits. Runtime workflows in this package are
instructions, not a claim that every host/CI/version combination has been live-tested.

## Install and source

Source collection: [norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
From the collection root, install this complete folder with the local installer:

```bash
python3 scripts/install.py --destination <project>/.claude/skills --skill norml-wp-developer
```

Replace `<project>` with the real project directory. The installer does not overwrite
existing packages by default, mutate runtime settings, fetch credentials or install dependencies.
See the collection README for verified installation/runtime scope. Provider and project
workflows in the skill are instructions; installation is not live-operation verification.

## Inside the installed package

- `SKILL.md` — Two-path developer router.
- `standards/inherited-projects.md` — Respect/refactor decisions and framework-independent patterns.
- `standards/sage-framework.md` — Sage/Acorn/Blade/Vite foundation.
- `standards/acf-blocks.md` — Metadata and legacy blocks with preview acceptance.
- `standards/css-design-system.md` — Tokens/components/block layout and responsive checks.
- `standards/ci-cd.md` — Standalone release, artifact and rollback procedure.
- `standards/qa-gates.md` — Pre-merge, pre-deploy and post-deploy checks.
- `standards/antipatterns/` — Auditable implementation bans and fixes.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
