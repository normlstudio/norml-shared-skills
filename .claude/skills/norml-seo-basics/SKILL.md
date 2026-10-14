---
name: norml-seo-basics
version: 1.0.0
description: >
  Run the reusable launch-level SEO basics for any public website.
  Use when the user says "run through SEO basics," "set up the SEO basics,"
  "make this site search-ready," "run the monthly SEO basics check," "connect Google Tag
  Manager," "check Google Analytics,"
  "add Microsoft Clarity," "add the favicon and social sharing image,"
  "connect Search Console," "connect Bing Webmaster Tools," "set up consent
  mode," "set up basic schema," "check for 404s,"
  "configure Rank Math," or "run norml-seo-basics." Resolves
  the platform, selects one concern-per-file recipe from recipes/, expands
  recipe dependencies, audits or fixes the selected baseline, verifies the
  public result, and stores an immutable project-folder report. Google Analytics is a
  presence-only check and is never provisioned by this skill. Microsoft Clarity
  is installed through Google Tag Manager when explicitly selected; on WordPress
  the GTM container is owned by an admin-managed integration, never embedded in
  theme or repository code. The catalog also owns indexability, core metadata,
  sitemap/robots, 404 discovery, Google Search Console, Bing Webmaster Tools,
  consent management, and WordPress Media Library alt text/Rank Math. It is not
  a full technical SEO audit, keyword-research workflow, or advanced schema build.
metadata:
  author: "Norml Studio"
---

# Norml SEO Basics

Make a new or neglected website mechanically search-ready through a reusable,
dependency-aware recipe catalog. Each integration or deliverable has one recipe,
one owner, one verification contract, and one rollback path.

## System role

This is the **launch-baseline recipe runner** in Norml's SEO
layer. It handles the narrow, repeatable checks every public website needs
without assuming that every site is WordPress. It may implement explicitly
requested setup/fixes; read-only recurring-service orchestration belongs to the
service skill that invokes this runner.

The full baseline covers:

1. indexability and canonical-environment agreement;
2. one core metadata owner;
3. one canonical XML sitemap plus matching `robots.txt`;
4. Google Search Console and Bing Webmaster Tools ownership plus sitemap
   submission;
5. Google Tag Manager as the site's tag-management layer;
6. a recorded consent decision and Consent Mode/CMP implementation when needed;
7. Google Analytics presence, delivery owner, and duplicate detection only;
8. favicon, social-sharing-image, and truthful base-schema output;
9. internal 404 discovery with source-inlink evidence;
10. Microsoft Clarity through Google Tag Manager when selected;
11. WordPress-specific Rank Math and Media Library alt work when applicable;
12. source, runtime, browser, live-HTTP, and durable project-folder reporting.

It does **not** replace a full crawl/Core Web Vitals/internal-linking/hreflang
audit, keyword research, bulk metadata program, advanced schema engagement, or
content publishing.

## Modes

Infer the mode from the request; do not ask when the verb is clear.

| Mode | Triggers | May change the site? | Process |
|---|---|---:|---|
| **Analyze only** | run through, audit, inspect, check, analyze, or report | No | `processes/analyze-only.md` |
| **Analyze and fix** | explicit set up, connect, configure, fix, repair, or launch implementation | Yes, within mutable selected recipes | `processes/analyze-and-fix.md` |

`Run through SEO basics` means **Analyze only**. Mutation requires an explicit
setup, connect, configure, fix, repair, or implementation verb. A named
integration request selects that recipe plus its dependencies; it does not
silently run every other recipe.

## Recipe catalog

Every recipe lives directly under `recipes/`. One file owns one concern.

<!-- recipe-catalog:start -->
| Recipe | Applicability | Full-baseline status | Dependency |
|---|---|---|---|
| `indexability.md` | Every public site; state follows environment intent | Required | — |
| `metadata.md` | Every indexable public site | Required | — |
| `sitemap-and-robots.md` | Every indexable public site | Required | `indexability.md` |
| `google-search-console.md` | Managed public indexable sites unless opted out | Required | `sitemap-and-robots.md` |
| `bing-webmaster-tools.md` | Managed public indexable sites unless opted out | Required | `sitemap-and-robots.md` |
| `google-tag-manager.md` | Every managed public site unless explicitly opted out | Required | — |
| `consent-management.md` | Selected analytics/advertising or policy requires a decision | Conditional | `google-tag-manager.md` |
| `google-analytics.md` | Every managed public site unless explicitly opted out; presence check only | Required | — |
| `microsoft-clarity.md` | Sites approved for behavioral analytics | Recommended | `google-tag-manager.md`, `consent-management.md` |
| `favicon.md` | Every public site | Required | — |
| `social-sharing-image.md` | Every public site | Required | — |
| `schema-basics.md` | Every public site | Required | — |
| `404-issues.md` | Every public site; check-only crawl and inlink evidence | Required | — |
| `wp-media-alt-text.md` | WordPress sites with image attachments | Conditional | — |
| `wp-rank-math.md` | WordPress only; only after ownership review | Conditional | — |
<!-- recipe-catalog:end -->

