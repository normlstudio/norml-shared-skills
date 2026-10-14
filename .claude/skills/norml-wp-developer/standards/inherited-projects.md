# Inherited Projects (Non-Sage / Existing Themes)

This document defines how to work inside a WordPress project thin projects didn't start from scratch — usually a theme inherited from a client, a previous agency, or an in-house developer. Most often these themes are **not on Roots Sage**; they may be vanilla WordPress, a custom theme, Understrap, GeneratePress, a Genesis child theme, a Bootstrap-based starter, or anything else.

The other reference files in this skill describe **how This package builds new themes from scratch** (Sage + Acorn + Blade + Tailwind v4 + Vite + Alpine.js + ACF PRO). This file describes **how this package applies its core principles inside someone else's existing structure** without rewriting the world.

**Read this file FIRST whenever you open a WordPress project you didn't scaffold yourself.**

---

## The default: respect the existing architecture

When you open an inherited theme:

1. **Read the existing structure end-to-end before writing anything.** Start by mapping:
   - Theme entry point (`functions.php`, `inc/`, `lib/`, `includes/`, or whatever the theme uses)
   - Template hierarchy in use (`single-{cpt}.php`, `archive-{cpt}.php`, `page-{slug}.php`, partials)
   - Section / component organization (often `template-parts/`, `partials/`, `parts/`, `components/`, `blocks/`, or none at all)
   - Asset pipeline (Webpack, Vite, Gulp, Mix, plain CSS/JS, none)
   - How CPTs and taxonomies are registered (PHP code in theme? CPT UI plugin? ACF PRO? a custom plugin?)
   - How ACF is used (PHP-registered fields? Local JSON sync? Synced from admin? Not at all?)
   - How blocks are registered (native Gutenberg `block.json`? ACF blocks via `acf_register_block_type()`? Both? A page builder instead?)
   - What page builder, if any, the editor uses today (Elementor, Divi, WPBakery, Beaver Builder, Bricks, Oxygen, native Gutenberg)

2. **Match the existing patterns when you add new code.** If the theme keeps sections under `template-parts/sections/`, your new section goes there — not in a freshly invented `resources/views/sections/`. If it uses `get_template_part()` includes, use that — don't bolt Blade onto a non-Sage theme. If field group keys look like `group_5fc83e1234567`, don't suddenly start writing `group_descriptive_name`. Consistency beats your preference.

3. **Don't introduce a new framework, build system, or templating engine without explicit approval.** Don't add Sage. Don't add Acorn. Don't add Blade. Don't add Vite. Don't add Tailwind v4. Don't add Alpine.js. Don't replace the existing CSS pipeline. Each of those is a separately scoped refactor that ripples through every other file — they belong to a planned project with its own scope, not a "while I was in there" addition.

4. **If the existing architecture is genuinely bad and worth refactoring**, call it out explicitly and propose it as a separate scope. Examples of "worth surfacing":
   - Templates with thousands of lines of inline HTML and no partial extraction
   - ACF fields hard-coded in PHP that should be JSON-synced for diffability
   - jQuery soup with no module boundaries and broken interactivity
   - "Blocks" rendered via huge `the_content()` filters or shortcodes instead of real block registration
   - Page builder lock-in that makes content unportable
   - No design tokens — every color is a hex literal in 200 places

   The conversation looks like: *"This theme's section organization is going to be hard to extend. We can keep matching the existing pattern, or we can refactor `X` to `{Y}`. Refactor would touch ~Z files and unblock {benefits}. Want me to plan it as a separate ticket?"* Then **wait for the user's decision** — never silently refactor while doing something else.

---

## Core principles that apply regardless of framework

This package's core principles for WordPress are not Sage-specific. Sage just makes them ergonomic. Apply them in any theme:

### 1. Sections / Components / Partials separation

Whatever the theme calls them, three layers should exist:

| Layer | What it is | Typical non-Sage location |
|---|---|---|
| **Sections** | Full-width page blocks (hero, benefits, FAQ, CTA). One file per section. | `template-parts/sections/`, `partials/sections/`, `parts/sections/`, `blocks/` |
| **Components** | Small reusable UI atoms (button, card, icon, modal). One file per component. | `template-parts/components/`, `parts/components/`, `components/` |
| **Partials** | WordPress loop fragments (`content.php`, `content-single.php`, `content-page.php`). | Root of `template-parts/` |

