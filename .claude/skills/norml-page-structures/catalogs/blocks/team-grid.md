# Team grid block

> Grid of [team member cards](team-member-card.md). Used on About and Team listing pages.

## Purpose

Display the team visually. Each card surfaces a person; the grid is the index. Filterable by department / role / location when team is large.

## Required elements

- **Heading** (optional — depends on page context)
- **Grid of team cards** — see [team-member-card](team-member-card.md) for the canonical card
- **3–4 columns desktop, 2 columns tablet, 1 column mobile**

## Optional elements

- **Filter pills** — by department / role / location (reuse [category-pills](category-pills.md) shape)
- **Featured row above grid** — leadership / founders shown in a 2–4 card row before the regular grid
- **Department headers** — group cards by department with a heading per group
- **"Open roles" card** — final card in the grid is a CTA to careers ("Want to join?")

## Gutenberg + ACF default (primary)

**Block name:** `acf/team-grid`
**ACF field group:** `Team grid`

Fields:
- `heading` — text, optional
- `selection_mode` — radio: `all | by_taxonomy | hand_picked | featured_first`, default `all`
- `taxonomy_filter` — taxonomy select, conditional on `by_taxonomy`
- `picked_members` — relationship, conditional on `hand_picked`
- `featured_members` — relationship, conditional on `featured_first` (2–4 people shown first)
- `columns` — radio: `2 | 3 | 4`, default `3`
- `show_role` — true_false, default true
- `show_short_bio` — true_false, default false
- `card_style` — radio: `photo-square | photo-circle | minimal-text`, default `photo-square`
- `show_hiring_card` — true_false, default false
- `hiring_card_url` — URL, conditional

**Blade template:** `resources/views/blocks/team-grid.blade.php`

Queries the team CPT (or `user` if team members are WP users) and renders [team-member-card](team-member-card.md) for each.

## Elementor fallback

Use Elementor's Team Member widget repeater (Elementor Pro) or a custom Loop Grid wired to a Team CPT.

## Variations

- **Flat grid (all team)** — simplest
- **Featured-first grid** — leadership row + regular grid
- **Filtered grid** — pills above, query-string-driven filter
- **Department-grouped** — sub-headings between department groups
- **With hiring card** — last card is "We're hiring" CTA

## Used on

- [About](../pages/about.md) — featured-first or trimmed grid
- [Team listing](../pages/team-listing.md) — full grid
- Home — leadership-only row (variant)

## Don'ts

- Don't mix photo styles in one grid — pick square OR circle OR no-photo, consistent
- Don't show 4 columns on a 6-person team — 2 or 3 columns reads better
- Don't surface "hiring card" if there are no open roles
- Don't query by taxonomy with no taxonomy term set — empty grid is the result
- Don't make cards different heights — `display: flex` with `align-items: stretch`
- Don't link a card to nowhere — every card goes to its [team-member](../pages/team-member.md) page
