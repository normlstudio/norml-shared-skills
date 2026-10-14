# The WordPress content model — the primitives

> Builder- and framework-agnostic. This is what WordPress *is* underneath every theme,
> page builder, and block. Decide the primitive here; build it elsewhere.

## The one mental model that explains everything

Almost all WordPress content lives in **one database table: `wp_posts`.** A blog post, a
page, a case study, a nav-menu item, a media attachment, a reusable block — they are all
rows in `wp_posts`, distinguished by a single column: **`post_type`.** "Custom post type"
sounds exotic; it is just *a value in that column that you registered.*

Classification (categories, tags, industries, regions) lives in a **separate set of
tables** (`wp_terms` + `wp_term_taxonomy` + `wp_term_relationships`) and is attached to
posts by relationship. Extra structured data (a client name, a date, a stat) lives in
**`wp_postmeta`** (which is what ACF reads and writes).

So every modelling decision is really three smaller questions:

1. **What `post_type` is this?** (page / post / a custom one)
2. **Does it need classification?** (a taxonomy — or not)
3. **What structured attributes does it carry?** (post meta / ACF fields)

Get those three right and the URLs, templates, archives, and admin UI mostly fall out for
free. Get them wrong — most commonly by forcing a repeatable collection into Pages — and
you fight WordPress for the life of the site.

---

## The primitives

### Page (`post_type = page`)

A **single, one-off content node.** Pages are **hierarchical** (a page can have a parent,
producing nested URLs like `/about/team/`) and have **no built-in taxonomy** and no
chronology. There is no "list of pages" surface for visitors — pages are individuals.

**Use a Page when there is exactly one of the thing and it won't repeat:**
Home, About, Contact, Pricing, Privacy, Terms, a one-off campaign landing page.

**The tell:** you would never say "the *next* one" or "*all* of them." There is one About
page. There is not an archive of About pages.

> ⚠️ **The #1 mistake this whole skill exists to prevent:** building a *repeatable
> collection* (services, case studies, team, locations) as a pile of individual Pages —
> usually because a page builder makes "new Page" the path of least resistance. You lose the
> archive, lose filtering, lose a single source of layout, and multiply every future edit.
> If you catch yourself making "Service: X", "Service: Y", "Service: Z" as Pages → stop,
> it's a CPT.

### Post (`post_type = post`)

The **built-in blog primitive.** Chronological, and the *only* type that ships with
taxonomies out of the box: **categories** (hierarchical) and **tags** (flat). Has an
author, a date, and the main blog feed.

**Use Posts for genuinely blog-shaped content:** articles, news, updates, editorial.

**Do NOT overload Posts for non-blog collections.** "We'll just make case studies regular
Posts and use a category to separate them" works for about a month, then the blog feed,
the category archives, and the SEO all tangle together. A distinct collection deserves a
distinct post type. Posts are for the blog; everything else that repeats is a CPT.

### Custom Post Type (CPT)

A **post type you register** for a **repeatable collection that has its own shape, its own
listing, and its own URLs.** This is the workhorse of real WordPress information
architecture.

**Use a CPT when ALL of these are true:**

- There are (or will be) **many** of the thing, each with the **same structure**.
- They should be **listed somewhere** (an archive / index page).
- Each deserves **its own URL** and possibly its own detail page (a "single").
- They are **conceptually distinct** from blog posts and from each other.

**Common CPT examples:** `case_study`, `service`, `team_member` (or `team`),
`testimonial`, `project` / `portfolio`, `event`, `location`, `resource`, `faq` (when FAQs
are a managed library rather than a block), `job` / `vacancy`.

**Key registration attributes (decided here, set wherever the code lives):**

- `public` — visible to visitors and queryable on the front end. Almost always `true`.
- `has_archive` — does it get an automatic listing page? `true` for anything with an index
  (`/case-studies/`); `false` for collections that are only ever shown *inside* other pages
  (e.g. testimonials surfaced as a block, never browsed on their own).
- `hierarchical` — `false` for the vast majority (CPTs behave like posts). `true` only when
  items genuinely nest like Pages (rare — e.g. a documentation tree).
- `rewrite` slug — the URL base (`case-studies`). See `urls-and-templates.md`.
- `supports` — which core features (title, editor, thumbnail, excerpt, author, …). Turn off
  what the type doesn't need (a testimonial may not need the block editor at all if it's
  pure ACF).
- `show_in_rest` — `true` to use the block editor and the REST API. Package default `true`.

**"Has archive" vs "shown as a block" — an important fork.** Some collections are browsed
(case studies → people land on `/case-studies/`). Others are only *composed into* pages
(testimonials, logos, stats) and never browsed standalone. Both can be CPTs — the
difference is `has_archive` and whether you build a single template. A CPT with
`has_archive=false` and no single is still the right call when you want *managed, reusable,
queryable* items even though visitors never see a dedicated page for one.

### Taxonomy

A **way to classify and group** content so it can be **filtered and browsed by a
dimension.** A taxonomy is itself a managed list of **terms**, and each term gets its own
archive URL.

Two shapes:

