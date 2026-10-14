---
recipe: google-analytics
version: 1.1.0
scope: universal
baseline: required
depends_on: []
applies_when: "A managed public website should have its Google Analytics presence checked unless explicitly opted out."
---

# Recipe — Google Analytics presence

## Outcome

The run determines whether Google Analytics is present on the canonical public
site, whether it appears to collect once under the intended consent state, and
which system owns it. The result is a check, not an analytics implementation.

This recipe never creates or changes a Google Analytics account, property, web
stream, Measurement ID, Google tag, GTM tag, trigger, consent rule, or published
container version—even in Analyze and fix mode.

## Inputs

- Exact canonical public URL and environment intent.
- Recorded consent decision when one exists.
- Read-only access to the platform, GTM, or GA inventory when available.
- An isolated browser context for source and network evidence.

Property access is useful for ownership confirmation but is not permission to
provision or edit measurement. Never invent a `G-` or `GT-` identifier.

## Ownership rules

- Prefer one approved Google tag delivered through the site's established Google
  Tag Manager container.
- Report direct `gtag.js`, Site Kit measurement, Rank Math Analytics, theme
  settings, plugin embeds, or multiple Measurement IDs as ownership evidence;
  do not move or disable them in this recipe.
- Presence is not inferred from an admin toggle alone. Reconcile public source,
  network traffic, consent behavior, and read-only settings.
- This recipe does not decide a legal basis, banner, consent category, region,
  event plan, conversion, ecommerce data layer, or reporting model.

## Procedure

1. Open the final canonical URL in a fresh isolated browser context and capture
   the redirect, visible source, script URLs, data layer, and network traffic.
2. Identify every `G-`, `GT-`, `UA-`, Google tag, GA loader/config call, and GA
   collection request without copying unrelated request data or user identifiers.
3. When a consent interface exists, observe the first-visit state and the
   approved accept/reject states without changing the site's saved configuration.
4. Inspect platform and GTM configuration read-only when access is available to
   identify the delivery owner and detect a second implementation.
5. Classify the recipe:
   - `PASS` — one intended implementation is present and observable under the
     approved state, with no duplicate owner;
   - `FIX` — GA is absent or the public implementation is objectively broken;
   - `ESCALATE` — multiple/legacy owners, mismatched domains, or consent behavior
     require a measurement owner to decide the repair;
   - `BLOCKED` — access/consent prevents reliable presence determination;
   - `N/A` — an explicit project decision opts out of Google Analytics.
6. Record the candidate finding and hand it to human review. Do not provision or
   repair analytics as a continuation of this recipe.

## Verification

- Public source/network evidence states whether a Google tag and collection
  request are present, absent, blocked by consent, or duplicated.
- The observed canonical hostname and safe Measurement ID(s), when visible, are
  recorded without cookies, client IDs, payloads, or secret values.
- One delivery owner is identified, or the ambiguity is explicitly escalated.
- No GA/GTM/platform state changed during the check.

## Rollback

`N/A — check-only recipe.` This recipe makes no target-side change. If a later,
separately authorized measurement implementation changes GA, that workflow owns
its backup, GTM version, deployment, and rollback.

## Evidence to record

- Canonical URL, timestamp, isolated-browser state, and consent state tested.
- Safe visible Measurement/Google tag ID(s) and delivery owner, when present.
- Loader/config and collection-request counts without request payloads.
- Duplicate/direct implementation evidence or an evidence-backed absence.
- Human-review status and the owner of any separate measurement follow-up.

## Hard stops

- Do not create a property, stream, Measurement ID, Google tag, GTM tag, trigger,
  or published version.
- Do not disable or migrate an existing owner merely because another route is
  preferred.
- Stop at `BLOCKED` when consent behavior or access makes presence indeterminate;
  never accept/reject on behalf of a real user or invent the intended policy.
- Never capture cookies, client identifiers, event payloads, or credentials in
  the report.

## Sources

- [Google Analytics: verify that Analytics is collecting data](https://support.google.com/analytics/answer/9333790)
- [Google Tag Manager: Google tag](https://support.google.com/tagmanager/answer/14842872)
