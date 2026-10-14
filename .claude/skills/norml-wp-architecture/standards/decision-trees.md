# Decision trees — the fast lookup card

> The reference card for the Architecture Pre-Check. When a brief names a noun, find it
> here first. When it's not listed, run the three core trees at the bottom. Builder- and
> framework-agnostic — the answer is the same on Sage, vanilla ACF, Elementor, or Divi.

## The one question under everything

> **One of a kind, or many of a kind?**
> One → **Page.** Many (same shape, listed somewhere) → **CPT.** Blog-shaped → **Post.**

Everything below is that question applied to the nouns that actually come up in projects.

---

## Common nouns → primitive (the lookup table)

| Brief says… | Primitive | Taxonomy | Archive / Single | Notes / the trap it avoids |
|---|---|---|---|---|
| "a **service page**" | **Page** if there's genuinely one service / one-off landing; **CPT `service`** if there are several services each with its own page + a services index | `service_category` only if you'll filter/group services | CPT → `/services/` + `/services/{slug}/` | The trap: making `/services/seo/`, `/services/ppc/`, `/services/design/` as separate **Pages**. Three+ services that share a shape = a CPT with one template, not N Pages. |
| "**case studies** / portfolio / our work" | **CPT `case_study`** | `industry` (and/or `service`/`tech`) for filtering | `/case-studies/` + `/case-studies/{slug}/` | Almost always a CPT. The flagship example of a repeatable collection. |
| "a **team page** / team members / our people" | **CPT `team_member`** (often `has_archive=false`, no single) — items are ACF-structured and surfaced on the Team page | `department` only if you'll group/filter | usually archive-less; the "/team/" Page composes them | Don't hand-build 15 people as ACF repeater rows if they recur elsewhere or need their own pages; a CPT keeps them managed + reusable. A pure repeater is fine only if they appear in exactly one place and never get a detail page. |
| "**testimonials** / reviews" | **CPT `testimonial`** (`has_archive=false`, no single) surfaced as blocks | optional | none — composed into pages | Managed, reusable, queryable items shown via a block. Not Pages, not hardcoded. |
| "**blog** / news / articles / insights" | **Post** (built-in) | built-in category + tag (add custom only if needed) | built-in | Don't invent a `blog` CPT — Posts already are the blog. |
| "**FAQs**" | A **block** if it's a handful on one page; a **CPT `faq`** if it's a managed, reused, or filterable library | `faq_category` if a library | library → optional archive | Small/local → block (page-structure catalog). Big/reused → CPT. |
| "**events** / webinars" | **CPT `event`** | `event_type`; consider date handling | `/events/` + `/events/{slug}/` | Often needs date-based ordering + past/upcoming split. |
| "**locations** / stores / clinics" | **CPT `location`** | `region` | `/locations/` + `/locations/{slug}/` | Local-SEO friendly; pairs with schema. |
| "**products**" | **WooCommerce** product CPT if it's real commerce; a plain **CPT `product`** if it's a non-transactional catalog | product cats/tags or custom | per Woo / per CPT | Don't rebuild commerce by hand; don't pull in Woo for a brochure catalog. |
| "**resources** / downloads / whitepapers" | **CPT `resource`** | `resource_type` | `/resources/` + single or gated | — |
| "**pricing** / **about** / **contact** / **home**" | **Page** | no | no | Genuine one-offs. The right place for a Page. |
| "a **landing page** for a campaign" | **Page** (one-off) | no | no | Even if it looks like a service page; it's a single, often throwaway. Record the override if it resembles a collection. |
| "**team departments** / **industries** / **service categories** to filter by" | a **taxonomy** on the relevant CPT | (it *is* the taxonomy) | term archives `/industry/{term}/` | The dimension you filter by is the taxonomy; the thing being filtered is the CPT. |
| "the **client name / date / stat** on a case study" | an **ACF field** on the CPT | no | no | A display attribute, not a filter — field, not taxonomy. |
| "global **CTA / social links / footer text**" | **ACF options** (singleton) | no | no | One place, read site-wide. Not a Page, not per-page. |

