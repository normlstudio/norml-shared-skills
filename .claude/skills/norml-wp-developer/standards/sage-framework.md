# Sage Framework — Foundation

Read this FIRST. This document is the foundation every other reference file in this
skill sits on top of. The other references (`theme-architecture.md`, `file-structure.md`,
`component-system.md`, etc.) describe **This package's conventions on top of** what this
document describes — the **stock Sage framework** that every WordPress theme
starts from.

If you don't understand what Sage ships out of the box, you will end up fighting the
framework. Read this, then read the package standards.

Source: <https://roots.io/sage/docs/>

Examples reflect a Sage 11/Acorn 5 baseline. Verify current official compatibility and the
project lockfiles before choosing versions or commands. Existing project decisions win.

---

## What Sage is

**Sage** (from Roots) is a WordPress starter theme. It's not a WordPress plugin,
builder, or block library — it's a scaffolded theme that replaces the default PHP
template system with a Laravel-style architecture:

- **Composer** for PHP dependency management and PSR-4 autoloading
- **Acorn** — a Laravel IoC container adapted to run inside WordPress
- **Blade** as the template engine (compiled, cached, component-based)
- **Vite** for the asset build pipeline (dev server with HMR, production manifest)
- **Tailwind CSS** wired into the build with WordPress editor integration
- An opinionated `app/` / `resources/` / `public/` directory layout

Everything This package adds — SCSS alongside CSS, ACF PRO, Alpine.js, Splide, custom image
helpers, the responsive image size grid, ACF JSON sync, the dev-developer split of
ACF block files — is layered on top of this framework. The framework is the floor;
This package is the walls.

---

## Required versions

Baseline for a Sage theme:

| Dependency | Version |
|---|---|
| PHP | ≥ 8.2 |
| WordPress | ≥ 6.6 |
| Composer | 2.x |
| Node.js | ≥ 20.0.0 |
| Roots Acorn | ^5.0 |
| Sage | 11.x baseline; use verified stable/pinned compatible release |

Confirm these in the theme's `composer.json` (`"require": { "php": ">=8.2", "roots/acorn": "^5.0" }`)
and `package.json` (`"engines": { "node": ">=20.0.0" }`) before you start. If the host
server doesn't meet these, the build will not run and Acorn will fail to boot.

---

## Scaffolding a new theme

From the WordPress `wp-content/themes/` directory:

```bash
# Latest stable release
composer create-project roots/sage your-theme-name


cd your-theme-name
npm install
npm run build           # produces public/build/manifest.json
```

Failure to run `npm run build` before loading the theme produces this error:

> `Vite manifest not found at [/path/to/sage/public/build/manifest.json] cannot be found.`

After scaffolding:

1. Edit the `base` path in `vite.config.js` to match the theme's URL on the server
   (This package uses a dev vs. prod split — see "Vite pipeline" below).
2. Activate the theme in WP Admin → Appearance → Themes, **or** run
   `wp theme activate your-theme-name` from the theme root.
3. Replace the default `style.css` metadata block with the project-specific theme
   name, version, and author.

---

## What Sage ships out of the box

This is the stock Sage directory layout **before** This package adds anything. Compare with
`file-structure.md` to see whin projects layers on top.

```
your-theme-name/
├── app/                          # PHP application logic (namespaced App\)
│   ├── Providers/
│   │   └── ThemeServiceProvider.php   # Acorn service provider (Sage base)
│   ├── View/
│   │   ├── Components/                # Class-based Blade components
│   │   └── Composers/                 # View composers (data → views)
│   ├── filters.php                    # WordPress filters (excerpt_more, etc.)
│   └── setup.php                      # Theme setup: enqueues, menus, supports
│
├── resources/                    # Source assets & Blade templates
│   ├── css/
│   │   ├── app.css                    # Primary stylesheet
│   │   └── editor.css                 # Block editor styles
│   ├── fonts/
│   ├── images/
│   ├── js/
│   │   ├── app.js                     # Primary JS
│   │   └── editor.js                  # Block editor JS
│   └── views/                         # Blade templates
│       ├── layouts/
│       │   └── app.blade.php
│       ├── components/                # Anonymous Blade components
│       ├── forms/
│       ├── partials/                  # Loop content fragments
│       ├── 404.blade.php
│       ├── index.blade.php
│       ├── page.blade.php
│       ├── search.blade.php
│       ├── single.blade.php
│       └── template-custom.blade.php
│
├── public/                       # Vite build output — NEVER hand-edit
│   └── build/
│       ├── manifest.json
│       └── assets/
│           └── theme.json             # Auto-generated from Tailwind config
│
├── vendor/                       # Composer deps (gitignored)
├── node_modules/                 # Node deps (gitignored, never uploaded)
│
├── composer.json                 # roots/acorn, PSR-4 autoload App\
├── functions.php                 # Autoload + Acorn boot + file includes
├── index.php                     # WordPress template wrapper
├── package.json                  # Node scripts & deps
├── screenshot.png                # WP Admin theme preview
├── style.css                     # Theme metadata ONLY (no actual styles)
├── theme.json                    # Preprocessed; final generated by build
└── vite.config.js                # Asset build configuration
```