If the inherited theme doesn't separate these — files dumped at the theme root, or one giant `template-parts/` with no sub-folders — **add the missing folder rather than continuing the mess.** Match the theme's existing naming convention: if it uses `parts/` instead of `template-parts/`, use `parts/`.

### 2. Sections fetch their own ACF data; components receive props

A **section** is responsible for getting its own ACF data and rendering. A **component** is stateless — it takes data via arguments and renders. This rule is framework-agnostic.

In Blade (Sage projects):
```blade
{{-- template-parts/sections/benefits.blade.php --}}
@php $items = get_field('items') ?: []; @endphp
@foreach ($items as $item)
    <x-card :title="$item['title']" />
@endforeach
```

In vanilla PHP (`get_template_part()` style — most inherited themes):
```php
<?php
// template-parts/sections/benefits.php
$items = get_field('items') ?: [];
foreach ($items as $item) {
    get_template_part('template-parts/components/card', null, [
        'title' => $item['title'],
    ]);
}
```

The component file then reads its props from `$args` (WordPress 5.5+):
```php
<?php
// template-parts/components/card.php
$title = $args['title'] ?? '';
?>
<div class="card"><?= esc_html($title); ?></div>
```

The syntax doesn't matter — the **separation of concerns** does. Sections own data. Components own rendering. Partials own loop content. A component must NEVER call `get_field()` directly. A section must NEVER hardcode markup that belongs in a component.

### 3. Gutenberg + ACF for content authoring (the default)

Even without Sage, This package's preferred way to build editor-facing content is **Gutenberg as the editor + ACF blocks as the building blocks**. This holds for:

- New pages built from blocks in the editor
- New CPT singles (`single-{cpt}.php` renders `the_content()` which renders the ACF blocks)
- New CPT archives (`archive-{cpt}.php` may use blocks for the surrounding chrome + a loop for the items)

**Compatibility decisions:**

| Inherited setup | What to do |
|---|---|
| Native Gutenberg + ACF PRO already in use | Continue the existing pattern. Add new ACF blocks for new sections. |
| Native Gutenberg without ACF | Fine — keep registering native blocks via `block.json` and React render. Don't force ACF in. |
| ACF without proper block registration (page-level fields + empty `the_content()`) | Most common refactor candidate. Surface it. Propose migrating page-level ACF to ACF blocks so the editor can rearrange. |
| Elementor / Divi / WPBakery / Beaver Builder / Bricks / Oxygen | **Do NOT silently introduce Gutenberg as a parallel system.** Either stay inside the existing builder for the task, or surface the trade-off and plan a migration as a separate scope. See the project build workflow for the migration playbook on small jobs. |
| Classic editor with shortcodes everywhere | Surface. Almost always worth a migration plan. |

### 4. ACF block registration pattern (works in any theme)

The package ACF block registration — usable inside `acf-blocks-{dev}.php` (Sage) or inside any `functions.php`-derived structure (non-Sage):

```php
<?php
// inc/acf-blocks.php (or wherever the theme keeps init code)

add_action('acf/init', function () {
    if (! function_exists('acf_register_block_type')) {
        return;
    }

    acf_register_block_type([
        'name'              => 'benefits',
        'title'             => __('Benefits', 'theme-textdomain'),
        'description'       => __('Three-column benefits grid.', 'theme-textdomain'),
        'category'          => 'project',          // see custom block category below
        'icon'              => 'star-filled',
        'mode'              => 'preview',
        'supports'          => [
            'align'  => false,
            'anchor' => true,
            'jsx'    => true,
        ],
        'example'           => [
            'attributes' => [
                'mode' => 'preview',
                'data' => ['is_example' => true],
            ],
        ],
        'render_callback'   => function ($block) {
            // In Sage:
            //   echo view('sections.benefits', ['block' => $block]);
            //
            // In vanilla PHP — pass $block to the template via set_query_var:
            set_query_var('block', $block);
            get_template_part('template-parts/sections/benefits');
        },
    ]);
});
```

