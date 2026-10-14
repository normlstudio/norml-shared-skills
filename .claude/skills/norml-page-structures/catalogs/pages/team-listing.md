# Team listing page

> The "all of us" page — every team member shown with photo, name, role. Often filterable by department / team / location.

## Purpose

Surface the people behind the brand. Convert "is this real?" into "yes, real humans." Each card links to a [team-member](team-member.md) page for deeper bio + posts authored.

## Required structural elements (top → bottom)

1. **Header**
2. **Page hero** — H1 ("Our team" / "Meet the team" / "Who we are") + intro paragraph
3. **Department / role filter (optional)** — [category-pills](../blocks/category-pills.md) shape, filters by department or role (only if the team is 15+ people)
4. **[Team grid](../blocks/team-grid.md)** — [team member cards](../blocks/team-member-card.md) in a grid, 3–4 columns desktop
5. **[CTA](../blocks/cta.md)** — typically "We're hiring" or "Get in touch"
6. **Footer**

## Recommended (situational) blocks

- **Leadership section** — call out 2–4 leadership members in a featured row above the main grid
- **Stats strip** — "27 team members across 5 countries"
- **Office locations** — small map / list if the team is distributed
- **Values block** — reuse from [about.md](about.md) — reminder of what brings the team together
- **"Open roles" callout** — link to careers page, sticky or in-grid

## Common variations

- **Single-department firm** — flat grid, no filter
- **Multi-department firm** — filter by department, grouped grid OR pills above flat grid
- **Distributed / remote-first** — show location with each card
- **Leadership-first** — leadership team in featured row + rest of team below

## SEO / schema notes

- H1 on page title
- Schema: `Organization` with `employee` array (each Person)
- Each team member's card links to their [team-member](team-member.md) page (which has its own `Person` schema)
- Avoid emitting Person schema for unlisted / anonymous team members

## Common page-level ACF fields

- `intro_dek` — paragraph under H1
- `show_filter` — true_false, default false (auto-true if team count >15)
- `filter_taxonomy` — select: `department | role | location`, conditional
- `leadership_featured` — relationship to 2–4 team members shown in a featured row
- `hiring_message` — textarea, optional (renders in CTA section if set)
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't show stock-photo team members
- Don't ship team cards with inconsistent photo treatments (mix of headshots and casual photos) — pick one style and apply across all
- Don't show a 30-card grid with no filter — readers can't scan; add filter or break into departments
- Don't link cards to nowhere — every card goes to a [team-member](team-member.md) page; if you don't have a member page yet, scaffold one with at least a stub
- Don't claim "we're hiring" if there are no open roles — link goes to a 404 or empty careers page
- Don't sort by alphabetical alone — surface leadership first, then alphabetical or by department
