# File Structure Standard

This document defines the exact file structure for every WordPress project.
Do NOT create files outside these locations. Do NOT invent new directories.

---

## Root Theme Directory

```
{theme-name}/
├── acf-json/                          # ACF field groups and CPT JSON sync
│   ├── group_{descriptive_name}.json  # Field groups (named descriptively)
│   ├── post_type_{hash}.json          # Custom post type registrations
│   └── README.md                      # ACF JSON conventions
│
├── app/                               # PHP application logic (PSR-4: App\)
│   ├── acf-blocks-{developer}.php     # ACF block registrations (one per developer)
│   ├── block-patterns.php             # WordPress block patterns
│   ├── filters.php                    # WordPress filter hooks
│   ├── forms.php                      # Form handling (AJAX endpoints)
│   ├── helpers.php                    # Global helper functions (autoloaded)
│   ├── setup.php                      # Theme setup, asset enqueue, CPT config
│   ├── setup-header-menu.php          # Header menu configuration (if complex)
│   ├── newsletter-form.php            # Newsletter form handler (if needed)
│   ├── Helpers/                       # Helper classes
│   │   └── NavigationHelper.php       # Menu/nav data transformation
│   ├── Providers/
│   │   └── ThemeServiceProvider.php   # Acorn service provider
│   ├── View/
│   │   └── Composers/                 # View composers (data injection)
│   │       ├── App.php                # Global data (site name, etc.)
│   │       ├── Post.php               # Post-specific data
│   │       └── Comments.php           # Comment-specific data
│   └── Walkers/                       # Custom menu walkers
│       ├── NavWalker.php
│       └── FooterMenuWalker.php
│
├── resources/                         # Frontend resources (compiled by Vite)
│   ├── components/                    # Interactive JS component modules
│   │   └── {component-name}/
│   │       ├── {component-name}.js    # Alpine.js component registration
│   │       ├── {component-name}.css   # Component-specific styles (optional)
│   │       └── README.md              # Component documentation (optional)
│   │
│   ├── css/                           # CSS source files
│   │   ├── app.css                    # Main entry — imports everything
│   │   ├── theme-colors.css           # Design tokens: colors & gradients
│   │   ├── theme-breakpoints.css      # Breakpoint definitions
│   │   ├── fonts.css                  # @font-face declarations
│   │   ├── components.css             # @layer components — reusable classes
│   │   ├── sections.css               # Section-specific styles (minimal)
│   │   ├── utilities.css              # @layer utilities — custom utilities
│   │   ├── animations.css             # @keyframes definitions
│   │   ├── editor.css                 # Gutenberg editor styles
│   │   └── editor-styles.css          # Additional editor CSS
│   │
│   ├── scss/                          # SCSS source files (legacy/supplementary)
│   │   ├── app.scss                   # SCSS entry point
│   │   ├── editor.scss                # Editor SCSS
│   │   ├── abstracts/
│   │   │   ├── _variables.scss        # SCSS variables & CSS custom properties
│   │   │   └── _mixins.scss           # Media query & utility mixins
│   │   └── base/
│   │       └── _reset.scss            # CSS reset/normalize
│   │
│   ├── js/                            # JavaScript source files
│   │   ├── app.js                     # Main JS entry — Alpine init + all imports
│   │   ├── editor.js                  # Gutenberg editor JS
│   │   └── utils/
│   │       ├── helpers.js             # Shared JS utility functions
│   │       ├── form-api.js            # Form API helpers
│   │       └── tailwind.js            # Tailwind runtime helpers
│   │
│   ├── views/                         # Blade templates
│   │   ├── layouts/
│   │   │   └── app.blade.php          # Main layout (html, head, body, header, footer)
│   │   ├── sections/                  # Page sections (header, footer, hero, etc.)
│   │   │   ├── header.blade.php
│   │   │   ├── footer.blade.php
│   │   │   ├── hero.blade.php
│   │   │   ├── {section-name}.blade.php
│   │   │   └── modals.blade.php
│   │   ├── components/                # Reusable Blade components
│   │   │   ├── icon.blade.php
│   │   │   ├── picture.blade.php
│   │   │   ├── button.blade.php
│   │   │   ├── accordion.blade.php
│   │   │   ├── slider.blade.php
│   │   │   ├── modal.blade.php
│   │   │   ├── {component-name}.blade.php
│   │   │   └── form/                  # Form-specific components
│   │   │       ├── input.blade.php
│   │   │       ├── select.blade.php
│   │   │       ├── textarea.blade.php
│   │   │       ├── checkbox.blade.php
│   │   │       ├── radio.blade.php
│   │   │       └── multi-step/        # Multi-step form components
│   │   ├── partials/                  # Non-section partial templates
│   │   │   ├── content.blade.php
│   │   │   ├── content-page.blade.php
│   │   │   ├── content-single.blade.php
│   │   │   ├── footer-content.blade.php
│   │   │   └── entry-meta.blade.php
│   │   ├── forms/
│   │   │   └── search.blade.php
│   │   ├── front-page.blade.php       # Homepage template
│   │   ├── page.blade.php             # Default page template
│   │   ├── page-{slug}.blade.php      # Named page templates
│   │   ├── single.blade.php           # Default single post
│   │   ├── single-{cpt}.blade.php     # CPT single templates
│   │   ├── archive-{cpt}.blade.php    # CPT archive templates
│   │   ├── category.blade.php         # Category archive
│   │   ├── search.blade.php           # Search results
│   │   ├── index.blade.php            # Fallback template
│   │   └── 404.blade.php              # 404 page
│   │
│   ├── fonts/                         # Custom font files (woff2, ttf)
│   ├── icons/                         # SVG icons (compiled into sprite)
│   ├── images/                        # Static images (processed by Vite)
│   ├── video/                         # Video files
│   └── animations/                    # Lottie JSON animation files
│
├── public/                            # Vite build output (gitignored)
│   └── build/
│       ├── manifest.json
│       └── assets/
│
├── storage/                           # Cache and logs
│   ├── framework/cache/
│   └── logs/
│
├── vendor/                            # Composer dependencies (gitignored)
│
├── .env.example                       # Environment variables template
├── .editorconfig                      # Editor formatting rules
├── .prettierrc                        # Prettier config
├── .prettierignore                    # Prettier ignore
├── .blade-formatter.json              # Blade formatter config
├── .gitignore
├── composer.json                      # PHP dependencies
├── package.json                       # Node dependencies
├── functions.php                      # Theme bootstrap (Acorn boot + file includes)
├── index.php                          # WordPress fallback
├── init.sh                            # Deployment initialization script
├── post-deploy.sh                     # Post-deployment script
├── style.css                          # WordPress theme metadata (no styles)
├── screenshot.png                     # Theme screenshot
├── tailwind.config.js                 # Tailwind configuration
├── theme.json                         # WordPress theme.json (preprocessed by Vite)
└── vite.config.js                     # Vite build configuration
```

