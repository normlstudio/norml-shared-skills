# Author bio block

> Short bio + photo + link to author archive at the end of a blog post. Builds authority and trust.

## Purpose

Tell the reader who wrote this. Supports E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) — Google explicitly favors articles with named expert authors. Also a touchpoint for further reading: the link to author archive surfaces other articles by the same person.

## Required elements

- **Photo** — author headshot, circle crop, ~80–120px
- **Name** — author display name
- **Bio** — 1–3 sentences (title, expertise, credibility hook)
- **Link to author archive** — `/author/{slug}/` or `/team/{slug}/`

## Optional elements

- Title / role under name ("Head of Strategy at Norml" / "Senior Copywriter")
- Social links (LinkedIn, X, personal site, etc.)
- "Articles by {author}" count
- Brand author variant — for projects without human bylines, show brand logo + brand description

## Gutenberg + ACF default (primary)

**Block name:** `acf/author-bio`
**ACF field group:** `Author bio`

Fields (when block is configurable per post — usually pulls from the WordPress user profile automatically):
- `override_author` — true_false, default false (false = use post's author_id; true = manual override below)
- `override_name` — text, conditional
- `override_photo` — image, conditional
- `override_bio` — textarea, conditional
- `override_archive_url` — URL, conditional

**WordPress user profile fields** (extended via `user_meta`):
- `photo` — image
- `title` — text (role)
- `bio` — textarea
- `linkedin_url` — URL
- `x_url` — URL
- `website_url` — URL

**Theme Options page** (brand-byline mode):
- `brand_byline_mode` — true_false, default false — when true, ALL posts use brand author instead of WP user
- `brand_name` — text, default project's brand name
- `brand_photo` — image, default brand logo
- `brand_bio` — textarea
- `brand_link` — URL (usually `/about/`)

**Blade template:** `resources/views/blocks/author-bio.blade.php`

## Elementor fallback

Use Elementor's Team Member widget for the bio block, with image + name + role + bio fields. Set link target to author archive.

## Variations

- **Compact byline** — small avatar + name + date inline in post header (not a full bio block — that's the meta row)
- **Full bio at end** — large card with photo, name, bio, social links — default
- **Brand byline** — single brand-author across all posts (e.g., "by the product-catalog example"), uses Theme Options brand fields
- **Co-authors** — multiple bio cards stacked, with a "Co-authored by" heading
- **Guest author** — same shape as default but with `Guest author` tag and link to author's external site

## Used on

- Blog post (default — every post)
- Case study (with project lead's bio)
- Resource pages (when authored by an individual)

## Don'ts

- Don't ship a generic placeholder bio ("John is a writer.") — even brand bylines need 2 sentences of substance
- Don't use a low-resolution or pixelated photo — it cheapens the whole brand
- Don't link the author's name to the post itself (or to nowhere) — link to the author archive
- Don't use stock photos for authors who don't exist — fabricating an authority is worse than not having one
- Don't put the bio in the middle of the article — only at the end (or compact byline at the top)
- Don't show social icons that link to dead/orphaned accounts
- Don't auto-pick the WP user's Gravatar without checking it's not the default mystery-person — fall back to brand logo if no real photo is set
