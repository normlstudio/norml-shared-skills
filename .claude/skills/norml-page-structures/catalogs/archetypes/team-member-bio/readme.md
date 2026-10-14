# Team member bio — page archetype

A single-person bio page rendered from a CPT (`team`, `instructor`, `attorney`, `staff`, etc.). Lives at URLs like `/team/{slug}/`, `/instructor/{slug}/`, `/attorneys/{slug}/`. Industry-standard layout across legal firms, education platforms, sports/fitness sites, agencies.

## Public scope

This is a generalized text archetype. Reference screenshots, named individuals,
client routes and private staging URLs are excluded. Verify the user's real
person/content records before rendering a bio or Person graph.

## Page skeleton (top → bottom)

1. **Breadcrumb** — `Home / Team / {Name}` (or `/ Attorneys /`, `/ Instructors /` etc.)
2. **Hero (two-column)**
   - LEFT (~40%): photo, square aspect or portrait. Sticky on scroll for tall pages.
   - RIGHT (~60%): name (H1, large display), role (subtitle in brand accent), optional one-line intro, optional CTA button.
3. **About** — short bio paragraph (1–2 sentences). The "elevator pitch" version.
4. **Professional background** — long bio, 2–5 paragraphs. The detailed story: experience, philosophy, what makes them effective.
5. **Optional inline media block** — action photo, illustration, or short embedded video. Breaks up the long text.
6. **Areas of interest / Practice areas / Expertise** — bullet list, sometimes grouped into 2–3 columns. Title varies by industry:
   - Legal: "Practice areas"
   - Education: "Areas of expertise" / "Teaches"
   - Sports/fitness: "Coaches" / "Specialties"
   - Generic: "Focus areas"
7. **Credentials & certifications** — accordion-style list with chevron toggles. Each row: cert name + optional issuer + optional verification URL. Closed by default; clicking expands a short description.
8. **Languages spoken** *(legal/multilingual contexts only)* — bullet list or pill row.
9. **Connect / Follow** — social icons (LinkedIn primary, then platform-relevant: Avvo for attorneys, Instagram for fitness, YouTube for educators).
10. **Related items** — horizontal scroll OR grid of related entities by this person:
    - Legal: case results, blog posts they authored, practice-area landing pages they own
    - Education: courses they teach
    - Sports: programs they coach
    - Agency: client work they led
11. **Contact / inquiry CTA** — full-width band at the bottom. Either a Gravity Form embed ("Schedule a consultation") or a CTA button to the firm-wide contact page.

## Section visibility rules

Not every person has data for every section. The template MUST conditionally hide empty sections — never render an empty `<h2>Practice areas</h2>` with no list under it.

| Section | Required | Hide if empty |
|---|---|---|
| Breadcrumb | yes | — |
| Hero (photo + name + role) | yes (role can be a placeholder like "Team member") | — |
| About | yes | — |
| Professional background | no | yes |
| Inline media | no | yes |
| Areas of interest | no | yes |
| Credentials | no | yes |
| Languages | no | yes |
| Connect | no | yes |
| Related items | no | yes |
| Contact CTA | yes (site-wide pattern) | — |

## ACF schema (canonical field group)

Field group key: `group_team_bio` (or `group_{cpt}_bio` if the CPT is named differently).

