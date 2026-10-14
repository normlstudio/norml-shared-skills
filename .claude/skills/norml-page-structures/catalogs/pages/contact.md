# Contact page

> Make it easy to reach you. Form + alternatives + location signals.

## Purpose

Convert visitors who've decided "I want to talk to a human." The page should remove friction, not add it. Multiple paths to contact (form, email, call, calendar) accommodate different preferences.

## Required structural elements (top → bottom)

1. **Header**
2. **Page header** — H1 ("Contact" or "Get in touch" or "Let's talk") + one-line dek
3. **Two-column layout** (desktop) — [contact form](../blocks/contact-form.md) on one side, contact details on the other; stacked on mobile
4. **Direct contact info** — email address (clickable `mailto:`) + phone number (clickable `tel:`) + physical address (if applicable)
5. **Calendar link** — Calendly / Cal.com / SavvyCal embed or button (per project)
6. **Hours / availability** — when the team is reachable, response-time expectation ("We reply within 1 business day")
7. **Social media links** — official profiles with recognizable icons
8. **[Map](../blocks/map-embed.md)** — only if foot traffic / office visits matter
9. **Per-department contacts (optional)** — separate routes for support / sales / press / partnerships / accounting when justified
10. **Footer**

## Recommended (situational) blocks

- **[Testimonials](../blocks/testimonials.md)** strip — short, to reduce hesitation at the contact point
- **[FAQ](../blocks/faq.md)** — answer "what happens after I submit?" / "how fast do you reply?" / "what's the next step?"
- **Service routing** — "For sales: X · For support: Y · For press: Z" inline cards or accordion
- **Live chat / chatbot** — for high-consideration services where prospects need quick answers
- **Office photo** — small photo of the team / office to humanize the contact point

## Common variations

- **B2B SaaS contact** — short form, calendar embed prominent, no phone
- **Agency / consultancy contact** — longer form (budget, project type), no calendar (qualified call only)
- **Local business contact** — form + map + phone-first, calendar optional
- **Support-focused contact** — separate from sales contact; routes to help desk
- **Multi-office contact** — list of offices with per-office address + phone + map

## Form fields — keep it minimal

Required:
- Name
- Email
- Message

Add only when justified:
- Company / role (B2B sales qualification)
- Phone (if you'll actually call)
- Project type / budget (agency qualification)
- How did you hear about us (marketing attribution)

**Hard rule:** every additional field cuts conversion. Don't add a field unless someone will read the answer and act on it. See [contact-form.md](../blocks/contact-form.md) for full spec.

## SEO / schema notes

- H1 on the page title
- Schema: `ContactPage` + `Organization` with `contactPoint` (email, phone, contactType)
- For multi-department: emit one `contactPoint` per department, each with `contactType` (`customer service`, `sales`, `technical support`, etc.)
- If local: `LocalBusiness` schema with `address`, `geo`, `openingHours`

## Common page-level ACF fields

- `intro_text` (the dek under H1)
- `email_address`
- `phone_number`
- `physical_address`
- `calendar_embed_url` (or shortcode)
- `social_links` (repeater)
- `show_map` (toggle)
- `map_coordinates` — group with `latitude` + `longitude`, conditional
- `office_hours` — repeater (day_label, hours_range)
- `response_time_expectation` — text (e.g., `"Within 1 business day"`)
- `departments` — repeater (department_name, contact_email, contact_phone, conditional)
- `form_destination_email` (where submissions go)
- `success_message` (post-submit text)
- `seo_title`, `seo_description`

## Don'ts

- Don't require 10 fields in the form — name, email, message is enough for first contact
- Don't have a captcha that triggers on every submission — use invisible/honeypot
- Don't hide the email address behind a form — power users will email anyway, give them the option
- Don't redirect to a generic "thanks" page — show inline success with next-step info
- Don't auto-respond with a generic "we got your message" if you can do better (e.g., "you'll hear from [name] within 1 business day")
- Don't bury the per-department contacts — when they exist, surface them as a visible second-level after the main form
- Don't ship a calendar embed with no times available next week — better to skip the embed than show "no slots"
- Don't show "we reply within 1 hour" if you actually take 3 days — calibrate to reality
