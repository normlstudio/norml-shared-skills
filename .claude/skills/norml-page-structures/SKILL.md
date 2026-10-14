---
name: norml-page-structures
version: 1.0.0
description: >
  Norml's source-backed page structure catalog: one Markdown specification per
  page type, linked block specifications and screenshot-backed archetypes.
  Use for "our page structure", "what elements belong on this page", "blog
  single and archive templates", "check missing page elements", or before
  scaffolding a page or template with a known type. Preserves required,
  recommended, optional and conditional elements from the existing catalog.
  Build skills must load it before scaffolding and verify element coverage
  before declaring completion. WordPress primitives belong to
  WordPress architecture review; page.md/wireframe/admin/task orchestration belongs to
  page planning/build workflow; theme implementation belongs to WordPress development workflow or
  WordPress implementation workflow. This skill owns the page and block specifications.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml Page Structures

Use the existing catalog to determine what belongs on a page. Do not reconstruct
it from memory or from an index summary. The canonical source is this installed
package. It needs no external catalog, private repository or other skill.

## Required reading

1. Read [the catalog orientation](catalogs/readme.md) and
   [the page index](catalogs/pages.md). Select the matching page type and read
   its entire `catalogs/pages/{type}.md` file before scaffolding.
2. Read [the archetype index](catalogs/archetypes/readme.md). If a matching
   archetype exists, read its text specification. Reference screenshots are not
   bundled. Inspect images only when the user supplies or approves them; missing
   images do not block using the text contract and do not authorize client-asset reuse.
3. Read [the block index](catalogs/blocks.md), then the complete specification
   for every block referenced by the selected page type that is in scope.
   The page file's summary does not replace a block's detailed requirements.
4. For archive and single work, load both page specifications and their shared
   card/block specifications. For blog templates these are
   [blog post](catalogs/pages/blog-post.md),
   [blog archive](catalogs/pages/blog-archive.md) and the linked block files.

Load only the relevant files. Do not load the whole catalog for each build.
If the requested type has no specification, record that gap and use the explicit
project brief. Do not label a guessed structure as a catalog requirement.

## Select and preserve a block variant

Read [the variant contract](catalogs/variant-contract.md) when selecting a
block layout. Record its stable ID, source revision, selection reason, content
fit and responsive/interaction contract in the existing page coverage record.
If a legacy specification has only prose variations, preserve that evidence
and mark missing details unresolved; do not invent a variant manifest.

Structure and typed content slots are distinct from project-owned visual
tokens and target-specific code. Adapters may change tags/classes or required
framework nesting, but may not silently change slots, content types or
composition. A grayscale preview is not an approved client design.

## Structure coverage — before scaffolding and at completion

In the consuming workflow's existing page contract, task or QA record, account
for every element in the selected specification. Include the source section,
its requirement level and condition, its planned template/block and editing
source, and its final status with evidence. Reuse existing project artifacts;
this skill does not introduce a competing task system.

- Preserve **required**, **recommended**, **optional**, **off by default** and
  **conditional** exactly as the source states. An optional item inside a
  "Required structural elements" list remains optional. Evaluate source
  conditions rather than treating the list heading as an unconditional rule.
- The explicit project brief or recorded design decision may override a
  default. Record the affected element and the actual override. An existing
  incomplete implementation or missing data is not an override.
- If a page specification, block specification or archetype conflicts, record
  the conflicting source sections and obtain or reuse an explicit project
  decision. Do not silently resolve the conflict by inventing a new rule.
- Missing required content, an unavailable integration or an unreadable spec
  stays **unresolved**. Do not silently omit it, invent content, or substitute
  another block and claim the original requirement passed.
- Distinguish an implemented template slot from populated content and from a
  working integration. A hidden empty slot proves neither content completeness
  nor integration behavior. Report those states separately.
- At completion, compare the actual rendered page with the source-derived
  coverage record, including order, block details, mobile behavior and editor
  fields. For blog TOCs, also verify [the required-navigation contract](qa/toc-required.md).
  Missing required elements prevent a claim of structural completion.
  Conditional omissions need the condition and evidence; optional/recommended
  omissions need their disposition, not fabricated content.
- Verify the selected variant against [block-variant acceptance](qa/block-variants.md).
  Test actual runtime content, optional/long-content states, editor constraints,
  interaction and responsive composition. A wireframe render is not proof that
  generated target-system code works. Declared schema metadata is not emitted
  schema; inspect the actual output when a block requires structured data.

For blog posts, the table of contents is required regardless of word count or
number of headings. Read the blog page and TOC block specifications: desktop
navigation is on the left of the article, starting at the body. Choose and record
one of the two blog compositions: a centered TOC/article pair, or a left-edge TOC
with the article centered within the remaining pane. Verify the actual coordinates
and balanced outside space for the chosen mode. Mobile navigation collapses above
the left-aligned prose. An
unsectioned article uses one truthful body anchor rather than invented headings.
Do not introduce visibility thresholds or per-post opt-outs for this requirement.
Google Preferred Source eligibility remains a separate preflight gate. An ineligible publication's
dated evidence can justify suppressing its control; an unverified status cannot.

## Ownership and maintenance

- Page specifications: `catalogs/pages/`; block specifications:
  `catalogs/blocks/`; deep page references: `catalogs/archetypes/`.
- Follow the existing contribution sections in the catalog. Use traceable
  existing sources for changes; do not invent new page elements during a
  migration. Keep both indexes current and all relative links resolvable.
- Update this skill's semantic version and `changelog.md` when its catalog
  changes. Reconcile its guides through `human documentation maintenance` and publish through
  `project Git workflow`; keep structural knowledge here rather than in a Drive copy or
  duplicated inside consuming skills.
- Project content, brand tokens, claims and credentials stay in their existing
  project homes. Reference screenshots describe composition; they are not
  reusable client content or approved brand assets.

## Optional companions

`norml-page-types` helps select destination families; `norml-wp-architecture`
helps map them to WordPress primitives; `norml-wp-developer` can implement them.
They are optional. With this package alone, read the user's brief and existing
CMS/build contracts, record structural coverage, and hand it to their developer.

## Public boundary

Screenshots and client assets are not bundled. The team-member archetype retains
its portable field/layout contract; inspect the user's approved assets instead.
Catalog defaults are authored recommendations, not universal SEO requirements.
Do not invent proof, contacts, prices, deadlines, branding or missing content.
