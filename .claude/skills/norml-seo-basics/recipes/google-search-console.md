---
recipe: google-search-console
version: 1.1.0
scope: universal
baseline: required
depends_on:
  - sitemap-and-robots
applies_when: "A managed public indexable site has not explicitly opted out of Google Search Console."
---

# Recipe — Google Search Console

## Outcome

The canonical public site has one correctly scoped Search Console property with
durable verified ownership, appropriate team access, and its passing canonical
sitemap submitted and readable.

## Inputs

- Passing sitemap-and-robots recipe and exact canonical domain/origin.
- Approved Norml/client Google account ownership and user-access plan.
- Write-scoped Google API authorization for property verification/submission
  when mutation is required. A read-only ADC connection is inventory-only.
- DNS access for a Domain property or an approved URL-prefix verification route.
- Existing Search Console property inventory.

Connection/authentication belongs to provider-supported authentication as described in `standards/access-and-safety.md`; this recipe owns the
property setup and verification result, not a second credentials procedure. A
working read-only GSC connection does not grant write scopes or create a
property.

## Ownership rules

- Reuse an existing correctly scoped property; do not create a duplicate because
  access is missing or unclear.
- Prefer a Domain property when the team owns the full domain and needs all
  protocols/subdomains. Domain properties use DNS verification.
- Use a URL-prefix property when scope must be limited to one protocol, host, or
  path, or when domain-level DNS control is not appropriate.
- Keep verification durable. Do not remove another owner's DNS record, HTML
  file, meta tag, GA, or GTM verification token.
- Use the least Search Console permission that supports each person's role.

## Procedure

1. Inventory existing Domain and URL-prefix properties through the Search
   Console Sites API and Site Verification API, including verified owners,
   users, verification methods, and submitted sitemaps.
2. Match the canonical URL and organizational scope to the correct existing
   property before creating anything.
3. When a new property is required, choose Domain versus URL-prefix from the
   verified scope—not convenience. Use the Site Verification API `getToken`
   operation for the exact `INET_DOMAIN` or `SITE` resource.
4. Publish the returned token through the durable owner:
   - Domain property: add the exact Google-provided DNS TXT/CNAME record through
     the domain's real provider API/CLI after route and collision checks;
   - URL-prefix property: prefer an existing supported platform verification,
     GTM, or GA owner; use HTML/meta/file only through the platform's durable
     setting or deployment owner.
5. Ask the Site Verification API to verify/insert the resource, then ensure the
   exact property is present through Search Console `Sites.add`/`Sites.list`.
   Preserve existing verification methods and confirm the new method passes.
6. Add approved teammates/clients at the appropriate permission level.
7. Submit the exact passing canonical sitemap URL through the Search Console
   Sitemaps API, then list/get it from the exact property.
8. Check the property for Security Issues, Manual Actions, Page Indexing, and
   sitemap-processing errors; record findings without pretending new sites have
   immediate performance/index data.

## Verification

- Property type/scope covers the intended canonical site and no wrong-host
  duplicate was created.
- At least one durable verified owner remains, with the approved team access.
- DNS/meta/file/GTM/GA verification token is still live and its owner is known.
- Submitted sitemap URL matches the recipe dependency, is accepted/readable, and
  uses the preferred HTTPS host.
- Security Issues and Manual Actions are checked and recorded.
- A representative URL can be inspected in the correct property; lack of fresh
  index data is not misreported as a technical failure.

## Rollback

Restore only the setting/record added by this run after confirming another
verified owner and recovery route remain. Never remove the sole verification
method or another owner's token. Search Console property removal from one user's
view is not a substitute for cleaning up the real verification owner.

## Evidence to record

- Property type/name/scope, verified owners, user permissions, and verification
  method/owner without secret values.
- Submitted sitemap URL/status, representative URL Inspection result, and the
  Security Issues/Manual Actions review.
- Changed DNS/platform setting, rollback precondition, and activity-log entry.

## Hard stops

- Existing property ownership or canonical property scope is ambiguous.
- Required write-scoped Google authorization is unavailable.
- DNS/platform target cannot be uniquely verified.
- The change would overwrite another verification token or remove sole access.
- Sitemap dependency does not pass.

## Sources

- [Google: add a Search Console property](https://support.google.com/webmasters/answer/34592?hl=en)
- [Google: verify site ownership](https://support.google.com/webmasters/answer/9008080?hl=en)
- [Google: submit and monitor sitemaps](https://support.google.com/webmasters/answer/7451001?hl=en)
- [Google: URL Inspection](https://support.google.com/webmasters/answer/9012289?hl=en)
- [Google Site Verification API workflow](https://developers.google.com/site-verification/v1/invoking)
- [Search Console API: add a site](https://developers.google.com/webmaster-tools/v1/sites/add)
- [Search Console API: submit a sitemap](https://developers.google.com/webmaster-tools/v1/sitemaps/submit)