Key structural rules, directly from the Sage docs:

- **`app/` is namespaced under `App\`** with automatic Composer PSR-4 autoloading.
  Any PHP you add to `app/` should live in the `App` namespace or a sub-namespace.
- **`public/` is never hand-edited.** It's the Vite build output. Anything there is
  regenerated on `npm run build`.
- **`node_modules/` is never uploaded; production-only `vendor/` is required at runtime.**
  Build production dependencies in a verified compatible artifact or use the approved server install.
  Never omit the Composer runtime autoloader.
- **`functions.php` is a bootloader only.** Its only jobs are to require the Composer
  autoloader, boot the Acorn application, and include the theme's PHP files.
  Never put feature logic directly in `functions.php`.
- **`index.php` is a WordPress template wrapper.** It's what WordPress loads; the
  Sage layout (`resources/views/layouts/app.blade.php`) is rendered inside it.

---

## Acorn — the Laravel container inside WordPress

Acorn is what makes Sage different from a plain WordPress theme. It's a
Laravel-style IoC container that boots when WordPress finishes loading the theme, and
provides:

- **Service providers** — Laravel-style bootstrapping for theme features
- **Blade** — compiled templates with components, directives, composers
- **View composers** — data injection into Blade views (see `composers.md` on roots.io)
- **View components** — class-based components backing `<x-name />` tags
- **WP-CLI integration** — the `wp acorn ...` command namespace

### How it boots

`functions.php` contains exactly three responsibilities:

```php
<?php
use Roots\Acorn\Application;

// 1. Load the Composer autoloader
if (! file_exists($composer = __DIR__.'/vendor/autoload.php')) {
    wp_die(__('Error locating autoloader. Please run <code>composer install</code>.', 'sage'));
}
require $composer;

// 2. Boot the Acorn application with the theme's service provider
Application::configure()
    ->withProviders([App\Providers\ThemeServiceProvider::class])
    ->boot();

// 3. Register theme files (one per topic, expanded by the project)
collect(['setup', 'filters', /* ...Project additions */])
    ->each(function ($file) {
        if (! locate_template($file = "app/{$file}.php", true, true)) {
            wp_die(sprintf(__('Error locating <code>%s</code>.', 'sage'), $file));
        }
    });
```

### `ThemeServiceProvider`

Extends `Roots\Acorn\Sage\SageServiceProvider`. Override `register()` to bind
services into the container, and `boot()` to run code after all providers have
registered. The Package default keeps this minimal — only override when you genuinely
need a custom binding or Blade directive.

### WP-CLI commands (run against the verified WordPress root with the correct active theme)

| Command | When to run |
|---|---|
| `wp acorn view:cache` | Pre-compile all Blade templates — required in post-deploy |
| `wp acorn view:clear` | Clear compiled templates when debugging stale views |
| `wp acorn optimize:clear` | Clear Acorn's config/view/route cache |
| `wp acorn optimize` | Cache config + views for production (do NOT run after `view:cache`) |
| `wp acorn make:component ComponentName` | Scaffold a class-based Blade component + view |
| `wp acorn make:composer ComposerName` | Scaffold a View Composer |

**WP Engine note:** on WP Engine, run `wp acorn view:cache` as the LAST Acorn command
in post-deploy. Running `wp acorn optimize` after `view:cache` can invalidate the view
cache. See `post-deploy.sh` in any Sage theme for the canonical sequence.

---

## Blade in Sage — WordPress template hierarchy

Sage replaces WordPress's PHP template files with Blade equivalents, mapping
one-to-one onto WordPress's standard template hierarchy. Every hierarchy file is a
`.blade.php` in `resources/views/`:

| WordPress hierarchy | Sage Blade file |
|---|---|
| 404 | `404.blade.php` |
| Index (archives, blog) | `index.blade.php` |
| Search | `search.blade.php` |
| Single post | `single.blade.php` |
| Page | `page.blade.php` |
| Front page | `front-page.blade.php` |
| Home (blog index) | `home.blade.php` |
| Category archive | `category.blade.php` |
| Author archive | `author.blade.php` |
| CPT single | `single-{post_type}.blade.php` |
| CPT archive | `archive-{post_type}.blade.php` |
| Named page template | `page-{slug}.blade.php` or `template-{name}.blade.php` |

All of these extend the base layout:

```blade
@extends('layouts.app')

