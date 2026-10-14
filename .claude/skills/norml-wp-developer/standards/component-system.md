# Component System

This document defines how to build Blade components, sections, and partials in
WordPress projects. Follow these patterns exactly.

---

## Three Template Types

### 1. Sections (`resources/views/sections/`)

Full-width page blocks. These are the building blocks of pages.

**When to create a section:**
- It represents a visually distinct block on a page (hero, benefits grid, FAQ, CTA)
- It may be backed by ACF fields (either as a block or via page fields)
- It's included in page templates via `@include('sections.name')`

**Section anatomy:**
```blade
{{-- Section Comment --}}
@props([
    'containerClass' => 'default classes',  // Optional override props
    'isStackItem' => false,
])

@php
    // 1. Get ACF data with defaults
    $title = get_field('section_title') ?: 'Default Title';
    $items = get_field('items') ?: [];

    // 2. Computed values
    $hasItems = !empty($items);
@endphp

<section class="py-20" {!! isset($block['anchor']) ? 'id="' . esc_attr($block['anchor']) . '"' : '' !!}>
    <div class="section-container">
        {{-- Section header --}}
        @if ($title)
            <div class="text-center mb-12">
                <h2 class="text-{project}-primary-blue">{{ $title }}</h2>
            </div>
        @endif

        {{-- Section content --}}
        @if ($hasItems)
            <div class="grid md:grid-cols-3 grid-cols-1 gap-4">
                @foreach ($items as $item)
                    <x-card :title="$item['title']" :description="$item['description']" />
                @endforeach
            </div>
        @endif
    </div>
</section>
```

**Section rules:**
- ACF data is retrieved at the top of the file in `@php` block
- ALWAYS provide fallback defaults: `get_field('name') ?: 'default'`
- Use `section-container` for the main width constraint
- Use semantic HTML: `<section>`, not `<div>`
- Support block anchor: `{!! isset($block['anchor']) ? 'id="..."' : '' !!}`
- Mobile-first responsive classes
- Sections can accept `@props` for override customization from parent templates

**Including sections in pages:**
```blade
@extends('layouts.app')

@section('content')
    @include('sections.hero')

    {{-- With overrides --}}
    @include('sections.carrier-logos', [
        'containerClass' => 'relative border-t border-t-{project}-border-light'
    ])

    {{-- Gutenberg content (includes ACF blocks) --}}
    @while (have_posts())
        @php(the_post())
        {!! the_content() !!}
    @endwhile
@endsection
```

---

### 2. Components (`resources/views/components/`)

Reusable UI elements. Used across multiple sections via `<x-name />` syntax.

**When to create a component:**
- It's used in 2+ places
- It encapsulates a distinct UI pattern (button, card, modal, accordion)
- It accepts props and renders consistently

**Component anatomy:**
```blade
{{--
  Component Name
  @param {type} $prop - Description
--}}

@props([
    'title' => '',
    'description' => '',
    'type' => 'default',
    'class' => '',
])

@php
    $typeClasses = [
        'default' => 'bg-white text-{project}-primary-blue',
        'highlight' => 'bg-{project}-primary-blue text-white',
    ];
    $classes = $typeClasses[$type] ?? $typeClasses['default'];
@endphp

<div class="rounded-2xl p-6 {{ $classes }} {{ $class }}">
    @if ($title)
        <h5 class="mb-2">{{ $title }}</h5>
    @endif
    @if ($description)
        <p class="text-body-medium">{{ $description }}</p>
    @endif
    {{ $slot ?? '' }}
</div>
```

**Component rules:**
- ALWAYS use `@props([])` at the top to declare accepted props with defaults
- Document props in a comment block at the very top
- Components are STATELESS — they receive data via props, never call `get_field()` directly
- Use `$slot` for flexible content injection
- Use `$attributes` bag for passing through HTML attributes
- Compute variant classes in the `@php` block, not inline

**Using components:**
```blade
{{-- Simple --}}
<x-icon name="arrow-right" class="w-4 h-4" />

{{-- With props --}}
<x-benefit-card :title="$item['title']" :description="$item['description']" type="highlight" />

{{-- With slot --}}
<x-modal id="get-started">
    <p>Modal content here</p>
</x-modal>

{{-- With Alpine.js attributes --}}
<x-icon name="plus" x-show="!expanded" class="w-6 h-6" />
```

---

### 3. Partials (`resources/views/partials/`)

Template fragments for WordPress loop content. NOT reusable UI components.

**When to create a partial:**
- It's a content template used inside the WordPress loop
- It's used by `index.blade.php`, `single.blade.php`, etc.

**Partial naming:**
- `content.blade.php` — Default post content
- `content-page.blade.php` — Page content
- `content-single.blade.php` — Single post content
- `content-search.blade.php` — Search result item
- `entry-meta.blade.php` — Post metadata (date, author, etc.)
- `footer-content.blade.php` — Footer inner content

---

## Core Components (Always Available)

These components exist in every The project:

### `<x-icon>`
SVG icon from the sprite system.
```blade
<x-icon name="arrow-right" class="w-4 h-4 text-{project}-primary-blue" />
<x-icon name="plus" size="lg" />  {{-- xs, sm, md, lg, xl presets --}}
<x-icon name="close" width="32" height="32" />
```

### `<x-picture>`
Responsive image with WebP support.
```blade
{{-- Static image from manifest --}}
<x-picture src="resources/images/hero.jpeg" alt="Hero" class="w-full h-full object-cover" />

{{-- ACF image field --}}
<x-picture :acf-field="get_field('image')" alt="Feature" size="responsive-lg" class="rounded-2xl" />

{{-- ACF image ID --}}
<x-picture :acf-id="$item['image_id']" alt="Card" size="responsive-md" />
```

