# Contact form block

> The primary form on the [contact](../pages/contact.md) page. Minimal fields, easy submission, clear success state.

## Purpose

Capture inbound leads. The fewer fields, the higher the conversion. Every additional field costs ~10% of submissions on average — never add a field without a real downstream use.

## Required elements

- **Form heading** (often omitted if the page hero already says "Contact us")
- **Email field** — `type="email"`, required, autocomplete
- **Name field** — text, required, autocomplete
- **Message field** — textarea, required, 4+ rows
- **Submit button** — clear action label
- **Privacy consent text** — link to privacy policy
- **Spam protection** — honeypot OR invisible reCAPTCHA OR hCaptcha (one only)

## Optional elements (add only when justified)

- **Subject / project type select** — useful for routing
- **Phone field** — only if someone will actually call
- **Company / role** — B2B sales qualification
- **Budget select** — agency qualification
- **How did you hear about us** — marketing attribution
- **File attachment** — for design briefs, RFPs
- **Newsletter opt-in checkbox** — separate consent
- **Inline success message** instead of redirect to thank-you page

## Gutenberg + ACF default (primary)

**Block name:** `acf/contact-form`
**ACF field group:** `Contact form`

Fields:
- `heading` — text, optional
- `dek` — textarea, optional
- `fields` — repeater:
  - `field_type` — select: `text | email | tel | textarea | select | checkbox | file`
  - `field_label` — text
  - `field_placeholder` — text, optional
  - `field_required` — true_false
  - `field_options` — textarea (one per line, for select / checkbox), conditional
  - `field_name` — text (the HTML `name` attribute, used for form payload)
- `submit_label` — text, default `"Send message"`
- `consent_text` — wysiwyg, default privacy-policy line
- `success_mode` — radio: `inline-message | redirect-page`, default `inline-message`
- `success_message` — wysiwyg, conditional on `inline-message`
- `success_redirect_url` — URL, conditional on `redirect-page`
- `spam_protection` — radio: `honeypot | recaptcha | hcaptcha | none`, default `honeypot`
- `destination_email` — email (where the submission is sent)

**Theme Options:**
- `default_destination_email` — fallback if block doesn't specify
- `recaptcha_site_key` / `hcaptcha_site_key` — provider credentials

**Form backend** — submission handler. Options (in order of simplicity):
1. **WP Forms / Gravity / Formidable plugin** — most common; ACF block wraps the plugin's shortcode
2. **Native PHP handler** — POST to a theme handler that emails the destination
3. **Webhook / external service** — POST to Make/Zapier/n8n/custom endpoint
4. **CRM-native** — HubSpot / Salesforce / Pipedrive form embed

**Blade template:** `resources/views/blocks/contact-form.blade.php`

## Elementor fallback

Elementor's Form widget (Pro). Has email integration + spam protection + redirect natively. For non-Pro: use any form plugin's shortcode in an HTML widget.

## Variations

- **Minimal** — name + email + message — default
- **Sales qualification** — adds company + budget + project type
- **Inline contact strip** — one-line email-only with submit (for newsletter-equivalent)
- **Multi-step** — paginated form for complex submissions (RFPs, briefs)
- **Calendar embed** — instead of form, embed Calendly/Cal.com (use Calendar block instead)

## Used on

- [Contact](../pages/contact.md) — canonical
- Landing pages (high-intent conversion)
- Service pages (final CTA → contact form modal)
- Home page (footer contact widget)

## Don'ts

- Don't require 10 fields for first contact
- Don't ship without spam protection — bots will fill the inbox in days
- Don't use a CAPTCHA that triggers on every legitimate submission
- Don't redirect to a generic "thanks" page — show inline success with what happens next
- Don't auto-respond with a robotic message ("We got your message")
- Don't expose the form's destination email in HTML — bots scrape mailto strings
- Don't ship a form without an actual receiver — submissions vanishing into nothing is a hidden bug
- Don't validate fields aggressively (e.g., reject names with apostrophes) — false-positive validation loses real leads
- Don't auto-fill country / language from IP without an override option
