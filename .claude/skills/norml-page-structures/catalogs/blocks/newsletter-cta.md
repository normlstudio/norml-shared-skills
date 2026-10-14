# Newsletter CTA block

> Email signup band at the bottom of pages. Distinct from the generic [cta](cta.md) block — this is specifically for email capture.

## Purpose

Convert a reader into a subscriber. The newsletter signup is the most durable channel a content site has — email survives algorithm changes, social platform deaths, and SEO disruption. Goes at the bottom of archives, posts, and the home page.

## Required elements

- **Headline** — value-prop oriented ("Get weekly insights" / "Join 5,000 readers" / "Don't miss our next post")
- **Email input** — `type="email"`, required, autocomplete `email`
- **Submit button** — clear action label ("Subscribe" / "Sign me up" / "Join")
- **Consent line** — minimal — link to privacy policy (GDPR mandatory for EU traffic)

## Optional elements

- **Sub-headline** — one supporting sentence under headline
- **Social proof** — "Join 5,000+ subscribers" (only if number is real and impressive)
- **Frequency disclosure** — "One email per week, no spam"
- **Visual** — illustration, photo, or icon to the side
- **First-name field** — only if the project's email tool actually uses {{first_name}} merge tags
- **Lead magnet hook** — "Subscribe and get the free guide" with downloadable PDF on confirm

## Gutenberg + ACF default (primary)

**Block name:** `acf/newsletter-cta`
**ACF field group:** `Newsletter CTA`

Fields:
- `headline` — text, required
- `sub_headline` — textarea, optional
- `placeholder` — text, default `"your@email.com"`
- `button_label` — text, default `"Subscribe"`
- `consent_text` — wysiwyg, default `"By subscribing you agree to our <a href='/privacy/'>privacy policy</a>."`
- `frequency_disclosure` — text, optional (e.g., `"One email per week. Unsubscribe anytime."`)
- `social_proof` — text, optional
- `layout` — radio: `centered | split | full-bleed-band | inline`, default `full-bleed-band`
- `background` — radio: `accent | dark | light`, default `accent`
- `lead_magnet_url` — URL, optional (PDF / resource sent on confirm)

**Theme Options page** (`ACF Options → Site → Newsletter`):
- `provider` — select: `mailchimp | activecampaign | convertkit | beehiiv | substack | klaviyo | custom_form_action | webhook`, default depends on project
- `list_id` — text (the provider's list/audience ID)
- `success_message` — wysiwyg, default `"Check your inbox to confirm."`
- `error_message` — wysiwyg, default `"Something went wrong. Try again or email us."`
- `default_consent_text`, `default_frequency_disclosure` — text (used as block-level fallbacks)

**Blade template:** `resources/views/blocks/newsletter-cta.blade.php`

The form's submission target is determined by the Theme Options `provider`. Most providers ship a JavaScript snippet (Mailchimp's `mc-embedded-subscribe-form` action, ConvertKit's form embed, etc.). For Webflow/Squarespace-equivalent simplicity, a custom Webhook-mode posts the email to a Cloudflare Worker / serverless function that forwards to the provider's API — used when projects don't want third-party scripts on the page.

## Elementor fallback

Elementor's Form widget with email + button, configured to submit to the project's email provider via the widget's native integrations (Mailchimp, ActiveCampaign, etc. are built into Elementor Pro). Style the Container to match the spec's background variants.

## Variations

- **Full-bleed band** — full-width section, background fill, centered headline + form (default)
- **Centered card** — bordered card, narrower max-width, sits inside content margin
- **Split** — headline + copy left, form right (works well for 1200px+ layouts)
- **Inline** — narrow form embedded in body text (rare — usually article-context)
- **Footer-strip** — slim above-footer band, single-line: headline + email input + button

## Used on

- Blog archive (above footer) — default
- Blog post (above footer / before related-posts depending on order)
- Home page (above footer if newsletter is a primary growth lever)
- Resource pages (with lead-magnet hook)
- Landing pages

## Don'ts

- Don't ship without GDPR-compliant consent text + link to privacy policy if there's any EU traffic
- Don't auto-show a newsletter modal on page load — invasive; if you must do modal, exit-intent only
- Don't claim "Join 5,000+ subscribers" if you have 87 — readers can smell it
- Don't add 6 fields (name, company, role, country…) — email-only converts ~5–10×; every extra field cuts conversion in half
- Don't ship without testing the actual submission flow end-to-end — broken forms are the #1 leak in vibecoded sites
- Don't show the success message in the same spot the form was — clear the form, show confirmation, keep them oriented
- Don't add multiple newsletter blocks on the same page — one is enough; repeating it feels spammy and skews analytics
- Don't promise frequency you can't keep — "Daily" sounds great until you skip a week and look dead