When the noun isn't here, run the trees below.

---

## Tree 1 — Page vs Post vs CPT

```
Is it the blog (articles / news / editorial, chronological)?
  └─ YES → Post  (built-in category + tag; add a custom taxonomy only if you need another axis)
  └─ NO  → Is there more than one of this thing, each with the same shape?
        └─ NO  (exactly one, won't repeat) → Page
        └─ YES → Do you list them / want each to have its own URL / want to filter them?
              └─ YES → Custom Post Type   (archive + single; add taxonomy per Tree 2)
              └─ NO, they only ever appear composed inside one page, few in number, no detail page
                    → judgment: a CPT (has_archive=false) if they recur or need managing;
                      an ACF repeater on that one page if they truly live in exactly one place
```

The hard line: **"many of the same shape, listed somewhere" = CPT.** The most expensive
WordPress mistake is answering this with "Pages."

## Tree 2 — Custom taxonomy vs ACF field (vs nothing)

```
Do you need to filter, group, or browse the collection by this dimension?
  └─ NO → it's just a displayed attribute → ACF field (text/select/etc.)
  └─ YES → Is the dimension a reusable, recurring vocabulary (same values across many items)?
        └─ NO  (unique/freeform per item) → ACF field, maybe a select if it's a small fixed list
        └─ YES → Should each value have its own archive URL (/dimension/value/)?
              └─ YES → custom taxonomy   (hierarchical if structured/nested; flat if tag-like)
              └─ NO, but you still want WP to manage the term list + counts → still a taxonomy
                    (you just may not link the archives)
```

Hierarchical (category-like: checkboxes, parent/child — `industry`, `region`) vs flat
(tag-like: freeform — `technology`, `topic`). Default to **hierarchical** for controlled
vocabularies, **flat** for open-ended labels.

## Tree 3 — Plugin vs theme (vs child / mu-plugin)

```
Is it presentation (templates, styles, blocks, layout)?
  └─ YES → theme   (child theme if the parent is third-party: Divi/Elementor/marketplace)
  └─ NO → it's functionality (content existence, integrations, behavior):
        Should it survive a theme switch?
          └─ YES → plugin
                Must it be impossible to deactivate (untrusted admin / critical glue)?
                  └─ YES → mu-plugin
                  └─ NO  → site-core plugin  ({client}-core)
          └─ NO (fast, owner-controlled, short-lived build) →
                ACF-JSON-in-theme is acceptable — state the orphaning tradeoff in the spec
```

Full reasoning, the orphaned-content failure mode, and the escalation rule live in
`code-placement.md`.

---

## Worked examples (pre-check in action)

**"Can you build a service page for their SEO offering?"**
→ *"Is this their only service page, or one of several services? If there'll be SEO, PPC,
design, etc., I'd make `service` a CPT now — `/services/` index + `/services/seo/` single,
one template for all — instead of separate Pages we'd maintain by hand. If it's genuinely a
one-off landing page, a Page is right. Which is it?"*

**"Add our 12 case studies, each as a page with the layout I sent."**
→ *"Those are a textbook repeatable collection → I'd make a `case_study` CPT: one
`single-case_study` template, an `/case-studies/` archive, and an `industry` taxonomy so the
archive can filter. Built as 12 Pages instead, there's no index, no filtering, and your
layout change becomes 12 edits. Want me to register the CPT + taxonomy and hand the build
skill the spec?"*

**"We want to filter the team by department."**
→ *"Team members → `team_member` CPT (you already have several, same shape). 'Department' is
the filter dimension → a `department` taxonomy on that CPT, which gives you
`/department/design/` archives for free. Sound right?"*

**"Where should the case-study post type be registered?"**
→ *"Principle: in a `{client}-core` plugin, so the case studies survive a future re-theme.
This package's fast default is ACF-JSON-in-the-theme, which is fine for a site we fully control but
couples the content to this theme + ACF. Since the client owns this site long-term, I'd put
it in the plugin. Agree?"*
