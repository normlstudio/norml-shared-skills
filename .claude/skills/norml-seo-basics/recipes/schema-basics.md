---
recipe: schema-basics
version: 1.0.0
scope: universal
baseline: required
depends_on: []
applies_when: "Every indexable public website."
---

# Recipe — Basic schema

## Outcome

The site exposes one valid, connected JSON-LD graph describing the real publisher,
website, and current page, plus only the page-type entities supported by visible
content.

## Inputs

- Canonical site/page URLs and approved publisher identity.
- Visible page content and verified organization/person facts.
- Approved logo and social-profile URLs only when they truly exist.
- Current schema owner (CMS, SEO plugin, application, or theme).

## Ownership rules

- Exactly one system owns the base graph. Extend that graph instead of printing a
  competing second graph.
- Prefer JSON-LD because it is maintainable and Google recommends it when the
  platform supports it.
- On WordPress, the selected mature SEO plugin normally owns the base graph;
  `wp-rank-math.md` defines the blank-site default.
- Do not use GTM as the normal schema delivery layer. Schema belongs with the
  page/CMS data it describes.
- Stable canonical IDs use fragments such as `#organization`, `#person`,
  `#website`, and `#webpage`.

## Base graph

Every applicable public page needs:

- one `Organization` **or** `Person` publisher;
- one `WebSite` linked to that publisher;
- one `WebPage` linked to the WebSite and canonical page URL.

Add a `logo` entity only for an approved logo—not merely because a Site Icon
exists.

## Conditional types

| Type | Add only when |
|---|---|
| `Article` / `BlogPosting` | The page is an authored article/post with visible dates/author |
| `BreadcrumbList` | The page hierarchy/breadcrumb trail is real and coherent |
| `Service` | The visible page offers or describes that service |
| `FAQPage` | The same questions and answers are visible on the page |
| `Product` / `Offer` | Product, price, currency, availability, and offer are visible/current |
| `LocalBusiness` | Verified NAP/location and real local-business context exist |
| `Person` | The person is visible or an approved project fact |

Complex CPT/product/local/multi-template systems route to `norml-seo-schema`.

## Procedure

1. Parse every live JSON-LD block and inventory types, IDs, owners, and duplicates.
2. Reconcile claims with visible content and approved project facts.
3. Choose one base owner and remove/disable same-purpose duplicates before adding
   anything.
4. Configure the connected base graph through the platform/SEO owner.
5. Add only supported conditional entities and link their `@id` references.
6. Keep defaults conservative: for example, do not label every generic Page as an
   Article.

## Verification

- Every `application/ld+json` block parses.
- Expected base types exist once with absolute canonical IDs.
- Publisher → WebSite → WebPage references resolve coherently.
- No duplicate stable IDs or competing same-purpose entities exist.
- Every conditional entity/property matches visible current content.
- Google's Rich Results Test passes for eligible page types; syntax success does
  not excuse a false claim.
- Representative templates are tested after deployment and cache purge.

## Rollback

Restore the previous schema-owner settings/code, purge caches, and verify the old
graph. Do not leave both old and new owners active during rollback.

## Evidence to record

- Owner, graph types, stable IDs, and representative URLs.
- Visible fact/source for every conditional type.
- Duplicate counts, parser/Rich Results Test result, and rollback point.

## Hard stops

- Publisher identity or canonical URL is ambiguous.
- The entity would claim facts absent from visible/approved content.
- Multiple schema owners remain unresolved.
- Required properties for the selected rich-result type are unavailable.

## Sources

- [Google Search: introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Schema.org](https://schema.org/)
