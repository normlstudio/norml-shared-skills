---
recipe: wp-media-alt-text
version: 1.0.0
scope: wordpress
baseline: conditional
depends_on: []
applies_when: "The target is WordPress and its Media Library contains image attachments."
---

# Recipe — WordPress Media Library alt text

## Outcome

Every WordPress image attachment is reviewed against its pixels and real usage.
Meaningful images have concise factual alt text; decorative/redundant images have
documented intentional blank alt; no unexplained or guessed values remain.

## Inputs

- Passing WordPress capability scan and exact Media Library target.
- Complete image-attachment inventory, actual pixels, and known page/theme/ACF/
  featured-image/SEO-setting usage.
- Production backup and approved content-management route.

## Ownership rules

- WordPress attachment `_wp_attachment_image_alt` is the reusable media value;
  rendered blocks/components may override it only when context genuinely differs.
- `supported WordPress REST API or WP-CLI` owns Media Library and attachment-meta operations.
- Alt text describes the image's purpose in its current context. It is not a
  keyword field, caption, tooltip, or automatic filename cleanup.
- Preserve useful existing values and intentional blank decorative values.

## Procedure

1. Inventory every image attachment, including unattached media and images used
   only in options, featured images, custom fields, or SEO/plugin settings.
2. Capture attachment ID, filename/title, dimensions, current alt, parent, and
   known public usages—but do not use names as substitute visual evidence.
3. Inspect the actual pixels and representative rendered context.
4. Classify each use as informative, functional, text-bearing, complex,
   decorative, or redundant.
5. Preserve accurate values. Repair only blank, filename-only, meaningless, or
   objectively wrong values with concise factual text.
6. Keep decorative/redundant alt intentionally empty and record attachment ID,
   usage, and reason.
7. Mark uninspectable or context-ambiguous images `ESCALATE`; never guess.
8. Apply reviewed changes through WordPress management and verify rendered HTML.

## Verification

- Reviewed count equals the complete image-attachment inventory count.
- Every meaningful public use has accurate alt or a documented context-specific
  override.
- Every empty alt has a recorded decorative/redundant reason.
- No filename-only, generic `image`/`photo`, keyword-stuffed, or unsupported
  description remains.
- Changed attachments render the intended alt on representative public pages.
- Useful existing values and unrelated attachment fields remain unchanged.

## Rollback

Restore the recorded before value for each changed attachment through the same
management path, then verify attachment meta and rendered HTML. Do not replace a
database/site backup merely to undo a small reviewed media set unless the owning
recovery workflow requires it.

## Evidence to record

- Total/reviewed/changed/escalated counts and every changed attachment ID.
- Pixels/usage inspected, before/after value, classification, and decision reason.
- Intentional blank IDs/reasons, rendered verification URLs, and rollback point.

## Hard stops

- Actual pixels or real usage cannot be inspected.
- The target/attachment inventory or backup route is incomplete.
- Proposed alt relies on filename, title, keywords, or inferred business intent.

## Sources

- [WordPress accessibility: alternative text for images](https://make.wordpress.org/accessibility/handbook/content/alternative-text-for-images/)
- [W3C WAI image decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)
