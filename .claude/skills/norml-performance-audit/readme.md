# Norml Performance Audit

> Measure website performance and turn observed bottlenecks into specific, testable recommendations.

## The problem

A performance score alone does not identify which asset, request or interaction causes the delay.

The package combines lab and available field evidence with HTTP/HTML and optional source inspection,
then states what the data can support.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Run a performance audit of this URL | *"Run a performance audit of this URL"* |
| Why is this page slow | *"Why is this page slow"* |
| Investigate LCP or layout shifts | *"Investigate LCP or layout shifts"* |
| Check mobile and desktop loading | *"Check mobile and desktop loading"* |
| Inspect render-blocking resources | *"Inspect render-blocking resources"* |
| Compare performance before and after this change | *"Compare performance before and after this change"* |

## A typical run

1. Supply the page URL and optionally its source repository.
2. The agent gathers mobile/desktop PSI where available, follows actual redirects and records
timing/resource evidence.
3. It separates field p75/window from lab diagnostics and identifies a specific measured bottleneck.
4. It writes `docs/performance-audit.md` with resource-level fixes, limitations and a comparable
verification plan.

---

## Inputs and outputs

The exact URL is required; local source path, baseline measurements and approved tooling are
optional. The audit is read-only. It writes one developer-facing Markdown report using the
bundled template, with unavailable checks labelled. Raw JSON/header/HTML evidence can be
kept privately where it won't expose cookies, user records or auth state.

## Evidence sources

`procedures/collect-evidence.md` includes percent-encoded PSI requests, mobile/desktop
separation and GET-based curl timing/header commands. PSI may require authorized provider
access or hit quota. The package reuses a supported existing connection rather than asking
for pasted keys. Missing API data is a limitation, not a fabricated score.

Inspect actual compression/cache validators/protocol/redirects, image bytes/dimensions,
font loading, third-party scripts, blocking resources and HTML/DOM payload. With source
access inspect compiler splitting/minification and server configuration without changing them.
A file's size or name does not by itself prove unused code or a safe removal.

## Field versus lab

Lighthouse navigation describes a controlled lab run. CrUX describes available real-user
aggregated field data, labelled URL or origin, device and time window. Core Web Vitals field
assessment uses p75 LCP, CLS and INP. TBT is a lab diagnostic, not substituted INP.
Record missing samples explicitly; diagnostic interaction traces are not CrUX population data.

## Recommendations

Every finding needs resource/selector/audit or source evidence, affected metric, causal
rationale, qualitative scope, a stack-specific fix and verification. Don't invent effort
hours, costs or numeric timing gains. Don't lazy-load an above-fold/LCP image or blindly
defer scripts that depend on execution order. Preserve consent, accessibility and features.

## Comparable verification

Keep URL/device/tool version/throttling/auth/consent/cache conditions comparable. Repeat
runs where variability matters; record sample count and median/range when measured.
A warm local desktop run cannot prove a cold public mobile improvement. Proposed fixes
remain unverified until post-change measurements and functional checks exist.

## When something breaks

| Gap | Response |
|---|---|
| PSI quota/auth failure | Record exact gap; use already authorized installed measurements |
| No CrUX samples | Report field metrics unavailable rather than deriving INP from TBT |
| No local source | Base findings on public resource/HTTP evidence and label source limits |
| Field and lab disagree | Explain device/window/sample/cache differences before conclusions |
| Metric gain is uncertain | State validation needed; no promised numerical gain |

## Scope

This package does not fix the site, install tools, create provider accounts, spend credits,
audit all SEO requirements or guarantee scores/rankings. Optional SEO analysis can consume
the report, but the performance pipeline is self-contained.

## Install and source

Source collection: [norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
From the collection root, install this complete folder with the local installer:

```bash
python3 scripts/install.py --destination <project>/.claude/skills --skill norml-performance-audit
```

Replace `<project>` with the real project directory. The installer does not overwrite
existing packages by default, mutate runtime settings, fetch credentials or install dependencies.
See the collection README for verified installation/runtime scope. Provider and project
workflows in the skill are instructions; installation is not live-operation verification.

## Inside the installed package

- `SKILL.md` — Read-only audit pipeline and scope.
- `procedures/collect-evidence.md` — PSI/HTTP/resource collection and metric interpretation.
- `templates/performance-audit.md` — Measured findings, fixes and validation template.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