### `<x-accordion>`
Expandable content sections powered by Alpine.js.
```blade
<x-accordion 
    :items="$items" 
    :defaultExpanded="$items[0]['id']"
    containerClass="flex flex-col p-8"
    buttonText="Learn more"
    :showButton="true"
/>
```

Items array format:
```php
$items = [
    [
        'id' => 'unique-id',
        'title' => 'Item title',
        'description' => 'Item content',
        'link' => '/url',
        'titleTag' => 'h5',        // Optional, default: h5
        'titleClass' => 'h5 ...',  // Optional
        'image' => $acf_image,     // Optional ACF image
        'expanded' => true,        // Optional default state
    ],
];
```

### `<x-slider>`
Splide.js carousel wrapper.
```blade
<x-slider 
    sliderId="my-slider" 
    :options="['perPage' => 3, 'gap' => '1rem', 'type' => 'loop']"
    externalPrevSelector="#prev-btn"
    externalNextSelector="#next-btn"
>
    @foreach ($items as $item)
        <li class="splide__slide">
            {{-- Slide content --}}
        </li>
    @endforeach
</x-slider>
```

### `<x-modal>`
Modal dialog with Alpine.js + custom event system.
```blade
{{-- Trigger --}}
<button onclick="window.dispatchEvent(new CustomEvent('modal:open:my-modal'))">Open</button>

{{-- Modal --}}
<x-modal id="my-modal">
    <x-slot:header>Modal Title</x-slot:header>
    <x-slot:body>Content here</x-slot:body>
    <x-slot:footer>
        <button class="btn-secondary">Submit</button>
    </x-slot:footer>
</x-modal>
```

---

## Alpine.js Integration Pattern

When a Blade component needs JavaScript interactivity:

1. **Register Alpine component** in `resources/components/{name}/{name}.js`:

```javascript
import Alpine from 'alpinejs';

Alpine.data('componentName', (config = {}) => ({
    // Reactive state
    isOpen: config.defaultOpen || false,
    items: config.items || [],

    // Lifecycle
    init() {
        // Setup code
    },

    // Methods
    toggle() {
        this.isOpen = !this.isOpen;
    },

    // Computed-like
    get isEmpty() {
        return this.items.length === 0;
    },
}));
```

2. **Import in `resources/js/app.js`**:
```javascript
import '../components/component-name/component-name.js';
```

3. **Use in Blade template**:
```blade
<div x-data="componentName({ defaultOpen: true, items: @js($items) })">
    <button @click="toggle()" :aria-expanded="isOpen">Toggle</button>
    <div x-show="isOpen" x-collapse x-cloak>
        Content
    </div>
</div>
```

**Alpine.js rules:**
- Use `x-data` for component initialization
- Use `@js()` Blade directive to pass PHP data to Alpine
- Use `x-cloak` with `[x-cloak] { display: none !important; }` to prevent FOUC
- Use `x-collapse` plugin for animated show/hide
- Use custom events for cross-component communication: `window.dispatchEvent(new CustomEvent('event:name'))`
- Register components via `Alpine.data()`, never inline complex logic in `x-data`

---

## Page Template Pattern

Standard page template structure:

```blade
{{--
  Template Name: Page Name
  Description: Brief description.
--}}

@extends('layouts.app')

@section('content')
    {{-- Static sections (hardcoded in template) --}}
    @include('sections.hero')
    @include('sections.features')

    {{-- Gutenberg blocks (dynamic ACF blocks) --}}
    @while (have_posts())
        @php(the_post())
        {!! the_content() !!}
    @endwhile

    {{-- More static sections --}}
    @include('sections.cta')
@endsection
```

**Two approaches:**
1. **Hardcoded sections** — for pages with fixed layout (homepage, about)
2. **Gutenberg blocks** — for pages built with ACF blocks in the editor (solution pages, flexible pages)

For Gutenberg-driven pages, `the_content()` renders the ACF blocks. Each block has its
own `render_callback` that calls `view('sections.name', ['block' => $block])`.

The hybrid approach is common: some sections are hardcoded (header, footer, CTA),
while the middle content is built with blocks in the editor.

---

## Layout (`layouts/app.blade.php`)

The main layout wraps every page:

```blade
<!doctype html>
<html @php(language_attributes())>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {{-- Let WordPress title-tag support emit the title; avoid duplicate title output. --}}
    {{-- Google Fonts link --}}
    @php(do_action('get_header'))
    @php(wp_head())
</head>
<body @php(body_class())>
    @php(wp_body_open())

    {{-- Header with conditional styling --}}
    @if (is_front_page())
        @include('sections.header')
    @else
        @include('sections.header', [
            'bgClass' => '...solid background classes...',
            'scrolledBgClass' => 'bg-{project}-primary-blue',
        ])
    @endif

    <main id="main" class="main">
        @yield('content')
    </main>

    @hasSection('footer')
        @yield('footer')
    @else
        @include('sections.footer')
    @endif

    @include('sections.modals')

    @php(do_action('get_footer'))
    @php(wp_footer())
</body>
</html>
```

**Layout rules:**
- Header receives different props based on `is_front_page()` (transparent vs solid)
- Footer is includable or yieldable (some pages override footer)
- Modals are always included at the bottom
- Never add custom `<script>` or `<style>` tags — use Vite pipeline