@section('content')
    {{-- page-specific content --}}
@endsection
```

The layout (`resources/views/layouts/app.blade.php`) contains `<html>`, `<head>`,
`<body>`, `wp_head()`, `wp_footer()`, the header/footer includes, and yields
`@yield('content')`. Everything renders inside it, which in turn is wrapped by the
root `index.php`.

### Blade components — two flavors

Sage supports both anonymous and class-based components:

- **Anonymous** — a Blade file at `resources/views/components/name.blade.php`, with
  a `@props([])` directive at the top. No PHP class. Used via `<x-name />`.
- **Class-based** — a Blade file plus a class at `app/View/Components/Name.php`
  extending `Roots\Acorn\View\Component`. Use when you need non-trivial PHP logic
  (e.g. fetching, transforming data before render).

Scaffold a class-based component with `wp acorn make:component Name`. This package uses
anonymous components by default — see `component-system.md`.

**Naming — constructor args vs HTML attributes.** When you pass data to a
class-based component, constructor args use `camelCase` and the HTML attributes use
`kebab-case`:

```blade
<x-example-component :image-id="$image" />
```

```php
public function __construct($imageId = null) { /* ... */ }
```

### View composers

Composers let you inject data into a Blade view automatically, no matter who renders
it. The class lives at `app/View/Composers/Name.php` and declares which views it
applies to via a `$views` property:

```php
namespace App\View\Composers;

use Roots\Acorn\View\Composer;

class App extends Composer
{
    protected static $views = ['*'];   // or 'partials.page-header', etc.

    public function with(): array
    {
        return ['siteName' => get_bloginfo('name', 'display')];
    }
}
```

Public methods **or** the values returned from `with()` become template variables:
`$siteName` in Blade. PSR-4 autoloading is what makes them discoverable — the class
file path and namespace must match the PSR-4 map in `composer.json`.

---

## Vite pipeline — dev, build, theme.json

Sage ships with Vite as the asset bundler, wired together by three plugins:

- **`laravel-vite-plugin`** — handles entry points, HMR refresh on Blade + PHP changes
- **`@roots/vite-plugin`** — adds WordPress-aware asset URLs and generates
  `theme.json` from the Tailwind config
- **`@tailwindcss/vite`** — Tailwind CSS v4 integration (replaces the v3 PostCSS plugin)

### Dev vs. build

| Command | Purpose |
|---|---|
| `npm run dev` | Start the Vite dev server with HMR. `vite.config.js` must match the site's local dev URL. |
| `npm run build` | Production build. Writes `public/build/` including `manifest.json` and `assets/theme.json`. |
| `npm run watch` | Rebuild on change (no dev server). |
| `npm run preview` | Preview a production build locally. |

### Entry points

`vite.config.js` declares an array of entry files. Sage's stock set is just
`resources/css/app.css`, `resources/js/app.js`, `resources/css/editor.css`,
`resources/js/editor.js`. These themes extend this with SCSS pairs
(`resources/scss/app.scss`, `resources/scss/editor.scss`) because we keep a legacy
SCSS pipeline alongside the Tailwind v4 CSS entry.

### The manifest

After `npm run build`, `public/build/manifest.json` maps source paths to hashed
output files. PHP reads this manifest to enqueue the correct files. The file paths
inside the manifest are relative to the theme root (e.g. `resources/css/app.css`).

The official Sage way to reference built assets in PHP/Blade is via the `Vite`
facade:

```php
use Illuminate\Support\Facades\Vite;

