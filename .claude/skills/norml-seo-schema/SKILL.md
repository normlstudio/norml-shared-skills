---
name: norml-seo-schema
version: 1.0.0
description: >
  Select, audit and generate truthful Schema.org JSON-LD for WordPress; map fields
  to WordPress core or ACF and prepare conditional PHP integration. Use for schema
  markup, structured data, JSON-LD, Product, Article, FAQPage, Organization,
  LocalBusiness, BreadcrumbList, Service, Person, returns or archive schema.
  Bundles per-type field maps/PHP templates and local validation. No private
  ecosystem or other skill is required; deployment follows the user's workflow.
metadata:
  author: Norml Studio
---

# Norml SEO Schema

Turn visible page content and verified entity facts into maintainable JSON-LD.
Keep dynamic content in its existing source, not hardcoded copies in schema code.
A valid graph does not guarantee a rich result, ranking or immediate indexing.

## Inputs and modes

Use the conversation and project documents before asking for missing inputs:
URLs/theme path, generate/audit mode, page/CMS query type, content source, entity
facts, active SEO/ecommerce owners, ACF availability and deployment policy.

- **Audit:** fetch authorized public pages or local rendered HTML, inventory all
  schema blocks, parse them and compare claims with visible content. Return
  `type | status | evidence | issue | proposed fix`. Do not mutate live state.
- **Generate:** prepare JSON-LD, field mapping, conditional PHP and handoff.
  Implement only when the user requests code changes in the verified project.
  Deployment is a separate authorized action through that project's workflow.

## Supported type contracts

Read every selected file completely before generating code.

| Type | Contract | Fit |
|---|---|---|
| Person | [person](schemas/person.md) | Verified author/person profile |
| Product / Offer | [product](schemas/product.md) | Actual product/offer; extend WooCommerce owner |
| Organization / WebSite | [organization](schemas/organization.md) | Publisher/site identity |
| BreadcrumbList / ItemList | [navigation](schemas/navigation.md) | Real hierarchy/visible listing |
| Article / BlogPosting / NewsArticle | [content](schemas/content.md) | Actual editorial article |
| FAQPage | [Q&A](schemas/qa.md) | Same real visible questions/answers; no Google FAQ rich result |
| Service | [service](schemas/service.md) | Real service facts; entity semantics |
| MerchantReturnPolicy | [returns](schemas/returnpolicy.md) | Approved policy; merchant/offer linkage |
| LocalBusiness and relevant subtype | [local](schemas/local.md) | Verified actual location/business facts |

For another type, confirm scope and read its official documentation. Do not imply
this package's validator has exhaustive support. Google feature support changes;
read [eligibility and current guidance](standards/eligibility.md) before promises.

## Workflow

1. **Inspect existing ownership.** Read project instructions, current theme/plugin
   architecture, actual query types and active SEO/ecommerce output. Search source
   for `application/ld+json`, `rank_math/json_ld`, `wpseo_schema` and
   `woocommerce_structured_data_product`. Inventory core/ACF fields and emitted
   types/IDs. Extend the existing owner where practical; replacement needs an
   explicit migration decision and rollback. Do not output competing duplicates.
2. **Record the handoff.** Use [the handoff template](templates/schema-handoff.md)
   in the user's project. Markdown is the default; a connected native Google Doc
   may be chosen explicitly. No external document or private skill is required.
3. **Select relevant entities.** Match actual page intent, visible content and
   verified entity relationships. Separate Schema.org vocabulary validity from
   Google feature eligibility. One connected graph can contain many same-type
   entities; each real entity needs a coherent identity, not a universal type cap.
4. **Map every dynamic property.** Reuse existing WordPress core/ACF/commerce data.
   Propose new fields only for actual missing facts. Record property, source getter,
   field type, required/conditional rule, empty behavior and visible counterpart.
   Do not invent prices, addresses, certifications, logos, reviews or policy terms.
5. **Prepare PHP.** Adapt the selected type templates. ACF templates require ACF;
   guard absent plugin APIs or use approved core fallbacks. Keep one responsibility
   per file, normally `inc/schema/{type}-schema.php`, unless the existing theme uses
   a loader/service module. Prefer collecting entities then encoding one graph.
6. **Render safely.** Use `wp_json_encode` with `JSON_HEX_TAG | JSON_HEX_AMP |
   JSON_HEX_APOS | JSON_HEX_QUOT` for script context. Do not HTML-escape values
   before JSON encoding; sanitize URLs/data at the source. Omit genuinely missing
   optional fields, preserve meaningful zero, and flag missing required facts.
7. **Load conditionally.** Hook once into `wp_head` after WordPress resolves its
   query. Match real registered CPT/taxonomy/template roles, not guessed slugs.
   Child themes use the correct stylesheet/source path. Respect plugin ownership;
   never hook and include the same renderer twice or emit before the document.
8. **Verify before shipping.** PHP lint every changed file; render populated,
   missing-optional, zero-value and long-content states. Run the bundled validator
   and actual Schema.org Validator/Rich Results Test for supported types. Check
   visible parity, entity IDs and duplicate ownership. A local lint is advisory,
   not Google's complete policy validator. Follow [acceptance](qa/acceptance.md).
9. **Authorized deploy and monitor.** Back up and follow the user's declared Git/
   CI/CD workflow, staging only this change. Test cache-purged production output.
   Optional GSC inspection returns Google's *indexed* version; compare last crawl
   with deployment date and report delayed evidence honestly.

## Validation commands

Node 20+; no npm package dependency:

```bash
node scripts/validate-schema.mjs ./rendered.html
node scripts/validate-schema.mjs --json --type Product https://example.com/item/
```

Exit `0`: local checks clean; `1`: warnings; `2`: errors/input failure. The
validator cannot prove visible-content truth, complete vocabulary compliance,
JavaScript output, indexing or search appearance. Review those separately.

Optional authorized Search Console inspection:

```bash
python3 scripts/gsc-inspect.py --site sc-domain:example.com https://example.com/item/
```

Read [Search Console access](processes/search-console-access.md). Use the user's
existing provider-supported credentials, never a company-specific project/schema.
Missing GSC access does not prevent local generation/validation.

## Outputs

Project-local handoff, selected JSON-LD, field-group proposal/mapping, conditional
PHP integration, representative test URLs and evidence-backed validation report.
The optional installed `norml-wp-developer` and `norml-wp-architecture` can help
implement the handoff; ordinary WordPress APIs and project procedures suffice.
