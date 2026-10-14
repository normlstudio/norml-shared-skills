# Performance audit — {URL}

- Date/tool version/device/throttling: {actual metadata}
- Final URL/redirects/cache/auth/consent state: {observed conditions}
- Source inspection: {path/scope or unavailable}
- Runs/sample/variability: {actual evidence}

## Measurement summary

| Metric | Mobile lab | Desktop lab | Field p75/window | Provenance/status |
|---|---|---|---|---|
| Lighthouse performance score | {value/unavailable} | {value/unavailable} | n/a | {tool/version} |
| LCP | {value/unit} | {value/unit} | {URL/origin/window or unavailable} | {status} |
| CLS | {value} | {value} | {URL/origin/window or unavailable} | {status} |
| INP | n/a unless measured interaction trace | n/a unless measured | {field value or unavailable} | {status} |
| FCP / TTFB / TBT | {diagnostics} | {diagnostics} | {available diagnostics} | {not CWV substitutes} |

## Prioritized findings

### {finding title}

- Observation and affected metric: {specific measured problem}
- Evidence: {audit ID, resource/selector, size, timing, local file or trace}
- Impact: {High/Medium/Low with measured causal rationale}
- Scope/dependencies: {qualitative, no invented duration/cost}
- Proposed fix: {stack-specific implementation, configuration or snippet}
- Validation: {comparable test and functional checks}
- Limits: {what the evidence cannot establish; no promised numeric gain}

## What's working

{Observed good behavior worth retaining}

## Implementation checklist

- [ ] {evidence-backed fix, owner if verified}
- [ ] {comparable post-change measurement and regression check}

## Unchecked/unavailable

{Quota, field data, source access, authenticated pages, real interaction or provider limitations}
