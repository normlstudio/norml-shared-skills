# Map embed block

> Embedded map showing the business location. Google Maps, Mapbox, or OpenStreetMap.

## Purpose

Help local customers find the business. Important for storefronts, offices with foot traffic, and local SEO.

## Required elements

- **Embedded map** — iframe (Google Maps) OR JS-rendered (Mapbox / OSM / Leaflet)
- **Pin or marker** at the business location
- **Address text** below or alongside the map
- **"Get directions" link** to the maps provider with the destination pre-filled

## Optional elements

- **Multiple locations** — multi-pin for businesses with several offices
- **Custom pin / marker** branded
- **Hours of operation** as overlay
- **"Open now" indicator**
- **Street view link**

## Gutenberg + ACF default (primary)

**Block name:** `acf/map-embed`
**ACF field group:** `Map embed`

Fields:
- `provider` — radio: `google | mapbox | openstreetmap`, default `google`
- `address` — text (the displayed address)
- `latitude` — number (for JS providers)
- `longitude` — number
- `zoom` — number, default 14
- `pin_label` — text, optional (tooltip text)
- `height` — number (px), default 400
- `show_directions_link` — true_false, default true
- `embed_url` — text, conditional on `google` (the iframe `src` from Google Maps embed share)

**Theme Options:**
- `default_provider` — same options
- `mapbox_access_token` — text, conditional on Mapbox

**Blade template:** `resources/views/blocks/map-embed.blade.php`

## Elementor fallback

Elementor's Google Maps widget. Native.

## Variations

- **Single location** — most common
- **Multi-location grid** — multiple maps side-by-side for businesses with several offices
- **Map with sidebar info** — map on one side, hours + address + phone + directions on other
- **Full-bleed map** — entire row, address overlay

## Used on

- [Contact](../pages/contact.md) — canonical
- About page (when office matters)
- Footer (small inline map for local businesses)
- Store locator page (multi-location variant)

## Don'ts

- Don't embed without consent banner — Google Maps drops third-party cookies (GDPR concern in EU)
- Don't ship a static screenshot of a map — defeats the purpose of being interactive
- Don't show a pin in the wrong spot — verify the lat/lng or address against Google Maps
- Don't use a map provider with a daily quota you'll exceed
- Don't auto-zoom too close — show enough surrounding context that visitors orient themselves
- Don't ship maps without an "Open in Maps" link for mobile users (most prefer native apps)
- Don't show a map for a business that doesn't accept visitors
