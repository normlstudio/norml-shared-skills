---
recipe: social-sharing-image
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every public website that can be shared by URL."
---

# Recipe — Social sharing image

## Outcome

Every public page has one valid Open Graph/Twitter sharing set and a dependable
default social image, with page-specific overrides where approved content exists.

## Inputs

- Approved brand identity, page title/description, and canonical URL.
- Approved default social-card artwork.
- Existing metadata/SEO owner and platform editing path.

## Asset contract

- catalog default: **1200 × 630 px** (1.91:1).
- Use JPEG or PNG unless a target platform has a documented approved exception.
- Keep important text/logos away from edges and inspect both wide preview and
  smaller crop/thumbnail contexts.
- Use an absolute HTTPS public URL with an image MIME type.
- Give changed bytes a fresh versioned/content-addressed URL to defeat stale
  social caches.

## Ownership rules

- One SEO/metadata system owns Open Graph and Twitter output.
- The default card is a fallback; a page-specific approved image may override it.
- Do not let theme, plugin, and CMS integrations emit competing tag sets.
- The image's `og:image:alt` describes the image, not a caption or keyword list.

## Procedure

1. Inventory current `og:*`, Twitter/X card tags, owners, image responses, and
   duplicates on representative page types.
2. Create/approve the 1200 × 630 default card from verified brand assets and copy.
3. Upload it through the platform's durable media/admin path or versioned assets.
4. Configure the one owner to emit at minimum `og:title`, `og:type`, `og:url`,
   `og:image`, and accurate description/site-name data.
5. Emit image URL, MIME type, width, height, and meaningful image alt metadata.
6. Configure a `summary_large_image` Twitter card with explicit title,
   description, image, and image alt where the owner supports it.
7. Add page-specific cards only when their assets and copy are approved.

## Verification

- Exactly one intended Open Graph/Twitter set exists in live HTML.
- Canonical URL and `og:url` use the same preferred HTTPS origin.
- Image URL returns 2xx, an image MIME type, and actual 1200 × 630 dimensions or
  the documented exception.
- Live bytes match the approved asset hash and changed images use a fresh URL.
- `og:image:alt` is present and factual.
- Representative homepage, content page, and article/post preview data are
  correct; no placeholder/default theme image survives.

## Rollback

Restore the previous metadata-owner settings and image URL, purge relevant caches,
and verify the previous live tag set.

## Evidence to record

- Metadata owner and settings location.
- Default/page-specific image URLs, dimensions, MIME, hashes, and source assets.
- Live duplicate counts and representative page checks.
- Cache-busting URL and rollback point.

## Hard stops

- No approved brand/image source exists.
- More than one unresolved metadata owner emits the same tags.
- The image/copy would introduce an unsupported claim.

## Sources

- [The Open Graph protocol](https://ogp.me/)
