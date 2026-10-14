# Local page

> A local page inherits its parent service-page structure and adds verified
> service-area differences. Read [service.md](service.md) and the block links.
> Only create eligible service-area pairs with substantive distinct content;
> a city-name substitution is not enough. There is no bulk-generation dependency.


## Purpose

Capture "{service} in {city}" search intent by cloning an existing canonical service page across N cities (× optional L languages). Every visible thing on a local page comes from the parent service page (the structure, the sections, the visual treatment, the components, the design tokens). The local page contributes ONLY: city-aware substitutions inside the cloned content + a handful of override fields (H1, SEO meta, schema `areaServed`).

Evaluate each relationship individually. Preserve the parent service composition; record local differences, source facts, canonical route and eligibility.

## The structural spec is: "the parent service page"

There is intentionally no list of "required structural elements" here. If the parent has a hero, a process block, an FAQ, a calculator widget, a Gravity Form, and a sticky CTA, the local page has all of those — because the local page renders the parent's `post_content`. If the parent has none of those, the local page has none of those.

If you find yourself drawing up a per-section composition for the local page (hero / intro / SEO body / area-served / CTA), STOP. You are violating the hard rule. The parent service page is the spec. If the parent doesn't have what you want, fix the parent first.

## Page-level ACF fields (the city-override envelope)

The ONLY fields stored on the local-page CPT itself:

```
parent_service       → Post Object (filter: post_type = page OR the existing service CPT)
target_city          → Text (slug, e.g. "miami")
target_city_display  → Text (display name, e.g. "Miami")
hero_h1              → Text — computed override "{Service Name} in {City Display}"
seo_title            → Text — max 60 chars, "{Service} {City} | {Brand}"
seo_description      → Textarea — max 160 chars, city-specific one-liner
```

That's the entire ACF page-level field group. Anything that looks like body content (intro paragraphs, SEO-text blocks, area-served lists) belongs in the cloned content — sourced from the parent and modified by the substitution map locked at workflow step L3.

## Template (single-{cpt}.php) is thin

The single template is a thin wrapper that calls `the_content()` and lets WP's normal filter chain (Divi / Gutenberg / Elementor / custom) render the cloned content. Sketch:

```php
<?php
if ( ! defined( 'ABSPATH' ) ) exit;
get_header();
the_post();
?>
<main id="main-content" class="local-service-page" role="main">
    <?php the_content(); ?>
</main>
<?php get_footer();
```

The schema.org `Service` JSON-LD with `areaServed = $target_city_display` is injected via RankMath filter (or raw `wp_head` if RankMath isn't active). The template itself adds nothing visual.

## SEO / schema notes

- **H1** — exactly one per page. The H1 lives in the cloned content (post-substitution) and ALSO as the `hero_h1` ACF field for RankMath title + schema. If the parent's H1 isn't in a place the substitution map cleanly hits, the seed script overrides it explicitly in the cloned content too.
- **Canonical** — self-canonical. Do NOT canonical to the parent service. These are meant to rank as themselves.
- **Schema** — `Service` with `provider` (Org-level), `serviceType` (matches parent), `areaServed` (target city).
- **Title tag** — `{Service Name} {City} | {Brand}` via RankMath, sourced from `seo_title` field.
- **Internal linking** — the cloned content typically already links to other site sections; the substitution map preserves those links. If the parent doesn't link back to itself, no need to add a link to the local page either.

## When to use a different page type

If the brief asks for a single hand-crafted "city landing page" with bespoke copy unique to that city (no multiplication intended), that's just a **landing page** built normally — not a local page. Local pages are specifically for the (service × city × language) multiplication pattern; they're a workflow primitive, not a hand-built page type.

## Don'ts

- **Don't compose the local page from scratch.** Clone the parent.
- **Don't add ACF fields beyond the override envelope above.** If you need more, the answer is to put it in the parent service page, not in the local-page CPT.
- **Don't write per-page unique long-form copy** the way the v1.5.0 model suggested. That copy belongs in the parent. The local page applies substitutions; it doesn't generate new body content.
- **Don't run this workflow without a parent service page.** Hard rule #1.
- **Don't bridge multiple services on one local page.** Hard rule #2. One service per local page; multiply services as separate batches.
- **Don't `noindex` local pages.** Defeats the purpose.
- **Don't canonical-tag the parent service.** Each local page is its own canonical.
