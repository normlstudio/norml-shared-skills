# Page-structure catalog

This package owns static page and block specifications. It describes structure,
content slots and editing/data shape. The user's design system owns visual tokens;
their CMS and build process own implementation. No other skill is required.

## Read only the relevant contracts

1. Select a page in [pages.md](pages.md) and read its complete specification.
2. Check [archetypes](archetypes/readme.md) for deeper field/layout guidance.
3. Follow each block link and read its complete contract from [blocks.md](blocks.md).
4. Apply [variant selection](variant-contract.md), record coverage and overrides,
   then verify actual rendered content with the bundled QA contracts.

## Anatomy

- `pages/`: 16 page specifications with block order, requirements and editing fields.
- `blocks/`: 43 reusable block specifications with required/optional slots and variants.
- `archetypes/`: text-only whole-page guidance; client screenshots are excluded.
- `variant-contract.md`: stable variant IDs, source version, composition and adapter rules.

## Contributions

Keep both indexes complete. A new spec needs evidence, explicit requirement levels,
condition/omission rules and a useful field contract. Update semantic version and
public changelog. Preserve existing IDs and record project overrides rather than
changing catalog defaults for one user's site. Implementation assets remain in
that project's source; do not pretend this catalog contains build code.