**Custom block category** — register once per theme so all ACF blocks group together in the inserter:

```php
add_filter('block_categories_all', function ($categories) {
    array_unshift($categories, [
        'slug'  => 'project',
        'title' => __('Project Blocks', 'theme-textdomain'),
        'icon'  => null,
    ]);
    return $categories;
});
```

**Rules that hold across frameworks:**

- Register inside `acf/init` action, guarded by `function_exists('acf_register_block_type')`
- Each block has a **dedicated section / template file** — never inline the render markup in the registration array
- Each block declares a **block category** (use the shared `project` category)
- Each block supports `anchor` so editors can link to specific sections
- Each block has a **preview** visible in the inserter (see next section — non-negotiable)
- Field group key follows the existing theme's convention (descriptive `group_benefits_section_block` if the theme uses that style; hashed `group_xxxxxxxxx` if the theme uses ACF's auto-generated style)
- One file per block registration when the theme has 10+ blocks; group small batches by feature when there are only 2–3

### 5. Block previews in the admin (the Package default)

**Every ACF block must have a preview visible from the block inserter.** Editors choosing a block should see what the block looks like, not a generic dashicon. A plain icon is not enough.

**Package default: live preview via `example` + `mode: 'preview'`.** Static screenshot is the fallback for blocks too heavy or unreliable to live-render.

#### Live preview (default)

The block registers an `example` payload that triggers `render_callback` in "example" mode. The section template detects `$block['data']['is_example']` and renders with hardcoded sample content. This gives a real, styled live preview in the inserter (Gutenberg → block inserter → hover the block) and inside the editor when the block is first inserted.

Registration:
```php
'mode'    => 'preview',
'example' => [
    'attributes' => [
        'mode' => 'preview',
        'data' => ['is_example' => true],
    ],
],
```

Section template:
```php
<?php
// template-parts/sections/benefits.php
$block       = get_query_var('block');
$is_example  = ! empty($block['data']['is_example']);

if ($is_example) {
    $title = 'Sample benefits headline';
    $items = [
        ['title' => 'Fast', 'description' => 'Built for speed.'],
        ['title' => 'Reliable', 'description' => 'Tested in production.'],
        ['title' => 'Flexible', 'description' => 'Adapts to any workflow.'],
    ];
} else {
    $title = get_field('section_title') ?: 'Benefits';
    $items = get_field('items') ?: [];
}
?>

<section class="benefits">
    <h2><?= esc_html($title); ?></h2>
    <div class="benefits-grid">
        <?php foreach ($items as $item) : ?>
            <?php
            get_template_part('template-parts/components/card', null, [
                'title'       => $item['title'],
                'description' => $item['description'],
            ]);
            ?>
        <?php endforeach; ?>
    </div>
</section>
```

The example payload should match what the block looks like with realistic content — not lorem ipsum so generic the editor can't tell what they're picking.

#### Static screenshot (fallback)

For blocks too heavy or unreliable to live-render (complex sliders, blocks that depend on external API data, blocks with global state), place a PNG at `{theme}/assets/blocks/previews/{block-name}.png` and serve it via `render_callback` in example mode:

```php
'render_callback' => function ($block) {
    if (! empty($block['data']['is_example'])) {
        $url = get_stylesheet_directory_uri() . '/assets/blocks/previews/' . sanitize_key(str_replace('acf/', '', $block['name'])) . '.png';
        echo '<img src="' . esc_url($url) . '" alt="' . esc_attr(($block['title'] ?? 'Block preview')) . '" style="width:100%;height:auto;display:block;" />';
        return;
    }
    // Real render
    set_query_var('block', $block);
    get_template_part('template-parts/sections/' . sanitize_key(str_replace('acf/', '', $block['name'])));
},
```

**Rules for static screenshots:**

- Capture from the staging site at desktop width (≥1440px) cropped tight to the block
- Save as PNG, ≤300KB (use `pngquant` or similar if heavier)
- File name matches the block's registered `name` exactly (`benefits.png`, `pricing-table.png`)
- Re-capture whenever the block design changes — stale screenshots actively mislead editors
- Document in the theme README which blocks use screenshot fallback (so a future dev knows to refresh them after design changes)

