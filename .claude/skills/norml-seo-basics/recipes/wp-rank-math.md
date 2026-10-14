---
recipe: wp-rank-math
version: 1.0.1
scope: wordpress
baseline: conditional
depends_on: []
applies_when: "The target is WordPress and has no established mature SEO owner, or already uses Rank Math."
---

# Recipe — WordPress Rank Math

## Outcome

Rank Math is the single verified WordPress owner for metadata, the base schema
graph, and XML sitemaps, with settings grounded in the real site architecture.

## Inputs

- Passing WordPress capability scan and exact production target.
- Current active/must-use plugin and theme output inventory.
- Approved site/publisher identity, homepage copy, social image, and schema facts.
- Actual post types, taxonomies, author model, archive policy, and indexability.
- Production backup and source/deployment contract.

## Ownership rules

- **Blank/new WordPress site with no SEO owner:** use current Rank Math free from
  the official WordPress plugin repository.
- **Established Rank Math site:** repair it in place and preserve unrelated
  settings.
- **Yoast, SEOPress, AIOSEO, or mature custom owner exists:** mark this recipe
  `N/A — existing owner` unless the user explicitly requests a migration.
- Never run two metadata/schema/sitemap owners concurrently.
- Rank Math Analytics stays off. Preserve one approved existing Google Analytics
  owner, preferably GTM; `google-analytics.md` checks its presence without
  provisioning it.

## Procedure

1. Through `supported WordPress REST API or WP-CLI`, capture plugins, relevant options/meta, public head
   output, schema, sitemaps, and caches before mutation.
2. Create the required database/plugin/code rollback checkpoint.
3. Install/activate the current official free plugin through WordPress management
   and verify its WordPress.org checksum.
4. Skip external account registration unless a separately approved feature needs
   it. Use Advanced setup mode.
5. Enable the minimum relevant modules:
   - Link Counter;
   - SEO Analysis;
   - Sitemap;
   - Schema (Rich Snippets).
6. Leave Analytics, Content AI, AI Visibility, Instant Indexing, ecommerce,
   community, and other integrations off unless the actual site requires them.
7. Configure from verified facts:
   - organization/person identity and approved logo only when one exists;
   - homepage title, description, canonical, robots, and social image;
   - conservative archives and attachment redirects;
   - no default Article schema on generic Pages;
   - post-type/taxonomy sitemap inclusion from actual architecture;
   - author archives off/noindex for a single-author site and reviewed for a real
     multi-author publication;
   - tags/attachments and other thin outputs excluded unless intentionally useful.
8. For code-backed projects, derive an idempotent project script from
   `templates/configure-rank-math.php`, commit it, and run it twice to prove stable
   output. This script stores reproducible SEO settings; it must not contain GTM,
   GA, or Clarity embeds. The template preserves existing active modules and
   adds the required baseline modules; disabling any existing module needs its
   own reviewed scope and before/after map.
9. Flush Rank Math sitemap cache, rewrite rules, object/page/CDN caches as needed.

## Verification

- Rank Math is active at a recorded version and its checksum passes.
- The setup/wizard state is complete without an unnecessary account dependency.
- Only justified modules are active; Rank Math Analytics is off when GA uses GTM.
- Exactly one title/description/robots/canonical/OG/Twitter set exists.
- Exactly one connected base schema graph exists with no duplicate IDs.
- `/sitemap_index.xml` and sampled child maps return valid XML.
- Core `/wp-sitemap.xml` is disabled/redirected or deliberately documented as the
  chosen owner instead of Rank Math.
- `robots.txt` points once to the canonical sitemap and does not block public
  indexing.
- The idempotent project config, when used, succeeds twice without duplicate
  media/settings drift.

## Rollback

Restore the database/options checkpoint, plugin state, and prior code commit;
purge caches; then verify that the original single SEO owner and public output are
restored.

## Evidence to record

- Plugin version/checksum, modules, setup mode, and account-connection decision.
- Metadata/schema/sitemap owner table and representative live counts.
- Post-type/taxonomy/archive policy.
- Config-script path/run result, backup, activity log, commit/deploy when code was
  involved, and rollback result.

## Hard stops

- Another mature SEO owner exists and migration was not explicitly requested.
- Production backup or WordPress capability record is missing.
- Site identity/entity facts or indexability intent are ambiguous.
- Public output remains duplicated or cache-purged verification fails.

## Sources

- [Rank Math setup guide](https://rankmath.com/kb/how-to-setup/)
- [Rank Math sitemap configuration](https://rankmath.com/kb/configure-sitemaps/)
- [Rank Math titles and meta settings](https://rankmath.com/kb/titles-and-meta/)
