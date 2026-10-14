---
name: norml-performance-audit
version: 1.0.0
description: >
  Audit mobile and desktop website performance using PageSpeed Insights, direct HTTP/HTML evidence and optional local source inspection. Use for speed audits, Core Web Vitals, slow pages, LCP, CLS, INP, TTFB or render-blocking investigations. Produces evidence-backed prioritized findings and validation steps; no automatic fixes or promised gains.
metadata:
  version: "1.0.0"
  author: "Norml Studio"
---

# Norml Performance Audit


Investigate the supplied URL and optional local repository. Produce a developer-facing report
with specific measurements, resource evidence, proposed remedies and honest limitations.
No private ecosystem, paid provider or credentials convention is required.

## Inputs and output

Require the exact URL; accept optional source path, affected template URLs, before/after
baseline and approved measurement tools. Read current project instructions and code context.
Default report: `{project-root}/docs/performance-audit.md` or the user's chosen Markdown path.
Keep raw measurement JSON private outside the repository when it carries unnecessary data.
Audit is read-only; changes, subscriptions, tool installs and production writes are separate.

## 1. Collect mobile and desktop evidence

Read [measurement procedure](procedures/collect-evidence.md). Gather both PSI strategies,
Lighthouse audits and available CrUX field data. Preserve timestamp, URL/final URL, tool
version, device/throttling, run count and cache conditions. Label URL versus origin field
data, aggregation window and insufficient samples. If PSI is unavailable/quota-limited,
report the exact gap and use already installed local Lighthouse plus HTTP evidence; do not
invent a score, field INP or successful tool integration.

## 2. Inspect actual causes

Inspect response timing/headers, redirects, HTML, resource waterfall where authorized,
images, fonts, third-party payloads and DOM. With local source inspect lockfiles, bundler,
asset sizes, loading strategy, caching and server configuration. Match recommendations to
the existing stack. Record the actual resource/selector/file location and observed metric.
A resource merely lacking lazy loading is not a defect when it is above-fold/the LCP image.

## 3. Prioritize

Group by High/Medium/Low impact based on measured bottleneck. Explain scope and dependency
complexity qualitatively; do not assign invented hours, costs or numeric metric gains.
LCP > 2.5 s, CLS > 0.1 and INP > 200 ms warrant investigation against field p75 and source.
These cutoffs do not make Lighthouse's score a Core Web Vitals pass/fail result.

A high measured TTFB can delay LCP; an LCP image's encoded bytes/render size/load priority
may be causal; layout shifts need actual attribution; interaction delays need trace or
real-user interaction evidence. TBT is a lab diagnostic, not an INP replacement.

## 4. Report and validate

Use [the report template](templates/performance-audit.md). Each finding contains observation,
evidence, affected metric, scope, precise fix, limitations and a comparable verification plan.
Include what's working and preserve supported behavior, consent, images and accessibility.
Record what wasn't checked. Treat a proposed improvement as unverified until comparable
post-change measurements exist; repeat measurements when variability affects the conclusion.

Optional `norml-seo-technical-analysis` may consume the findings. This package does not perform
a general SEO audit, implement fixes, install tools or promise scores/ranking/timing gains.
