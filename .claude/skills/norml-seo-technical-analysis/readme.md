# Norml SEO Technical Analysis

> Audit eight technical SEO areas and produce a prioritized report with explicit evidence and
coverage.

## The problem

A score or sampled crawl can hide unavailable checks and unverified site-wide assumptions.

The audit records exact coverage, measured findings and blocked sources in six report sections.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Run a technical SEO audit | “Run a technical SEO audit” |
| Audit indexation and canonicals | “Audit indexation and canonicals” |
| Check Core Web Vitals | “Check Core Web Vitals” |
| Review hreflang | “Review hreflang” |
| Find broken URLs | “Find broken URLs” |

## A typical run

1. Resolve the canonical site and enumerate robots/sitemap/provider sources.
2. Audit representative templates and full available crawl data through all eight areas.
3. Measure mobile/desktop performance while separating field CWV from lab diagnostics.
4. Fill the report template, identify the five urgent actions and disclose partial or blocked
checks.

---

## Details

### Inputs

- Target URL/subdomains, CMS, locales, crawl scope/rate, report directory and available authorized
data.

### What it creates or changes

- Immutable six-section Markdown report and prioritized evidence-backed findings; optional JSON/CSV
tables.

### Capabilities

- **Eight areas:** Indexation, speed, metadata, schema, mobile, linking, international and serving.
- **Six report sections:** Summary, crawl, speed, meta, schema and unified findings.
- **Evidence discipline:** Separate lab/field, URL/origin and live/indexed observations.
- **Limited tooling:** Representative public checks with explicitly partial coverage.

### Inside the skill

| Path | Role |
|---|---|
| [SKILL.md](SKILL.md) | Scope, audit and reporting router. |
| [processes/eight-area-audit.md](processes/eight-area-audit.md) | Detailed technical check catalog. |
| [standards/evidence.md](standards/evidence.md) | Coverage and measurement interpretation. |
| [templates/technical-report.md](templates/technical-report.md) | Six report sections and evidence columns. |
| [qa/acceptance.md](qa/acceptance.md) | Completion and honesty gate. |

### Limits

- Read-only; no website/provider mutation or deployments.
- No invented health score, hours, cost or named assignees.
- A sample cannot establish complete crawl/inlink/orphan coverage.
- Provider failures remain blocked checks, not guessed data.

### When something is missing

Read the runtime contract and relevant bundled procedure. Report missing source
facts, access, required content or verification as unresolved/blocked; continue
independent checks. Keep project decisions and credentials outside the package.
Never guess evidence or treat a template/default as a verified live result.

### Installation and source

Copy this complete folder into the supported skill directory of your chosen
agent runtime. The runtime must discover SKILL.md and its relative supporting
files. See the collection guide for tested local installation. No remote CLI
installation or runtime compatibility is promised without that verification.

Source: the supplied norml-shared-skills collection. This package is standalone;
related Norml packages mentioned in SKILL.md are optional companions.

---

Covers SKILL.md v1.0.0
Last changelog entry: v1.0.0
Generated: 2026-10-13
