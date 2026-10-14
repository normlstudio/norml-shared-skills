# Theme Architecture

This document defines the core framework architecture for WordPress projects.

---

## Framework Stack

These themes are built on **Roots Sage** with **Acorn v5**, which brings Laravel-style
patterns to WordPress:

- **Composer** for PHP dependency management and PSR-4 autoloading
- **Acorn** as the application container (Laravel IoC container for WordPress)
- **Blade** as the template engine (compiled, cached, component-based)
- **View Composers** for data injection into templates
- **Service Providers** for bootstrapping theme features

---

## Bootstrap Flow

### `functions.php` — Theme Entry Point

```php
<?php
use Roots\Acorn\Application;

// 1. Composer autoloader
require __DIR__.'/vendor/autoload.php';

// 2. Boot Acorn with theme service provider
Application::configure()
    ->withProviders([App\Providers\ThemeServiceProvider::class])
    ->boot();

// 3. Include theme function files
collect(['setup', 'filters', 'forms', 'newsletter-form', 'block-patterns', 'acf-blocks-{dev}'])
    ->each(function ($file) {
        if (! locate_template($file = "app/{$file}.php", true, true)) {
            wp_die(sprintf(__('Error locating <code>%s</code>.', 'sage'), $file));
        }
    });
```

**Rules:**
- `functions.php` ONLY does three things: autoload, boot Acorn, include files
- Never put logic directly in `functions.php`
- Add new function files to the `collect()` array
- ACF block files are named per developer: `acf-blocks-{name}.php`

### `app/Providers/ThemeServiceProvider.php`

Extends `SageServiceProvider`. Use for:
- Registering custom bindings
- Bootstrapping theme services
- Adding custom Blade directives

Default is minimal — only override `register()` and `boot()` when needed.

### `app/setup.php` — Theme Setup

This is the main theme configuration file. It handles:

1. **Asset enqueue** — Vite-aware asset loading (dev server detection + production manifest)
2. **Theme support** — `title-tag`, `post-thumbnails`, `html5`, `editor-styles`, etc.
3. **Navigation menus** — `register_nav_menus()` with semantic names
4. **Image sizes** — Responsive breakpoint sizes (`responsive-xl`, `responsive-lg`, etc.)
5. **Sidebar registration** — `register_sidebar()` for widget areas
6. **Custom post type configuration** — Rewrite rules, query modifications
7. **Plugin overrides** — Dequeue unwanted plugin styles

**Asset Enqueue Pattern:**
```php
function app_enqueue_assets()
{
    // 1. Check if Vite dev server is running
    // 2. If dev: inject <script type="module"> tags directly
    // 3. If prod: read manifest.json, enqueue CSS and JS files
    // 4. Localize script with ajaxParams (ajax_url + nonce)
}
add_action('wp_enqueue_scripts', __NAMESPACE__.'\\app_enqueue_assets', 20);
```

The asset system auto-detects dev vs production mode. In dev, it injects Vite HMR client.
In production, it reads the Vite manifest for hashed filenames.

**Editor assets** are enqueued separately via `enqueue_block_editor_assets` to ensure
Tailwind classes work in the Gutenberg editor.

### `app/filters.php` — WordPress Filters

Handles WordPress filter hooks:
- Excerpt modification
- **ACF JSON save/load paths** — CRITICAL: redirects ACF JSON to `acf-json/` directory

```php
// ACF JSON sync configuration
add_filter('acf/settings/save_json', function ($path) {
    return get_stylesheet_directory().'/acf-json';
});

add_filter('acf/settings/load_json', function ($paths) {
    unset($paths[0]);
    $paths[] = get_stylesheet_directory().'/acf-json';
    return $paths;
});
```

### `app/helpers.php` — Global Helper Functions

Autoloaded via Composer (`"files": ["app/helpers.php"]`). Contains:

- `bg_image($src)` — Background image with WebP + CSS image-set() support
- `acf_responsive_image($image, $size, $attr)` — Responsive `<img>` from ACF field
- `acf_picture($image, $size, $attr)` — `<picture>` element with WebP source
- `get_blog_categories($post_type)` — Category list for archive filtering
- `custom_breadcrumbs()` — Breadcrumb data array
- `get_reading_time($content)` — Estimated reading time
- `get_custom_categories($post_id)` — Formatted category spans

**Rules for helpers:**
- Every function MUST be wrapped in `if (! function_exists('name'))` guard
- Functions return data, not HTML (exception: image helpers return HTML strings)
- Helper functions are project-agnostic utilities

---

## View Composers

View composers inject data into Blade templates automatically:

```php
namespace App\View\Composers;

use Roots\Acorn\View\Composer;

class App extends Composer
{
    protected static $views = ['*']; // Applies to all views

    public function siteName(): string
    {
        return get_bloginfo('name', 'display');
    }
}
```

**Rules:**
- `$views = ['*']` for global data, or specify view names
- Methods become template variables: `$siteName` in Blade
- Use for computed data that multiple templates need

---

## Custom Post Types

ACF UI/JSON is one registration option; site-core PHP registration is appropriate for portable content.

CPT ownership follows the project architecture: durable registration may belong in a plugin.
Use ACF UI/JSON only when its ownership and dependency tradeoff are deliberately selected.

If a CPT needs custom rewrite rules or query modifications, add those in `app/setup.php`:

```php
// Modify CPT rewrite rules
add_filter('register_post_type_args', function ($args, $post_type) {
    if ($post_type === 'case_study') {
        $args['rewrite']['slug'] = 'case-studies';
        $args['rewrite']['with_front'] = false;
        $args['has_archive'] = 'case-studies';
    }
    return $args;
}, 10, 2);

// Custom rewrite rules for pagination
add_action('init', function () {
    add_rewrite_rule('case-studies/page/([0-9]+)/?$', 'index.php?post_type=case_study&paged=$matches[1]', 'top');
});
```

---

## Navigation Menus

Menus are registered in `app/setup.php`:

```php
register_nav_menus([
    'primary_navigation' => __('Primary Navigation', 'sage'),
    'header-menu' => __('Header Menu', 'sage'),
    'footer-company' => __('Footer - Company', 'sage'),
    'footer-who-we-serve' => __('Footer - Who We Serve', 'sage'),
    'footer-solutions' => __('Footer - Solutions', 'sage'),
    'footer-learn' => __('Footer - Learn', 'sage'),
    'footer-legal' => __('Footer - Legal', 'sage'),
]);
```

Menu data is transformed via `NavigationHelper` class for Blade consumption.
Custom walkers in `app/Walkers/` handle complex menu rendering.

---

## Image Sizes

Standard responsive image sizes registered in `app/setup.php`:

| Name | Width | Height | Crop | Breakpoint |
|------|-------|--------|------|------------|
| `responsive-xl` | 1920 | 1080 | No | 1200px+ |
| `responsive-xl-crop` | 1920 | 1080 | Yes | 1200px+ |
| `responsive-lg` | 1200 | 675 | No | 992–1199px |
| `responsive-lg-crop` | 1200 | 675 | Yes | 992–1199px |
| `responsive-md` | 992 | 558 | No | 768–991px |
| `responsive-md-crop` | 992 | 558 | Yes | 768–991px |
| `responsive-sm` | 768 | 432 | No | 576–767px |
| `responsive-sm-crop` | 768 | 432 | Yes | 576–767px |
| `responsive-xs` | 576 | 324 | No | <576px |
| `responsive-xs-crop` | 576 | 324 | Yes | <576px |

Use cropped variants (`-crop`) when exact aspect ratio is required (cards, thumbnails).
Use uncropped variants for hero images and flexible layouts.
