# Team member card (template part)

> One tile in a [team grid](team-grid.md). Photo + name + role + (optional) short bio. Whole card links to [team-member](../pages/team-member.md) page.

## Purpose

Canonical card shape for any team-member listing. Centralized so About / Team listing / Home don't diverge.

## Required elements

- **Photo** — consistent crop and treatment across all cards in a grid
- **Name** — display name
- **Role** — short text (e.g., "Head of Design")
- Whole card clickable, links to the person's [team-member](../pages/team-member.md) page

## Optional elements

- **Short bio** — 1 sentence under role
- **Department / location tag** — small pill
- **Social icons** — LinkedIn / X / personal site (small icons inline)
- **Hover state** — subtle elevation, image effect, accent color
- **"New hire" badge** — for members added in last 30 days

## Gutenberg + ACF default (primary)

Not a standalone ACF block — a Blade template part included by [team-grid](team-grid.md) and other contexts.

**Template part path:** `resources/views/partials/team-member-card.blade.php`

Parameters passed in via Blade `@include`:
- `$member` — team member object (CPT or User)
- `$size` — `large | medium | small`
- `$show_role` — boolean
- `$show_short_bio` — boolean
- `$show_socials` — boolean
- `$style` — `photo-square | photo-circle | minimal-text`

**Theme Options** (`ACF Options → Site → Team`):
- `default_card_style` — radio (same as above), default `photo-square`
- `photo_aspect_ratio` — radio: `1:1 | 4:5 | 3:4`, default `1:1`
- `new_hire_badge_days` — number, default 30 (0 = disable)

## Elementor fallback

Elementor's Team Member widget. Configure photo/name/role positions per spec.

## Variations

- **Photo-square (default)** — square crop, name + role below
- **Photo-circle** — circle crop, more editorial
- **Minimal-text** — no photo, just name + role (used in compact lists, footer team strip)
- **With socials** — small icon row under role
- **Department badge** — small pill above the name
- **Featured / leadership** — larger photo, longer bio under role

## Used on

- [Team grid](team-grid.md)
- [About](../pages/about.md) — team section
- Home — leadership row (variant)
- Footer (rare — small "made by" strip)

## Don'ts

- Don't show different photo aspect ratios across cards in one grid
- Don't truncate the name with ellipsis — use small font size before truncating; reading "Ana M…" is worse than reading small text
- Don't link the photo to a different URL than the card text — the whole card links to one place
- Don't show stock photos
- Don't ship with placeholder names ("John Doe") — fill or hide
