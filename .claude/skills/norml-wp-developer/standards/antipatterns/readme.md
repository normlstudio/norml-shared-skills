# Development antipattern catalog — v1.0.0

Audit code-shipping tasks before completion. Record detector output and PASS/FAIL/WAIVED
with a technical reason; no unwaived failure may be silently called complete.

| Pattern | Detector/fix |
|---|---|
| Per-page CSS shadow design system | [Per-page CSS](per-page-css-files.md) |

The catalog supplements [the CSS system](../css-design-system.md) and inherited-project
standards. It governs implementation patterns, not a universal visual taste. Pure docs
and read-only QA have no authored code to audit. Add future entries only with grounded
failure/acceptance evidence and an explicit public package version/changelog update.
