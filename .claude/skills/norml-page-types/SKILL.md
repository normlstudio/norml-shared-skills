---
name: norml-page-types
version: 1.0.0
description: >
  Select and extend reusable public-website page families: archive/hub,
  single, category and child pages, plus industry × service, service × location
  and other explicitly eligible intersections. Use for "what page types should
  this site have", "suggest website architecture", "archive and single",
  "industry pages and their service children", "areas of service",
  "About Us plus team-member pages", or "add a page type". One folder per family
  with a same-name overview and flat member files; root index.md and
  add-page-type.md own discovery and extension. Feeds sitemap planning;
  WordPress architecture review decides actual CMS primitives; norml-page-structures owns
  blocks and elements. Includes learning-directory, brand, tool, portfolio and
  optional commerce/membership companion patterns grounded in project review.
  Includes maintained comparison archives and evidence-backed offering pairs.
  No site implementation, page multiplication or publishing.
metadata:
  author: Norml Studio
---

# Norml Page Types

A **page type is a family of related pages**, not one layout or one URL.
Use this catalog to propose the kinds of destinations a website needs and how
they connect. It works across clients and platforms. Archive/single terminology
is the shared architectural vocabulary; WordPress is an implementation mapping.

## When to use

- "What page types should this site have?" / "Suggest website architecture."
- "What should we build next?" when the question concerns missing page families.
- "Industry pages and their service children" / "service × location pages".
- "About Us plus team-member pages" / "FAQ archive and answers".
- "Add a page type" / "add a page to an existing type".

For block order and elements, use `norml-page-structures`. For a complete sitemap,
use `sitemap planning`. For actual WordPress primitives and routing, use
`WordPress architecture review`. Implementation stays with the relevant build skill.

## Required reading and selection

1. Resolve the project and read its context entry point, brief/SMC, current
   inventory and recorded architecture decisions. For catalog-only questions,
   no project access is needed. Keep observed, approved-planned and proposed
   pages distinct; do not invent a client’s services, people, locations or facts.
2. Read [index.md](index.md), then [architecture principles](standards/architecture.md).
   Match by entity, visitor purpose and relationships, not label or path alone.
3. Read `page-types/{family}/{family}.md` and every relevant member file named in
   its local table. Read both parents for intersections. A summary/index row is
   not the complete contract. Read only selected families, not the entire catalog.
4. For project-derived additions, also read [project-pattern rules](standards/project-patterns.md)
   and [the provenance review](standards/pattern-notes.md). A URL in XML is
   a discovery lead; page content and final response establish the observed role.
   Public page evidence does not establish functional checkout, tools or forms.
5. For each candidate choose **include**, **embed**, **defer** or **omit**, with
   source-backed rationale and unresolved dependencies. Not every family or
   member belongs on every site. No fixed count or depth limit applies.
6. Pin archive/hub and single availability, category/depth decisions, canonical
   parent(s), route orientation, record identity and source of content truth.
   Run the intersection gate for every proposed pair; never approve a Cartesian
   product from entity counts alone. More axes require an explicit new contract.
7. Hand the result to `sitemap planning` using the output contract below.
   For WordPress, `WordPress architecture review` resolves the actual primitive and query
   role. Load matching `norml-page-structures` specs before block design/build.
   A missing structure spec is a gap, not permission to claim guessed blocks
   as catalog requirements.
8. Validate against [catalog cases](qa/catalog-cases.md). Persist project
   decisions in its established architecture/sitemap/task records, not this
   reusable skill. No competing tracker or automatic client mutation.

## Quick family index

The [complete index](index.md) links **every included member specification**,
its matching conditions and branches. Use this table only for orientation.