### 6. CPT + archive + single = blocks-based by default

When adding a new custom post type with both archive and single views:

**Single template** (`single-{cpt}.php` or `single-{cpt}.blade.php`):

- Render `the_content()` so the editor controls the body via Gutenberg blocks
- Hardcode only the truly fixed chrome (hero with title/meta, related-posts at the bottom, share buttons)
- Wrap the chrome itself in ACF blocks too whenever the layout might vary across posts in the same CPT (e.g., some case studies have a video hero, others have an image hero)

**Archive template** (`archive-{cpt}.php` or `archive-{cpt}.blade.php`):

- The surrounding page (intro section, filters, CTA) is built from ACF blocks placed on the **CPT archive's editable page** — either an ACF options-style group bound to the archive URL, or an independently named controlling page whose content is queried by the archive template without claiming the same public route
- The actual loop renders item cards using a reusable card component
- One archive page = one editable block stack that the editor can rearrange without a developer

**The test:** the editor should never have to ask a developer to change the hero copy on the blog index page, or to reorder sections on a case study page. If the architecture forces that, it's wrong — surface it.

### 7. CSS architecture — the 3-layer model (NO per-page stylesheets, EVER)

**This is the non-negotiable rule for every new block, section, or page on every inherited theme.** It exists because the alternative — letting each new page or block grow its own `css/blocks-{page}-page.css` with its own palette tokens, button styles, and typography — has measurably fragmented client sites. Per-page stylesheets are how a site stops looking like one site and starts looking like a stack of unrelated landing pages held together by a header.


#### The model

| Layer | What it is | Where it lives | When it loads |
|---|---|---|---|
| **1 — Tokens** | CSS variables at `:root` (colors, fonts, spacing, radii) | Foundational stylesheet (`css/header.css :root`, `css/components.css :root`, or wherever the theme already declares its base palette) | Always |
| **2 — Components** | ONE shared stylesheet of reusable visual primitives — buttons, cards, sections, accordions, banners, stats, eyebrows, display utility, container | `css/components.css` (single file) | Always — enqueued globally on every page |
| **3 — Block layout** | Per-block layout-only stylesheet — grid/flex/positioning/decorative pseudo-elements | `css/blocks/{block-slug}.css` | Conditionally via `has_block()` — only on pages containing the block |

**Per-page stylesheets (`css/blocks-{page}-page.css`, `style-{page}.css`, anything scoped to one page) are FORBIDDEN.** If you find yourself reaching for one, stop. The pattern always re-defines buttons, cards, typography, eyebrows, and accordions inside the per-page file, which drifts the site's visual system, fragments the brand, and creates maintenance debt nobody pays back.

#### Layer 1 — Tokens (shared, global)

CSS variables at `:root`. Single source of truth for the site's palette, fonts, and any other design primitive. Typically two sources:

- Project extensions added to `css/components.css :root` when the base palette doesn't cover a needed semantic role (`--site-light`, `--site-border`, `--site-muted`, `--site-accent-dark`, `--site-danger`, `--site-font-display`, `--site-font-body`, etc.)

**Before introducing a new token:** confirm none of the existing ones covers it. If you genuinely need a new one, add it to `components.css :root` with a one-line comment on its semantic role. Never add per-page tokens (`--page-dark`, `--pricing-gold`, `--landing-accent`).

#### Layer 2 — Components (shared, site-wide, ALWAYS enqueued)

ONE file: `css/components.css`. Holds the site's reusable visual primitives that every block on every page composes:

- `.site-container` — site-standard width wrapper
- `.site-display` — display-font utility
- `.site-eyebrow` — small accent uppercase tag text above H2s
- `.site-section` (+ `--white` / `--alt` / `--dark` variants) — standard content section (padding, type)
- `.site-card` (+ variants) — generic card primitive
- `.site-card-grid` — auto-fit card layout
- `.site-stats-bar` / `.site-stat` — big-number stats row
- `.site-banner` — full-width banner (urgency, announcement)
- `.site-accordion` — Q/A unit
- `.site-review-card` — testimonial card

