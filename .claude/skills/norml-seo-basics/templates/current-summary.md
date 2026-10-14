---
project: "{Project Name}"
domain: "https://example.com"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
latest_result: "PASS | FAIL | BLOCKED"
latest_report: "{project-relative immutable Markdown path}"
skill: "norml-seo-basics@1.0.0"
---

# SEO basics — current state

> Latest full evidence: `{project-relative immutable Markdown path}`
> Last checked: `{timestamp}` · `{environment}` · `{mode}`
> Human review: `{complete | Pending review | N/A}`

## Latest run

- Run ID: `{YYYY-MM-DD-HHMM}`
- Result: `{PASS | FAIL | BLOCKED}`
- Run/review owner: `{owner}`
- Fix owner: `{owner | N/A}`
- Machine evidence: `{project-relative run folder}`

## Current recipe state

<!-- current-recipe-matrix:start -->
| Ref | Recipe | Automated status | Human review | Last checked | Evidence |
|---|---|---|---|---|---|
| SEO-01 | `indexability` |  |  |  |  |
| SEO-02 | `metadata` |  |  |  |  |
| SEO-03 | `sitemap-and-robots` |  |  |  |  |
| SEO-04 | `google-search-console` |  |  |  |  |
| SEO-05 | `bing-webmaster-tools` |  |  |  |  |
| SEO-06 | `google-tag-manager` |  |  |  |  |
| SEO-07 | `consent-management` |  |  |  |  |
| SEO-08 | `google-analytics` |  |  |  |  |
| SEO-09 | `microsoft-clarity` |  |  |  |  |
| SEO-10 | `favicon` |  |  |  |  |
| SEO-11 | `social-sharing-image` |  |  |  |  |
| SEO-12 | `schema-basics` |  |  |  |  |
| SEO-13 | `404-issues` |  |  |  |  |
| SEO-14 | `wp-media-alt-text` |  |  |  |  |
| SEO-15 | `wp-rank-math` |  |  |  |  |
<!-- current-recipe-matrix:end -->

Use the latest applicable status for every row. Do not turn a `Pending review`
candidate into a confirmed issue in this summary.

## Confirmed open issues

Only include findings whose Human review is `Issue Detected`.

| Ref | Confirmed issue | Review evidence | Fix owner | Recheck state |
|---|---|---|---|---|
|  |  |  |  |  |

Use `None confirmed` when every non-pass result is still pending/clarifying or
the reviewer verified no issue.

## Report history

Append newest first. Never delete a prior report pointer.

- `{YYYY-MM-DD HH:MM} — result — project-relative report path`