For a full run, execute every Required recipe, evaluate Recommended recipes, and
add every Conditional recipe whose `applies_when` rule matches. A Recommended
recipe without an approved account/project ID becomes `SKIP — not provisioned`,
not a fabricated setup and not a failure of unrelated recipes.

### Dependency resolution

1. Select recipes from the request and the full-baseline rules above.
2. Read each selected recipe's frontmatter.
3. Add every `depends_on` recipe recursively.
4. Reject missing/circular dependencies, then de-duplicate and run dependencies
   before dependants.
5. Read every selected recipe completely before touching the target.
6. Record `PASS`, `FIX`, `BLOCKED`, `SKIP`, `ESCALATE`, or `N/A` for each
   selected recipe.

Google Analytics is an independent presence-only audit. It never creates or
changes a GA property, stream, tag, consent rule, or GTM version. Microsoft
Clarity must never duplicate GTM or consent setup and begins only after those
dependencies are `PASS` or evidence-backed `N/A`.

### Adding a recipe later

Copy `templates/recipe.md` to one kebab-case Markdown file directly under
`recipes/`. Use the same frontmatter and section order as the existing files:

```yaml
---
recipe: product-slug
version: 1.0.0
scope: universal | wordpress
baseline: required | recommended | conditional
depends_on: []
applies_when: "Evidence-backed condition"
---
```

Then include: Outcome, Inputs, Ownership rules, Procedure, Verification,
Rollback, Evidence to record, Hard stops, and Sources. Do not add the same
procedure to another recipe. WordPress-only recipe filenames use the `wp-`
prefix.

Add the new filename to the marked recipe catalog and report matrix, then run:

```bash
node scripts/validate-recipes.mjs
```

The validator checks frontmatter, required section order, missing/circular
dependencies, and catalog/report synchronization. A failing validator blocks
the recipe change.

## Required reading — every run

Read these files completely before touching the target:

1. `standards/baseline-contract.md`
2. the selected mode file under `processes/`
3. `qa/acceptance-contract.md`
4. `standards/hard-stops.md`
5. every selected recipe and every dependency under `recipes/`

Then read project context, in this order when present:

- the project's `CLAUDE.md`, `.claude/CLAUDE.md`, and native `AGENTS.md`;
- `.claude/ci-cd.md`;
- `.claude/docs/seo/`;
- the platform-management knowledge for the target;
- application/theme architecture docs;
- the Strategic Messaging Context or product-marketing context;
- the project SEO brief and approved business facts.

## Platform and operation boundary

This skill coordinates the baseline. It does not bypass the target platform's
management or deployment safety layer.

### All platforms

- Prefer the platform's supported admin/integration surface for site-wide IDs and
  third-party connections.
- Keep one implementation owner per output. Inventory existing integrations
  before installing another one.
- Use a purpose-built API, MCP connector, or CLI when available. Use browser/admin
  automation only when the requested recipe explicitly requires that admin
  surface and the user's request authorizes it.
- Route platform code through the applicable build/deployment skill and contract.
- Use provider authentication and the operating system protected credential store for credentials. Never request or print a secret that
  already belongs in operating-system protected credential store or SSH configuration.

### WordPress

- Use supported WordPress REST API or WP-CLI for capability initialization and WordPress/database
  operations: plugins, options, media, post meta, permalinks, caches, and activity
  logging.
- Use the project WordPress development workflow for theme/plugin code, assets, linting, Git, CI/CD,
  and deployment.
- **GTM exception:** the container ID lives in WordPress Admin through the
  approved admin-managed integration. Never paste the GTM loader or noscript
  iframe into a theme, child theme, snippets file, mu-plugin, or GitHub source.
- An existing Google Analytics implementation should live inside the approved
  GTM container, not in Rank Math, Site Kit, theme settings, or direct page code;
  this skill audits that state but does not provision or move GA. Microsoft
  Clarity lives inside GTM when explicitly selected for setup.
- `wp-rank-math.md` owns WordPress SEO-plugin setup. It must not duplicate an
  established SEO owner.

### Non-WordPress

Use the platform's native site-wide integration/settings surface when it can
emit the required output reliably. If no admin-managed integration exists, code
is allowed only through the project's declared source/deployment contract and
only after the recipe records why the admin route is unavailable.

### Verify supported access

Read [access and safety](standards/access-and-safety.md). Reuse the user's existing
provider identity and verified platform target. No company-specific credentials
schema or sibling skill is required. Missing access blocks the affected recipe;
continue independent public checks and report the exact missing permission.