Naming convention: `.site-{component}` and `.site-{component}__{element}` (BEM). Variants use `--variant` modifiers. The `.site-*` prefix isolates project-authored classes from theme / plugin / page-builder classes.

**When to add to Layer 2:** the pattern could appear on another page (button, card, eyebrow, accordion, review, banner, stat). Promote it here so the system grows. The audit-first rule below decides this for you.

**Body-level scoping for page-specific tweaks:** when a page needs scoped CSS (e.g. hide a builder's auto-printed title), use a body class set by `body_class` filter that checks `has_block('acf/{slug}', $content)`, then target it in `css/components.css` as `body.has-{class} .selector { ... }`. Never hardcode post IDs.

#### Layer 3 — Block layout (per-block, conditionally enqueued)

`css/blocks/{block-slug}.css`. **LAYOUT ONLY.** Grid, flex, positioning, decorative pseudo-elements, responsive breakpoints unique to the block. Class naming: `.{block-slug}__{element}` (e.g. `.featured-hero__grid`, `.featured-hero__trust-strip`). The block slug prefix isolates the styles so two blocks with similar element names don't collide.


**Conditional enqueue (in `_bootstrap.php` or equivalent):**

```php
add_action('wp_enqueue_scripts', function () {
    // Layer 2 — always
    wp_enqueue_style('site-components',
        get_stylesheet_directory_uri() . '/css/components.css',
        [], filemtime(get_stylesheet_directory() . '/css/components.css'));

    // Layer 3 — only if the block is on the page
    if (is_singular() && has_block('acf/featured-hero')) {
        wp_enqueue_style('block-featured-hero',
            get_stylesheet_directory_uri() . '/css/blocks/featured-hero.css',
            ['site-components'], filemtime(get_stylesheet_directory() . '/css/blocks/featured-hero.css'));
    }
});

// Load the same sheets in the editor so previews match the front-end.
add_action('enqueue_block_editor_assets', function () { /* same enqueues */ });
```

This keeps every page's CSS payload tight without sacrificing the design system.

#### Don't vs do (the cheat sheet)

| Don't | Do |
|---|---|
| Create `css/blocks-{page}-page.css` or any per-page stylesheet | Put reusable patterns into `css/components.css` (Layer 2) — block-specific files are layout only |
| Introduce parallel page-scoped tokens (`--page-dark`, `--pricing-gold`, `--landing-accent`) | Reference the site's existing palette tokens, plus `--site-*` extensions in `css/components.css :root` |
| Add Barlow Condensed / Poppins / etc. from a Figma export | Use the site's already-loaded fonts via `var(--site-font-display)` / `var(--site-font-body)` |
| Build new `.cta-button` styles | Inherit / match the site's existing button class (`.et_pb_button` for Divi-based themes, the theme's primary button class otherwise) |
| Copy-paste mockup CSS verbatim | Audit the mockup → map every color / font / radius / spacing to an existing token or `.site-*` component → only ship what reuses the system |
| Hardcode hex values (`#0d1317`, `#ebd14a`) inside block files | Reference the variables (`var(--header-color-dark)` or `var(--site-*)`) so a future palette change cascades |

#### The audit-first rule (before writing ANY visual styling)

Before opening a new block file:

1. **Audit `css/components.css` first.** Does it already contain the pattern (card, button, eyebrow, accordion, banner, stat)? If yes → use it.
2. **If not, ask: would another block on another page also use this?** If yes → promote it to Layer 2 (`components.css`). If genuinely unique to this one block → Layer 3.
3. **Only then** open `css/blocks/{slug}.css` for the layout glue.

#### Pre-flight checklist for any new block

Before opening `inc/blocks/{slug}.php` (or wherever the theme registers blocks):

