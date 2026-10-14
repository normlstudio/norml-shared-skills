---
recipe: consent-management
version: 1.0.0
scope: universal
baseline: conditional
depends_on:
  - google-tag-manager
applies_when: "A selected analytics/advertising tag or project policy requires a documented consent decision."
---

# Recipe — Consent management and Google Consent Mode

## Outcome

The project has an approved consent decision. When consent applies, one banner/
CMP owner sends user choices before non-essential tags act, and Google Consent
Mode v2 plus third-party GTM tag gating match that decision.

## Inputs

- Passing Google Tag Manager recipe and complete selected-tag inventory.
- Project/legal/privacy decision for applicable audiences and regions.
- Approved CMP/banner owner, policy copy, category model, and access.
- Required integrations and their cookie/storage/network behavior.

This recipe implements an approved decision; it does not provide legal advice or
invent which law, region, lawful basis, or banner copy applies.

## Ownership rules

- The CMP/banner is the one owner that obtains and stores the user's choice.
- Consent Mode communicates choices to Google tags; it is not a banner, CMP, or
  substitute for the project's legal/privacy decision.
- In GTM, use one consent-initialization owner. Prefer the approved CMP's
  supported template/integration over duplicate custom consent code.
- Google tags use their built-in consent checks. Add explicit consent checks to
  third-party tags such as Clarity according to the approved category model.
- Do not put a second banner, direct consent script, or duplicate default/update
  commands into theme code when the platform/CMP/GTM owner already exists.

## Procedure

1. Inventory the banner/CMP, GTM consent overview, consent commands/events,
   cookies/storage, and every selected tag's pre-consent network behavior.
2. Obtain the recorded project decision: no gating (`N/A` with approver/evidence),
   basic consent mode, advanced consent mode, region-specific behavior, and the
   categories each tag requires.
3. When consent applies, configure the approved CMP/platform integration and
   policy links/copy through its real owner.
4. Set default consent before measurement tags can act. Configure all approved
   Consent Mode v2 states that apply: `analytics_storage`, `ad_storage`,
   `ad_user_data`, and `ad_personalization`.
5. Send updated states on the same page when the user changes a choice, before
   navigation. Preserve/reopen choices through the CMP.
6. Map GA/Google tags to built-in consent behavior; configure Clarity and other
   third-party tags with the approved additional checks/triggers.
7. Preview all states, then publish named CMP/GTM versions with rollback.

## Verification

- First visit, accept all, reject all, category-specific choice, revisit/change,
  reload, and applicable regional behavior are tested in a fresh context.
- GTM Consent Overview/Tag Assistant shows the intended defaults before tag
  execution and the correct updates after interaction.
- Google tags reflect the approved built-in consent states without contradictory
  additional checks.
- GA, Clarity, and every other non-essential tag/cookie/request follow the
  approved category decision in each tested state.
- Banner choices persist/reopen correctly and required public/admin flows still
  work.
- No duplicate CMP, consent commands, or direct measurement owner exists.

## Rollback

Restore the previous CMP configuration and GTM container version together,
purge relevant caches, and verify the previous banner plus tag behavior returns.
Do not roll back one layer while leaving contradictory defaults or triggers live.

## Evidence to record

- Decision owner/date, applicable regions, mode, CMP/platform owner, and category
  map.
- Consent defaults/updates, selected tag checks, named published versions, and
  the full state-test matrix.
- Cookie/network evidence and rollback versions without visitor identifiers.

## Hard stops

- The project/legal/privacy decision or required banner copy is missing.
- CMP/GTM consent ownership is duplicated or ambiguous.
- Defaults cannot run before non-essential tags, or reject/change behavior fails.
- Implementing consent would require invented legal conclusions.

## Sources

- [Google: about consent mode](https://support.google.com/tagmanager/answer/10000067?hl=en)
- [Google: set up consent mode on websites](https://developers.google.com/tag-platform/security/guides/consent)
- [Google: Tag Manager consent mode support](https://support.google.com/tagmanager/answer/10718549?hl=en)
- [Google: consent checks for Google tags](https://support.google.com/tagmanager/answer/12962079?hl=en)
