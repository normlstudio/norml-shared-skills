# Blog post

> One editorial article. SEO-optimized, scannable, with the structural cues readers expect from a modern blog. Catalog default: every post includes a [Share with AI](../blocks/share-ai.md) block plus a required [Google Preferred Source](../blocks/preferred-source.md) slot for eligible publications.

## Purpose

Educate, rank, build authority. The visitor came from search or social, needs to find the answer quickly, and (if you're lucky) read end-to-end.

## Required structural elements (top → bottom)

1. **Header**
2. **[Breadcrumb](../blocks/breadcrumb.md)** — `Home > Blog > Category > Post Title` (or back-link variant)
3. **Post header** — category badge → H1 (post title) → meta row (author + publish date + last-updated date if applicable + read time)
4. **Featured image** — hero visual under or above the header (template choice; the editorial example uses image-with-title-overlay)
5. **[TL;DR](../blocks/tldr.md) (optional)** — for long-form (>2000 words) — 2–3 sentence summary
6. **[Table of contents](../blocks/toc.md)** — auto-generated from H2s, on the left of the article and sticky on desktop where possible. Required on every post, including short articles and news; no word-count or minimum-heading gate. Use existing H3s when no H2s exist, or one body anchor labelled "Article" for unsectioned content
7. **[Text-content](../blocks/text-content.md) body** — the article itself, with proper heading hierarchy, lists, blockquotes, in-content images
8. **Inline [CTA](../blocks/cta.md) (optional)** — mid-article, especially in long-form (>2000 words)
9. **[Key takeaways](../blocks/key-takeaways.md) (recommended)** — 3–7 bullets summarizing the article
10. **[FAQ](../blocks/faq.md) (recommended)** — 4–6 common questions, accordion. Emits `FAQPage` schema
11. **[Sources](../blocks/sources.md) (optional)** — cited references for data-driven / YMYL content
12. **[Share with AI](../blocks/share-ai.md)** — Catalog default block — three buttons opening ChatGPT with takeaway / summarize / explain-simple prompts
13. **[Google Preferred Source](../blocks/preferred-source.md)** — required template slot and eligibility preflight; render on every post when the canonical domain/subdomain is eligible
14. **[Share social](../blocks/share-social.md)** — LinkedIn / X / Facebook / Pinterest / copy-link
15. **[Author bio](../blocks/author-bio.md)** — short bio + photo + link to author archive (or brand byline per project decision)
16. **[Related posts](../blocks/related-posts.md)** — 3–4 cards, same category or hand-picked
17. **[Newsletter CTA](../blocks/newsletter-cta.md)** — convert the engaged reader
18. **Comments (off by default)** — see decisions below
19. **Footer**

## Recommended (situational) blocks

- **Inline [CTA](../blocks/cta.md)** — mid-article, especially in long-form
- **Pull quotes** — break up long sections
- **Code blocks** — for technical articles, with syntax highlighting
- **Embedded video / tweet / Loom** — where the source reinforces the point
- **Lead magnet** — content upgrade tied to the article topic
- **Update timestamp** — "Last updated 2026-05-22" — for evergreen content that gets refreshed

## Common variations

- **How-to article** — step-by-step with numbered H2s, screenshot per step
- **Listicle** — H2 per list item, intro at top
- **Deep-dive / longform** — TOC mandatory, inline CTAs, pull quotes, generous spacing, TL;DR at top
- **News / announcement** — short, compact TOC, big featured image, single CTA, Share with AI tuned for news prompts ("what changed, who it affects")
- **Comparison piece** — `X vs Y vs Z` — table-heavy, FAQ resolves last-mile

## SEO / schema notes

- H1 on post title only (single H1 per page)
- Schema: `BlogPosting` (or `NewsArticle` for news) with `author`, `datePublished`, `dateModified`, `image`, `publisher` (emitted by Yoast / RankMath when post type is `post`)
- FAQ block → `FAQPage` schema
- Key takeaways block → optional `ItemList` schema (AI-overview-friendly)
- Recipe / how-to → corresponding schema if relevant
- `og:image` from featured image; `og:type=article`
- `hreflang` per language via Polylang / WPML

## Common post-level ACF fields

- `read_time` — auto-calc from word count (words ÷ 225), can be overridden
- `featured_image` (core post field)
- `excerpt` — short summary, used in cards and meta description fallback
- `last_updated_visible` — true_false, default false (show "Last updated…" line in meta row)
- `author` — post author (or brand byline if project uses brand-byline mode)
- `co_authors` — repeater, optional
- `seo_title`, `seo_description`, `og_image` — RankMath / Yoast fields
- TOC visibility is template-owned and required; do not add a per-post `show_toc` opt-out
- `show_tldr` — true_false, default false
- `tldr_text` — textarea, conditional on `show_tldr`
- `key_takeaways` — repeater, conditional
- `faq` — repeater (question + answer), conditional
- `sources` — repeater (label + url), conditional
- `show_inline_cta` — true_false, default false
- `inline_cta_position` — radio: `after-h2-1 | after-h2-2 | midpoint`, default `midpoint`
- `share_ai_enabled` — true_false, default true (per-post override of Theme Options)

Google Preferred Source deliberately has no per-post toggle: it is a template-level
publication control, not article content.

## Theme Options for posts (project-wide defaults)

Set under `ACF Options → Site → Blog`:

- `share_ai_enabled_globally` — true_false, default true
- `share_ai_default_destination` — select (ChatGPT / Claude / Gemini), default ChatGPT
- `share_ai_industry_guardrails` — textarea (appended to all prompts; e.g., `"– No legal recommendations"` for legal/medical projects)
- `google_preferred_source_enabled_globally` — true_false, default false until eligibility is verified
- `google_preferred_source_domain` — text, canonical hostname only (no scheme or path)
- `google_preferred_source_eligibility` — select: `unverified | eligible | ineligible`, default `unverified`
- `google_preferred_source_verified_at` — date, required when status is eligible or ineligible
- `google_preferred_source_theme` — select: `light | dark`, default `light`
- `google_preferred_source_lang` — text, optional; omit for browser-language localization
- `comments_enabled` — true_false, **default false** (off by framework default; project can opt in)
- `brand_byline_mode` — true_false, default false (false = use WP user as author; true = use brand byline)
- TOC has no word-count or heading-count threshold; short posts use the same required navigation
- `default_post_card_layout` — see [post-card.md](../blocks/post-card.md)

## Decisions locked at framework level (default, project may override)

- **Comments:** disabled by default (off in `wp options` AND not rendered in the template). Project opts in if their content strategy needs them. Cost of comments: spam, moderation load, no SEO benefit. the editorial example / the manufacturer example both ship comments off.
- **Share with AI:** enabled by default — Catalog default block
- **Share with AI destination:** ChatGPT by default; project can change in Theme Options
- **Google Preferred Source:** the template slot and eligibility check are required. Eligible canonical domains/subdomains render it on every post; ineligible publications record dated evidence and suppress the dead control; `unverified` is incomplete
- **Google Preferred Source placement:** directly after Share with AI and before social sharing
- **Brand vs human byline:** decided per project — ask the editor. Default to brand byline for editorial sites with a single voice; human byline for multi-author / personality-led blogs
- **TOC:** required on every post, including short posts and news. Generate links from real H2s; use real H3s when no H2s exist. For unsectioned content, link once to the article body with the label "Article". Never invent headings to fill the TOC
- **Key takeaways:** recommended; not auto-rendered (editor opts in per post)
- **FAQ:** recommended; not auto-rendered (editor opts in per post — better to skip than to ship 1-question FAQ)
- **Inline CTA:** opt-in per post

## Locked layout pattern — full-width intro + body-only split (catalog default)

> This is the locked catalog editorial blog layout. Every new blog single template starts here. Project-specific tweaks live on top; the skeleton is non-negotiable unless the project explicitly overrides with a recorded design decision.

**Visual shape (top → bottom):**

```
┌────────────────────────────────────────────────────────────────┐
│ Site header (sticky)                                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   POST INTRO — full container width                            │
│   ┌────────────────────────────────────────────────────────┐   │
│   │  Breadcrumb                                            │   │
│   │  H1 (post title)              [40px desktop / 28 mob]  │   │
│   │  Meta: date · by Author · X min read    [14px muted]   │   │
│   │  Featured thumbnail (16:9, container-wide, rounded)    │   │
│   └────────────────────────────────────────────────────────┘   │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   BODY — centered TOC + article pair                           │
│     ┌──────────────────┬────────────────────────────────┐      │
│     │ TOC (sticky)     │ Article body                   │      │
│     │ ≈ 280px          │ Readable project measure       │      │
│     │ At body top      │ Per-post blocks                │      │
│     │                  │                                │      │
│     │                  │ Share with AI                  │      │
│     │                  │ Preferred Source               │      │
│     │                  │ Social sharing                 │      │
│     └──────────────────┴────────────────────────────────┘      │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  Author bio band — full width, tinted background               │
├────────────────────────────────────────────────────────────────┤
│  Related posts band — full width, white                        │
├────────────────────────────────────────────────────────────────┤
│  Newsletter band — full width, dark (block paints own bg)      │
├────────────────────────────────────────────────────────────────┤
│  Site footer                                                   │
└────────────────────────────────────────────────────────────────┘
```

**Why this shape (not the alternative "TOC beside everything from breadcrumb down"):**

The TOC's job is to navigate the **article body**, not the entire page. Aligning the TOC with the body means it appears where reading actually starts — readers look up from a paragraph to the TOC, not from the breadcrumb. It also gives the featured thumbnail room to breathe at full project container width, which is a stronger editorial signal than a thumbnail squeezed beside a sidebar that's mostly empty above the fold.

**Required structural rules:**

1. **Post intro spans the container** — breadcrumb + title + meta + thumbnail all live in a single `<section>` at full container width. No sidebar in this section.
2. **Body section starts a NEW composition** — TOC on the left, article on the right. Select one of the two permitted compositions below; center the combined pair or the article within its remaining pane. Do not leave the pair pinned to one gutter with a large unused channel on the other side.
3. **TOC starts at the top of the body section** — never at the top of the article. The "top of body" is where the user can read prose, not metadata.
4. **Sidebar grid item uses default `align-items: stretch`** — DO NOT set `align-items: start`. The sidebar must stretch to content-column height so the inner TOC's `position: sticky` has scroll room within. (`start` collapses the sidebar to its intrinsic height = TOC height, and sticky has nowhere to track.)
5. **Share-with-AI + Preferred Source + share-social are inside the content column at its bottom** — same column as `the_content()`, not in a separate band, in that order.
6. **Author / related / newsletter are full-width bands BELOW the body section** — outside the container, edge-to-edge so colored backgrounds reach the viewport edges.
7. **Tablet/mobile:** at the recorded project breakpoint, body grid collapses to a single column and the TOC collapses above the article. Put the sidebar first in DOM order so keyboard and visual order agree. Layout, sticky CSS and collapse JavaScript must use that same breakpoint. Keep the prose left aligned; use project type and spacing tokens.

### Two permitted desktop compositions

Source: Norml Studio, Oct 10, 2026. These choices supersede the earlier right-TOC
example. Record the selected composition in the project page/component contract.

| Composition | TOC placement | Article placement | Centering check |
|---|---|---|---|
| `centered-pair` (default) | Left track, beside the article body | Right track, capped at the project reading measure | Center the combined TOC + gap + article within the guttered body; outside left and right space must match |
| `left-edge-toc` | At the very left of the guttered body block | Centered within the pane remaining after TOC + gap | Article center equals the remaining pane's center; do not center it against the entire viewport |

Both keep the title/meta/image intro above the split and lower bands outside it.
Center the layout, never the prose text. The gap is deliberate and adjacent;
do not push the TOC and article to opposite viewport edges. The article keeps a
readable measure and may shrink at narrower desktop sizes. Use `minmax(0, …)` to
prevent tables or long links from expanding a grid track. No cap is added to the
full-width page wrapper; a reading measure belongs to the reading component.

QA must measure the actual TOC and article coordinates at narrow desktop, normal
desktop and wide desktop widths, not merely the absence of overflow. Check equal
outside space for `centered-pair`, or centering inside the remaining article pane
for `left-edge-toc`. Also check body-top alignment, sticky scroll room and the
mobile collapse/keyboard order. Document any explicit project override.

**Reference single.php** (paste into `{theme}/single.php` and adapt):

```php
<?php
get_header( 'blog' );

while ( have_posts() ) :
    the_post();

    // Computed meta
    $word_count   = str_word_count( wp_strip_all_tags( get_post_field( 'post_content', get_the_ID() ) ) );
    $read_minutes = max( 1, (int) ceil( $word_count / 225 ) );

    // Brand byline vs human author
    $brand_byline_mode = (bool) get_field( 'brand_byline_mode', 'option' );
    $author_name = $brand_byline_mode
        ? ( get_field( 'brand_byline_name', 'option' ) ?: get_bloginfo( 'name' ) )
        : get_the_author();

    // Translatable label scaffolding (Polylang strings or i18n .po)
    $by_template       = function_exists( 'pll__' ) ? pll__( 'By %s' )       : __( 'By %s',       'theme' );
    $min_read_template = function_exists( 'pll__' ) ? pll__( '%d min read' ) : __( '%d min read', 'theme' );
?>

    <section class="post-intro">
        <div class="container post-intro__inner">
            <?php echo render_block( array( 'blockName' => 'fc/breadcrumb', 'attrs' => array() ) ); ?>
            <h1 class="post-intro__title"><?php the_title(); ?></h1>
            <p class="post-intro__meta">
                <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date() ); ?></time>
                <span><?php echo esc_html( sprintf( $by_template, $author_name ) ); ?></span>
                <span><?php echo esc_html( sprintf( $min_read_template, $read_minutes ) ); ?></span>
            </p>
            <?php if ( has_post_thumbnail() ) : ?>
                <figure class="post-intro__thumb"><?php the_post_thumbnail( 'large' ); ?></figure>
            <?php endif; ?>
        </div>
    </section>

    <section class="post-body">
        <div class="container">
            <div class="post-body__row post-body__row--centered-pair">
                <aside class="post-body__sidebar">
                    <?php echo render_block( array( 'blockName' => 'fc/toc', 'attrs' => array() ) ); ?>
                </aside>
                <div class="post-body__content">
                    <div class="entry-content"><?php the_content(); ?></div>
                    <?php echo render_block( array( 'blockName' => 'fc/share-ai',     'attrs' => array() ) ); ?>
                    <?php echo render_block( array( 'blockName' => 'fc/preferred-source', 'attrs' => array() ) ); ?>
                    <?php echo render_block( array( 'blockName' => 'fc/share-social', 'attrs' => array() ) ); ?>
                </div>
            </div>
        </div>
    </section>

    <section class="band band--author">    <div class="container"><?php echo render_block( array( 'blockName' => 'fc/author-bio',     'attrs' => array() ) ); ?></div></section>
    <section class="band band--related">   <div class="container"><?php echo render_block( array( 'blockName' => 'fc/related-posts',   'attrs' => array() ) ); ?></div></section>
    <section class="band band--newsletter">                       <?php echo render_block( array( 'blockName' => 'fc/newsletter-cta',  'attrs' => array() ) ); ?></section>

<?php endwhile;

get_footer( 'blog' );
```

**Reference CSS** (px-based, theme-base-agnostic — use the same shape regardless of project rem base):

```css
.post-intro { padding: 48px 0 32px; background: #fff; }
.post-intro__title {
    font-size: 40px; line-height: 1.18; font-weight: 700;
    letter-spacing: -0.015em; color: #111827;
    margin: 20px 0; max-width: 820px;
}
.post-intro__meta {
    font-size: 14px; line-height: 1.4; color: #6b7280;
    display: flex; flex-wrap: wrap; align-items: center;
    gap: 6px 16px; margin: 0 0 32px;
}
.post-intro__meta > * + *::before {
    content: '·'; margin-right: 16px; color: #d1d5db; display: inline-block;
}
.post-intro__thumb {
    margin: 0; border-radius: 12px; overflow: hidden; background: #f3f4f6;
}
.post-intro__thumb img {
    display: block; width: 100%; height: auto;
    aspect-ratio: 16 / 9; object-fit: cover;
}

.post-body { padding: 48px 0 64px; background: #fff; }
.post-body__row {
    display: grid;
    /* Illustrative component measures; replace with project tokens. */
    --toc-width: 280px;
    --article-measure: 660px;
    grid-template-columns: var(--toc-width) minmax(0, var(--article-measure));
    justify-content: center;
    gap: 64px;
    /* default align-items: stretch — REQUIRED so the sticky TOC inside the sidebar has scroll room */
}
/* Default: the two tracks form one centered pair. */
.post-body__row--left-edge-toc {
    grid-template-columns: var(--toc-width) minmax(0, 1fr);
    justify-content: normal;
}
.post-body__content { min-width: 0; width: 100%; max-width: var(--article-measure); }
.post-body__row--left-edge-toc .post-body__content { justify-self: center; }
.post-body__sidebar { min-width: 0; }

.band { display: block; margin: 0; padding: 0; }
.band--author     { padding: 48px 0; background: #f9fafb; border-top: 1px solid #f3f4f6; }
.band--related    { padding: 48px 0; background: #fff; }
.band--newsletter { padding: 0; background: transparent; }

/* Example project breakpoint: use the same value for grid, sticky and collapse JS. */
@media (max-width: 1024px) {
    .post-intro { padding: 32px 0 24px; }
    .post-intro__title { font-size: 28px; line-height: 1.22; margin: 16px 0; }
    .post-intro__meta { margin-bottom: 24px; }
    .post-intro__thumb { border-radius: 8px; }

    .post-body { padding: 32px 0 48px; }
    .post-body__row, .post-body__row--left-edge-toc {
        grid-template-columns: minmax(0, 1fr);
        justify-content: normal;
        gap: 24px;
    }
    .post-body__content, .post-body__row--left-edge-toc .post-body__content { justify-self: start; }
    /* Sidebar is first in DOM order; its TOC collapses above content on mobile. */

    .band--author, .band--related { padding: 32px 0; }
}
```

**Sticky-TOC mechanics (debugging checklist):**

- TOC block's OWN render.php carries `position: sticky; top: 100px` inside a desktop media query. The single.php sidebar wrapper does NOT add another sticky — let the block own it.
- If the TOC isn't sticking on desktop, check the sidebar grid item's height in DevTools. If it equals the TOC's intrinsic height, you accidentally set `align-items: start` somewhere — remove it.
- If the TOC sticks below where the body section ends (overshoots into the author band), check the body section's `overflow` — if it's `hidden`, sticky positioning falls back to absolute at the edge.
- Grid, TOC sticky state and collapse JavaScript must share the recorded project breakpoint; do not create a viewport band with mismatched desktop/mobile behavior.
- If the reading pair appears off-center, measure its outside margins rather than the prose alone. For the left-edge variant, measure the article against its remaining pane, not the viewport.

**Read-time calculation:** word count / 225 (industry standard ≈ Medium's), `max(1, ceil(...))`. Don't import a heavy library for this. Compute inline.

**Brand byline vs human author:** decided per-project in Theme Options (`brand_byline_mode`). Brand byline is preferred for editorial sites with a single voice (the product-catalog example, the manufacturer example). Human byline for multi-author / personality-led blogs. The single.php branch logic above handles both.

**i18n** — the meta-row strings `By %s` and `%d min read` MUST be either:
- registered via `pll_register_string` for Polylang projects (so translators can edit them in WP admin → Languages → Strings translations), OR
- wrapped in `__( '...', 'theme' )` for vanilla i18n via .po files.

NEVER hard-code the strings in the template.

**Block-layout-responsibility principle:**

Blocks that are designed to live in a sticky sidebar (TOC, share-sticky, callouts) MUST carry their OWN `position: sticky` in their render.php — the template does not add a wrapper sticky. This keeps the block self-contained: it can be dropped into any sidebar (column, grid item, flex item) and behave correctly. Conversely, blocks that are NOT designed for sidebars (post-card, FAQ, newsletter-cta) must NOT carry sticky CSS; that would break them inside content flow. Verify by computed-CSS measurement that exactly one `position: sticky` ancestor exists in the cascade for any element you expect to stick.

---

## Don'ts

- Don't put the blog TOC on the right or leave the reading pair off-center without an explicit recorded project override
- Don't center article text to compensate for a misplaced reading layout
- Don't use H1 anywhere except the post title
- Don't skip heading levels (H2 → H4 with no H3 = bad for accessibility and SEO)
- Don't omit a TOC because a post is short or has fewer than three headings
- Don't auto-play embedded video
- Don't put 5 different CTAs in the post body — pick one primary, repeat it 2–3 times
- Don't ship Share with AI without the post URL in the prompt — the LLM can't fetch the article without it (see [share-ai.md](../blocks/share-ai.md))
- Don't treat Google Preferred Source as a `/blog` preference, ranking guarantee, or per-post field — verify the canonical domain/subdomain once, record the result, and follow the [block gate](../blocks/preferred-source.md)
- Don't render a Google Preferred Source control for an unverified or known-ineligible hostname
- Don't render Key Takeaways AND TL;DR right next to each other unless the post is genuinely long-form (>2500 words)
- Don't enable comments without a moderation plan — spam will fill the section in days
- Don't ship a post with placeholder lorem ipsum copy in any block — fill or remove
- Don't link the author byline at the top to nothing — link it to the author archive
- Don't show "Last updated" in the meta row unless the post was actually re-edited substantively — readers see through cosmetic date refreshes
- **Don't put the TOC beside the breadcrumb / title / thumbnail.** TOC navigates the body — it starts at the body. Putting it beside the intro creates a tall empty sidebar above the fold and a 780px (not 1140px) thumbnail. Wrong shape.
- **Don't set `align-items: start` on the body grid row.** Sticky TOC will fail silently (sidebar collapses to TOC height; sticky has no scroll room).
- **Don't wrap the sidebar item in another `position: sticky`.** Let the TOC block own its sticky behavior; double-sticky causes z-index and overflow conflicts.
- **Don't omit the read-time / by-line / breadcrumb from the intro** to "save space" — they're standard reading-comprehension cues. Readers scan the meta row before they decide to read.
- **Don't render a full-width band inside the body container.** Bands go OUTSIDE the body's `<section>`, after the closing tag. Otherwise the band can't reach the viewport edges and you get the band painted at container width with awkward gutters.
