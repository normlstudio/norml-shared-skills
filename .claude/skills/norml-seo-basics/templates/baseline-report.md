---
project: "{Project Name}"
domain: "https://example.com"
mode: "analyze-only | analyze-and-fix"
run_id: "YYYY-MM-DD-HHMM"
checked_at: "YYYY-MM-DDTHH:MM:SSZ"
result: "PASS | FAIL | BLOCKED"
skill: "norml-seo-basics@1.0.0"
report_path: "{project-relative immutable Markdown path}"
human_review: "Pending review | complete | N/A"
---

# SEO basics

## Target

- Project slug: `{project-slug}`
- Platform/CMS: `{platform}`
- Environment: `{production | staging | local}`
- Requested URL: `{url}`
- Final canonical URL: `{url}`
- Platform target/document root: `{reference-only value; no secrets}`
- Immutable report: `{project-relative path}`
- Machine evidence: `{project-relative run folder}`
- Run/review owner: `{SEO expert | trained QA reviewer | owner}`
- Fix owner: `{development/content/measurement owner | N/A}`
- Active theme/application version: `{value or N/A}`
- SEO owner: `{Rank Math | Yoast | SEOPress | AIOSEO | custom}`
- Sitemap owner: `{owner}`
- Schema base owner: `{owner}`
- Metadata evidence source: `{approved artifact / visible page}`
- Keyword target: `{verified phrase | unverified}`

## Result

`{PASS | FAIL | BLOCKED}` — {one evidence-backed sentence}

## Recipe and dependency matrix

<!-- recipe-matrix:start -->
| Recipe | Selected because | Dependency | Applicability | Automated status | Human review | Owner/evidence |
|---|---|---|---|---|---|---|
| `indexability` |  | — |  | `{PASS/FIX/BLOCKED/N/A}` | `{Pending review/Verified/Issue Detected/Issue Resolved/Clarify/Not applicable/N/A}` |  |
| `metadata` |  | — |  |  |  |  |
| `sitemap-and-robots` |  | `indexability` |  |  |  |  |
| `google-search-console` |  | `sitemap-and-robots` |  |  |  |  |
| `bing-webmaster-tools` |  | `sitemap-and-robots` |  |  |  |  |
| `google-tag-manager` |  | — |  |  |  |  |
| `consent-management` |  | `google-tag-manager` |  |  |  |  |
| `google-analytics` |  | — |  |  |  |  |
| `microsoft-clarity` |  | `google-tag-manager`, `consent-management` |  | `{PASS/FIX/BLOCKED/SKIP/N/A}` |  |  |
| `favicon` |  | — |  |  |  |  |
| `social-sharing-image` |  | — |  |  |  |  |
| `schema-basics` |  | — |  |  |  |  |
| `404-issues` |  | — |  |  |  |  |
| `wp-media-alt-text` |  | — |  |  |  |  |
| `wp-rank-math` |  | — |  |  |  |  |
<!-- recipe-matrix:end -->

Keep every catalog row. Use `N/A` or `SKIP` with a reason so the full baseline
remains visible. An automated non-pass is a candidate until the Human review
column confirms it.

## Tag and analytics ownership

- GTM container: `{GTM-… | opted out | blocked}`
- GTM embed owner/settings location: `{platform integration}`
- Google Analytics presence: `{present once | absent | duplicate | blocked | opted out}`
- Observed Google tag/Measurement ID and delivery owner: `{safe identifiers + owner | N/A}`
- GA mutation performed by this run: `None — presence-only recipe`
- Microsoft Clarity project ID: `{safe identifier | SKIP/N/A}`
- Microsoft Clarity delivery owner: `{GTM required | N/A}`
- Consent decision owner/mode/regions: `{verified project decision}`
- CMP/platform and GTM consent owner: `{owner/settings location | N/A}`
- Consent state test matrix: `{first visit/accept/reject/change/reload result}`
- Published GTM version and rollback version: `{values}`
- Direct/duplicate embed scan: `{result}`

## Google Search Console

- Property type/scope: `{Domain | URL-prefix | opted out | blocked}`
- Verified owner and method: `{reference-only owner/method; no secret tokens}`
- Approved users/permissions: `{summary}`
- Submitted canonical sitemap/status: `{url + status}`
- URL Inspection sample: `{url + result}`
- Security Issues / Manual Actions: `{result}`

## Bing Webmaster Tools

- Canonical site URL: `{url | opted out | blocked}`
- Bing user/protected-store reference: `{identity + service/account names; no key}`
- Verified ownership/method: `{IsVerified result + durable method/owner}`
- Public verification proof: `{DNS hostname/target | XML/meta location}`
- Submitted canonical sitemap/status: `{url + GetFeeds status}`
- Diagnostics/security review: `{result}`

## Baseline matrix

