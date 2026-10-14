---
name: norml-skill-creator
version: 1.0.0
description: >
  Create, extend, migrate or package source-backed skills with clear audience,
  portable naming, semantic folders, truthful human docs and explicit runtime
  discovery. Use for create a skill, scaffold a skill, build a client skill set,
  where should this skill live, migrate existing skills, or prepare skills for sharing.
metadata:
  author: Norml Studio
---

# Norml Skill Creator

Build reusable procedures in a user-owned package. A folder or polished guide alone does not
prove a skill works. This public edition needs no company registry, repository naming scheme,
cloud drive or global setup installer.

## Inputs and discovery

Resolve intent (scaffold/build/extend/migrate/public packaging), process, audience, owning project,
expected outcomes, source material, authorized destination and permitted verification effects.
Read project instructions, existing adjacent skills and installed names before choosing a new name.
Use the author identity explicitly configured by the user; never guess an email or use `whoami`.

Current explicit decisions win over historical rules. Source evidence supplies facts, not unlimited
implementation authority. Separate confirmed behavior, inferred structure, unresolved choices and
promised follow-ups. Do not invent credentials, variants, acceptance results, pricing or forecasts.

## Choose a recipe

Read [routing](recipes/index.md), [naming/storage](standards/naming-and-storage.md) and
[package anatomy](standards/package-structure.md), then the applicable procedure:

| Request | Recipe |
|---|---|
| Reusable method across projects | [Shared skill](recipes/create-shared-skill.md) |
| Organization-private operation | [Internal skill](recipes/create-internal-skill.md) |
| One client’s procedures or flow tests | [Client skill](recipes/create-client-skill.md) |
| Product-coupled implementation | [Product-local skill](recipes/create-product-skill.md) |
| External sharing | [Public package](recipes/prepare-public-skill.md) |
| Move/rename an existing source | Also [migration](recipes/migrate-existing-skill.md) |

All routes use [create and verify](processes/create-and-verify.md). Extend an existing owner when
it already fits; do not create duplicate vague triggers to avoid resolving overlapping ownership.
A one-off deliverable runs the existing procedure instead of generating another skill. A third-party
pack retains its provenance and chosen reference location; do not install it globally by inference.

## Completion

Run [creation acceptance](qa/creation-contract.md), then report actual source, version, files,
validation, intended runtime discovery and unverified boundaries. [Routing cases](qa/routing-cases.md)
exercise creator changes. A scaffold is explicitly incomplete; a package is not a published release.

Commit/push, remote creation, visibility changes, public releases, website publication and runtime
installation each obey the user’s requested scope. Optional bundled `norml-git` supplies Git mechanics
and `norml-security` supplies credential handling; neither is required to follow the inline boundaries.
If unresolved work needs durable planning, optional `norml-tasks` can capture it in its actual owner.

## Hard boundaries

- Reusable procedure/source belongs in the package; client/account data, live evidence and secrets do not.
- Use one canonical source. Runtime adapters point to it, never maintained competing copies.
- A colleague-share request does not authorize public hosting or sharing another client’s material.
- No generic support drawers, machine-specific paths, copied auth sessions or empty claims of readiness.
- No live purchases, refunds, publishing or customer mutations merely to prove migration or packaging.
- Preserve source hashes and history before a move; archive/remove only after verified cutover authority.
- Prefer supported APIs/CLIs; failed auth is not permission for browser takeover or secret copying.
- Record evidence-backed verification, missing access and blocked branches honestly.
