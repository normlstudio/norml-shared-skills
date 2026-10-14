---
recipe: favicon
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every public website."
---

# Recipe — Favicon and site icons

## Outcome

The site exposes a recognizable, approved icon family across browsers, search,
bookmarks, Apple touch surfaces, and installed-web-app contexts.

## Inputs

- Approved logo mark, monogram, or existing site identity source.
- Canonical site name and approved brand colors.
- Access to the platform's Site Icon/favicon management surface and code/assets
  only when that platform requires them.

Do not invent a logo. WordPress/core/host/theme placeholder art is not an approved
identity source.

## Required asset set

| Role | Format | Size |
|---|---|---:|
| Modern scalable favicon | SVG | square viewBox |
| Legacy root favicon | ICO | include 16 × 16 and 32 × 32 |
| Browser PNG fallbacks | PNG | 16 × 16 and 32 × 32 |
| Apple touch icon | PNG | 180 × 180 |
| Web-app/site icons | PNG | 192 × 192 and 512 × 512 |
| WordPress Site Icon | PNG | square, at least 512 × 512 |

Google Search accepts a square favicon from 8 × 8 and recommends more than
48 × 48. Norml's complete family above covers browser/search, Apple, legacy, and
manifest roles without treating the minimum as the delivery target.

## Ownership rules

- The platform/CMS owns its Site Icon setting; approved source assets remain in
  the project's durable asset source when code-backed.
- WordPress Site Icon output and theme favicon/manifest output must not create
  unnecessary same-role duplicates.
- A Site Icon is not automatically the Organization logo used in schema.
- Keep the favicon URL stable during normal operation. When replacing heavily
  cached bytes, publish one new versioned/content-addressed URL, switch references,
  then keep that URL stable.

## Procedure

1. Inventory live favicon links, `/favicon.ico`, manifest, platform Site Icon,
   actual pixels, MIME types, and current source provenance.
2. Verify the approved identity source and crop/optically simplify it for small
   square use without inventing a new mark.
3. Generate the required sizes deterministically from the approved source.
4. Inspect actual rendering at 16, 32, 180, and 512 pixels.
5. Set the platform Site Icon through its admin surface. On WordPress, use the
   Media Library/Site Icon setting with the 512 source.
6. Add the SVG/ICO/PNG/Apple/manifest links through the platform's durable owner.
7. Make `/favicon.ico` return the approved ICO bytes with an image MIME type.
8. Purge relevant caches and use fresh URLs when the icon bytes changed.

## Verification

- All declared URLs return 2xx image responses with correct MIME and dimensions.
- `/favicon.ico` returns non-empty image bytes, not a homepage HTML fallback.
- Live favicon hashes match the approved generated family.
- Googlebot/Image can crawl the homepage and favicon URL.
- The icon is recognizable at 16 and 32 pixels.
- Manifest JSON parses and its 192/512 icon declarations match real files.
- WordPress, when applicable, points `site_icon` to a valid square ≥512 attachment.
- No WordPress/default/host placeholder survives in a fresh browser context.

## Rollback

Restore the previous Site Icon setting and asset references, purge caches, and
verify the previous public bytes. Preserve earlier files until rollback is proven.

## Evidence to record

- Approved identity source and role decision.
- Asset paths/URLs, dimensions, MIME types, and SHA-256 hashes.
- Platform Site Icon attachment/setting, manifest result, and root-favicon result.
- Rendered small-size inspection and rollback point.

## Hard stops

- No approved identity source exists.
- The proposed asset is WordPress/core/host/theme placeholder art.
- Live URLs return HTML, wrong MIME, wrong dimensions, or stale unapproved bytes.

## Sources

- [Google Search favicon requirements](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [WordPress: create a favicon / Site Icon](https://wordpress.org/documentation/article/create-a-favicon/)
- [Apple: webpage touch icons](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)