- **Hierarchical** (like **categories**): terms can have parents/children; admin UI is
  checkboxes; good for a **controlled, structured** set. Use for: `industry`,
  `service_category`, `region`, `product_type`.
- **Non-hierarchical / flat** (like **tags**): free-form, no nesting; admin UI is a
  comma/typeahead field; good for **open-ended labelling**. Use for: `technology`, `topic`,
  loose keyword-style tagging.

**Use a custom taxonomy when:**

- You need to **filter or group** a collection by a dimension ("case studies *by
  industry*", "team *by department*"), **and**
- The dimension is a **managed, reusable list** (the same industries recur across many
  items), **and/or**
- Each value should have **its own archive page** (`/industry/fintech/` listing all fintech
  case studies — useful for SEO and navigation).

**Taxonomy vs. just an ACF field — the decision that trips people up:**

| Use a **taxonomy** when… | Use an **ACF field** (select/text) when… |
|---|---|
| You filter or browse the collection by it | It's a display attribute, not a filter |
| The values recur across many items (a shared vocabulary) | The value is unique/freeform per item |
| Each value deserves its own archive URL | No archive needed — it's just shown on the item |
| You want WordPress to manage the term list + counts | A fixed, code-owned list is fine |

Example: a case study's **`industry`** → taxonomy (you'll filter by it, it recurs, it wants
`/industry/fintech/`). A case study's **`client_name`** → ACF text field (unique per item,
never filtered as a shared list, no archive). A case study's **`project_year`** → judgment
call: ACF field if you just display it; taxonomy if you want `/year/2025/` archives.

> Don't create a taxonomy you'll never browse or filter by. A taxonomy with one term per
> post and no archive is just an ACF field with extra tables.

### Custom fields / ACF — the structured-data layer

**Custom fields are structured attributes attached to any post / page / CPT / term / user /
options object.** They are *not* a content type — they are the **typed data layer** on top
of one. In WordPress core they live in `wp_postmeta`; **ACF (Advanced Custom Fields)** is
the tool This package uses to define, group, and render them with a real UI and typed return
values.

**Use ACF fields for:** every structured attribute that isn't the freeform body — client
name, dates, roles, stats, ratings, related-item relationships, hero image, CTA target,
repeatable rows (a list of results, a list of speakers).

ACF is also **how This package builds blocks and options pages** — but those are presentation /
settings concerns (`builders-on-top.md` and the "options" note below), not new primitives.
At the data-model layer, the rule is simple: **body content → the editor; everything
structured → ACF fields.**

**Field-shape signals:**

- One value → text / number / select / image / link.
- A fixed small set of named values → individual fields or a group.
- A variable-length list of the same shape → **repeater** (or, for mixed shapes, flexible
  content — though for *layout* flexibility prefer blocks over flexible content; see
  `builders-on-top.md`).
- A pointer to other content → **relationship / post-object** field (e.g. a case study's
  "related services" pointing at `service` CPT items).

### Options / site settings (singletons)

Site-wide values that aren't content and aren't per-page: global CTA text + link, social
URLs, footer copy, contact details, default fallback images. These belong in an **ACF
options page** (or theme customizer / theme.json for truly theme-level tokens) — **not** a
Page, and **not** repeated on every page. The tell: "this same value appears site-wide and
is edited in one place." One options object, read everywhere.

### The reusable-layout primitives (mentioned, owned elsewhere)

**Menus** (navigation), **widgets / block-areas**, **block patterns**, and **synced
patterns** (formerly "reusable blocks") are WordPress's reuse mechanisms for *navigation and
layout chunks.* They are real primitives but they are **presentation**, so the *what-blocks*
decisions live in the approved page specification and the *how-to-build* lives in the build
skills. Flagged here only so the model is complete: when something is "the same chunk of
layout in several places," reach for a pattern / synced pattern, not a copy-paste or a CPT.

---

## The model at a glance

| You have… | Primitive | Taxonomy? | Notes |
|---|---|---|---|
| One About / Contact / Pricing page | **Page** | no | hierarchical if nested |
| The blog / news / articles | **Post** | category + tag (built-in) | don't reuse for non-blog |
| Many case studies with a `/case-studies/` index | **CPT** `case_study` | `industry` (filter) | archive + single |
| Many services, each its own page + a services index | **CPT** `service` | maybe `service_category` | archive + single |
| Team members shown on a Team page | **CPT** `team_member` | maybe `department` | often `has_archive=false`, no single |
| Testimonials surfaced as blocks site-wide | **CPT** `testimonial` | optional | `has_archive=false`, no single |
| "Filter X by industry / region / type" | (the X is a CPT) + **taxonomy** | — | taxonomy gives the archive + filter |
| A unique attribute on an item (client, date, stat) | **ACF field** on the CPT | no | not a taxonomy |
| Global CTA / socials / footer text | **ACF options** | no | singleton, not a Page |
| The same layout chunk reused in places | **pattern / synced pattern** | no | presentation — build-skill territory |

When the call isn't obvious from this table, go to `decision-trees.md` for the
walk-through, and `urls-and-templates.md` for what the CPT/taxonomy choice does to URLs and
templates.
