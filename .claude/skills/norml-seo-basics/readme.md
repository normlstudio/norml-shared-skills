# Norml SEO Basics

> Audit or fix a website’s SEO launch baseline with dependency-aware recipes and live evidence.

## The problem

A saved setting can fail to produce the expected public metadata, sitemap or tag behavior.

One output owner, recipe-specific checks and immutable reports make the baseline reviewable.

## How to use it

| When you want to… | Say something like… |
|---|---|
| Run through SEO basics | “Run through SEO basics” |
| Set up SEO basics | “Set up SEO basics” |
| Connect Search Console | “Connect Search Console” |
| Check Google Analytics | “Check Google Analytics” |
| Check for 404s | “Check for 404s” |

## A typical run

1. “Run through SEO basics” selects analyze-only and all applicable baseline recipes.
2. Read the baseline/acceptance contracts, resolve dependencies and inventory output owners.
3. Gather live HTML/assets/sitemap and tag network/runtime evidence; keep unavailable checks
blocked.
4. Run validate-recipes.mjs and the applicable HTTP profile, then write the report and current
summary.

---

## Details

### Inputs

- Exact URL/platform/environment, output directory, approved identity/assets, selected recipe scope
and authorized access where needed.

### What it creates or changes

- Immutable timestamped Markdown report, current-state summary, machine evidence and authorized
in-scope changes with rollback.

### Capabilities

- **Recipe catalog:** 15 recipes cover launch metadata, search properties, tags, assets and
WordPress specifics.
- **Audit/fix modes:** Read-only is the default for run-through/check requests.
- **HTTP validator:** Source/asset/schema/sitemap checks for the WordPress baseline profile.
- **Current reporting:** Immutable full report plus one latest-state index.
- **Rank Math settings:** The configuration template preserves existing active
  modules and adds baseline modules idempotently; disabling modules is separate
  reviewed work.

### Inside the skill

| Path | Role |
|---|---|
| [SKILL.md](SKILL.md) | Mode selection and recipe matrix. |
| [recipes/](recipes/) | One concern, ownership and rollback per file. |
| [processes/](processes/) | Analyze-only and analyze-and-fix execution. |
| [standards/access-and-safety.md](standards/access-and-safety.md) | Portable authentication and target boundaries. |
| [scripts/validate-baseline.mjs](scripts/validate-baseline.mjs) | Public HTTP/source profile checks. |
| [templates/baseline-report.md](templates/baseline-report.md) | Immutable evidence and recipe outcomes. |

### Limits

- GA is presence-only; no property, stream, tag or version provisioning.
- 404 discovery is check-only; candidates require separate remediation review.
- No keyword research, full technical audit or legal/privacy decisions.
- Requires authorized platform/provider access for selected mutations.

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
