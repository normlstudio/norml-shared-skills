# norml-skill-creator

> Build source-backed skills with clear audience, portable structure, truthful docs and verified
discovery.

## The problem

A copied folder can retain private paths, dependencies and data. A polished guide can also promise
behavior that the source never implemented.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Create a skill | *"create a skill"* |
| Scaffold a skill | *"scaffold a skill"* |
| Build a client skill set | *"build a client skill set"* |
| Where should this skill live | *"where should this skill live"* |
| Migrate existing skills | *"migrate existing skills"* |
| Prepare skills for sharing | *"prepare skills for sharing"* |

## A typical run

1. Resolve audience, intent, source owner and adjacent skills.
2. Select shared, internal, client, product or public packaging.
3. Write grounded procedures, failures and acceptance checks.
4. Check links, boundaries, scripts and truthful human docs.
5. Execute these separate effects only when requested.

---

## Details

### Inputs

- Build/scaffold/extend/migrate intent and intended audience.
- Canonical source, actual owner and authorized destination.
- Permitted verification effects and runtime scope if installation is requested.

### What it creates or changes

- One matching slug/frontmatter source package.
- Semantic procedures/contracts and truthful Markdown documentation.
- Source/destination hash mapping for migrations.
- Explicit package, discovery and publication status.

### Commands in depth

#### Create a skill

*"create a skill"* — Resolve intended outcome/audience, existing source and adjacent skills before
building grounded procedures.

#### Scaffold a skill

*"scaffold a skill"* — Create requested structure and label missing procedures/tests; do not claim
an empty scaffold is usable.

#### Build a client skill set

*"build a client skill set"* — Verify client prefix/source owner and actual flow definitions; keep
current client data separate.

#### Where should this skill live

*"where should this skill live"* — Choose storage by process ownership and audience, independent
of cwd or data-folder location.

#### Migrate existing skills

*"migrate existing skills"* — Inventory/hashes first, preserve source, normalize links and verify
before removing originals.

#### Prepare skills for sharing

*"prepare skills for sharing"* — Classify include/rewrite/omit, produce a separate portable
edition and verify the requested local package.

### Inside the package

- [SKILL.md](SKILL.md)
  Audience/action routing and completion contract
- [index.md](recipes/index.md)
  Creation scope selection
- [prepare-public-skill.md](recipes/prepare-public-skill.md)
  Include/rewrite/omit public boundary
- [migrate-existing-skill.md](recipes/migrate-existing-skill.md)
  Source hashes, preservation and cutover
- [create-and-verify.md](processes/create-and-verify.md)
  Grounded build and discovery lifecycle
- [package-structure.md](standards/package-structure.md)
  Semantic anatomy and source/doc roles
- [creation-contract.md](qa/creation-contract.md)
  Evidence-based readiness gates

### Limits

- No mandatory company registry, cloud drive or host organization.
- Scaffolds are explicitly incomplete.
- Package creation does not authorize remote creation, visibility change, runtime installation or
  website release.
- Live transactions are not migration verification fixtures.

### When something breaks

- **A skill already owns the procedure.** Extend that owner; do not invent overlapping triggers.
- **Destination or runtime name collides.** Inspect exact target and preserve the existing
  directory/link.
- **Original changed during migration.** Reconcile against fresh hashes before any cutover.
- **Install or live test cannot run.** Report created/not installed or unverified, not ready
  everywhere.

### Source of truth

[SKILL.md](SKILL.md) routes runtime operations. The linked procedures provide the full operational
checks. This guide explains the public package and does not add authority or claim live access.

---

_Covers SKILL.md v1.0.0 | Last changelog entry: v1.0.0 | Generated: 2026-10-13._
