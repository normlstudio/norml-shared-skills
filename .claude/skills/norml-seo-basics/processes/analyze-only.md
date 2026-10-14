# Process — Analyze only

Use this process when the user asks to audit, inspect, check, analyze, or report
on SEO basics without requesting changes.

## 1. Resolve context, platform, and access

1. Resolve the project pointer and exact public target through `provider authentication and the operating system protected credential store`;
   perform bounded missing-pointer recovery when evidence is unambiguous.
2. Read project instructions, SEO docs, CI/CD, and platform-management knowledge.
3. Identify the CMS/platform before selecting platform-specific recipes.
4. On WordPress, use supported WordPress REST API or WP-CLI for read-only capability initialization
   when its durable knowledge files are missing.
5. State that the run is read-only. Do not install integrations/plugins, change
   options, publish GTM versions, purge caches, upload media, edit files, or deploy.
6. Production is the normal target for a recurring read-only invocation because
   the website itself will not be changed. The invoking service skill owns any
   tracker, review, or reporting integration outside this report.

## 2. Resolve the recipe graph

Select recipes from the request. For a full baseline, use the catalog in
`SKILL.md`; for a named integration, select only that recipe and its recursive
dependencies. Read every selected recipe completely and build the ordered ledger:

| Recipe | Why selected | Dependency | Applicability | Current owner |
|---|---|---|---|---|
|  |  |  |  |  |

Do not mark an analytics recipe `PASS` merely because an ID exists in an admin
screen. Public source/network evidence must prove it.

`google-analytics` is a presence-only check with no dependency. Do not create or
edit GA/GTM state while gathering its evidence.

## 3. Capture four evidence layers

### Public HTTP and rendered source

- final redirect chain, HTTPS/canonical host, response status, and indexability;
- exact counts for title, description, robots, canonical, Open Graph/Twitter,
  icons, manifest, JSON-LD, viewport, H1, and `lang`;
- favicon/social/manifest asset status, MIME, dimensions, and approved bytes;
- `robots.txt`, canonical sitemap index, and representative child sitemaps;
- bounded 404-crawl start/final host, coverage, URL count, client-error export,
  and source-inlink export;
- every visible `GTM-`, GA/Google tag, and Clarity identifier or direct embed.

For the WordPress profile, run:

```bash
node scripts/validate-baseline.mjs https://example.com \
  --expect-schema=Organization,WebSite,WebPage \
  --json=.claude/evidence/norml-seo-basics/{run-id}/live-validation.json
```

Adjust expected schema only from visible/project facts.

### Browser and network

Use an isolated browser context; never take over the user's current tab.

- record GTM loader and noscript counts plus the actual container ID;
- inspect GTM/GA/Clarity requests and duplicate page-view/tag firing;
- use Tag Assistant Preview when access is available without publishing changes;
- capture console/page errors, failed resources, desktop/mobile rendering, and
  horizontal overflow.

### Platform/runtime

Capture the applicable admin/integration state without mutation.

On WordPress, through supported WordPress REST API or WP-CLI, collect:

- core/PHP version, URLs, `blog_public`, front-page mode, locale, permalinks;
- active/must-use plugins, theme, GTM/SEO/cache/security integrations;
- GTM4WP option owner without dumping unrelated options;
- Site Icon, relevant SEO settings, homepage meta, schema/sitemap modules;
- every image attachment and current `_wp_attachment_image_alt` plus real usage.

For another platform, capture the equivalent site-wide integration, favicon,
metadata, schema, sitemap, and analytics settings through its supported manager.

### Source and Git

Read-only inspect the source-of-truth repo for assets, manifest, metadata/schema
owners, deploy contract, branch/remote/status, and direct third-party embeds.
On WordPress, explicitly prove the theme/repository contains no GTM container,
loader, noscript iframe, direct GA, or direct Clarity implementation.

## 4. Reconcile evidence

Build the ownership table and score every selected recipe and baseline-contract
row `PASS`, `FIX`, `BLOCKED`, `SKIP`, or `N/A`.

Order remediation by dependency:

1. exact target, platform, and indexability;
2. duplicate ownership;
3. metadata and sitemap/robots;
4. Search Console property and sitemap submission;
5. GTM container;
6. consent decision/CMP/Consent Mode when applicable;
7. GA presence and GTM-dependent optional Clarity;
8. bounded internal 404 candidates and source inlinks;
9. social/favicon/schema;
10. WordPress-specific Rank Math and Media Library gaps;
11. documentation and CI verification.

Do not estimate hours or cost.

## 5. Write the report

Create a new immutable full report using `templates/baseline-report.md`:

```text
Project report folder:
.claude/docs/seo/reports/
  {YYYY-MM-DD}-{HHMM}-seo-basics-{environment}-analyze-only.md
```

Then update `{project}/.claude/docs/seo/norml-seo-basics.md` from
`templates/current-summary.md` as the current summary/index pointing to the
immutable report. Migrate current evidence from a
legacy `wordpress-baseline.md` when present; do not maintain both as canonical.
These are internal pipeline artifacts, so do not auto-open them.

The chat handoff contains only target, platform, read-only mode, overall result,
recipe/dependency matrix, critical ownership/indexability/404 problems,
immutable report path, and the owning skill/person for deeper work. Do not mutate
the site, call automated candidates confirmed bugs, or imply the fixes were
applied.