$assetUrl = Vite::asset('resources/images/example.svg');        // URL
$assetContent = Vite::content('resources/images/example.svg');  // contents
```

```blade
<img src="{{ Vite::asset('resources/images/example.svg') }}">
```

In CSS:

```css
.bg { background-image: url("@images/example.svg"); }
```

(The `@images/` alias is configured in `vite.config.js` → `resolve.alias`.)

**Existing-project adapter caveat:** our themes historically read `manifest.json` directly in
`app/setup.php` rather than going through the `Vite` facade. This is so the asset
enqueue can auto-detect whether the Vite dev server is running (by pinging
`/@vite/client`) and switch between dev-server `<script type="module">` injection
and production manifest reads. See `theme-architecture.md` and
`app/setup.php` in any The project for the canonical pattern.

### theme.json is auto-generated

The `theme.json` at the theme root is a **preprocessed template**. The real
`theme.json` WordPress reads is generated during `npm run build` at
`public/build/assets/theme.json`, and Sage filters WP to load it from there:

```php
add_filter('theme_file_path', function ($path, $file) {
    return $file === 'theme.json' ? public_path('build/assets/theme.json') : $path;
}, 10, 2);
```

The generator copies Tailwind colors, font families, and font sizes into
`theme.json` so the block editor palette matches the frontend. Disable per-category
with:

```js
wordpressThemeJson({
  disableTailwindColors: false,
  disableTailwindFonts: false,
  disableTailwindFontSizes: false,
}),
```

Because `theme.json` is generated, **never hand-edit the copy WordPress actually
reads**. Edit the preprocessed `theme.json` at the theme root, or edit
`tailwind.config.js`, then rebuild.

### Block editor (Gutenberg)

- Sage enqueues `resources/js/editor.js` and `resources/css/editor.css` in the
  editor context. Editor-only CSS goes in `editor.css`.
- Sage's `editor.css` expects the editor to be iframed. All blocks must support
  block API version 3, or the editor won't iframe and styles break.
- Because `theme.json` is generated from Tailwind, `add_theme_support()` calls for
  palette, font sizes, etc. are **ignored** — configure those via Tailwind + the
  preprocessed `theme.json`.

---

## Deployment

### Pre-deploy (local or CI)

```bash
npm run build
composer install --no-dev --optimize-autoloader
```

### What to upload

Upload the theme directory **without**:

- `node_modules/`
- Dev-only Composer packages (use `--no-dev` on the server)

Upload `public/build/` (the Vite output), `vendor/` (production-only), and
everything else.

### Post-deploy (on the server)

```bash
# Ensure Acorn's storage scaffolding exists
mkdir -p storage/framework/{cache,sessions,testing,views}
mkdir -p storage/logs
chmod -R 755 storage

# Activate the theme if it isn't already
wp theme is-active your-theme-name || wp theme activate your-theme-name

# Clear Acorn caches, then pre-compile views (LAST — do not run `optimize` after)
wp acorn optimize:clear
wp acorn view:cache

# Flush WP caches + rewrite rules
wp cache flush
wp rewrite flush
```

This is exactly the sequence in every Sage theme's `post-deploy.sh`.

### Blade file security

Every file in the theme folder is publicly accessible by default. `.blade.php`
files can leak source code. Add a server rule to block them:

**Nginx:**

```nginx
location ~* \.(blade\.php)$ { deny all; }
```

**Apache / `.htaccess`:**

```apache
<FilesMatch ".+\.(blade\.php)$">
  <IfModule mod_authz_core.c>
    Require all denied
  </IfModule>
</FilesMatch>
```

WP Engine handles this at the platform level; Kinsta and most managed hosts do not.
Verify after every migration or server change.

---

## This package's delta on top of stock Sage

This section is the "and here's what we added." It summarizes the differences
between a freshly-scaffolded Sage theme and a Sage theme. Each item has a
pointer to the other reference file that describes it in detail.

### PHP / `app/` additions

| Project file | Purpose |
|---|---|
| `app/helpers.php` | Global helpers (`bg_image`, `acf_responsive_image`, `acf_picture`, `custom_breadcrumbs`, etc.), autoloaded via Composer `"files"`. |
| `app/forms.php` | AJAX form handlers. |
| `app/newsletter-form.php` | Newsletter form handler. |
| `app/block-patterns.php` | WordPress block patterns. |
| `app/Helpers/NavigationHelper.php` | Menu/nav data transformation. |
| `app/Walkers/{Name}Walker.php` | Custom menu walkers. |

Each of these is added to the `collect(['setup', 'filters', 'forms', ...])` array in
`functions.php`. See `theme-architecture.md` for details.

### Resource pipeline additions

| Addition | Why |
|---|---|
| SCSS entry (`resources/scss/app.scss`, `resources/scss/editor.scss`) alongside CSS | Legacy SCSS for parts of the system that aren't Tailwind-native yet. Both are Vite entry points. |
| `resources/components/{name}/` | JS + CSS co-located with their Blade component. |
| `resources/icons/` + `vite-plugin-svg-icons` | SVG sprite, rendered via `<x-icon>`. |
| `resources/animations/` | Lottie JSON files. |
| `resources/fonts/` + `@font-face` in `resources/css/fonts.css` | Custom fonts. |
| `vite-imagetools` in `vite.config.js` | Generates WebP + JPEG/PNG variants at build time. |
| Custom "fix-imagetools-manifest-keys" Vite plugin | Rewrites the manifest so the PHP layer can resolve image originals + WebP counterparts. |
| `resolve.alias` (`@scripts`, `@styles`, `@scss`, `@fonts`, `@images`, `@components`, `@videos`) | Cleaner imports from Blade/CSS/JS. |

### Asset enqueue pattern (overrides Sage default)

An optional existing adapter replaces Sage's stock enqueue with a custom `app_enqueue_assets()` function in
`app/setup.php` that:

1. Checks if the Vite dev server is reachable (`GET /@vite/client`, 0.5s timeout).
2. **Dev mode:** injects `<script type="module">` tags for `@vite/client` and each
   entry, bypassing `wp_enqueue_script` (which can't handle `type="module"` ordering
   cleanly).
3. **Prod mode:** reads `public/build/manifest.json` and enqueues CSS/JS via
   `wp_enqueue_style` / `wp_enqueue_script` with hashed filenames.
4. Localizes the script bundle with `ajaxParams` (`ajax_url`, nonce).

The `vite.config.js` `base` path switches between dev and prod:

```js
const basePath = isProduction
  ? '/wp-content/themes/{theme-name}/public/build/'
  : '/app/themes/{theme-name}/public/build/';  // WP Engine-style dev path
