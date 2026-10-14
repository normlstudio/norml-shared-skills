# Builders on top — page builders don't change the data model

> The insight that makes this whole skill builder-agnostic: **Gutenberg, Elementor, Divi,
> and Blade are presentation layers that sit ON TOP of the same WordPress data model.** They
> change *where the layout lives and how you build it* — never *what the thing should be.*
> A case study is a `case_study` CPT in all of them.

## The layering

```
        ┌─────────────────────────────────────────────────────────┐
        │  PRESENTATION / LAYOUT (the builder — varies per project)│
        │  Gutenberg+ACF blocks · Blade templates · Elementor      │
        │  templates · Divi Theme Builder · classic PHP            │
        ├─────────────────────────────────────────────────────────┤
        │  DATA MODEL (this skill — same everywhere)               │
        │  post types · taxonomies · ACF fields · options          │
        ├─────────────────────────────────────────────────────────┤
        │  WordPress core: wp_posts · wp_terms · wp_postmeta       │
        └─────────────────────────────────────────────────────────┘
```

The bottom two layers are what this skill decides, and they're **identical regardless of the
builder.** The top layer is the the existing project stack documentation catalog's domain. So the workflow is always:
**decide the model here (builder-agnostic) → hand it to the build stack to render.**

This is why the architecture decision comes **first** and is made **once.** You don't decide
"CPT or page" differently because the project uses Divi. You decide `case_study` is a CPT,
then Divi builds its single via a Theme Builder template, Elementor via an Elementor
template, Sage via `single-case_study.blade.php`. Same model, different render.

---

## What each builder changes (and what it doesn't)

| | Where layout lives | How you build a CPT single | Changes the model? |
|---|---|---|---|
| **Gutenberg + ACF** (vanilla) | Files: `single-{cpt}.php` + ACF blocks | PHP template + ACF blocks | **No** |
| **Gutenberg + ACF + Sage** (Package standard) | Files: Blade `single-{cpt}.blade.php` + ACF blocks | Blade template + ACF blocks | **No** |
| **Elementor** | Database: an Elementor **Theme template** assigned to the CPT | Elementor Theme Builder, condition = the CPT | **No** |
| **Divi** | Database: a Divi **Theme Builder** template for the CPT | Divi Theme Builder, assigned to the CPT | **No** |

The model remains independent of the chosen renderer. Use the project's supported builder documentation for implementation details.

> **Dynamic content is the bridge.** On a CPT single, every builder pulls the item's fields
> dynamically — Elementor "Dynamic Tags," Divi "Dynamic Content," ACF `get_field()` in a
> Blade/PHP template. One template, many items. That dynamic binding is the builder feature
> that makes "one CPT single template for all 200 case studies" work. If a build is
> hardcoding each item's content into a static layout, that's the antipattern below.

---

## The antipattern this skill exists to catch (builder edition)

Page builders make **"create a new Page and lay it out"** the path of least resistance.
That ease is exactly what lures projects into the most expensive WordPress mistake:

> **Building a repeatable collection as a stack of individual builder-made Pages** — twelve
> "Case Study: …" Pages each hand-laid-out in Elementor/Divi — **instead of a CPT with one
> dynamic Theme template + an archive.**

The cost is identical to the generic version, amplified by the builder:

- **No archive** — no `/case-studies/` index; you hand-build and hand-maintain a links page.
- **No filtering** — no taxonomy archives; "case studies by industry" is impossible without
  rebuilding it manually.
- **N× maintenance** — a design change to the single layout is 12 (then 30, then 80) manual
  edits instead of one template change.
- **No consistency** — the 40th page drifts from the 1st; QA surface explodes.
- **Bad SEO + bad URLs** — ad-hoc `/our-work-acme/` slugs instead of a clean
  `/case-studies/acme/` structure.

When the pre-check sees a builder project heading this way, it interrupts:

> *"I can see Elementor makes it tempting to build each case study as its own Page — but
> they're a repeatable collection. Let's make `case_study` a CPT and build **one** Elementor
> Theme template for the single (with Dynamic Tags pulling each item's fields) plus an
> archive template. Then adding case study #13 is just 'new case study,' and a layout change
> is one edit. Want me to set up the CPT + taxonomy and hand the Elementor build the spec?"*

---

## Phrasing the hand-off per stack

The architecture spec is the same; only the closing hand-off line changes to speak the
project's language. (The spec — primitive, taxonomy, fields, archive/single, code home — is
defined in the SKILL.md "Output" section.)

- **Gutenberg + ACF + Sage (Package standard):** *"→ Implement with the existing Sage workflow (optionally `norml-wp-developer`): build
  `archive-case_study.blade.php` + `single-case_study.blade.php`; register the ACF blocks;
  fields per the approved page specification."*
- **Vanilla Gutenberg + ACF:** *"→ build `archive-case_study.php` + `single-case_study.php`
  with `template-parts/` sections; register ACF blocks in `inc/`; per `the project stack specification:
  gutenberg-acf`."*
- **Elementor:** *"→ build an Elementor **Theme template** for the archive and one for the
  single (condition: `case_study`), using Dynamic Tags for the fields; per `the project stack specification:
  elementor`. CPT/taxonomy registered in the child theme's `inc/` or a `{client}-core`
  plugin — not as Elementor content."*
- **Divi:** *"→ build a Divi **Theme Builder** template set (body for the single, archive
  for the listing) using Dynamic Content; per `the project stack specification: divi`. CPT/taxonomy registered in
  the child theme / core plugin."*

In every case this package specifies the model; the build workflow registers and renders it.

---

## One more: blocks vs. the data model

A frequent confusion worth settling: **"should this be a block or a CPT?"** They're not
alternatives — they're different layers.

- A **block** is a unit of **layout** placed *into* a page or template (a hero, an
  FAQ accordion, a logo cloud). It's presentation.
- A **CPT** is a unit of **content** that exists independently and can be listed/queried (a
  case study, a service).

They compose: a `case_study` CPT's single template is **built out of blocks**; an archive
**block** might query and display `case_study` items. So the question is never "block or
CPT" — it's "what content exists independently (→ model: CPT/taxonomy/fields, this skill)"
*and* "what layout renders it (→ blocks/templates, the build skills + the approved page specification)." Decide
the content first; the blocks come after.
