# Team member page (Person page)

> One team member's detail page. Bio, photo, role, expertise, articles they've written, contact / social.

## Purpose

Build credibility around the individual. Author archive — surface all blog posts written by this person (supports E-E-A-T). Single landing page for press / LinkedIn / external linking to a specific expert.

## Required structural elements (top → bottom)

1. **Header**
2. **[Breadcrumb](../blocks/breadcrumb.md)** — `Home > Team > {Name}`
3. **Person hero** — large photo + name (H1) + role + 1-sentence bio
4. **Long bio** — 2–4 paragraphs, written in first or third person consistently
5. **Expertise / areas of focus** — bullet list or tag pills
6. **Articles by {Name}** — query loop of posts where this person is the author, 3–6 cards, link to author archive for "see all"
7. **Social / contact links** — LinkedIn, X, personal site, email (optional, person's preference)
8. **CTA strip** — back to team / contact / read blog
9. **Footer**

## Recommended (situational) blocks

- **Featured project / case study** — if the person led a specific notable project
- **Quote / testimonial about the person** — what colleagues or clients say
- **Talks / speaking engagements** — list of conferences / podcasts
- **Education / certifications** — for fields where credentials matter (medical, legal, engineering)
- **Personal interests** — humanizing strip ("when not at work, I…") — keep one line

## Common variations

- **Expert / thought-leader page** — long bio, expertise tags, articles list prominent, talks visible
- **Operational / team-member page** — short bio, role focused, no articles list, simpler shape
- **Founder / executive page** — story-led bio, prominent quote, featured case studies, press mentions

## SEO / schema notes

- H1 on the person's name
- Schema: `Person` with `name`, `jobTitle`, `image`, `worksFor` (the org), `sameAs` (social links), `description` (bio)
- Each article in "Articles by {Name}" links to the post (which has BlogPosting schema with `author = this Person`)
- Author archive URL (`/author/{slug}/`) should redirect or alias to this page — pick one canonical URL per person

## Common page-level ACF fields

- `photo` — image, required
- `display_name` — text (defaults to WP user display name)
- `role` — text (e.g., "Senior Strategist")
- `short_bio` — textarea (1 sentence, used in cards)
- `long_bio` — wysiwyg
- `expertise` — repeater (tag name) or relationship to taxonomy
- `linkedin_url`, `x_url`, `personal_site_url`, `email`
- `featured_project` — relationship to a case study, optional
- `testimonial` — group: `quote` + `attribution` + `affiliation`, optional
- `talks` — repeater (title, event, year, url), optional
- `certifications` — repeater (label, issuer, year), optional
- `seo_title`, `seo_description`, `og_image`

## Don'ts

- Don't ship a person page without a real photo
- Don't write the bio in the third person on some people and first person on others — pick one per project
- Don't auto-show all posts ever (could be 200+) — paginate or cap at 6 with "see all" link
- Don't claim certifications or credentials that can't be verified
- Don't link to dead LinkedIn / X accounts
- Don't include private contact info (personal phone, personal email) — use work email or contact form
- Don't write a bio that's 95% job-history and 5% personality — both, ideally
- Don't link the photo to itself or to nothing — link to author archive or no link at all