## Baseline workflow

### 0. Resolve the exact target and platform

Record the project slug, public URL, preferred canonical host, platform/CMS,
environment policy, source-of-truth repo when one exists, and deployment contract.
Confirm the hostname from platform settings, DNS, and the live redirect chain.

For a first WordPress run, initialize `site-capabilities.md`, `project-notes.md`,
and `activity-log.md` through supported WordPress REST API or WP-CLI before mutation.

### 1. Select recipes and inventory ownership

Resolve the recipe graph, then capture current owners before choosing tools:

| Output | Preferred owner | Duplicate rule |
|---|---|---|
| Indexability/canonical environment | Platform/SEO owner plus real host/CDN header owner | Public and staging intent may not conflict |
| Core metadata | Existing mature SEO owner | Exactly one title/description/robots/canonical set |
| XML sitemap and robots.txt | Existing mature platform/SEO owner | One canonical index and one pointer |
| Google Search Console property | Existing verified organization/client property | No duplicate property caused by missing access |
| Bing Webmaster Tools site | Existing exact canonical site in approved Bing user | No HTTP/HTTPS, host, or slash duplicate caused by missing access |
| GTM container embed | CMS/admin integration; GTM4WP on blank WordPress sites | Exactly one loader and one noscript fallback |
| Consent/CMP | Approved CMP/platform plus one GTM consent-initialization owner | Consent Mode is not a second banner |
| Google Analytics | Existing approved Google tag, preferably inside GTM | Presence-only audit; report missing/duplicate ownership, never provision it here |
| Microsoft Clarity | Official Clarity tag/template inside GTM | No direct site embed |
| Title, description, robots, canonical, OG/Twitter | Existing mature SEO owner; Rank Math on blank WordPress sites | Exactly one owner |
| Base schema | Existing mature SEO/schema owner; Rank Math on blank WordPress sites | One connected graph, no duplicate IDs |
| XML sitemap | Existing mature SEO owner; Rank Math on blank WordPress sites | One canonical index |
| Site Icon | Platform/CMS | Theme assets may be the approved source |

Capture live source/network output as well as admin settings. A setting that does
not produce the intended public result is not a pass.

### 2. Ground page intent, identity, and entity facts

Use approved project context and visible copy. Never invent a focus keyword,
legal entity, address, review, rating, offer, social profile, founder, business
type, logo, GTM ID, GA measurement ID, or Clarity project ID.

Schema must describe visible facts. `FAQPage` requires visible Q&A; `Service`
requires a visible service; `Product`/`Offer` requires visible current product and
offer data; `LocalBusiness` requires verified NAP and real local context. Route a
complex multi-template system to `norml-seo-schema`.

### 3. Produce the recipe plan

Compare the inventory with `standards/baseline-contract.md` and each recipe.
Classify every selected item:

- **PASS** — correct, live, and owned once;
- **FIX** — safe in-scope repair;
- **BLOCKED** — missing required input or unsafe target;
- **SKIP** — an optional/recommended recipe was not provisioned;
- **N/A** — the applicability rule does not match, with evidence.

Analyze-only mode writes the report and stops before mutation. Analyze-and-fix
continues without asking for routine implementation approval. `404-issues` and `google-analytics` are
check-only even inside Analyze and fix; their findings require review and a
separate remediation/measurement action.

### 4. Back up before production mutation

Before changing production plugins, database/settings, media, permalinks,
rewrites, or code:

1. create the platform-appropriate dated backup outside the public web root;
2. record current integrations, plugin/theme versions, and relevant settings;
3. confirm a recoverable code state and Git remote when code is involved;
4. record the rollback point without secret values.

### 5. Execute recipes in dependency order

Follow each selected recipe exactly. A recipe is complete only after its own live
verification passes. A blocked recipe does not authorize fabricated IDs or a
different installation path; continue independent recipes and report the block.

Automated crawl findings are candidates, not confirmed bugs. Record them as
`FIX`, `BLOCKED`, or `ESCALATE` in the run evidence, then require human review
before a developer changes a link, redirect, page, analytics owner, or other live
state.

### 6. Complete every selected launch recipe

Indexability, metadata, sitemap/robots, Google Search Console, Bing Webmaster
Tools, and WordPress Media Library alt text are explicit recipes; there is no
hidden inherited checklist beside the catalog. A full run selects them,
resolves their dependencies, and reports each outcome. WordPress still uses the
Rank Math recipe when applicable and preserves the idempotent
configuration/validator workflow.

### 7. Ship atomically

When code is required, work locally, run checks, stage only this run's paths,
commit with a Conventional Commit, push to the project-declared Git remote, and deploy
through the declared workflow. Anything shipped to production must be committed
and pushed in the same turn.

