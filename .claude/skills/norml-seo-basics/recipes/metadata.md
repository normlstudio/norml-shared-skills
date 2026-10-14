---
recipe: metadata
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every indexable public website."
---

# Recipe — Core page metadata

## Outcome

Representative public pages expose one accurate title, description, robots
directive, canonical URL, primary H1, language, and responsive viewport through
one durable metadata owner.

## Inputs

- Approved page intent, visible copy, and canonical URL.
- Strategic Messaging Context, project analysis, page SEO contract, or keyword
  research when those artifacts exist.
- Current metadata owner and representative URL/template inventory.

Do not invent keywords, claims, proof, offers, or page intent to fill a field.

## Ownership rules

- Exactly one CMS, SEO plugin, application, or theme system owns each output.
- Social/Open Graph/Twitter image work belongs to
  `social-sharing-image.md`; schema belongs to `schema-basics.md`.
- Preserve an established mature owner. A theme fallback may run only when the
  chosen owner is unavailable and must not duplicate it.
- Bulk page-by-page copy production routes to `metadata writing`; this
  recipe owns the launch-level template and representative-page baseline.

## Procedure

1. Inventory title, description, robots, canonical, H1, `lang`, and viewport on
   the homepage plus each representative public template.
2. Trace every duplicate/missing output to its platform, plugin, theme, or code
   owner.
3. Ground copy and intent in approved artifacts, then visible page content.
4. Choose one owner and disable same-purpose duplicates before adding output.
5. Configure one non-empty, intent-specific title and accurate description for
   each selected representative page/template.
6. Emit one absolute HTTPS canonical and one robots directive matching the
   approved indexability decision.
7. Align the visible primary H1 and document language with the real page intent
   without forcing them to repeat the title verbatim.

## Verification

- Exactly one non-empty `<title>` and meta description exist.
- Exactly one robots meta and one absolute HTTPS canonical exist.
- Canonical origin matches the final redirect and preferred host.
- One visible page-primary H1, valid `<html lang>`, and one responsive viewport
  exist.
- Copy is readable, intent-specific, and supported by visible/approved facts.
- No second SEO/theme/platform owner emits equivalent tags.
- Representative homepage, page, post, archive, and custom templates are checked
  where they exist.

Length guidance is diagnostic, not an automatic pass/fail cutoff. Accuracy and
intent outrank forcing copy into a character count.

## Rollback

Restore the previous owner/settings or revert the exact source change, purge
caches, and verify the earlier single output set returns.

## Evidence to record

- Representative URLs, selected owner, and copy/fact source.
- Before/after counts and values for title, description, robots, canonical, H1,
  language, and viewport.
- Duplicate-owner resolution and rollback point.

## Hard stops

- Page intent or canonical URL is ambiguous.
- The proposed copy would introduce unsupported claims or fabricated keywords.
- More than one unresolved metadata owner remains.

## Sources

- [Google: title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google: snippets and meta descriptions](https://developers.google.com/search/docs/appearance/snippet)
- [Google: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
