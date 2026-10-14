---
recipe: microsoft-clarity
version: 1.0.0
scope: universal
baseline: recommended
depends_on:
  - google-tag-manager
  - consent-management
applies_when: "The project approves behavioral analytics and has a Microsoft Clarity project."
---

# Recipe — Microsoft Clarity

## Outcome

Microsoft Clarity records the intended site through one Clarity tag inside the
verified Google Tag Manager container.

This recipe never installs GTM, decides consent, or embeds Clarity directly on
the site. Run `google-tag-manager.md` and `consent-management.md` first.

## Inputs

- Passing Google Tag Manager recipe and edit/publish access to its container.
- Approved Clarity project mapped to the exact canonical site.
- Clarity project ID and passing/evidence-backed-N/A consent decision.

If no project exists or behavioral analytics is not approved, record
`SKIP — not provisioned`; do not create a speculative project.

## Ownership rules

- GTM is the only website-side owner of Clarity.
- Prefer Microsoft's official Clarity GTM template or Clarity's guided GTM
  connection.
- Do not paste Clarity's manual tracking script into theme code, CMS header
  fields, snippet plugins, or another analytics plugin.
- One Clarity project maps to one intended tag unless the project documents a
  deliberate environment split.

## Procedure

1. Confirm the GTM and consent-management dependencies pass (or consent is an
   evidence-backed `N/A`), then inspect the live site/GTM workspace for an
   existing Clarity tag or direct `clarity.ms` embed.
2. Verify the Clarity project belongs to the exact production domain.
3. In GTM, create a tag from **Microsoft Clarity — Official**, enter the approved
   project ID, and use `All Pages` unless an approved consent design requires a
   different trigger.
4. Alternatively, use Clarity's `Settings → Setup → Google Tag Manager` guided
   connection when the account permissions and project policy allow it.
5. Preview the tag, inspect its network request, and publish a named GTM version.

## Verification

- GTM Preview shows the Clarity tag firing once under the intended condition.
- Browser network evidence shows the intended Clarity project request.
- Clarity's setup verification recognizes the installation.
- No direct Clarity snippet exists in public source, CMS settings, or repository
  code outside the GTM-delivered tag.
- No duplicate Clarity project/tag fires on one page view.

## Rollback

Restore the previous GTM container version or pause/remove the Clarity tag,
publish, and verify Clarity requests stop while GTM and GA remain intact.

## Evidence to record

- Clarity project name and safe project ID.
- GTM tag/template, trigger, and published container version.
- Preview, live request, duplicate, and Clarity verification results.
- Consent state and rollback version.

## Hard stops

- GTM or consent-management dependency does not pass.
- Project/domain mapping is ambiguous.
- Behavioral analytics is not approved or required consent gating is unresolved.
- An existing direct or GTM Clarity implementation has unresolved ownership.

## Sources

- [Microsoft: install Clarity with Google Tag Manager](https://learn.microsoft.com/en-us/clarity/third-party-integrations/google-tag-manager)
