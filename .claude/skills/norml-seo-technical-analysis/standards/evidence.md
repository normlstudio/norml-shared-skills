# Evidence and interpretation

## Measurement source

Record URL/final response, timestamp, tool/version, device/network, raw artifact
path and scope for every finding. Do not publish visitor identifiers, tokens or
private response dumps. Use provider-managed OAuth or OS-protected credentials
for authorized analytics/search sources. Never put keys in request arguments/logs.

## Core Web Vitals

Use current official thresholds and real field observations when available:
LCP good ≤2.5s, INP good ≤200ms, CLS good ≤0.1 at the 75th percentile. Distinguish
URL versus origin scope and mobile versus desktop. Missing field data is unknown,
not failure or success. Lighthouse lab scores and synthetic metrics are diagnostics;
they cannot prove field INP or full Core Web Vitals acceptance.

[Web Vitals guidance](https://web.dev/articles/vitals)
[PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/about)

## Coverage and recommendations

- Crawling vs indexing is distinct; robots blocking is not a guaranteed deindexing
  mechanism. A noindex directive must be seen by the crawler to be processed.
- A canonical is a signal; compare live intention with indexed evidence when available.
- Metadata lengths, link counts, click depth, font sizes and TTFB values are heuristics
  to contextualize, not universal search-policy pass/fail thresholds.
- Hreflang applies to verified alternate language/region representations, with
  reciprocal relations and correct canonical scope. x-default is optional.
- Retired search features/tests are not required checks. FAQ rich results and the
  Sitelinks Search Box are retired; Mobile-Friendly Test is retired. Confirm current
  Google feature guidance before recommendations.
- Review header/cache recommendations against actual platform/route needs. HSTS
  changes require a separate authorized implementation/recovery review.
- No defined source scoring method exists for a combined health score. Omit it or
  explicitly show an approved reproducible formula; do not invent authoritative math.

[Google Search documentation](https://developers.google.com/search/docs)
[Search documentation updates](https://developers.google.com/search/updates)