```

### ACF PRO conventions (Sage doesn't require ACF)

- JSON sync enabled in `app/filters.php` — save/load from `acf-json/`.
- Field group keys: `group_{descriptive_name}`.
- Field keys: `field_{descriptive_name}`.
- CPTs registered via ACF's built-in CPT UI, synced as `post_type_{hash}.json`.
- Blocks registered via `acf_register_block_type()` in `app/acf-blocks-{developer}.php`.

See `file-structure.md` and `acf-blocks.md`.

### Responsive image sizes

This baseline registers a standard grid of image sizes in `app/setup.php`:
`responsive-xl`/`-crop` (1920×1080), `-lg` (1200×675), `-md` (992×558),
`-sm` (768×432), `-xs` (576×324). Breakpoint math is fixed at 1200 / 992 / 768 / 576.

### JavaScript stack

Sage ships zero JS framework. This package adds:

- **Alpine.js** (+ `@alpinejs/collapse`) for interactivity
- **GSAP** for animations
- **Splide.js** for carousels
- **lottie-web** for JSON animations

All imported through `resources/js/app.js`. No jQuery, no vanilla DOM for
interactive features.

### Tailwind CSS v4

- Stock Sage supports Tailwind but version-agnostic. This package is **Tailwind v4**
  (`@tailwindcss/vite`, `tailwindcss@^4`) with the `@theme` directive for design
  tokens.
- Design tokens live in `resources/css/theme-colors.css` and
  `resources/css/theme-breakpoints.css`.
- Component classes in `resources/css/components.css` inside `@layer components`.

See `css-design-system.md`.

### Deployment artifact: `post-deploy.sh`

Every Sage theme ships with a `post-deploy.sh` at the theme root following
the WP Engine recipe (storage dirs, theme activation, `wp acorn optimize:clear`,
`wp acorn view:cache`, cache+rewrite flush). Do not reinvent this per project.

---

## Quick troubleshooting map

| Symptom | First check |
|---|---|
| `Vite manifest not found` | Run `npm run build`. |
| Styles missing in dev, work in build | Dev server not reachable. Check `vite.config.js` `base`, `server.host`, `server.port`, HTTPS cert. |
| Changes to Blade/PHP don't trigger HMR refresh | Confirm `laravel-vite-plugin`'s `refresh:` array includes the path. |
| Editor styles broken | Check that `editor.css` is enqueued via `enqueue_block_editor_assets` AND that all blocks are API v3. |
| `wp acorn ...` command not found | `composer install` didn't complete, or Acorn isn't in `composer.json` (should be `roots/acorn ^5.0`). |
| Views render stale after deploy | `wp acorn view:clear` then `wp acorn view:cache`. |
| `theme.json` palette doesn't match frontend | Rebuild — `theme.json` is regenerated from Tailwind on `npm run build`. |
| ACF field groups not appearing on other dev's machine | They're in `acf-json/`; they load automatically. Check `app/filters.php` has the save/load filters. |

---

## When to update this file

Update this reference when:

- Sage bumps a major version (currently 11.x) and changes directory layout, commands, or required versions.
- Acorn bumps a major version (currently 5.x).
- Roots replaces Vite with a different bundler (was Bud in Sage 10, Vite in Sage 11).
- The project standardizes a new customization on top of Sage and the delta list above no longer reflects reality.

For Project-side convention changes that don't touch Sage itself, update the matching
reference file instead (`theme-architecture.md`, `file-structure.md`,
`component-system.md`, etc.).
