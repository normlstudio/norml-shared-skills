---
name: norml-seo-technical-analysis
version: 1.0.0
description: >
  Audit website technical SEO across crawlability/indexation, performance/Core
  Web Vitals, metadata, schema, mobile/accessibility, internal links, hreflang and
  HTTPS/serving. Use for technical SEO audit, crawl/indexation, canonical, robots,
  sitemap, page speed, broken URLs or hreflang review. Produce six evidence-backed
  Markdown report sections and a prioritized findings table. No private templates
  or other skills are required; audits do not mutate websites.
metadata:
  author: Norml Studio
---

# Norml SEO Technical Analysis

Audit technical SEO with measured evidence and explicit coverage. Assess all eight
areas; mark genuinely irrelevant checks N/A with a reason and unavailable checks
blocked. A sampled public review is a partial audit, never a full crawl.

## Inputs

Resolve domain/subdomains, CMS/stack, canonical host, target locales, environment,
allowed crawl scope/rate, report directory and available provider/crawler access.
Read project instructions, SEO/architecture/marketing context and existing audit
history when present. No company folder, spreadsheet template or credentials
schema is required. Native Google Sheets may be used only when explicitly chosen
and accessible through a supported connector; Markdown/JSON is the default.

## Workflow

1. **Confirm target and coverage.** Record final host and scope. Inventory
   robots/sitemaps and known URLs, plus crawl/provider sources. Use an authorized
   crawler/export when available. Record skipped hosts, caps, auth, rate limits
   and sitemap-only coverage. Do not bypass access controls or operate provider
   browser sessions as a fallback to unavailable APIs.
2. **Select evidence tools.** Use existing authorized Site Audit/API/crawler
   access; tool names/endpoints vary and must be verified from official docs.
   Public HTTP fetches suffice for spot checks. Render JS-dependent public pages
   in an isolated approved browser. Read [evidence rules](standards/evidence.md).
3. **Run every area.** Follow [the eight-area audit](processes/eight-area-audit.md)
   in full. Inspect representative page types and all discovered URL data where
   feasible. Use PSI/Lighthouse for lab findings and CrUX/GSC where available
   for field CWV. Never substitute lab TBT or a score for actual field INP.
4. **Validate schema and mobile.** Parse actual emitted JSON-LD, visible parity
   and type-specific official requirements. Rich Results Test is an interactive
   external cross-check, not a fetch-only API. Record access/automation limits.
   Test real mobile layout, keyboard/navigation and resource failures.
5. **Prioritize findings.** Give each issue severity, affected URLs/count,
   source/time, concrete reproduction/evidence, impact, action, owner *role*
   and dependencies. Complexity labels are optional; never invent hours,
   cost, health score, impact/effort arithmetic or named owners.
6. **Persist and hand off.** Fill all six sections of
   [the report template](templates/technical-report.md). Default path:
   `{project}/.claude/docs/seo/reports/{timestamp}-technical-analysis.md`.
   Do not overwrite prior reports. Include crawl coverage, blocked checks,
   field/lab scope, five most urgent verified actions and evidence locations.
   Run [acceptance](qa/acceptance.md); report partial completion candidly.

## Limited-tooling route

Pull XML inventories; select 20–30 representative URLs across actual page types
when this provides useful coverage. Fetch each page/status/meta/canonical/schema
and one mobile/desktop PSI run per sampled type. Sample count is a recorded scope
choice, not proof of site-wide coverage. Orphan/inlink completeness requires a
complete graph; mark those checks blocked or partial without one. If a provider
fails, preserve successful independent evidence and state exactly what is missing.

## Boundaries and optional companions

Read-only audit: no plugin setup, link edits, redirects, sitemap changes,
cache purges, purchases, messages or deployments. Do not invent claims or keyword
intent. `norml-seo-basics` can repair authorized launch basics; `norml-seo-schema`
can prepare structured data; `norml-performance-audit` and `norml-wp-developer`
can address deeper code work. These are optional; users can hand the same report
to their own developers. Missing access blocks a check, not unrelated assessment.