1. **Tokens reused, not introduced.** Every color comes from `var(--site-color-*)` (the theme's base palette) or `var(--site-*)`. Zero hex literals in block files.
2. **No `font-family` override in block files.** Use the font tokens; usually a `.site-display` class on the element is enough.
3. **Buttons use existing patterns.** Inherit / match the site's existing button class. Never bespoke `.cta-button` styles.
4. **Block layout file ≤ 80 lines** for typical blocks — or justify in a comment at the top why it's bigger (e.g. a genuinely unique widget like a calculator).
5. **No per-page sheet.** If you find yourself reaching for `css/blocks-{this-page}-page.css`, stop and re-route into the 3-layer model.

#### Refactoring an existing per-page stylesheet


#### Note on Sage / Tailwind v4 projects

In Sage projects with Tailwind v4, the same 3-layer model applies — it's just expressed in Tailwind v4 conventions (design tokens in `@theme`, components in `@layer components` in `resources/css/components.css`, block layout as utility classes on the section template or scoped `@layer components` rules in the section's CSS file). The rule "no per-page stylesheets" still holds. See `css-design-system.md` for Sage-specific implementation.

---

## Decision flow when starting work on an inherited project

```
1. Read the theme top-to-bottom
   (functions.php → inc/lib/includes → template-parts → assets → acf-json or PHP fields)

2. Identify:
   - Framework / templating engine
   - Build system
   - ACF usage style
   - Block registration approach
   - CPT / taxonomy registration approach
   - Page builder, if any

3. Document what you found (one-paragraph summary back to the user)

4. For the requested task:
   ├── Does the existing pattern support it cleanly?
   │   └── YES → follow the existing pattern.
   │            Apply the core principles inside it.
   │
   └── NO → propose a refactor as a separate scope.
            ├── If user approves refactor →
            │     do it as its own task with its own changelog.
            └── If user defers →
                  match the existing (suboptimal) pattern for now,
                  note the debt in the project's CLAUDE.md or changelog.
```

If `{theme_root}/.claude/docs/` exists (scraped by read-only project discovery), read it first — that's where the architecture map already lives. If absent, map the existing theme and supported runtime evidence directly before non-trivial work.

---

## What you MAY introduce silently (no permission needed)

These fill obvious gaps without restructuring anything:

- A new section file under the theme's existing section folder
- A new component file under the theme's existing component folder
- A new ACF block registration in the theme's existing block-registration file
- A new ACF field group via the admin (will save wherever the theme has ACF JSON configured, or via PHP if that's the existing pattern)
- A new partial under the theme's existing partial folder
- A new utility class in the theme's existing CSS file
- A new icon under the theme's existing icon folder / sprite

## What you MUST NOT introduce silently (always ask)

These restructure the project and have wide downstream effects. Surface, propose, wait for approval, then do it as its own scope with its own changelog entry:

- A new framework or templating engine (Sage, Blade, Twig, Timber)
- A new build pipeline (Vite, Webpack rewire, esbuild, Gulp replacement)
- A new CSS framework (Tailwind v4, Bootstrap 5)
- A new JS framework (Alpine.js, React, Vue) if the theme doesn't already use it
- A new global folder structure (`resources/`, `src/`)
- Replacing PHP-registered ACF fields with JSON sync (changes the workflow for the whole team)
- Replacing native Gutenberg blocks with ACF blocks (or vice versa)
- Replacing CPT UI plugin with ACF-registered CPTs (or vice versa)
- Removing or replacing a page builder (Elementor, Divi, WPBakery, Bricks, Oxygen)
- Renaming or moving the theme's template-parts / parts / components folder

---

## When refactoring IS the task

If the user explicitly asks to refactor the inherited theme — for example, "let's migrate this Elementor site to Gutenberg" or "let's pull these PHP-registered ACF fields into JSON sync" — then refactor freely within the scope agreed.

Even then, do it in phases:

1. **Phase 0: snapshot** — full DB + files backup, `the authorized migration workflow` style. Document the rollback path.
2. **Phase 1: parity** — rebuild the existing structure in the target pattern. Don't change behavior yet.
3. **Phase 2: cutover** — switch the theme/page/post type to the new structure. QA gates per `standards/qa-gates.md`.
4. **Phase 3: cleanup** — remove the old structure. Drop dead code. Update theme README.

Treat each phase as its own PR with its own changelog. Never bundle a refactor into a feature PR.