Admin-managed IDs are not copied into theme code merely to create a commit. Record
their owner, safe identifier, and verification evidence in the project docs and
platform activity log.

### 8. Verify and reconcile

Run `qa/acceptance-contract.md` plus every selected recipe's checks. For the
WordPress profile, run:

```bash
node scripts/validate-baseline.mjs https://example.com \
  --expect-schema=Organization,WebSite,WebPage \
  --expect-icon-sha256=<approved-icon-digests> \
  --expect-social-sha256=<approved-social-card-digest>
```

Use browser/network evidence for GTM, GA, and Clarity. Include the 404 crawl
coverage, every discovered internal 4xx URL, and its source inlinks. A required
failure keeps an implementation run open; in a recurring analyze-only run it
remains an evidence-backed finding pending human review.

### 9. Persist the result

Every run writes an immutable full Markdown report under the user's selected
project report folder. Default:

```text
{project}/.claude/docs/seo/reports/
  {YYYY-MM-DD}-{HHMM}-norml-seo-basics-{environment}-{mode}.md
```


Use `templates/baseline-report.md`, then update
`{project}/.claude/docs/seo/norml-seo-basics.md` from
`templates/current-summary.md` as the latest-state index/summary with a pointer
to that immutable report. If the project still has the legacy
`wordpress-baseline.md`, read it as prior evidence and migrate its current state;
do not maintain two competing canonical summaries.

Update the platform activity log, project notes, architecture docs, and code
changelog where their owning skills require it.

## WordPress profile retained from v1

The renamed skill preserves the original WordPress launch operator. When the
platform is WordPress, the full baseline still requires:

- WordPress `home`, `siteurl`, `blog_public`, locale, and permalink review;
- one mature SEO-plugin owner, with Rank Math free as the blank-site default;
- approved favicon/Site Icon/social assets and a working root `/favicon.ico`;
- a truthful Organization-or-Person, WebSite, and WebPage graph;
- one sitemap index plus a matching `robots.txt` pointer;
- every Media Library image reviewed for meaningful alt text or a documented
  intentional decorative blank;
- plugin checksums, desktop/mobile rendering, public source counts, cache-purged
  verification, rollback evidence, and Git/production parity for code.

The project-specific Rank Math configuration template remains
`templates/configure-rank-math.php`. It may be copied into project source for
reproducible Rank Math settings. This exception does not permit GTM, GA, or
Clarity scripts or IDs in theme code.

## Completion contract

The run is complete only when:

- every selected recipe has an evidence-backed terminal status; an Analyze and
  fix implementation result is `PASS` only when every mutable
  Required/Conditional recipe is `PASS` or evidence-backed `N/A`;
- every dependency is `PASS` or evidence-backed `N/A` before its dependant;
- `node scripts/validate-recipes.mjs` passes for the catalog being executed;
- every output has exactly one owner;
- GTM loads once; on WordPress, Git/theme search finds no embedded GTM container;
- Google Analytics presence/absence and duplicate ownership are recorded without
  provisioning; Clarity, when selected for setup, fires through GTM once;
- schema parses, has no duplicate IDs, and contains no unsupported claims;
- favicon/social image URLs return correct MIME, dimensions, and approved assets;
- the canonical sitemap and `robots.txt` agree;
- the selected Search Console property is verified and its canonical sitemap is
  submitted/readable;
- the exact Bing Webmaster Tools site is verified and its canonical sitemap is
  submitted/listed;
- the consent decision and tested tag behavior agree when analytics is selected;
- the 404 crawl states its URL coverage and records every discovered internal
  4xx URL with source inlinks, or is explicitly `BLOCKED` as incomplete;
- the final public page renders at desktop and mobile without change-caused errors;
- an immutable full Markdown report exists inside the project folder and the
  latest-state summary points to it;
- production, platform settings, Git (for code), project docs, and activity logs
  describe the same state.

Report: target, mode, platform, selected recipe/dependency matrix, owners, fixes,
verification, code commit/deploy if any, rollback location, and blocked/skipped
items. Never expose credentials or secret command output.

## Optional companions

`norml-seo-technical-analysis` handles a full technical audit; `norml-seo-schema`
handles advanced structured data; `norml-wp-developer` can implement WordPress
code. `norml-connect`/`norml-security`, when installed, offer portable connection
help. They are optional: this package's access contract and recipe sources are
sufficient to select supported APIs/CLIs and secure provider authentication.

## Validator limits

The HTTP validator is a WordPress-oriented baseline profile. It checks source,
assets and sitemaps; it is not a browser renderer, privacy-law determination,
Google indexing verdict or complete crawler. Human/runtime evidence remains
required. Profile-specific defaults are declared catalog choices, not universal
search ranking requirements. Never treat absent optional manifest/robots meta
as a Google penalty. Record authorized project overrides separately.