---

## Naming Conventions

### Files
- Blade templates: `kebab-case.blade.php`
- PHP classes: `PascalCase.php`
- PHP function files: `kebab-case.php`
- CSS files: `kebab-case.css`
- JS files: `kebab-case.js`
- SCSS files: `_kebab-case.scss` (partials prefixed with underscore)
- ACF JSON: `group_{descriptive_name}.json` or `post_type_{hash}.json`

### Directories
- All directories: `kebab-case`
- Exception: PHP class directories follow PSR-4: `Providers/`, `View/`, `Walkers/`, `Helpers/`

### Page Templates
- Homepage: `front-page.blade.php`
- Named pages: `page-{slug}.blade.php` (e.g., `page-contact-us.blade.php`)
- CPT singles: `single-{post_type}.blade.php` (e.g., `single-solution.blade.php`)
- CPT archives: `archive-{post_type}.blade.php` (e.g., `archive-blog.blade.php`)
- Use slug-based naming that matches the WordPress page slug

### Sections vs Components vs Partials
- **Sections** (`sections/`): Full-width page blocks, typically map to ACF blocks or page regions. Named after their visual purpose: `hero.blade.php`, `benefits.blade.php`, `faq.blade.php`
- **Components** (`components/`): Reusable UI elements used across multiple sections. Named after what they are: `button.blade.php`, `accordion.blade.php`, `slider.blade.php`
- **Partials** (`partials/`): Template fragments for WordPress loop content. Named with `content-` prefix: `content-single.blade.php`, `content-page.blade.php`

---

## What Goes Where

| You want to... | Create file at... |
|----------------|------------------|
| Add a new page section | `resources/views/sections/{name}.blade.php` |
| Add a reusable component | `resources/views/components/{name}.blade.php` |
| Add component JavaScript | `resources/components/{name}/{name}.js` + import in `resources/js/app.js` |
| Add component CSS | `resources/components/{name}/{name}.css` + import in `resources/css/components.css` |
| Register an ACF block | `app/acf-blocks-{developer}.php` |
| Add a helper function | `app/helpers.php` |
| Add a WordPress filter | `app/filters.php` |
| Add a form handler | `app/forms.php` |
| Add a custom walker | `app/Walkers/{Name}Walker.php` |
| Add a view composer | `app/View/Composers/{Name}.php` |
| Add a service provider | `app/Providers/{Name}ServiceProvider.php` |
| Add a new icon | `resources/icons/{name}.svg` |
| Add a custom font | `resources/fonts/{name}.woff2` + declare in `resources/css/fonts.css` |
| Add a new image | `resources/images/{name}.{ext}` |
| Add design tokens | `resources/css/theme-colors.css` |
| Add a utility class | `resources/css/utilities.css` |
| Add a reusable CSS class | `resources/css/components.css` inside `@layer components` |
| Add an animation | `resources/css/animations.css` |
| Register a CPT | WordPress admin → ACF → Post Types (syncs to `acf-json/`) |
