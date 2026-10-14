---
name: norml-wp-architecture
version: 1.0.0
description: >
  Decide WordPress content types, taxonomies, fields, archive/single URLs and code placement before a theme or builder implements them. Use for CPT versus page, taxonomy versus field, plugin versus theme, or inherited content-model planning. Builder/framework independent; outputs a specification rather than production code.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml WordPress Architecture


Decide what content is before deciding how it looks. This package works without any private
skills, company storage or project bootstrap. WordPress itself supplies the underlying model.

## Architecture pre-check

For every request to create a page/template/content collection:

1. Identify one-off versus repeatable content and distinguish editorial posts from custom collections.
2. Recommend the primitive and rationale in a short statement. Explain the concrete consequence
   when the brief would create many separately maintained Pages instead of a reusable collection.
3. Use already confirmed project choices as authority. Resolve an ambiguous model before build.
   A knowing user override is acceptable; record the tradeoff and do not repeatedly question it.
4. On inherited sites discover registered post types/taxonomies first; extend the existing model.

Read [decision trees](standards/decision-trees.md) for named nouns and all three core decisions.

## Workflow and reading order

| Decision | Read | Record |
|---|---|---|
| Post/page/CPT, classification and structured attributes | [Content model](standards/content-model.md) | Primitive, public/query/editor behavior, fields and taxonomy |
| Archive/single routes and collisions | [URLs/templates](standards/urls-and-templates.md) | Rewrite base, archive/single URLs, template slots and redirects |
| Persistent behavior versus presentation | [Code placement](standards/code-placement.md) | Plugin/theme/child/mu-plugin, portability and dependencies |
| Builder handoff | [Builders](standards/builders-on-top.md) | Rendering template, dynamic field binding and editor source |

If CLI access is authorized, read `wp post-type list` and `wp taxonomy list` against the
verified site. Otherwise use supplied registration code or supported admin/API evidence;
label what could not be checked. Do not change live registrations during a planning audit.

## Spec output

Use [the specification template](templates/architecture-spec.md). For each collection state:

- Primitive/internal identifier and whether it repeats or has nested content.
- Classification/filter dimensions; choose taxonomy only when reusable/browsable values justify it.
- Typed field definitions, relationships, ownership and editor-facing source.
- Public/queryable/archive/single behavior; do not expose a composed-only collection by accident.
- Exact route bases, hierarchy slots, current-route collisions and redirect needs.
- Registration home and whether it survives a theme switch; ACF/license dependency if applicable.
- Permalink flush after changed registration, executed once through an authorized operation.
- Builder-specific dynamic rendering handoff and accepted exceptions.

## Scope

A Page suits a true singleton. Posts suit editorial chronology. A CPT suits a distinct
repeatable collection. A taxonomy classifies shared values; custom fields hold attributes.
Options store site-wide singleton settings; patterns reuse layout. CPTs and blocks compose
because they answer different questions: content identity and presentation.

Long-lived content registration usually belongs in a site-core plugin. ACF definitions in a
theme are an explicitly chosen coupling; published CPT records may persist in the database,
but JSON schema location, loader and registration ownership still affect portability.
Do not assume all ACF-created types vanish merely because the source JSON moves.

The package does not write templates, register production types, choose the project's design,
or migrate content. Optional `norml-wp-developer` can implement the spec and optional
`norml-page-structures` can supply page composition; neither is required to use this package.
