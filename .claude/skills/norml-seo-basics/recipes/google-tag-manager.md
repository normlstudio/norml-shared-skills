---
recipe: google-tag-manager
version: 1.0.1
scope: universal
baseline: required
depends_on: []
applies_when: "A managed public website needs a tag-management layer and has not explicitly opted out."
---

# Recipe — Google Tag Manager

## Outcome

One verified Google Tag Manager web container loads on every intended public page.
The platform's admin/integration layer owns the embed wherever that capability
exists.

## Inputs

- Exact production URL and platform/CMS.
- Approved GTM web-container ID in `GTM-XXXXXXXX` form.
- Access to the correct GTM account/container and the site's management surface.
- The project's production/staging policy and known consent/privacy context.

The container ID is an identifier, not a password, but never invent or substitute
one. A missing/ambiguous ID blocks this recipe only.

## Ownership rules

- Exactly one system embeds the GTM container.
- On WordPress, the owner is an admin-managed plugin/integration. On a blank site,
  Norml's default is GTM4WP (`duracelltomi-google-tag-manager`) from the WordPress
  plugin repository.
- On WordPress, store the ID in the plugin's WordPress option through WordPress
  Admin. Never paste the loader or noscript iframe into theme, child-theme,
  snippets, mu-plugin, or repository code.
- On another CMS/site builder, prefer its supported site-wide integration or
  custom-code field in the admin panel.
- Source-code installation is the last resort for a platform with no durable
  admin integration. It must follow the project's code/deployment contract.
- Existing/approved Google Analytics, Microsoft Clarity, and future measurement
  products should use separate GTM tags rather than another direct site embed.
  The Google Analytics recipe audits presence only and never creates that tag.
- Installing the empty/base container does not authorize non-essential tags to
  fire. `consent-management.md` owns the gating decision and implementation.

## Procedure

1. Inspect live HTML, browser network requests, platform settings, plugins, and
   source for every existing `GTM-` ID. Resolve conflicts before writing.
2. Confirm the approved container belongs to the correct site/account and choose
   the correct GTM environment.
3. Create the required production rollback checkpoint before changing the site.
4. Install/configure the one platform owner:
   - **WordPress:** use WordPress Admin to install/activate GTM4WP when no mature
     owner exists; open `Settings → Google Tag Manager`, enter the container ID,
     enable the container, retain the plugin's standard body-placement mode, and
     save. Do not enable unrelated data-layer integrations by default.
   - **Other managed platform:** use its supported admin integration and record
     the exact settings location.
   - **No admin capability:** implement Google's two standard snippets through
     the code source of truth—the loader high in `<head>` and noscript iframe
     immediately after `<body>`—only after recording why admin management is
     impossible.
5. Purge only the caches needed for the new public output.
6. Use GTM Preview/Tag Assistant before publishing container changes.

## Verification

- Logged-out public HTML identifies the intended `GTM-` container and no other
  container.
- One `gtm.js?id=GTM-…` network request succeeds.
- One noscript iframe points to the same container.
- `window.dataLayer` exists and receives the GTM bootstrap event.
- GTM Preview/Tag Assistant connects to the intended container.
- No new uncaught JavaScript or blocked baseline resource error appears.
- **WordPress:** a repository/theme search returns no GTM container ID, loader,
  or `googletagmanager.com/ns.html` embed. The public output identifies the
  admin-managed plugin as owner.

## Rollback

Disable the one admin integration or restore its previous option, purge caches,
and verify the GTM network request is gone. For a code-only platform, revert the
exact deployed commit through the project's rollback workflow.

## Evidence to record

- Container ID, environment, platform owner, and settings location.
- Plugin/integration name and version when applicable.
- Live request count/status, noscript count, Preview result, and duplicate scan.
- Backup/rollback point and activity-log entry.
- WordPress Git/theme negative-search result.

## Hard stops

- Container ID or production target is ambiguous.
- A different live container exists and ownership/migration is unresolved.
- WordPress would require theme/repository insertion instead of the approved
  admin-managed path.
- The live container already fires non-essential tags under known consent
  requirements and no safe pause/rollback exists while consent is resolved.

## Sources

- [Google: install a web container](https://support.google.com/tagmanager/answer/14847097?hl=en)
- [Google: add and publish tags in GTM](https://support.google.com/tagmanager/answer/14842872?hl=en)
