## Audit Scope — 8 Areas

Every audit covers these eight areas. If an area is not applicable (e.g., hreflang for a single-language site), explicitly mark it `N/A` in the report with a one-line reason.

### 1. Crawlability + indexation
- `robots.txt` exists, parseable, doesn't block important pages
- XML sitemap exists, listed in robots.txt, submitted to GSC
- No accidental `noindex` / `nofollow` on indexable pages
- Canonical tags present and self-referential (or correct cross-canonical)
- Record exact redirect hops; flag loops, incorrect destinations and avoidable chains
- 4xx / 5xx error count and trend (via Ahrefs `site-audit-issues` or crawl)

### 2. Site speed + Core Web Vitals
- Mobile LCP / INP / CLS — Good / Needs Improvement / Poor
- Desktop LCP / INP / CLS
- PageSpeed Insights score (mobile + desktop)
- Lighthouse Performance / Accessibility / Best Practices / SEO scores
- Render-blocking resources, image format optimization, font loading

**Tool:** PageSpeed Insights API via WebFetch. URL pattern:
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={target}&strategy=mobile&category=performance&category=seo
```

URL-encode the target URL as a query value; run mobile and desktop separately.
The documented HTTP endpoint is `runPagespeed`.
[Google PSI v5 request reference](https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed)


### 3. Meta tags + page-level on-page 
- Title tag: present, unique per page, accurate and distinct; length is an editorial warning, not a ranking gate
- Meta description: present, unique, accurate unique summary; length is guidance, not a validity rule
- H1: clear page-primary heading and coherent hierarchy; evaluate actual page intent
- Open Graph: og:title, og:description, og:image, og:url
- Twitter Card: at least summary_large_image
- Coverage % across all indexable pages

**Optional tool:** an authorized Ahrefs Site Audit/API export or equivalent crawler to pull title/meta/H1 across pages.

### 4. Schema markup 
- Which schema types are present site-wide? (Organization, WebSite, LocalBusiness, etc.)
- Which page-type-specific schemas are present? (Article, Product, Service, FAQ, BreadcrumbList, Review)
- Validation: do schemas pass Google Rich Results Test?
- Gaps: which page types are missing schema vs. what they should have?

**Required check:** For each page type (homepage, service page, blog post, product page, category page, contact page), list:
1. Schemas present
2. Schemas missing (per actual visible entities and current Google eligibility requirements)
3. Validation errors (if any)

### 5. Mobile + accessibility
- Viewport meta tag present
- Tap target sizes adequate (≥ 48px)
- Font sizes legible (≥ 16px body text)
- Horizontal scroll / overflow issues
- Actual responsive render/interactions per page type; do not rely on the retired Mobile-Friendly Test
- Accessibility score from Lighthouse

### 6. Internal linking + site architecture
- Average internal links per page (report distribution; no universal quota)
- Orphan pages (zero internal inlinks) — list them
- Pages with most internal inlinks — should be money pages, not random blog posts
- Anchor text diversity on internal links
- Click depth from homepage — evaluate important-page discoverability against the site architecture

**Tool:** complete crawl/inlink data or authorized provider exports; record source/coverage.

### 7. International / hreflang (if applicable)
- `hreflang` tags present where multi-language pages exist
- `hreflang` tags self-reference and cross-reference correctly
- `x-default` considered where an actual fallback/language selector exists, not mandatory universally
- No mismatch between declared language and actual content language

**If N/A:** Mark the whole section N/A in one row with reason "single-language site."

### 8. Security + serving
- HTTPS site-wide, no mixed content
- HSTS header present
- Measure TTFB by comparable route/conditions; distinguish observation from a universal pass threshold
- Compression (gzip / brotli) enabled
- Caching headers sane (long-cache for static, sensible for HTML)

---
