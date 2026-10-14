# Page archetypes — deep references

> Part of the shared [page-structure catalog](../readme.md). This is the **deep layer**: whole-page archetypes the catalog describes repeatedly — with text layout specs, ACF schemas and section lists; reference screenshots are excluded. The **lightweight layer** is [`../pages.md`](../pages.md) → `../pages/{type}.md` (text-only structural specs). An archetype here adds the visual + canonical-field detail on top of its matching page spec.

A *page type* is the entire composition of a route, not a single block. When you're scaffolding `single-{cpt}.php`, `page-{slug}.php`, or any new template that has a known shape across the industry, **read the matching entry here first** and use it as the structural baseline before deciding what's truly project-specific. (Atoms / molecules / organisms — the per-component mechanics — live in the project's component system.)

## When to read this

- Scaffolding a new template that has obvious genre conventions ("team member bio," "case study," "service page," "pricing page," "blog post," "course detail").
- Building from a single client mockup — cross-check against the catalog so you don't ship a one-off where a known archetype would do.
- Adding ACF fields to a CPT — see if the archetype already specifies the field schema, instead of guessing.

## When NOT to read this

- One-off marketing landing pages with no genre (e.g. a Black Friday campaign page) — those are pure layout decisions, not archetypes.
- Wireframing the homepage — see `wireframe composition` for the block catalog instead.

## Catalog

| Page type | Use when | Status |
|---|---|---|
| [team-member-bio/](./team-member-bio/) | A CPT (`team`, `instructor`, `staff`, `attorney`) renders one person's bio at `/team/{slug}/` or similar. | v1 |

(Add new entries by creating `{page-type}/` with the same internal structure as `team-member-bio/`.)

## Per-entry structure

Each entry contains `readme.md` with sections, content/data schema, behavior,
conditional visibility, and limits. Approved reusable diagrams may be added;
client screenshots, personal photos and confidential exports do not belong in a
public package. Keep source/version evidence in the author's private release record.

## Contribution flow

1. When you build a new template that follows a recognizable archetype, **before merging**: check if it's catalogued here.
2. If yes → use the spec; flag any deviation in the project's `.claude/changelog/daily.md` with reasoning.
3. If no but the archetype is likely reusable → add a new `{page-type}/` entry. Bare minimum: a complete text specification with sections and fields. Future projects benefit immediately.
4. Add a row to the Catalog table above, and link the archetype from its matching `../pages/{type}.md` spec. Version and changelog `norml-page-structures`; consuming build skills read its installed catalog.

Any approved reference images are reference-only — they're the source of truth for the *shape* of the page, not the brand styling. Brand always comes from the project's `project design brief` output.

## Optional reference images

Inspect reference images only when the user supplies or explicitly approves them.
This package ships text contracts without client screenshots. Missing images do
not block structural use; they leave only image-specific visual claims unverified.
