---
recipe: 404-issues
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every public website needs a bounded crawl for internal client-error URLs and their source inlinks."
---

# Recipe — 404 issues

## Outcome

A bounded Screaming Frog crawl records every discovered internal 4xx URL,
especially 404 responses, plus the pages/resources that link to it. The result is
an automated candidate list for human review—not an automatically confirmed bug
and never an automatic redirect plan.

This is the small broken-URL check inside SEO Basics. Site-wide crawlability,
internal-link architecture, Core Web Vitals, hreflang, and deeper technical
diagnosis remain `norml-seo-technical-analysis` work.

## Inputs

- Exact final canonical URL and environment policy.
- An authorized public target and a safe crawl rate for the host.
- Screaming Frog SEO Spider installed from the official source.
- A paid Screaming Frog licence only when the required crawl exceeds the free
  500-URL limit or needs restricted configuration/saving features.
- A run-specific machine-evidence folder under
  `{project}/.claude/evidence/norml-seo-basics/{run-id}/screaming-frog/`.

A basic crawl needs no API key. Do not ask for or invent one. If licence
activation is required, follow `provider authentication and the operating system protected credential store`: resolve the protected-store-backed
licence reference and leave the unavoidable desktop-app activation to the
operator. Never print the key, write `licence.txt` directly, or put the credential
in the report, command history, or project files.

## Ownership rules

- Screaming Frog owns crawl discovery; the live server owns HTTP truth.
- The immutable SEO Basics Markdown report owns the human-readable result. Raw
  crawl exports are supporting machine evidence, not the only report.
- A reviewer decides whether a 4xx is broken, intentional, blocked, obsolete, or
  a false positive. Development/content owners decide the remedy only after that
  review.
- Never convert every 404 into a homepage redirect. A valid remedy may be an
  inlink correction, content restoration, relevant redirect, intentional 404,
  410, access rule, or no change.

## Procedure

1. Confirm the canonical start URL, allowed scope, target stability, and the
   run-specific evidence directory. Never crawl staging/private hosts as public
   SEO evidence and never bypass authentication, robots/WAF controls, or rate
   limits.
2. Confirm Screaming Frog is installed. On macOS, the supported launcher is
   `ScreamingFrogSEOSpiderLauncher` inside the application bundle. The operator
   must open the desktop app once after installation to accept the EULA and
   select storage mode before headless use. If installation/first-run setup is
   missing, stop this recipe and point to the official guide; do not edit hidden
   app configuration or replace the crawl with guessed URLs.
3. Measure likely URL count from the sitemap and existing project evidence only
   to select tooling—not to claim crawl completeness. The free product crawls up
   to 500 URLs. If the site can exceed that and no licence is available, run no
   partial “PASS”; mark coverage `BLOCKED — 500 URL limit` or use an already
   approved, equivalently complete project crawler.
4. Run a headless internal crawl with a conservative configuration. Export at
   least:
   - `Internal:All`;
   - `Response Codes:Client Error (4xx)`;
   - `Response Codes:Client Error (4xx) Inlinks`.
5. Preserve raw exports in the run-specific machine-evidence folder. Do not put
   CSV files in the human-facing report folder and do not treat a local export as
   a Google Sheet or canonical tracker.
6. Re-request each discovered internal 4xx URL and representative source inlink
   over live HTTP to distinguish reproducible errors from transient blocks or
   crawler-only responses.
7. Record each candidate with response code, URL, content type, discovery source,
   source inlink(s), anchor/element when available, and live recheck result.
8. Mark the recipe `PASS` only when crawl coverage is complete and no reproducible
   internal 4xx candidate remains. Otherwise use `FIX`, `ESCALATE`, or `BLOCKED`
   and send every candidate to human review.

Example CLI shape after installation (adapt output paths to the project):

```bash
"/Applications/Screaming Frog SEO Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher" \
  --crawl "https://example.com" \
  --headless \
  --output-folder ".claude/evidence/norml-seo-basics/{run-id}/screaming-frog" \
  --export-tabs "Internal:All,Response Codes:Client Error (4xx)" \
  --bulk-export "Response Codes:Client Error (4xx) Inlinks"
```

## Verification

- The crawl identifies its exact start URL, final host, timestamp, crawler
  version/licence tier, URL limit, URLs crawled, and completion state.
- Every exported internal 4xx has at least one discovery source/inlink when the
  crawler provides one and a separate live HTTP recheck result.
- Redirected/canonical variants are not double-counted as different confirmed
  bugs without review.
- A zero-issue result is accepted only when coverage is complete; a stopped,
  blocked, rate-limited, or 500-URL-capped crawl cannot pass silently.
- The timestamped Markdown report links to the machine evidence folder and lists
  the full candidate table or an explicit zero-result statement.

## Rollback

`N/A — check-only recipe.` The crawl and report do not mutate the target. Raw
evidence may be regenerated, but the immutable Markdown report is never
overwritten.

## Evidence to record

- Screaming Frog version, free/licensed state, crawl limit, crawl configuration,
  start/final URL, start/end timestamp, and URLs crawled.
- Raw export paths and whether the crawl finished without a cap/block/error.
- One row per internal 4xx candidate: status, URL, source inlink(s), anchor or
  element, content type, and live recheck.
- Human review status and confirmed remediation owner, if any.

## Hard stops

- Target/environment is ambiguous or the crawl is not authorized.
- Screaming Frog or its completed first-run EULA/storage initialization is
  missing and no approved equivalent complete crawler exists.
- Crawl exceeds the free 500-URL cap without a licence or another approved
  complete source; record `BLOCKED`, never a partial pass.
- Host instability, WAF/rate limiting, authentication, or crawl errors prevent
  reliable coverage.
- A proposed redirect, deletion, restoration, or link edit lacks human review.

## Sources

- [Screaming Frog SEO Spider user guide](https://www.screamingfrog.co.uk/seo-spider/user-guide/general/)
- [Screaming Frog SEO Spider FAQ](https://www.screamingfrog.co.uk/seo-spider/faq/)
- [Screaming Frog command-line interface](https://www.screamingfrog.co.uk/seo-spider/user-guide/general/#command-line-interface)
- [Screaming Frog: find and fix 4xx client errors](https://www.screamingfrog.co.uk/seo-spider/issues/response-codes/external-client-error-4xx/)
