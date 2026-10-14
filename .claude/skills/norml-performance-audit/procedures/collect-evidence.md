# Collect performance evidence

## PageSpeed Insights

HTTP endpoint verified against [the official PSI reference](https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed) on Oct 13, 2026.

Use the provider's public API for the supplied URL. The endpoint may be quota limited and
may require provider-issued authentication. Reuse an authorized connection; protect keys in
the OS/provider store and redact URLs/logs. Never ask for pasted secret values.

```bash
curl --get --fail --silent --show-error \
  'https://www.googleapis.com/pagespeedonline/v5/runPagespeed' \
  --data-urlencode 'url=https://example.com/' \
  --data-urlencode 'strategy=mobile' \
  --data-urlencode 'category=performance' \
  --output mobile-psi.json
```

Repeat with `strategy=desktop` and a separate output file. Percent-encoding matters for URLs
with query strings. Record HTTP errors and whether Lighthouse/field data were actually returned.
Extract `lighthouseResult.categories.performance.score` (multiply by 100), audit numeric values,
units, display values and detail items. Preserve `loadingExperience` and
`originLoadingExperience` provenance separately when present. Neither may exist for low-traffic URLs.

Lighthouse navigation commonly reports LCP, CLS, FCP, TBT and Speed Index. It does not provide
field INP by simply substituting FID/TBT. INP is a field interaction metric; record real-user
p75 and window when available. Additional interaction traces are diagnostic samples, not CrUX.

## HTTP timing and headers

```bash
curl --location --compressed --silent --show-error \
  --output /dev/null \
  --write-out 'status=%{http_code} protocol=%{http_version} final=%{url_effective} redirects=%{num_redirects} dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total} bytes=%{size_download}\n' \
  'https://example.com/'
curl --location --compressed --silent --show-error \
  --dump-header response-headers.txt --output page.html 'https://example.com/'
```

GET headers better represent page behavior than assuming HEAD is identical. Inspect content
encoding, cache control, validators, protocol and redirect chains. Separate network location,
cold/warm cache and server response from frontend rendering. A single curl timing is not a
population estimate. Do not publish cookies or private response content in the report.

## HTML/resources

- Identify blocking styles/scripts, execution order and third-party domains; do not blindly defer
  code that another script needs first.
- Inspect image dimensions, encoded bytes, `srcset`, `sizes`, loading and fetch priority.
  Use correct `width`/`height` or aspect ratio. Do not lazy-load the primary LCP image.
- Inspect fonts, subsets, `font-display`, fallback metrics and duplicate requests.
  Only preload critical actually-used fonts/resources with correct cross-origin handling.
- Record large inline payloads, DOM count, JS long tasks and unused CSS evidence.
- With source access inspect Vite/Webpack splitting/minification, image pipeline and HTTP config.
  Filename or bundle size alone does not prove unused code or a safe deletion.

## Comparable before/after

Keep the same URL, device, test tool/version, throttling, auth/consent state and cache scenario.
Record repeated-run median/range where possible; state sampling limitations. Never compare a
warm local desktop run to a cold public mobile baseline as proof of improvement.

## Diagnostic cutoffs

| Metric | Good upper bound | Needs improvement | Poor |
|---|---|---|---|
| LCP | 2.5 s | >2.5 to 4 s | >4 s |
| CLS | 0.1 | >0.1 to 0.25 | >0.25 |
| INP | 200 ms | >200 to 500 ms | >500 ms |

Field Core Web Vitals assessment uses p75; Lighthouse navigation is laboratory evidence.
FCP, TTFB, TBT and Speed Index are additional diagnostics, not the three Core Web Vitals.
Consult current official metric/provider documentation when versions change before reporting.
