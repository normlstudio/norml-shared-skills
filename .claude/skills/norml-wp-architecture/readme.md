# Norml WordPress Architecture

> Choose the WordPress content model, routes and registration ownership before implementation.

## The problem

A repeatable collection built as separate Pages loses automatic archives, filters and a reusable
layout.

The package distinguishes content identity, classification, structured attributes and presentation
before a builder creates the wrong primitive.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Should this be a custom post type or a page | *"Should this be a custom post type or a page"* |
| Do we need a taxonomy | *"Do we need a taxonomy"* |
| Plan the case-study archive and single URLs | *"Plan the case-study archive and single URLs"* |
| Where should this code live | *"Where should this code live"* |
| Audit the inherited WordPress content model | *"Audit the inherited WordPress content model"* |
| Map this model to Elementor or Sage | *"Map this model to Elementor or Sage"* |

## A typical run

1. Ask whether a supplied group of case studies should be Pages or a collection.
2. The agent reads the existing model, recommends a `case_study` CPT and a reusable `industry`
taxonomy only if filtering/browse values justify it.
3. It records archive/single routes, fields and registration ownership, checks collisions and adds a
one-time permalink-flush note.
4. It hands the spec to the existing builder workflow; no production model or layout is changed.

---

## Inputs and outputs

Provide the content nouns, whether they repeat, listing/filter needs, expected URLs, builder
and existing registration evidence. The pre-check is framework-neutral and can run without
project bootstrap files. If authorized, `wp post-type list` and `wp taxonomy list` read the
verified installation; supplied registration code is also evidence. Unchecked live state is
labelled.

The output is a short architecture specification using `templates/architecture-spec.md`.
It contains primitives, taxonomies, fields, routing, ownership, dependencies and unresolved
decisions.

## Content-model decisions

| Content shape | Usual primitive | Question to resolve |
|---|---|---|
| One About/Contact/Pricing page | Page | Is it genuinely a singleton? |
| Blog/news/editorial feed | Post | Does chronological editorial behavior fit? |
| Distinct repeatable collection | CPT | Does it need public listings or detail routes? |
| Shared reusable filter values | Taxonomy | Is the vocabulary browsable/managed? |
| An item's displayed attribute | Custom field | Does it need classification or just display? |
| Global CTA/footer/contact defaults | Options | Who edits the singleton source? |
| Repeated layout chunk | Pattern/component | Is this presentation reuse rather than content identity? |

A CPT can be composed inside pages without a public archive. `has_archive=false` does not
alone disable public singles; decide public/queryable behavior deliberately for testimonial/team
collections that should not expose standalone pages. Typed fields also require return-format
and relationship decisions for the eventual builder.

## Classification versus attributes

Use a taxonomy for repeated shared terms, filtering or term archives. Choose hierarchical
terms for controlled/nested vocabularies and flat terms for open-ended labels. Do not create
one term per unique attribute simply to display it. ACF/select/text fields suit display values;
relationship/post-object fields point to independently managed content.

## Routes and templates

WordPress routes URLs into queries, then selects the first supported template in its hierarchy.
The package explains CPT archive/single, page, taxonomy/category/tag, index and 404 slots.
The published URL base differs from an internal post-type identifier: for example `case_study`
may use `/case-studies/`. Record both explicitly.

A Page at a CPT archive's same base can collide. Decide which route owns that base or use an
independent controlling page whose content the archive template reads. New registration/rewrite
changes require a deliberate one-time flush, not `flush_rewrite_rules()` on every request.
Preserve existing live URLs and plan redirects when the accepted model changes them.

## Registration ownership

Functionality that must outlive a visual theme usually belongs in a site-core plugin.
Presentation lives in the theme. A child theme protects changes to an updated third-party
parent. A custom theme without a third-party parent does not need a child merely by convention.
A must-use plugin suits intentionally always-on behavior but needs explicit maintenance ownership.

ACF JSON in a theme is an accepted convenience only when its coupling is recorded. Definitions,
loaders and persisted registrations may have different ownership; test actual ACF version/storage
behavior rather than claiming a theme switch always makes every ACF-created CPT disappear.
Long-lived content and future re-theming usually justify independent registration ownership.

## Builder-neutral handoff

| Builder | Spec-to-render path |
|---|---|
| Sage/Blade | Archive/single Blade views with dynamic item data and reusable components |
| Vanilla Gutenberg/ACF | PHP hierarchy templates and registered blocks/template parts |
| Elementor | Theme templates assigned to the content type; dynamic field binding |
| Divi | Theme Builder templates for the collection; dynamic content |

The builder does not change whether an item is a CPT or a field. A block is layout; a CPT
is independent content. An archive block may query CPT items, and a CPT single may contain blocks.
The package specifies this relationship but does not implement it or choose CSS values.

## Common scenarios

### Services with shared layouts

Confirm whether this is one campaign landing page or several durable offerings. For a collection,
select a service CPT and one single/archive system; add classification only for real filtering.
An intentionally one-off Page remains valid, with the override recorded.

### Team members used in several sections

A managed reusable CPT may fit better than duplicating repeater rows. Specify whether public
single/archives exist. A small one-location group with no independent detail can remain a repeater.

### Inherited builder content

Read existing types, taxonomy relationships and URL shape. Extend the current model rather than
creating a parallel collection. If a migration is needed, hand off an explicitly scoped plan;
architecture advice is not migration execution or destructive-data approval.

## When something breaks

| Finding | Response |
|---|---|
| New CPT URLs 404 | Verify registration and approved one-time rewrite flush |
| Archive base conflicts with a Page | Resolve route ownership before implementation |
| User wants a different primitive | Record the knowing tradeoff and proceed within that choice |
| Existing taxonomy does the job | Extend it instead of creating a duplicate |
| ACF ownership is unclear | Verify loader/schema/persisted registration behavior |
| Builder hardcodes each item | Bind one shared template to dynamic item fields |

## Scope and optional handoffs

The installed package contains all decision references. Optional `norml-wp-developer` implements
accepted specs, and optional page-structure packages can supply composition. Without them use
the existing build process and approved page specification. No private catalog is required.

## Install and source

Source collection: [norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
From the collection root, install this complete folder with the local installer:

```bash
python3 scripts/install.py --destination <project>/.claude/skills --skill norml-wp-architecture
```

Replace `<project>` with the real project directory. The installer does not overwrite
existing packages by default, mutate runtime settings, fetch credentials or install dependencies.
See the collection README for verified installation/runtime scope. Provider and project
workflows in the skill are instructions; installation is not live-operation verification.

## Inside the installed package

- `SKILL.md` — Architecture pre-check and routing.
- `standards/content-model.md` — WordPress primitives and field decisions.
- `standards/decision-trees.md` — Named nouns and three fast decision trees.
- `standards/urls-and-templates.md` — Routes, hierarchy and collision rules.
- `standards/code-placement.md` — Registration ownership and portability.
- `standards/builders-on-top.md` — Builder-neutral implementation handoff.
- `templates/architecture-spec.md` — Short durable output specification.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
