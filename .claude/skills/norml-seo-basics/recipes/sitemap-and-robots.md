---
recipe: sitemap-and-robots
version: 1.0.0
scope: universal
baseline: required
depends_on:
  - indexability
applies_when: "Every indexable public website."
---

# Recipe — XML sitemap and robots.txt

## Outcome

The site exposes one canonical, valid XML sitemap containing intentional
indexable URLs, and `robots.txt` points to it without blocking the public site.

## Inputs

- Passing indexability recipe and preferred canonical origin.
- Actual public page/content/taxonomy architecture.
- Current sitemap and robots owners across platform, SEO plugin, application,
  CDN, and host.

## Ownership rules

- Exactly one platform/SEO/application system owns the canonical sitemap index.
- `robots.txt` has one durable owner and one canonical `Sitemap:` pointer.
- Do not keep a second independent WordPress core/plugin/theme sitemap merely
  because both URLs return 200.
- A sitemap includes discoverable canonical URLs; it does not override
  `noindex`, redirects, authentication, or broken pages.

## Procedure

1. Inventory every advertised/discovered sitemap and every `Sitemap:` line.
2. Parse each candidate index/child map and sample its URLs, statuses,
   canonicals, indexability, and preferred-host origin.
3. Choose the established mature owner or the platform-native owner.
4. Configure inclusion from actual architecture: intentional public page/post/
   product/CPT types and useful archives only.
5. Exclude private, redirecting, error, attachment/thin, duplicate, and noindex
   URLs unless project architecture explicitly justifies them.
6. On WordPress, reconcile the selected SEO-plugin index with
   `/wp-sitemap.xml`; disable/redirect or explicitly retain one owner.
7. Make `/robots.txt` return successfully, avoid a production `Disallow: /`,
   and include one absolute preferred-host `Sitemap:` line.
8. Flush only sitemap/rewrite/cache layers needed by the owner.

## Verification

- Canonical sitemap/index returns 2xx XML with at least one valid `<loc>`.
- Every listed/sampled child map returns 2xx parseable XML.
- Sampled URLs are canonical, indexable, 2xx, and use the preferred HTTPS host.
- No independent duplicate sitemap owner remains.
- `/robots.txt` returns successfully, does not blanket-block production, and
  points once to the canonical sitemap.
- Staging/private URLs do not leak into the production sitemap or robots output.

## Rollback

Restore the prior sitemap/robots owner settings or source, flush the same caches,
and verify the previous index and pointer return without leaving both owners on.

## Evidence to record

- Owner, canonical sitemap URL, child-map count, and sampled URL results.
- Included/excluded content types/taxonomies and reasons.
- `robots.txt` status/pointer, duplicate-owner decision, and rollback point.

## Hard stops

- Indexability dependency does not pass.
- Sitemap/robots owner or intended content architecture is ambiguous.
- The proposed sitemap includes private, noindex, redirecting, or wrong-host URLs.

## Sources

- [Google: build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Google Search Console Sitemaps report](https://support.google.com/webmasters/answer/7451001?hl=en)
