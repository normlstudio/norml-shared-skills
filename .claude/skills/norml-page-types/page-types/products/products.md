# Products

Family ID: `products`. This overview describes the entire set of related pages.
Member files are flat siblings; actual project pages are instances of these specs.

## Purpose and fit

Visitors evaluate distinct products, including physical, digital, software or packaged offerings.

**Skip or use another family:** Do not assume every informational product page needs a cart, price or checkout; distinguish bespoke services from repeatable products.

## Canonical entity and model

One canonical product; optional categories and product-audience/industry relationship records.

Existing commerce model wins for transactional products; informational products can be a collection or a small approved set of Pages.
This is candidate modeling guidance; `WordPress architecture review` owns the actual
WordPress primitive. Match an inherited model before proposing another one.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `archive` | [archive.md](archive.md) | archive | Help visitors compare available products and choose a detail page. |
| `single` | [single.md](single.md) | single | Explain one product’s purpose, capabilities and acquisition path. |
| `category-archive` | [category-archive.md](category-archive.md) | taxonomy-archive | Browse products sharing a meaningful selection criterion. |
| `product-by-industry` | [product-by-industry.md](product-by-industry.md) | intersection | Explain a product in a distinct industry context. |
| `curated-listing` | [curated-listing.md](curated-listing.md) | archive | Browse a maintained selection such as sale items, new arrivals or gifts. |
| `compatibility-listing` | [compatibility-listing.md](compatibility-listing.md) | taxonomy-archive | Find items compatible with a specified model, format or system. |

These are available contracts, not mandatory URLs. Evaluate hub and detail
availability together. Record public, embedded-only, disabled, not applicable
or unresolved for any omitted counterpart; singletons need no artificial pair.

## Relationships, depth and combinations

Products archive → category → product single. Optional product × industry is a distinct product-context record, not the industry × service record.
Read [architecture principles](../../standards/architecture.md) before selecting
depth, classifications or combinations. Parent URLs do not dictate CMS storage.
Intersections reference canonical entities and have one owner and canonical route.

## Eligibility and content truth

Use the brief/SMC, actual inventory and approved records to decide include,
embed, defer or omit. Read each member’s distinct evidence/omission requirements.
This family does not fabricate client entities or authorize page generation.
Real facts and relationship-specific differences need maintained source owners.

## Handoff

Record family/member IDs, source version, entity/tuple, disposition/evidence,
observed/planned/proposed state, logical/native roles, parent(s), route, hub/single
availability, relationships/depth, content owner/source and unresolved work in
the project’s existing architecture record. Read each selected member’s exact
structure fit or gap; `norml-page-structures` owns blocks and elements.

## Additional project patterns

Browse a maintained selection such as sale items, new arrivals or gifts. Find items compatible with a specified model, format or system.
Read [pattern notes](../../standards/pattern-notes.md) and the new
member files for their exact matching, model and omission distinctions.

## Matching adjacent patterns

Manufacturer browsing uses [brands](../brands/brands.md); application browsing uses [solutions/application-single](../solutions/application-single.md). A compatibility listing and a curated sale/new/gift listing keep products canonical.
