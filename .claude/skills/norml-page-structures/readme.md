# Norml Page Structures

> Plan page elements and editing fields from a complete reusable page/block catalog.

## The problem

A template can look finished while missing required content, navigation or editor fields.

This catalog makes structure, content slots and conditional requirements explicit before building.

## How to use it

| When you want to… | Say something like… |
|---|---|
| What elements belong on this page? | “What elements belong on this page?” |
| Check missing page elements | “Check missing page elements” |
| Plan a blog single and archive | “Plan a blog single and archive” |
| Choose a block variant | “Choose a block variant” |

## A typical run

1. Select a service page in catalogs/pages.md and read its full specification.
2. Read the hero, benefits, proof, FAQ and other referenced block contracts.
3. Map fields and record missing required facts as unresolved; pin variants and explicit overrides.
4. Build using the user’s design system, then apply qa/block-variants.md against actual content.

---

## Details

### Inputs

- Page type, project brief, recorded design/content decisions and existing CMS/build contract.

### What it creates or changes

- Source-derived page coverage with requirement levels, conditions, editor sources and rendered
evidence.

### Capabilities

- **Page specifications:** 16 linked page specifications preserve ordered elements and conditional
defaults.
- **Block contracts:** 43 blocks include slot/data shapes, implementation choices and variants.
- **Variant acceptance:** Stable IDs, source version, use/avoid conditions and runtime coverage.
- **Bio archetype:** Text-only layout/ACF field contract without client screenshots.

### Inside the skill

| Path | Role |
|---|---|
| [SKILL.md](SKILL.md) | Runtime reading and coverage router. |
| [catalogs/pages.md](catalogs/pages.md) | Discover 16 page specifications. |
| [catalogs/blocks.md](catalogs/blocks.md) | Discover 43 block specifications. |
| [catalogs/variant-contract.md](catalogs/variant-contract.md) | Selection and adapter boundaries. |
| [qa/toc-required.md](qa/toc-required.md) | Actual blog-navigation acceptance. |

### Limits

- Does not contain target framework code or a visual design system.
- Cannot invent missing content, evidence, assets or integration behavior.
- Defaults may be overridden by an explicit recorded project decision.

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
