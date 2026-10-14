# Norml SEO Schema

> Generate truthful WordPress structured data with dynamic field maps, PHP handoffs and local
validation.

## The problem

Hardcoded JSON-LD can drift from content, duplicate plugin output or claim facts that do not exist.

A reviewed field map and one output owner keep the graph tied to real data.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Generate schema for this page | “Generate schema for this page” |
| Audit this JSON-LD | “Audit this JSON-LD” |
| Wire schema into this WordPress theme | “Wire schema into this WordPress theme” |
| Map Product schema to ACF | “Map Product schema to ACF” |

## A typical run

1. Inspect the theme’s SEO/WooCommerce output before choosing a Product renderer.
2. Read schemas/product.md and current eligibility guidance; extend the existing owner.
3. Map real title/image/price/currency/stock getters and preserve meaningful zero values.
4. Prepare the handoff and safe PHP, then validate actual rendered HTML and visible parity.

---

## Details

### Inputs

- Target pages/theme, visible content, verified entity facts, existing schema owner and available
core/ACF data.

### What it creates or changes

- Project handoff, selected JSON-LD, dynamic field proposal/map, conditional PHP and validation
evidence.

### Capabilities

- **Type contracts:** Nine schema files cover eleven core types plus article/local variants.
- **PHP mappings:** Complete reusable core/ACF field maps and conditional integration examples.
- **Advisory checks:** Node validator reads HTML/URL JSON-LD without npm dependencies.
- **Indexed inspection:** Optional provider-authenticated Search Console helper.

### Inside the skill

| Path | Role |
|---|---|
| [SKILL.md](SKILL.md) | Audit/generate and integration router. |
| [schemas/](schemas/) | Per-type fields, mappings and PHP examples. |
| [standards/eligibility.md](standards/eligibility.md) | Current vocabulary/search-feature distinctions. |
| [templates/schema-handoff.md](templates/schema-handoff.md) | Developer handoff and evidence table. |
| [scripts/validate-schema.mjs](scripts/validate-schema.mjs) | Local advisory validation. |
| [scripts/gsc-inspect.py](scripts/gsc-inspect.py) | Optional authorized indexed inspection. |

### Limits

- No guaranteed rich result, knowledge panel, ranking or immediate indexing.
- ACF examples need ACF or an approved guarded alternative.
- Local validation is not full Schema.org/Google policy validation.
- GSC inspection reports the indexed version, not a live test.

### When something is missing

Read the runtime contract and relevant bundled procedure. Report missing source
facts, access, required content or verification as unresolved/blocked; continue
independent checks. Keep project decisions and credentials outside the package.
Never guess evidence or treat a template/default as a verified live result.

### Installation and source

Copy this complete folder into the supported skill directory of your chosen
agent runtime. The runtime must discover SKILL.md and its relative supporting
files. See the collection guide for tested local installation. No remote CLI
installation or runtime compatibility is promised without that verification.

Source: the supplied norml-shared-skills collection. This package is standalone;
related Norml packages mentioned in SKILL.md are optional companions.

---

Covers SKILL.md v1.0.0
Last changelog entry: v1.0.0
Generated: 2026-10-13
