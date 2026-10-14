# URLs & templates — how WordPress routes a request

> Builder-agnostic. This is how a URL becomes a rendered page in WordPress, regardless of
> whether the template is a Blade file, a PHP file, a Divi Theme Builder template, or an
> Elementor template. Understanding it is what lets you predict the URLs and templates a
> modelling decision produces — and avoid the 404s that come from getting it wrong.

## The core loop: URL → query → template

Every front-end request goes through the same pipeline:

1. **Rewrite rules** parse the URL into a **query** (WordPress decides "this URL means: the
   archive of `case_study`" or "the single `case_study` with slug `acme-rebrand`" or "the
   `industry` term `fintech`").
2. **WP_Query** runs that query and loads the matching posts.
3. The **template hierarchy** picks the most specific template file that exists for that
   query and renders it.

So a content-model decision (page vs CPT vs taxonomy) is also, automatically, a **URL
decision and a template decision.** You don't wire URLs by hand — you choose the primitive
and its slugs, and WordPress derives the routing.

---

## The template hierarchy (the part people don't internalize)

For any query, WordPress looks for templates **from most specific to least specific** and
uses the first that exists. The ones that matter for architecture:

| The request is… | WordPress looks for (most → least specific) | Falls back to |
|---|---|---|
| The blog post index | `home.php` → `index.php` | `index.php` |
| A single blog post | `single-post.php` → `single.php` → `singular.php` | `index.php` |
| A **Page** | `page-{slug}.php` → `page-{id}.php` → `page.php` → `singular.php` | `index.php` |
| A **CPT single** | `single-{posttype}.php` → `single.php` → `singular.php` | `index.php` |
| A **CPT archive** | `archive-{posttype}.php` → `archive.php` | `index.php` |
| A **taxonomy term** archive | `taxonomy-{tax}-{term}.php` → `taxonomy-{tax}.php` → `taxonomy.php` → `archive.php` | `index.php` |
| A **category** archive | `category-{slug}.php` → `category.php` → `archive.php` | `index.php` |
| A **tag** archive | `tag-{slug}.php` → `tag.php` → `archive.php` | `index.php` |
| 404 | `404.php` | `index.php` |

**What this means for modelling:**

- Registering a CPT `case_study` with `has_archive=true` *automatically* gives you two
  routable surfaces — an **archive** (the listing) and a **single** (the detail page) — and
  two template slots to fill: `archive-case_study` and `single-case_study`. You get the
  listing for free; you just style it.
- A custom taxonomy `industry` *automatically* gives you `/industry/{term}/` archives backed
  by `taxonomy-industry` (or the generic `archive`/`taxonomy` template). Filtering-by-a-term
  is routing you get for free the moment you register the taxonomy.
- A **Page** only ever resolves to a `page-*` / `page.php` template — there is no archive
  concept. This is the structural reason a repeatable collection must not be Pages: Pages
  have no archive slot in the hierarchy, so you'd have to hand-build (and hand-maintain) the
  listing that a CPT hands you automatically.

> **Package note — the "blocks-based archive/single" pattern.** This package often renders CPT
> archives and singles *through ACF blocks placed on a controlling page or block template*
> rather than only through raw `archive-{cpt}.php` PHP. That is a **build technique**, not a
> different routing model — the template hierarchy still selects the template; the template
> just delegates to blocks. The routing facts above are unchanged. See
> the bundled inherited-project guide (CPT blocks-based pattern) for the
> build mechanics; don't reproduce them here.

---

## Permalinks & URL structure

### The global permalink setting

WordPress has a site-wide permalink structure (Settings → Permalinks). **Package default:
`/%postname%/`** ("Post name") — clean, slug-based URLs. Avoid the default "Plain"
(`?p=123`) and the dated structures (`/2025/06/slug/`) for anything that isn't a date-driven
blog. (A real news blog can justify a dated structure; most brochure sites do not.)

### How each primitive's URL is formed

| Primitive | URL shape | Controlled by |
|---|---|---|
| Page | `/{slug}/`, nested as `/{parent}/{child}/` | the page slug + page parent (hierarchy) |
| Post | per the permalink setting, e.g. `/{slug}/` | global permalink structure |
| Post category archive | `/category/{term}/` | the category base (changeable) |
| Post tag archive | `/tag/{term}/` | the tag base (changeable) |
| CPT single | `/{cpt-rewrite-slug}/{post-slug}/` | the CPT's `rewrite['slug']` |
| CPT archive | `/{cpt-rewrite-slug}/` (or `has_archive` string) | `rewrite['slug']` / `has_archive` |
| Custom taxonomy archive | `/{tax-rewrite-slug}/{term}/` | the taxonomy's `rewrite['slug']` |

**Designing CPT/taxonomy slugs — the decisions to make explicitly:**

- **Pick the rewrite slug deliberately.** `case_study` (the internal post-type *name*, with
  an underscore, ≤ 20 chars) is separate from its **URL slug** `case-studies` (hyphenated,
  human-facing, usually plural). Set `rewrite => ['slug' => 'case-studies']`. Don't ship the
  raw `case_study` in URLs.
- **Watch for base collisions.** A CPT archive at `/services/` and a Page also at
  `/services/` collide — one wins, the other 404s or behaves oddly. Decide who owns the base:
  usually the CPT archive *is* the "/services/" landing (so you don't also need a Page), or
  you give the CPT a distinct base. This collision is a common, confusing bug; flag it at
  modelling time.
- **Taxonomy bases want to read well too.** `/industry/fintech/` is good. Avoid leaving a
  taxonomy on an ugly default base if the archive is public and SEO-relevant.
- **Hierarchical pages nest; CPTs (usually) don't.** `/about/leadership/` (pages) vs
  `/team/jane-doe/` (a flat CPT). Only make a CPT hierarchical if items genuinely nest.

---

## The flush-rewrite-rules gotcha (the #1 "my CPT 404s" cause)

WordPress caches rewrite rules. **When you register a new CPT or taxonomy, or change a
rewrite slug, the new URLs 404 until the rewrite rules are flushed.** This catches everyone
at least once.

**To flush:**

- The lazy/manual way: visit **Settings → Permalinks** in wp-admin and click Save (no
  changes needed — the visit re-generates the rules).
- The CLI way: `wp rewrite flush`.
- The correct-in-code way: flush on plugin/theme **activation only** (`flush_rewrite_rules()`
  inside an activation hook) — **never** call `flush_rewrite_rules()` on every `init`, that's
  a performance footgun.

**Rule of thumb for the hand-off spec:** any architecture spec that introduces a CPT,
introduces a taxonomy, or changes a slug must carry a note — *"flush permalinks after
registering."* Put it in the spec so the build skill doesn't ship a 404ing archive.

---

## Quick reference: a CPT's full routing surface

Registering one CPT + one taxonomy produces this entire routable + templatable surface,
for free, the moment it's registered (and permalinks flushed):

```
CPT: case_study   (rewrite slug: case-studies, has_archive: true)
TAX: industry     (rewrite slug: industry, attached to case_study)

/case-studies/                 → archive-case_study.php   (listing of all case studies)
/case-studies/acme-rebrand/    → single-case_study.php    (one case study)
/industry/fintech/             → taxonomy-industry.php     (case studies in "fintech")
/industry/healthcare/          → taxonomy-industry.php     (case studies in "healthcare")
```

That is the leverage of choosing the right primitive: four useful, SEO-friendly,
maintainable surfaces from two registrations — versus building and hand-maintaining each as
a separate Page. Decide the primitive (`content-model.md`), name the slugs here, then hand
the spec to the build skill.