| Field name | Type | Required | Notes |
|---|---|---|---|
| `role` | text | yes | Short title shown under the name. Examples: "Attorney", "Yoga Instructor", "Head Coach". |
| `job_title` | text | no | Full version for schema's `jobTitle`. Falls back to `role`. |
| `photo` | image (array return) | no | Hero photo. Falls back to featured image if empty. |
| `short_bio` | textarea (~2–3 rows) | no | The "About" section. Also used for Person schema `description`. |
| `long_bio` | wysiwyg (basic toolbar) | no | The "Professional background" section. Multi-paragraph. |
| `inline_media` | image | no | Optional action photo between long bio and expertise. |
| `expertise` | repeater (`name` text) | no | Areas of interest / practice areas. Renders as a bullet list (or 2-col grid if >6 entries). |
| `credentials` | repeater (`name` text req, `issuer` text, `description` textarea, `url` url) | no | Accordion. Description (if present) shows when expanded. |
| `languages` | text | no | Comma-separated. Rendered as pill row. Also Person.knowsLanguage. |
| `education` | textarea (one school per line) | no | First line is Person.alumniOf in schema. |
| `social_links` | repeater (`label` text, `url` url req) | no | Connect section + Person.sameAs in schema. |
| `email` | email | no | Direct email. Linked in Connect block. |
| `phone` | text | no | Direct phone. Linked in Connect block. |
| `related_post_type` | select (`post`, `case_study`, `course`, `program`, `none`) | no | Drives the "Related items" section. `none` hides it. |
| `related_items` | relationship (filtered by `related_post_type`) | no | Optional manual curation; otherwise auto-query by author/category. |
| `knows_about` | textarea (one topic per line) | no | Schema-only: Person.knowsAbout array. Not rendered on the page. |

## Schema (JSON-LD, injected into `<head>`)

Type: `Person`. Mirror the site's existing schema owner — use the field map below and validate actual output.

Key fields to populate:
- `@id` → `{permalink}#person`
- `name`, `url`, `image`
- `worksFor` → site Organization `@id`
- `jobTitle`, `description`
- `knowsLanguage`, `knowsAbout`, `alumniOf`, `hasCredential` (one or array)
- `sameAs` from `social_links`
- `email`, `telephone`

Omit empty fields entirely. Never emit `"email": ""`.

## Layout / CSS notes

- **Hero photo aspect**: portrait 4:5 or square 1:1. Object-fit `cover`, `object-position: top` so faces don't get cropped at the chin.
- **Sticky photo on desktop** (`position: sticky; top: var(--header-height) + 24px`) so the photo stays visible while the long bio scrolls.
- **Two-column collapses to single column** below ~960px: photo on top, then text.
- **Type scale**: name uses the display font (the project-approved display font), role uses body font in brand accent color, sections use the standard H2 + body sizes from `components.css`.
- **Accordion** for credentials: use existing `.site-accordion` from `components.css` (Layer 2). Do NOT roll a new accordion.
- **Related items grid**: use existing `.site-card-grid` or `.site-card` from `components.css`.
- **Bottom CTA band**: use `.site-banner` or the project's existing contact-band component.

## Conditional rendering — what to do per industry

The template logic stays identical; only labels and a couple of optional sections vary by industry. Use a `team_type` ACF field on the CPT if a single template must serve multiple flavors. Otherwise duplicate the template with the right labels.

| Slot | Legal | Education | Sports/Fitness | Agency |
|---|---|---|---|---|
| Section 6 label | "Practice areas" | "Areas of expertise" | "Coaches" | "Specialties" |
| Section 7 label | "Bar admissions & credentials" | "Certifications" | "Certifications" | "Credentials" |
| Section 8 (languages) | shown | optional | hide | hide |
| Section 10 (related) | case results / authored posts | courses taught | programs led | client work / case studies |
| Section 11 (CTA) | "Schedule a consultation" + intake form | "Book a session" / course CTA | "Sign up for a program" | "Start a project" |

## Anti-patterns (don't do these)

- ❌ Render the whole bio in one giant `<div class="bio">` blob. Sections are real — give each its own block with conditional render.
- ❌ Hardcode the team member's name inside copy ("Schedule a consultation with Leo today"). Use the title dynamically: `the_title()` / `{name}` placeholder.
- ❌ Show the contact band ABOVE the related items — proven pattern is content → related → CTA, so the visitor sees what the person actually does before being asked to convert.
- ❌ Use stock-photo overlays / gradients on the hero photo that obscure the face. If a gradient is needed (e.g. for caption legibility), constrain it to the bottom ~15% of the image.
- ❌ Build a custom accordion for credentials. Use the `.site-accordion` already in `components.css`.
- ❌ Skip the schema. Person schema can describe a verified person; individual bio pages also serve readers and navigation.