| Area | Check | Status | Before | After/current | Evidence |
|---|---|---|---|---|---|
| Environment | HTTPS + preferred host | `{PASS/FIX/ESCALATE/N/A}` |  |  |  |
| Indexability | Platform visibility + headers + robots meta |  |  |  |  |
| Metadata | One title/description/robots/canonical |  |  |  |  |
| Social | OG + Twitter + image response |  |  |  |  |
| Identity | Site Icon + favicon family + manifest |  |  |  |  |
| Media | Image attachment alt-text coverage |  |  |  |  |
| Platform/plugin | One SEO owner + verified configuration |  |  |  |  |
| Schema | Valid connected homepage graph |  |  |  |  |
| Sitemap | Canonical index + child maps |  |  |  |  |
| Robots | Sitemap pointer + no blanket disallow |  |  |  |  |
| Search ownership | Google Search Console + Bing Webmaster Tools |  |  |  |  |
| Crawl | Internal 4xx coverage + source inlinks |  |  |  |  |
| Render | Desktop/mobile + no fatal/console/resource failures |  |  |  |  |
| Durability | Config script + docs + Git/prod parity |  |  |  |  |

## Output ownership

| Output | Owner | Fallback | Duplicate protection |
|---|---|---|---|
| Title/description/robots/canonical |  |  |  |
| Open Graph/Twitter |  |  |  |
| Base schema graph |  |  |  |
| Page-specific schema |  |  |  |
| XML sitemap |  |  |  |
| Site Icon/favicon/manifest |  |  |  |

## Canonical homepage contract

- Title: `{title}`
- Description: `{description}`
- Canonical: `{url}`
- Focus keyword: `{verified phrase | intentionally empty}`
- Social image: `{url and dimensions}`
- H1: `{visible heading}`
- Language: `{locale}`

## Schema graph

| Type | `@id` | Source | Visible-page evidence |
|---|---|---|---|
| Organization/Person |  |  |  |
| WebSite |  |  |  |
| WebPage |  |  |  |
| Conditional entities |  |  |  |

## Sitemap policy

- Canonical index: `{url}`
- Included post types: `{list}`
- Excluded post types: `{list}`
- Included taxonomies: `{list}`
- Excluded taxonomies: `{list}`
- Authors: `{policy + reason}`
- Images: `{policy}`
- Core WordPress sitemap: `{disabled | redirected | intentionally retained}`
- robots.txt sitemap line: `{line}`

## Internal 404 crawl

- Crawler/version: `{Screaming Frog version | approved equivalent}`
- Licence/cap: `{free 500 URL limit | licensed | approved equivalent}`
- Start URL/final host: `{values}`
- Crawl started/finished: `{timestamps}`
- URLs crawled: `{count}`
- Coverage: `{complete | BLOCKED — reason}`
- Raw evidence: `{project-relative machine-evidence paths}`
- Reproducible internal 4xx candidates: `{count}`

| HTTP status | URL | Source inlink(s) | Anchor/element | Content type | Live recheck | Human review |
|---:|---|---|---|---|---|---|
|  |  |  |  |  |  | `{Pending review/Issue Detected/Clarify/Not applicable}` |

Use `None — complete crawl found no reproducible internal 4xx URLs` when the
candidate count is zero. A capped, blocked, or incomplete crawl may not use that
statement.

## Changes applied

| Change | Environment | Durable source | Verification |
|---|---|---|---|
|  |  |  |  |

Use `None — analyze-only run` when no changes were authorized.

## WordPress Media Library alt audit

Use `N/A — non-WordPress` when the WordPress profile does not apply. Record the
equivalent platform image-alt review in the baseline matrix.

- Image attachments reviewed: `{count}`
- Meaningful existing alt preserved: `{count}`
- Alt values repaired: `{count; attachment IDs}`
- Intentional decorative/redundant blanks: `{count; attachment IDs + reasons}`
- Unexplained blank or meaningless alt values remaining: `{0 required for PASS}`

| Attachment ID | Public usage | Before | After/current | Decision evidence |
|---|---|---|---|---|
|  |  |  |  |  |

## Rollback

- Platform/data backup: `{path, version, or N/A for analyze-only}`
- Code starting point: `{commit}`
- Integration/plugin/theme inventory capture: `{artifact/log reference}`
- Rollback notes: `{notes}`

## Verification

- Validator command: `{redacted-safe command}`
- Validator result: `{PASS/FAIL; pass/warn/fail counts}`
- PHP/build/tests: `{result}`
- Plugin checksum: `{result}`
- Desktop browser: `{result}`
- Mobile browser: `{result}`
- Live cache-purged source: `{result}`
- Final commit/deploy: `{commit + environment, or N/A}`

## Escalations / next work

Only list work outside the baseline or facts that could not be verified. Do not
estimate time or cost.

- `{item → owning skill/person}`

## Activity log pointer

- Platform-management activity entry: `{path/date}`
- GTM container version/activity evidence: `{reference or N/A}`
- Architecture/application docs updated: `{paths}`
