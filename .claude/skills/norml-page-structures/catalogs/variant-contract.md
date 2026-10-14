# Block variant contract

The catalog owns structural requirements and source-backed variant selection.
Build skills own implementation assets and adapters; project contracts own
visual tokens and content. Do not create a second implementation library here.

## Minimum record for a documented variant

| Field | Meaning |
|---|---|
| Identity | Stable `{block}.{variation}` ID, source revision and source pointer |
| Purpose | The structural difference, not a color/font treatment |
| Selection | Use when, avoid when, content quantity/length fit |
| Composition | Layout, item anatomy, columns and ordering |
| Behavior | Static or interactive; interaction and state rules |
| Responsive | Desktop/tablet/mobile composition and reading order |
| Slots | Required/optional typed inputs, repeaters/groups and constraints |
| Evidence | Existing implementation/preview references and verification level |

Use a stable ID in page contracts, wireframes, admin contracts and QA. Preserve
the ID when correcting prose; give materially different anatomy or behavior a
different ID. Record source revision/commit so later changes remain traceable.
Project overrides name the original requirement and the approved replacement.

Existing blocks need not gain speculative variants. Where source evidence is
incomplete, label the missing detail unresolved and obtain a project decision
before building the affected behavior. Do not infer a tested adapter from the
existence of a layout description or screenshot.

## Selection and coverage

1. Read the complete block specification and relevant page requirements
2. Match content quantity, answer/copy length, interaction needs and available
   space to the documented use/avoid conditions
3. Record the selected ID, source revision, reason and constraints in the
   consuming workflow's existing coverage record
4. Map each source slot to its real editing/data source and target field name
5. Verify the actual runtime against the selected composition and constraints

Length budgets from an experimental variant are variant-specific source facts,
not universal copy rules. Keep their provenance and any approved override.
Rich-text length accounting must be defined by the builder; do not pretend a
WYSIWYG field enforces a budget merely because metadata contains `max_chars`.
Never truncate real content to make a variant fit; select another variant or
record an explicit composition revision.

## Projection boundary

Adapters may retag/reclass elements, add target-required nesting and omit empty
optional slots. They must preserve declared data types, required slots, reading
order, composition and static/interactive behavior. Adding undeclared slots or
changing the layout requires a documented variant/contract change, not a silent
adapter decision. CMS field aliases are explicit mappings, not duplicate slots.

Project design contracts supply colors, typography, surfaces, spacing and
motion. Structural columns and stacking live in the variant contract; exact
breakpoint values resolve through the consuming project's responsive contract.
Previews demonstrate composition only. They do not grant brand-asset reuse.
