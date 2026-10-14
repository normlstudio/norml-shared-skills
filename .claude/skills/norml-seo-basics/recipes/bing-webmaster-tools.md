---
recipe: bing-webmaster-tools
version: 1.0.0
scope: universal
baseline: required
depends_on:
  - sitemap-and-robots
applies_when: "A managed public indexable site has not explicitly opted out of Bing Webmaster Tools."
---

# Recipe — Bing Webmaster Tools

## Outcome

The canonical public site appears exactly once in the approved Bing Webmaster
Tools user, has durable verified ownership, and has its passing canonical
sitemap submitted through Bing's supported JSON/REST API.

## Inputs

- Passing `sitemap-and-robots` recipe and exact canonical HTTPS root URL.
- Approved Bing user identity and a passing laptop/API connection from
  [access and safety](../standards/access-and-safety.md).
- Existing Bing site inventory from a sanitized `GetUserSites` response.
- Unambiguous DNS-provider or website-platform ownership for the chosen
  verification method.
- Exact canonical sitemap URL.

provider-supported authentication as described in `standards/access-and-safety.md` stores and tests the user-scoped API key. This recipe owns the
website property, verification proof, sitemap submission, and project evidence;
it never stores or prints the key.

## Ownership rules

- Reuse an existing exact canonical site record. Missing access is not
  permission to add a duplicate HTTP/HTTPS, `www`/apex, or slash variant.
- Add the canonical HTTPS root URL, including the trailing slash expected by the
  API, only after the live redirect/canonical/sitemap origin agree.
- Prefer Bing's DNS CNAME verification when the authoritative DNS provider has
  a supported API/CLI and the exact zone route is proven. Use XML-file or meta
  verification only through the website's durable platform/code owner.
- Preserve the verification proof after success. Do not overwrite, edit, or
  remove another owner's DNS record, XML file, or meta token.
- A Bing API key proves one user's API identity; it is not website-ownership
  proof and never belongs in DNS, source, project docs, or command output.
- Use Bing's JSON endpoint. Do not add new SOAP or POX integrations.

## Procedure

1. Resolve the final canonical HTTPS root URL and the exact passing sitemap from
   the dependency. Stop if redirects, canonical, robots, and sitemap origins do
   not agree.
2. Call `GetUserSites` through the token-safe operating-system protected credential store pattern documented in
   provider-supported authentication as described in `standards/access-and-safety.md`. Reduce output to URL plus `IsVerified` before displaying or
   recording it; raw unverified records can contain ownership codes.
3. Compare normalized host/scheme records and reuse the exact existing site. If
   no correct site exists, call JSON `AddSite` with the exact canonical root.
4. Re-query `GetUserSites` and select the exact property returned by Bing. Read
   its verification fields only in process memory; never log the raw response.
5. Publish one durable ownership proof:
   - **DNS CNAME:** use the exact hostname/code and `verify.bing.com` target Bing
     returns. Resolve the authoritative provider/account first, capture current
     records, stop on any non-idempotent collision, add one record through that
     provider's API/CLI, and verify the answer from every authoritative
     nameserver;
   - **XML file or meta tag:** route the exact Bing proof through the site's
     platform/build owner, retain it durably, and verify the cache-purged public
     URL/source.
6. Call JSON `VerifySite` for the exact site URL. Re-query `GetUserSites`; both
   the verification call and the exact record's `IsVerified: true` state must
   pass.
7. Submit the exact canonical sitemap URL with JSON `SubmitFeed` only after site
   verification and the sitemap dependency pass.
8. Call JSON `GetFeeds` for the exact site. Require the submitted sitemap to be
   listed; record Bing's current processing status. An explicit processing
   error is a failure, while a newly submitted pending state is recorded without
   pretending crawl/index data is immediate.
9. Review Bing's site diagnostics/security messages available to the approved
   user and record material findings without turning a new site's empty data
   into a technical failure.

Provider writes follow the target provider's own connection runbook and
rollback rules. A DNS API key or hosting token is never substituted for a proven
zone/account route.

For every Bing JSON call, resolve the API base plus protected-store credential reference
from the non-secret service pointer, keep the key only in process memory, and
pipe the API-key-bearing request URL to `curl` through standard input. Request
bodies may contain the public site/feed URLs. Unset response/key variables after
the sanitized assertion; never use `set -x` or place `apikey=` in a process
argument, log, task note, or tracked file.

## Verification

- The exact canonical HTTPS site appears once in sanitized `GetUserSites`
  output with `IsVerified: true`.
- The ownership proof is still live and its durable owner is recorded.
- For DNS, the provider record exists exactly once and every authoritative
  nameserver returns the exact Bing CNAME target.
- The canonical sitemap returns valid XML on the preferred host, `SubmitFeed`
  succeeds, and `GetFeeds` lists the exact URL without an explicit error.
- No wrong-host or protocol duplicate was created.
- The project report contains only public/non-secret ownership evidence and the
  protected-store pointer name, never the API key or a raw API URL containing it.

## Rollback

Remove only the site record or verification proof added by this run, and only
after confirming another durable verified owner/recovery path remains. For DNS,
delete only the exact record whose before-state proved it was newly added; never
edit/delete a collision or another owner's proof. Do not remove the canonical
sitemap feed merely because processing is still pending.

## Evidence to record

- Bing user identity reference and protected-store credential reference names, without the
  key.
- Exact site URL, prior site inventory result, final `IsVerified` state, and
  verification method/owner.
- Public verification hostname/target or public XML/meta proof location.
- DNS provider/account route, before/after record evidence, and authoritative
  nameserver results when DNS is used.
- Submitted sitemap URL, `SubmitFeed` result, `GetFeeds` status, and check date.
- Rollback precondition and platform/provider activity entry.

## Hard stops

- Existing Bing site ownership, canonical URL, or duplicate property state is
  ambiguous.
- The protected-store-backed Bing connection fails or belongs to the wrong user.
- DNS/platform target cannot be uniquely matched to the canonical site.
- The proposed verification record collides with a non-identical existing
  record or would overwrite/remove another proof.
- The sitemap dependency does not pass.
- `VerifySite` does not produce an exact `IsVerified: true` site record.
- A procedure would expose the API key in chat, logs, process arguments, or a
  tracked file.

## Sources

- [Bing Webmaster API overview](https://learn.microsoft.com/en-us/bingwebmaster/)
- [Bing API-key access](https://learn.microsoft.com/en-us/bingwebmaster/getting-access)
- [Bing `GetUserSites`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.bing.webmaster.api.interfaces.iwebmasterapi.getusersites?view=bing-webmaster-dotnet)
- [Bing `AddSite`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.bing.webmaster.api.interfaces.iwebmasterapi.addsite?view=bing-webmaster-dotnet)
- [Bing `VerifySite`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.bing.webmaster.api.interfaces.iwebmasterapi.verifysite?view=bing-webmaster-dotnet)
- [Bing `SubmitFeed`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.bing.webmaster.api.interfaces.iwebmasterapi.submitfeed?view=bing-webmaster-dotnet)
- [Bing `GetFeeds`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.bing.webmaster.api.interfaces.iwebmasterapi.getfeeds?view=bing-webmaster-dotnet)
- [Bing: add and verify a site](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b)
