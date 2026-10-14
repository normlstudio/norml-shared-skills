# Product gallery block

> Multi-image gallery on the product page. Primary image + thumbnails + zoom + (optional) 360°.

## Purpose

Let buyers inspect the product from multiple angles. Hi-res zoom is the single biggest non-text conversion lever on a product page.

## Required elements

- **Primary image** — large, square or 4:5 aspect, above the fold
- **Thumbnail strip** — 3–8 alt images (below or left of primary, depending on layout)
- **Zoom on click / hover** — modal overlay or in-place magnification
- **Lazy-load** non-primary images

## Optional elements

- **360° rotate viewer** — for furniture / appliances / fashion
- **Video embed** — first thumbnail can be a video play button
- **Color-variant swap** — when buyer picks a color, gallery swaps to that variant's images
- **Lifestyle image carousel** — separate from product-only shots
- **AR view (iOS Quick Look)** — for furniture / décor

## Gutenberg + ACF default (primary)

**Block name:** `acf/product-gallery`
**ACF field group:** `Product gallery`

Fields (typically populated on the product CPT, not per-block):
- `gallery` — gallery field, min 3 images
- `video_embed_url` — URL, optional (renders as first thumbnail)
- `enable_360` — true_false, default false
- `360_image_sequence` — gallery, conditional (16+ images for smooth rotation)
- `enable_zoom` — true_false, default true
- `zoom_mode` — radio: `modal | inline-magnify | both`, default `modal`
- `thumbnail_position` — radio: `bottom | left | right`, default `bottom`
- `aspect_ratio` — radio: `1:1 | 4:5 | 3:4`, default `1:1`

**Blade template:** `resources/views/blocks/product-gallery.blade.php`

## Elementor fallback

Elementor's WooCommerce Product Gallery widget if using WooCommerce. Else build with Elementor Image Carousel + Lightbox.

## Variations

- **Bottom thumbnails** — primary big, thumbnail row below
- **Left thumbnails** — primary right, thumbnail column left (more horizontal real estate)
- **Right thumbnails** — mirrored
- **With 360°** — first thumbnail is a "360°" badge, opens dedicated rotator
- **With video** — first thumbnail is a video play button

## Used on

- [Product](../pages/product.md) — single product page (canonical use)
- Product quick-view modal (variant)

## Don'ts

- Don't show low-resolution images — every image must be at least 1200×1200 for zoom
- Don't ship with only 1 image — buyers want to see angles
- Don't lazy-load the primary image (above the fold)
- Don't auto-play product videos — let the buyer click
- Don't show a placeholder "image coming soon" — fix the product before listing it
- Don't disable zoom — it's the single highest-impact gallery feature
- Don't ship a 360° viewer that lags on mobile — degrade to static images if frame rate suffers
