# Search bar block

> Site-wide search input. Usually in the header, occasionally in archive pages.

## Purpose

Let visitors find content / products by query string. Justified when the site has enough content (50+ pages / 100+ posts) that browsing isn't efficient.

## Required elements

- **Input** — `type="search"`, placeholder
- **Submit button** OR icon-only (magnifying glass)
- **Search results page** — `/?s={query}` or `/search/?q={query}`

## Optional elements

- **Autosuggest / autocomplete** — live results as you type (requires JS + endpoint)
- **Scoped search** — dropdown to scope (All / Blog / Products / Pages)
- **Recent searches** — store + show recent queries
- **Popular searches** — pre-filled suggestion chips
- **Voice search** — `<button>` triggering Web Speech API (rare)

## Gutenberg + ACF default (primary)

**Block name:** `acf/search-bar`
**ACF field group:** `Search bar`

Fields:
- `placeholder` — text, default `"Search…"`
- `style` — radio: `inline | overlay-trigger | sticky-header-icon`, default `inline`
- `enable_autosuggest` — true_false, default false
- `autosuggest_endpoint` — URL, conditional
- `scope_options` — checkbox group (all / posts / products / pages), conditional on enabled
- `show_recent` — true_false, default false
- `show_popular` — true_false, default false

**Blade template:** `resources/views/blocks/search-bar.blade.php`

When autosuggest is enabled, expose a REST endpoint (`/wp-json/wp/v2/search?search={q}`) and wire a minimal JS listener.

## Elementor fallback

Elementor's Search Form widget. Native. Add autosuggest via a plugin (Ivory Search, SearchWP).

## Variations

- **Header inline** — always-visible input in the header
- **Header icon trigger** — magnifying glass icon, expands to input on click
- **Modal overlay** — full-screen search modal triggered by keyboard shortcut (⌘+K)
- **Archive-scoped** — search within current archive only

## Used on

- Site header (when search is justified — typically content-heavy sites)
- Blog archive (rare — only for 50+ posts)
- Product listing (when catalog is large)
- 404 page (always — help lost visitors find something)
- Docs / knowledge base (always)

## Don'ts

- Don't ship search on a 5-page site — pointless
- Don't ship search results page that returns "no results found" for common queries — at minimum, redirect to relevant archive
- Don't surface a search icon without making it accessible (keyboard focus, aria-label)
- Don't disable browser autocomplete — let the input behave like an `<input>`
- Don't track every keystroke without consent — autosuggest endpoints log queries
- Don't replace the search page's standard URL params (`?s=...`) with custom ones unless there's a reason — breaks search engines and bookmarks
