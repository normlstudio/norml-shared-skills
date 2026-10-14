# Page-type specs — index

The shared page-type catalog (read by `WordPress implementation workflow` and `WordPress development workflow`). Each file in `pages/` describes one type of page: what structural elements it must have, which blocks belong on it by default, and the situational extras. The consuming skill reads only the page-type file(s) it needs for the current build — keep this index light. Some types also have a deep, screenshot-backed archetype under [`archetypes/`](archetypes/).

## How to use

When the brief says "build a [page type]" or scaffolds a page but doesn't list sections:

1. Look up the page type in the table below
2. Read its file in `pages/{type}.md` — that's the source of truth for required structural elements
3. For each referenced block, open `blocks/{block}.md` to learn the field shape, default ACF structure, and Elementor fallback
4. Build top-to-bottom, deviating from the spec only when the brief explicitly overrides

If the brief specifies sections that aren't in the spec, **follow the brief** — the spec is a default, not a constraint. Add the new block file under `blocks/` if it's reusable.

## Index

| Page type | File | One-liner |
|---|---|---|
| Home | [home.md](pages/home.md) | The primary landing page — who/what/why/CTA in 5 seconds |
| About | [about.md](pages/about.md) | Mission, history, team, awards — trust-building, no sales pitch |
| Service | [service.md](pages/service.md) | One service offering with proof, process, and CTA |
| Service listing | [service-listing.md](pages/service-listing.md) | Index of all services with summary cards |
| Service category | [service-category.md](pages/service-category.md) | Filtered subset of services under one theme |
| Case study | [case-study.md](pages/case-study.md) | One project: problem → approach → outcome → testimonial |
| Case studies proof page | [case-study-page.md](pages/case-study-page.md) | Several anonymized client stories with challenge, approach, outcomes and metrics |
| Blog post | [blog-post.md](pages/blog-post.md) | Single editorial article with author, meta, TOC, body, Share-with-AI, and Google Preferred Source |
| Blog archive | [blog-archive.md](pages/blog-archive.md) | Listing of blog posts, filterable, paginated, optional featured slot |
| Team listing | [team-listing.md](pages/team-listing.md) | All team members in a grid, optional department filter |
| Team member | [team-member.md](pages/team-member.md) | One person's bio, expertise, articles, contact — deep archetype: [archetypes/team-member-bio/](archetypes/team-member-bio/) |
| Product listing | [product-listing.md](pages/product-listing.md) | Ecommerce shop index, filterable / sortable product grid |
| Product | [product.md](pages/product.md) | One product: gallery, price, CTA, reviews, trust strip (ecommerce single) |
| Product category | [product-category.md](pages/product-category.md) | Filtered subset of products under one category |
| Contact | [contact.md](pages/contact.md) | Form + alternatives (email, calendar link, address) |
| Local page | [local-page.md](pages/local-page.md) | One (service × city) landing page — generated in bulk via the [local-page contract](pages/local-page.md) |

## Adding a new page type

1. Copy an existing file as a template
2. Fill in: purpose, required blocks (in order), recommended blocks, variations, SEO, ACF page-level fields, don'ts
3. Add a row to the index above
4. If the new page references a block that doesn't have a spec yet, add it under `blocks/` too

## When the brief gives you a Figma

The Figma is authoritative for layout and visual. Use this catalog for: what fields each block needs, what ACF structure to scaffold, what's missing from the Figma that the page type usually requires (e.g., the Figma forgot the FAQ section — the spec reminds you to ask). Never let the catalog override an explicit design choice.
