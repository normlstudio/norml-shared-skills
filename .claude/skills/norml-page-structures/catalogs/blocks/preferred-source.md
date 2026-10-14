# Google Preferred Source block

> A site-level reader-acquisition control that lets someone add the publication's
> canonical domain or subdomain to Google Preferred Sources. On blog posts it sits
> directly after [Share with AI](share-ai.md) and before
> [social sharing](share-social.md).

## Purpose

Turn an engaged article reader into a repeat reader inside Google Search. For someone
who selects the publication, Google says its content is more likely to appear in Top
Stories and can carry a preferred badge in AI Overviews and AI Mode. This is a reader
preference control, not a ranking guarantee or an indexing mechanism.

## Eligibility gate (required before rendering)

1. Search for the exact canonical hostname in Google's Source Preferences tool:
   `https://www.google.com/preferences/source?q={DOMAIN}`.
2. Verify a **domain or subdomain**, such as `example.com` or `news.example.com`.
   A path such as `example.com/blog` is not eligible.
3. Record the checked hostname, status (`eligible` or `ineligible`), and verification
   date in the project context or Theme Options.

The template slot and eligibility check are required on every blog project:

- `eligible` → render the control on every single post;
- `ineligible` → suppress the control and retain the dated evidence;
- `unverified` → the blog go-live check remains incomplete.

Never render a control that sends readers into a known ineligible flow.

## Required elements

- **One explicit Google action** — the standard localized Google button or a custom
  control whose accessible name includes both the action and Google
- **Clear custom label** — use `Add {Publication} as a preferred source`; never use
  vague copy such as `Add {Publication} on Google`
- **Production hostname binding** — the source is the verified canonical domain or
  subdomain, never the current staging/local hostname
- **No-JavaScript fallback** — the official deeplink for the verified hostname:
  `https://www.google.com/preferences/source?q={DOMAIN}`
- **Placement** — after Share with AI and before social sharing, inside the article
  content column
- **Accessible interaction** — keyboard operable, visible focus, and a minimum
  44×44px target for custom controls

## Implementation choice

### Standard JavaScript button (recommended default)

Use this on server-rendered WordPress templates where the control is already in the
DOM when the library loads. Load the library once per page:

```html
<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
<div google-add-preferred-source-btn></div>
```

Optional supported attributes:

```html
<div google-add-preferred-source-btn data-theme="dark" data-lang="en"></div>
```

Omit `data-lang` to let Google localize from the reader's browser.

### Advanced JavaScript control (modern-framework default)

Use Google's manual control mode when a React, Next.js, or other client-routed app
needs its own UI or must initialize again after route navigation:

```html
<script
  async
  preferred-sources-control="manual"
  src="https://news.google.com/swg/js/v1/publisher.js">
</script>
```

```js
(self.PREFERRED_SOURCE = self.PREFERRED_SOURCE || []).push((preferredSource) => {
  preferredSource.init({theme: 'light', lang: 'en'});
  document.querySelector('#preferred-source-button')?.addEventListener('click', () => {
    preferredSource.addPreferredSource();
  });
});
```

The visible custom control must remain a real link to the deeplink. Prevent its
default navigation only when the SDK client is ready, so script blockers and load
failures still leave a working path.

### Deeplink-only fallback

Use only when the platform cannot run the JavaScript integration:

```html
<a
  href="https://www.google.com/preferences/source?q=example.com"
  target="_blank"
  rel="noopener noreferrer"
  aria-label="Add Example News as a preferred source on Google">
  Add Example News as a preferred source
</a>
```

### Persistent footer utility (optional)

A publication may also expose the same verified hostname through a persistent
footer utility link. Use the branded label `Add {Publication} as a preferred
source`, open the deeplink safely in a new tab, and keep this placement
deeplink-only. A footer link does not replace the required single-post slot and
must never cause Google's publisher SDK to load sitewide.

## Gutenberg + ACF default (primary)

**Block name:** `acf/preferred-source`

This is a template-managed block with no per-post editor fields. Editors must not be
able to remove it from individual articles. Configuration lives in Theme Options.

**Theme Options page** (`ACF Options → Site → Blog`):

- `google_preferred_source_enabled_globally` — true_false, default false until the
  eligibility gate passes
- `google_preferred_source_domain` — text, required when enabled; hostname only, no
  scheme or path
- `google_preferred_source_eligibility` — select:
  `unverified | eligible | ineligible`, default `unverified`
- `google_preferred_source_verified_at` — date, required for an `eligible` or
  `ineligible` status
- `google_preferred_source_theme` — select: `light | dark`, default `light`
- `google_preferred_source_lang` — text, optional; omit to use browser language

**Blade template:** `resources/views/blocks/preferred-source.blade.php`

```php
@php
  $enabled     = (bool) get_field('google_preferred_source_enabled_globally', 'option');
  $eligibility = get_field('google_preferred_source_eligibility', 'option');
  $theme       = get_field('google_preferred_source_theme', 'option') ?: 'light';
  $lang        = get_field('google_preferred_source_lang', 'option');
  $is_prod     = wp_get_environment_type() === 'production';
@endphp

@if ($enabled && $eligibility === 'eligible' && $is_prod)
  @once
    <script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
  @endonce
  <div class="preferred-source" aria-label="Add this publication as a preferred source on Google">
    <div
      google-add-preferred-source-btn
      data-theme="{{ esc_attr($theme) }}"
      @if ($lang) data-lang="{{ esc_attr($lang) }}" @endif>
    </div>
  </div>
@endif
```

For local/staging QA, render a non-interactive fixture or test the custom control's
deeplink. Do not let Google's SDK infer a staging hostname as the source.

## Verification

- Eligibility evidence names the exact canonical hostname and date checked
- The Google library is requested once, and only on routes that render the control
- Every eligible single post places the control after Share with AI and before social
  sharing
- A keyboard user can reach and activate it; custom targets measure at least 44×44px
- The no-JavaScript/deeplink path contains only the verified hostname, not `/blog`
- The signed-in Google flow identifies the expected publication and can return the
  reader to the article
- No layout overflow at 375, 768, 1024, 1440, or 1920px

## Used on

- Blog post (required template slot; render when eligible)
- News / press release pages using the blog single template
- Publication landing pages (optional secondary placement)
- Site footer utility/legal row (optional persistent deeplink)

## Don'ts

- Don't use a blog subdirectory as the source — Google accepts domains/subdomains only
- Don't render before eligibility has been checked and recorded
- Don't load the SDK through Google Tag Manager; keep ownership in the template
- Don't load the SDK site-wide for a persistent footer link; the footer is
  deeplink-only
- Don't load the script more than once per page
- Don't claim that selection guarantees rankings, traffic, or inclusion in Top Stories
- Don't point production readers at localhost, a preview domain, or a staging hostname
- Don't remove the deeplink fallback from a custom implementation

## Source

Google Search Central, "Help your readers find your site through preferred sources in
Google Search" (last updated 2026-08-20):
`https://developers.google.com/search/docs/appearance/preferred-sources`
