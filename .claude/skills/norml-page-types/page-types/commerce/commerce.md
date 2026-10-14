# Commerce and customer journeys

Family ID: `commerce`. The family is the complete set of related destinations.
Member files are flat siblings; project URLs are instances, not new catalog files.

## Purpose and fit

A website sells products and exposes cart, checkout, account or product-selection destinations alongside public content.

**Skip or use another family:** These are transactional/system states, not editorial CPTs or forced archive/single pairs. This catalog identifies pages; it does not operate purchases or design a complete account app.

## Canonical entity and model

Session/cart state, a customer account or a selection/configuration tied to canonical products.

Reuse the commerce platform’s actual system routes and state ownership. Guest, authenticated and empty states need explicit disposition.
Actual WordPress mapping belongs to `WordPress architecture review`; preserve a verified
inherited model and keep logical purpose distinct from native query role.

## Included members

| Member ID | File | Logical role | Purpose / when enabled |
|---|---|---|---|
| `cart` | [cart.md](cart.md) | utility | Review a visitor’s current selection before checkout. |
| `checkout` | [checkout.md](checkout.md) | utility | Complete the platform’s actual order journey. |
| `account` | [account.md](account.md) | utility | Access authenticated customer information and supported account actions. |
| `bundle-builder` | [bundle-builder.md](bundle-builder.md) | utility | Choose multiple eligible products as one supported bundle/cart selection. |
| `product-configurator` | [product-configurator.md](product-configurator.md) | utility | Assemble a valid combination with dependent choices. |

Every member is an option. Projects do not necessarily need every hub
or counterpart; read each member’s provenance and omission conditions. Supported
generalizations are not claims of observed implementation.

## Relationships, depth and combinations

Product catalog → optional builder/configurator → cart → checkout; account offers private order/preferences views. Public presence alone proves no payment or reward integration.
Read [architecture principles](../../standards/architecture.md). Native entity
relationships, URL nesting and navigation can differ. Extra public routes need a
distinct purpose and an explicit canonical decision, not only a stored relationship.

## Eligibility and content truth

Keep real records, content sources and operational state in the project. Select
include, embed, defer or omit using its actual evidence, purpose and owners.
Evaluate public hub/detail availability together without forcing useless pairs.
Page presence does not establish integration correctness or factual accuracy.

## Handoff and provenance

Record family/member, source version, identity, disposition/evidence, state,
logical/native roles, parents/route, counterpart availability, source owner,
structure fit and unresolved work in the existing architecture/sitemap artifact.
This family abstracts [generalized patterns](../../standards/pattern-notes.md);
member specifications describe generalized patterns; target observation is required.
