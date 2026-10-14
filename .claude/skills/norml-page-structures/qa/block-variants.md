# Block-variant acceptance

Apply to the selected variant, not every hypothetical variation in the catalog.
Record results in the consuming project's existing coverage/QA artifact.

- [ ] Stable variant ID, source revision, selection reason and slot mappings recorded
- [ ] Real content fits quantity/length constraints; overrides are explicit; nothing silently truncated
- [ ] Required editor fields match the specification; optional empty fields degrade safely
- [ ] Static/interactive behavior and reading order match the selected contract
- [ ] Desktop/tablet/mobile composition matches; long text and links do not overflow
- [ ] Keyboard/focus and open/closed or filter states work where applicable
- [ ] Project visual tokens remain separate; preview styling is not treated as approved design
- [ ] Actual target runtime renders populated data; generated-source checks and wireframe renders are labelled separately
- [ ] Required structured data exists in actual output and matches visible populated content; declared metadata is not counted as emitted schema

## FAQ regression cases

1. Accordion: three required pairs, independent expansion by default, coherent
   single/multiple-open configuration, keyboard operation, optional CTA absent
2. Two-column: each question pairs with its answer, static display, paired rows
   stack question-before-answer on mobile; no accidental switching answer panel
3. Grid-cards: three/two/one columns across structural breakpoints, all answers
   visible, rich-text lists/links valid, long content not clipped to fixed heights
4. CMS validation rejects fewer than three items; selected maxima agree with
   the editor; rich-text budgets use a documented validation/review rule
5. FAQPage JSON-LD read from the real populated page; no assumption that the
   adapter's `schema_emit` field proves this check

The existing IR suite covers generation and mapped-wireframe renders at 1440,
768 and 375 pixels. Preserve it as evidence of that scope only. A successful
run does not substitute for the project's target-runtime and editor checks.