| Page family | What is included / why select it |
|---|---|
| [Home](page-types/home/home.md) | Homepage |
| [About Us and people](page-types/about-us/about-us.md) | About Us archive/hub; Team-member single; Dedicated team directory; Department listing |
| [Services](page-types/services/services.md) | Services archive; Service single; Service-category archive; Service × location; Subservice or focused practice single; Contextual service-page index |
| [Industries](page-types/industries/industries.md) | Industries archive; Industry single; Industry × service; Industry × location; Subindustry single |
| [Areas of service](page-types/areas-of-service/areas-of-service.md) | Coverage archive; Service-area single; Child service area |
| [Physical locations](page-types/locations/locations.md) | Locations archive; Physical-location single |
| [Products](page-types/products/products.md) | Products archive; Product single; Product-category archive; Product × industry; Curated merchandising listing; Compatibility/format catalog landing |
| [Solutions, use cases and audiences](page-types/solutions/solutions.md) | Solutions archive; Solution/use-case single; Audience archive; Audience single; Product applications hub; Product-application landing |
| [Case studies and work](page-types/case-studies/case-studies.md) | Case-studies archive; Case-study single; Classified case listing |
| [Comparisons and alternatives](page-types/comparisons/comparisons.md) | Comparison archive; Comparison single for one eligible offering pair |
| [Blog and editorial articles](page-types/blog/blog.md) | Blog archive; Article single; Editorial topic archive; Author article archive |
| [FAQ and answers](page-types/faq/faq.md) | FAQ archive; FAQ answer single; FAQ topic archive |
| [Resources, guides and downloads](page-types/resources/resources.md) | Resources archive; Resource single; Resource category archive; Guide/documentation chapter; Installable resource/package single |
| [News and announcements](page-types/news/news.md) | News archive; Announcement single |
| [Events](page-types/events/events.md) | Events archive; Event single; Event-type archive |
| [Programs and courses](page-types/programs/programs.md) | Programs archive; Program/course single; Session/cohort single |
| [Careers and vacancies](page-types/careers/careers.md) | Careers hub/archive; Vacancy single |
| [Pricing and plans](page-types/pricing/pricing.md) | Pricing hub; Plan/package single |
| [Contact and enquiries](page-types/contact/contact.md) | Contact hub; Specific enquiry destination; Directory listing submission |
| [Testimonials and reviews](page-types/testimonials/testimonials.md) | Testimonials/reviews archive; Testimonial single; Review-submission journey |
| [Partners and affiliations](page-types/partners/partners.md) | Partners archive; Partner single; Partner/verification program destination |
| [Policies and legal information](page-types/legal/legal.md) | Legal/policy hub; Policy/document single |
| [Search and journey states](page-types/utility/utility.md) | Search results; Not-found state; Enquiry success state; Communication-preferences destination; Newsletter subscription destination |
| [Courses and learning directories](page-types/courses/courses.md) | Course catalog; Course offering single; Curated filter-preset landing |
| [Providers, schools and organizations](page-types/providers/providers.md) | Provider directory; Provider organization single |
| [Experts and external practitioners](page-types/experts/experts.md) | Expert directory; Expert/instructor single |
| [Disciplines and subject catalogs](page-types/disciplines/disciplines.md) | Discipline/subject hub; Discipline-category hub; Discipline landing |
| [Specialties and focused subjects](page-types/specialties/specialties.md) | Specialties hub; Specialty landing |
| [Brands and manufacturers](page-types/brands/brands.md) | Brand index; Brand landing |
| [Interactive tools and calculators](page-types/tools/tools.md) | Tools index; Calculator destination; Quiz/recommender destination; Timer or guided practice tool |
| [Memberships and loyalty programs](page-types/memberships/memberships.md) | Membership-program index; Membership/loyalty program single |
| [Commerce and customer journeys](page-types/commerce/commerce.md) | Cart destination; Checkout destination; Customer account entry; Bundle/quantity-set builder; Compatibility-aware product configurator |
| [Visual work and concept galleries](page-types/portfolio/portfolio.md) | Before-and-after gallery; Concept/unpublished-work gallery; Visual project/concept single |

## Outputs and handoff

Return a page-family recommendation and populate the consuming project’s
existing architecture record with these fields:

| Field | Required meaning |
|---|---|
| family / member | Stable IDs, e.g. `industries` / `industry-by-service` |
| source_spec | Portable skill path plus skill version |
| disposition / evidence | include, embed, defer or omit; why and from which source |
| state | observed, approved-planned or proposed; never conflate them |
| entity / identity | Canonical entity or unique relationship tuple |
| logical_role | archive, single, taxonomy-archive, singleton, intersection or utility |
| technical_role / model | Verified mapping, or unresolved for the CMS owner |
| parent(s) / route | Logical parents; one canonical pattern; hierarchy/orientation |
| archive / single availability | public, embedded-only, disabled, not applicable or unresolved |
| relationships / depth | Child members, classification and allowed intersections |
| content owner / source | Existing canonical records and relationship-specific differences |
| structure_spec / page_md | Matching structure spec; existing page contract path or pending |
| locale / translations | If relevant: canonical entity, locale and verified translation relationships |
| unresolved | Missing content, evidence, mapping or explicit project decision |

Do not invent hours, prices or delivery commitments; use `a separately approved evidence-backed estimation workflow` if asked.
This skill writes no CMS records, templates, live routes or deployments.

## Extend the catalog

Read [add-page-type.md](add-page-type.md) before adding or changing a family.
It preserves the authoring contract: one folder per family, a same-name overview,
any number of flat member files, complete root/local indexes and explicit branches.
Use the linked templates and QA gates there. Version, document, register and
publish through `package maintenance`, `human documentation maintenance` and `project Git workflow`.

## Hard boundaries

- No new CPT for every family by assumption; no inference from URL depth alone.
- A logical About Us archive may be implemented as a singleton querying people.
- No automatic service-area → physical-location conversion.
- No duplicate canonical route for the two orientations of one intersection.
- No unsupported local, industry, commercial, legal or outcome claims.
- No invented archive/single pair for genuine singleton or system pages.
- Project overrides are recorded; missing facts are unresolved, not overrides.
- Keep core entity facts in one source; combinations own contextual differences.

## Related skills

- `sitemap planning` consumes family choices and owns site-wide planning/navigation.
- `WordPress architecture review` translates the choices into verified WordPress primitives.
- `norml-page-structures` owns each destination’s blocks, elements and archetypes.
- `page planning/build workflow` turns the chosen destination into page/admin/build tasks.
- `wireframe composition` composes its low-fidelity block layout after selection.
- `package maintenance` owns catalog-package maintenance and registration.

## Standalone use

No other skill is required. With this package alone, select family/member contracts,
write the documented handoff into the user's architecture record, and flag unknown
CMS/block details. If installed, norml-page-structures and norml-wp-architecture are
optional deeper catalogs. Do not require another private planning or publishing system.
