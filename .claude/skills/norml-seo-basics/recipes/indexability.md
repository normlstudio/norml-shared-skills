---
recipe: indexability
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every public website; production must match its approved launch/indexing state."
---

# Recipe — Indexability and canonical environment

## Outcome

The final public environment has one preferred HTTPS host and exposes the
approved indexability state. Production launch pages can be crawled and indexed;
staging, private, and pre-launch environments remain protected.

## Inputs

- Exact production URL, platform/CMS, and environment policy.
- Approved launch/indexing state and preferred canonical host.
- Access to the platform, CDN/host, and SEO owner that can emit visibility
  controls.

Do not infer that a publicly reachable URL is approved for indexing.

## Ownership rules

- The platform/environment policy owns whether a site is public or private.
- One SEO owner emits page-level robots and canonical output.
- Host/CDN headers must not silently override the platform decision.
- `robots.txt` manages crawling; it is not the mechanism for keeping sensitive
  pages out of search. Use authentication or `noindex` through the real owner.

## Procedure

1. Follow HTTP through every redirect and identify the final HTTPS host.
2. Compare platform URLs, DNS/CDN, canonical tags, sitemap origins, and the
   approved preferred host.
3. Inventory environment-level privacy, authentication, maintenance mode,
   platform search visibility, `X-Robots-Tag`, and page robots meta.
4. On WordPress, review `home`, `siteurl`, `blog_public`, front-page mode,
   permalink structure, and the selected SEO owner's global/page robots.
5. Preserve private/noindex behavior on staging and pre-launch targets.
6. On an approved production launch, repair only the proven blocking owner and
   normalize redirects/canonical origin one layer at a time.
7. Purge relevant caches and repeat the checks as logged-out normal-user and
   Googlebot requests.

## Verification

- Final production response is 2xx HTML over HTTPS after one stable redirect
  policy.
- Platform URL settings, canonical, Open Graph URL, and sitemap origin agree.
- Approved indexable pages have no blocking authentication, maintenance page,
  `X-Robots-Tag: noindex`, or robots `noindex`/`nofollow` directive.
- Private/staging pages retain their approved protection.
- Canonical URLs are absolute, use the preferred host, and do not point across
  environments.
- Normal-user and Googlebot responses agree unless a documented feature explains
  the difference.

## Rollback

Restore the previous environment visibility, platform URL, header, robots, or
redirect setting through its owner. Purge caches and prove the prior public or
private behavior returns.

## Evidence to record

- Requested/final URL, redirect chain, preferred host, and environment state.
- Platform visibility setting plus header/meta robots evidence.
- Canonical output, normal-user/Googlebot comparison, owner, and rollback point.

## Hard stops

- Production/staging identity or approved launch state is ambiguous.
- A redirect, URL-setting, or noindex change could expose a private environment.
- Header/meta/SEO ownership is duplicated or unresolved.

## Sources

- [Google: block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Google: canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: robots.txt is not an indexing control](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
