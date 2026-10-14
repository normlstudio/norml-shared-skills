## Report structure

Six sections in one Markdown report, with matching JSON/CSV tables if useful. Every checked item gets a row.

### Section 1: Executive summary

Top-of-document one-pager.

| Column | Values |
|--------|--------|
| Domain | client URL |
| Audited on | date |
| CMS / stack | from gathered context |
| Pages audited | total count from crawl |
| Critical issues | count of `Critical` priority rows |
| High issues | count of `High` priority rows |
| Medium issues | count of `Medium` |
| Low issues | count of `Low` |
| Assessment status | Complete, partial or blocked with covered/unavailable areas |
| Top 5 fixes | the 5 evidence-backed priorities by severity, reach and dependencies; no invented effort score |

### Section 2: Crawlability + indexation

One row per finding. Columns: Issue / Severity (Critical/High/Medium/Low) / Affected URLs (or page count) / Evidence (screenshot/data) / Recommended fix / Owner type (Dev/Content/SEO).

### Section 3: Site speed (Core Web Vitals)

Per page type, table with mobile + desktop scores for LCP, INP, CLS, plus PSI score. Mark Good (green) / Needs Improvement (amber) / Poor (red). Include the specific lighthouse opportunity items per page type.

### Section 4: Meta + on-page (4.2)

Per indexable page (top 50 by traffic, or all if site has < 50 pages):

| Column | Values |
|--------|--------|
| URL | page URL |
| Page type | Homepage / Service / Blog / Product / Category / Contact / Other |
| Title | current title text |
| Title length | char count |
| Title status | OK / Too short / Too long / Missing / Duplicate |
| Meta description | current meta text |
| Meta description length | char count |
| Meta description status | OK / Too short / Too long / Missing / Duplicate |
| H1 | current H1 text |
| H1 status | OK / Missing / Multiple H1s / Mismatch with title |
| Recommended title | proposed rewrite (if needed) |
| Recommended meta | proposed rewrite (if needed) |

### Section 5: Schema audit (4.1)

Per page type, list:

| Column | Values |
|--------|--------|
| Page type | Homepage / Service / Blog / Product / etc. |
| Sample URL | one representative URL |
| Schemas present | list |
| Schemas missing | list per visible entities and current official eligibility |
| Validation errors | list with the specific error |
| Recommended action | "Add Service schema with provider/areaServed/serviceType," etc. |
| Priority | Critical / High / Medium / Low |

### Section 6: Findings + prioritized fixes

Master list of every issue, across all 8 areas, sorted by priority.

| Column | Values |
|--------|--------|
| # | priority order |
| Area | Crawlability / Speed / Meta / Schema / Mobile / Linking / International / Security |
| Issue | one-sentence problem statement |
| Severity | Critical / High / Medium / Low |
| Pages affected | URL list or count |
| Why it matters | one-sentence impact statement |
| Recommended fix | concrete action |
| Owner type | Dev / Content / SEO / Marketing |
| Difficulty | Easy / Medium / Hard (technical complexity, not hours) |
| Dependencies | "After CMS upgrade," "Needs design input," etc. |

---
