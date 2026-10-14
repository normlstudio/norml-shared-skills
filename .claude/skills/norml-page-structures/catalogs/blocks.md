# Block specs — index

The shared block catalog (read by `WordPress implementation workflow` and `WordPress development workflow`). Each file in `blocks/` describes one reusable block: its purpose, the required/optional elements, the default Gutenberg+ACF field shape, and the Elementor fallback for sites already on Elementor. The consuming skill reads only the block file(s) it needs for the current section — keep this index light. (These are the *specs*; the actual `block.json` + wireframe + preview *implementations* live in the user's implementation library.)

## How to use

When building a section:

1. Identify which block(s) the section maps to (the page-type spec usually names them)
2. Read `blocks/{block}.md` for required elements, ACF field shape, and Elementor fallback
3. Select a documented variant through [the variant contract](variant-contract.md), recording its ID, source, content fit and responsive/interaction behavior
4. Scaffold the ACF field group + Blade template per the spec; map source slots explicitly
5. If the section doesn't fit any existing block cleanly, add a source-backed block file before building

The block specs are **Gutenberg + ACF first**. Elementor is the fallback — used only if the site is already on Elementor, or for a one-off section per the Elementor escape-hatch rules in `WordPress implementation workflow/SKILL.md`.

## Index

| Block | File | Purpose | Common on |
|---|---|---|---|
| Hero | [hero.md](blocks/hero.md) | First section — headline + CTA + visual | Home, service, landing |
| Archive hero | [archive-hero.md](blocks/archive-hero.md) | H1 + intro band at top of archive pages (no CTA, no big visual) | Blog archive, category archives, product listing |
| Features | [features.md](blocks/features.md) | 3–4 offerings side-by-side with icons | Home, service |
| Benefits grid | [benefits-grid.md](blocks/benefits-grid.md) | Outcome-led cards (what the buyer GETS, not what the product IS) | Home, service, landing |
| Testimonials | [testimonials.md](blocks/testimonials.md) | Social proof — quotes from real people | Home, service, case study |
| FAQ | [faq.md](blocks/faq.md) | Interactive or static Q&A; paired rows or responsive cards | Service, blog post, landing, product |
| CTA | [cta.md](blocks/cta.md) | End-of-page call-to-action band | Most pages |
| Newsletter CTA | [newsletter-cta.md](blocks/newsletter-cta.md) | Email signup band — distinct from generic CTA | Blog archive, blog post, home |
| Text content | [text-content.md](blocks/text-content.md) | Rich text body with headings, lists, quotes | Blog post, about, legal |
| Image + text | [image-text.md](blocks/image-text.md) | Split section — image one side, copy the other | Home, service, about |
| Logo cloud | [logo-cloud.md](blocks/logo-cloud.md) | Trust strip of client / partner logos | Home, service |
| Pricing | [pricing.md](blocks/pricing.md) | 2–4 plan cards or single price card | Service, landing |
| Process steps | [process-steps.md](blocks/process-steps.md) | Numbered 3–7 step sequence with optional timeline | Service, home, product |
| Local SEO text | [local-seo-text.md](blocks/local-seo-text.md) | 400–600 words of unique long-form SEO copy per local page | Local pages only |
| Breadcrumb | [breadcrumb.md](blocks/breadcrumb.md) | Linked path showing site hierarchy + `BreadcrumbList` schema | All non-home pages |
| Table of contents | [toc.md](blocks/toc.md) | Required blog links; left TOC/right article with two centered compositions | Every blog post, service (long-form), docs |
| TL;DR | [tldr.md](blocks/tldr.md) | One-paragraph plain-prose summary (distinct from key-takeaways) | Blog post (long-form), news, case study |
| Key takeaways | [key-takeaways.md](blocks/key-takeaways.md) | 3–7 bulleted summary block | Blog post, service ("why this matters"), case study |
| Sources | [sources.md](blocks/sources.md) | Numbered list of cited references, E-E-A-T support | Blog post (data-driven / YMYL), reports |
| Author bio | [author-bio.md](blocks/author-bio.md) | Photo + bio + link to author archive (or brand byline) | Blog post |
| Share with AI | [share-ai.md](blocks/share-ai.md) | **Catalog default** — 3 buttons piping article into ChatGPT / Claude / Gemini with pre-baked prompts | Blog post, long-form pages |
| Google Preferred Source | [preferred-source.md](blocks/preferred-source.md) | Required blog-template slot that lets eligible readers prefer the publication in Google Search | Blog post, news |
| Share social | [share-social.md](blocks/share-social.md) | Social share row (LinkedIn / X / FB / Pinterest / copy-link) | Blog post, case study |
| Featured post | [featured-post.md](blocks/featured-post.md) | Large editor's-pick card at top of blog archive (Theme Options opt-in) | Blog archive |
| Category pills | [category-pills.md](blocks/category-pills.md) | Horizontal taxonomy filter row | Blog archive, product listing, case study archive |
| Post card | [post-card.md](blocks/post-card.md) | Canonical card shape used by archives + related + sidebar (template part) | Blog archive, related posts, home blog teaser |
| Related posts | [related-posts.md](blocks/related-posts.md) | 3–4 cards of related articles at end of post | Blog post |
| Most popular | [most-popular.md](blocks/most-popular.md) | Top-N posts by traffic / hand-picked editor's pick | Blog archive (optional), sidebar |
| Search bar | [search-bar.md](blocks/search-bar.md) | Site-wide search input (justified at 50+ pages / 100+ posts) | Header (when justified), archive (optional) |
| Team grid | [team-grid.md](blocks/team-grid.md) | Grid of team-member cards with optional filter | About, team listing, home |
| Team member card | [team-member-card.md](blocks/team-member-card.md) | One person tile (template part) | Team grid, about, footer strip |
| Contact form | [contact-form.md](blocks/contact-form.md) | Inbound lead form, minimal fields | Contact, landing, footer |
| Map embed | [map-embed.md](blocks/map-embed.md) | Embedded map (Google / Mapbox / OSM) with address | Contact, about, store locator |
| Case study card | [case-study-card.md](blocks/case-study-card.md) | An anonymized client story with challenge, approach, outcome and metric strip | Case studies proof page, home, service |
| Product gallery | [product-gallery.md](blocks/product-gallery.md) | Multi-image gallery + zoom + (optional 360°) | Product (ecommerce single) |
| Product info | [product-info.md](blocks/product-info.md) | Composite right column: name, price, CTA, variants, specs, stock | Product (ecommerce single) |
| Product reviews | [product-reviews.md](blocks/product-reviews.md) | Aggregate rating + breakdown + review cards + `AggregateRating` schema | Product (ecommerce) |
| Product instructions | [product-instructions.md](blocks/product-instructions.md) | Step-by-step usage / safety / maintenance / troubleshooting | Product |
| Related products | [related-products.md](blocks/related-products.md) | 4–8 product carousel ("You may also like" / "FBT") | Product, cart |
| Payment info | [payment-info.md](blocks/payment-info.md) | Accepted-payment-methods icon strip + "Secure checkout" badge | Product, checkout, footer |
| Delivery info | [delivery-info.md](blocks/delivery-info.md) | Shipping estimate + cost + options + (optional) zip checker | Product, cart |
| Return policy | [return-policy.md](blocks/return-policy.md) | Return window + conditions + refund method | Product, cart |
| Back in stock | [back-in-stock.md](blocks/back-in-stock.md) | Email-capture form when product is out of stock | Product (when stock is out) |

## Adding a new block

1. Copy an existing block file as a template
2. Fill in: purpose, required/optional elements, Gutenberg+ACF default, Elementor fallback, variations, used-on, don'ts
3. Add a row to the index above with the page types that typically include it
4. If the block becomes part of a page type's required structure, update the relevant `pages/{type}.md`
5. Document source-backed variants through [the variant contract](variant-contract.md); do not invent missing limits or claim an untested implementation is reusable

## Block hygiene

- Every block must work without optional elements (graceful degradation when ACF fields are empty)
- Every block needs a sensible mobile layout (don't make mobile an afterthought)
- Every block follows the project's design tokens — never hardcode colors, spacing, or type sizes
- Every block has an editor preview (`example` in the ACF block registration) so editors can see what it looks like before publishing
- Verify the selected layout, actual content/editor constraints and emitted schema through [block-variant acceptance](../qa/block-variants.md); preview-only tests do not prove runtime completeness
