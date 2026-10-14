# SEO basics baseline contract

This is the canonical scope and decision table for `norml-seo-basics`. A required item
is not complete merely because an admin setting exists; its rendered public
output and, where applicable, browser network behavior must pass the matching QA.

## Status vocabulary

| Status | Meaning |
|---|---|
| `PASS` | Correct, live, and owned exactly once |
| `FIX` | Incorrect/missing and safely repairable in this run |
| `BLOCKED` | A required input, safe target, or dependency is unavailable |
| `SKIP` | A recommended recipe is not provisioned or approved |
| `ESCALATE` | Requires deeper research, content/business input, or another skill |
| `N/A` | Genuinely not applicable, with an evidence-backed reason |

These are **automated recipe statuses**. `FIX`, `BLOCKED`, and `ESCALATE` are
candidates—not independently confirmed defects. Any downstream service or
review workflow must preserve that distinction.

## 0. Recipe bundle and dependency contract

A full baseline selects the recipes declared in `SKILL.md`. A named-integration
request selects only that recipe and its recursive dependencies. The procedure,
verification, rollback, and hard stops live in the recipe file—not duplicated in
this contract.

| Concern | Recipe | Baseline policy | Required live state |
|---|---|---|---|
| Indexability | `recipes/indexability.md` | Required | Environment intent, final host, headers/meta, and canonicals agree |
| Core metadata | `recipes/metadata.md` | Required | One accurate title/description/robots/canonical owner |
| Sitemap/robots | `recipes/sitemap-and-robots.md` | Required | One canonical index and matching robots pointer |
| Search Console | `recipes/google-search-console.md` | Required unless explicitly opted out | Correct verified property plus submitted readable sitemap |
| Bing Webmaster Tools | `recipes/bing-webmaster-tools.md` | Required unless explicitly opted out | Exact verified canonical site plus submitted/listed sitemap |
| Tag manager | `recipes/google-tag-manager.md` | Required unless explicitly opted out | One intended GTM loader and noscript fallback |
| Consent management | `recipes/consent-management.md` | Conditional dependency for selected measurement | Recorded decision; one CMP/consent owner when applicable |
| Google Analytics | `recipes/google-analytics.md` | Required unless explicitly opted out | Presence/absence and delivery owner checked without provisioning |
| Microsoft Clarity | `recipes/microsoft-clarity.md` | Recommended when approved/provisioned | One official Clarity tag inside GTM; no direct duplicate |
| Favicon | `recipes/favicon.md` | Required | Approved icon family, valid links/manifest/root fallback |
| Social image | `recipes/social-sharing-image.md` | Required | One OG/Twitter owner and approved default 1200 × 630 card |
| Base schema | `recipes/schema-basics.md` | Required | One truthful connected graph |
| Internal 404s | `recipes/404-issues.md` | Required, check-only | Complete bounded crawl plus reproducible 4xx/source-inlink evidence |
| Media alt | `recipes/wp-media-alt-text.md` | Conditional WordPress profile | Complete evidence-backed Media Library review |
| Rank Math | `recipes/wp-rank-math.md` | Conditional WordPress profile | One SEO owner; analytics remains in GTM |

Dependency rules:

- `sitemap-and-robots` cannot start until `indexability` passes; Google Search
  Console and Bing Webmaster Tools cannot submit until the sitemap dependency
  passes.
- `google-analytics` is a presence-only independent check. It does not wait for
  GTM/consent and never provisions measurement. `microsoft-clarity` cannot start
  until GTM passes and consent management is `PASS` or evidence-backed `N/A`.
- A GTM container setting does not prove the dependency; the public loader,
  noscript fallback, data layer, and Preview connection must work.
- On WordPress, the GTM container is stored through the approved admin-managed
  integration. Theme/repository code must contain no GTM embed.
- Missing IDs/property access block only their recipes. Never invent or
  substitute identifiers or create a duplicate Google/Bing/analytics owner.
- `404-issues` and `google-analytics` are check-only in both modes. Their results
  may identify separate work, but never authorize a redirect/link/analytics
  mutation inside the baseline run.

## 1. Environment and indexability

Operational steps and rollback live in `recipes/indexability.md`. The table
below remains the shared acceptance reference for the live validator/report.

| Requirement | Acceptance | Fix policy |
|---|---|---|
| Final public URL | HTTPS and one stable preferred host after redirects | Repair platform URLs/redirects only after confirming the production contract |
| Platform canonical URL settings | Match the intended environment and canonical origin | Change through the platform manager; on WordPress never use blind SQL replacement |
| Search engine visibility | Public/indexable on a site intended to launch | Preserve private/noindex on staging/pre-launch and mark the public baseline pending |
| Header indexability | No `X-Robots-Tag: noindex` on indexable public HTML | Trace owner (host, security plugin, app, CDN) before removal |
| Meta indexability | Exactly one robots directive, without `noindex`/`nofollow` on the homepage | SEO plugin owns it on public sites |
| Canonical host | Canonical URL, OG URL, sitemap URLs, and redirects use the same preferred origin | Normalize one layer at a time and retest |
| Permalinks | Non-empty pretty structure for content sites | Set only when existing URL/redirect implications are understood |
| Language | Valid `<html lang>` matching the visible primary language | Fix through the platform's locale/document owner |

## 2. Homepage structure and metadata

Operational steps and rollback live in `recipes/metadata.md` and
`recipes/social-sharing-image.md`.

Every public homepage needs:

| Output | Required state | Notes |
|---|---|---|
| `<title>` | Exactly one, non-empty, intent-specific title | Aim for roughly 30–60 characters; clarity outranks a mechanical cutoff |
| Meta description | Exactly one, non-empty, accurate description | Aim for roughly 120–165 characters; no invented proof/claims |
| Robots meta | Exactly one | Use `index, follow` plus preview directives when appropriate |
| Canonical | Exactly one absolute HTTPS URL | Self-referential after the final redirect |
| H1 | Exactly one visible primary heading | It may differ from the title but must share page intent |
| Viewport | One responsive viewport tag | Required for a public modern site |
| `og:type` | One; normally `website` for the homepage | Page-specific content may differ |
| `og:site_name` | One | Approved site/brand name |
| `og:title` | One | May equal SEO title |
| `og:description` | One | Accurate, readable social copy |
| `og:url` | One | Same canonical public URL |
| `og:image` | One absolute HTTPS URL | Prefer 1200 × 630; must return an image MIME type |
| Twitter card | `summary_large_image` unless the asset/design requires otherwise | Explicit title, description, and image are preferred |

Metadata ownership is a functional requirement. When Rank Math or another mature
SEO plugin is active, theme output must not duplicate the plugin. A theme fallback
may render only when the chosen SEO owner is unavailable and must be tested in both
states.

### Metadata source precedence

1. approved project analysis / keyword research;
2. page-level SEO contract;
3. Strategic Messaging Context / product context;
4. visible page content.

Do not invent a focus keyword. An empty focus-keyword field is valid when the
mechanical baseline is complete but research is not.

## 3. Favicon and site identity

### Required artifacts

- vector favicon (`favicon.svg`) when the approved mark can be represented safely;
- legacy ICO (`favicon.ico`);
- PNG favicon at 16 × 16 and 32 × 32;
- Apple touch icon at 180 × 180;
- PNG site icons at 192 × 192 and 512 × 512;
- on WordPress, `site_icon` set to a Media Library attachment of at least 512 × 512;
- a valid JSON manifest with name, short name, colors, and the 192/512 icons.
- the conventional root `/favicon.ico` path returning non-empty `image/*` bytes
  that match the approved icon family (never homepage HTML or a WordPress default).

The exact filename may follow the existing theme convention, but all public URLs
must return `200` and a matching image/manifest MIME. Prefer `manifest.json` when a
shared host serves `.webmanifest` with an incorrect MIME type.

### Identity rule

Use an approved logo mark, monogram, or existing site identity. A temporary
initial-based site icon is allowed only when the user/project explicitly approves
it as a temporary technical asset. Never disguise a newly invented logo as a
favicon fix.

The favicon family must not reuse WordPress core artwork, the host's placeholder,
the active theme's demo icon, or another vendor's mark. Verify the rendered pixels
at 16, 32, 180, and 512 pixels against the approved identity source; a working URL
and correct MIME type are not identity proof. When an icon changes, use a
content-hashed or otherwise new public URL so a fresh browser context cannot retain
the previous favicon indefinitely.

A WordPress Site Icon is not automatically the publisher's logo. Populate Rank
Math's knowledge-graph logo and a schema `logo` property only when the project has
an explicitly approved logo asset. When the project deliberately has no logo,
leave those fields empty and omit `#logo` from the graph.

The live validator treats identical Site Icon and Organization-logo bytes as a
failure by default. `--allow-site-icon-as-logo` is an explicit exception flag,
not an auto-detection shortcut; use it only when the baseline report identifies
the approved dual-role asset.

### Output ownership

The platform Site Icon owner and asset/manifest owner must not print duplicate
same-purpose tags. On WordPress, core prints generated PNG/apple tags once
`site_icon` is set; account for that before a theme adds SVG, ICO, manifest, and
theme-color tags.

## 4. WordPress Media Library image alternative text

Operational steps and rollback live in `recipes/wp-media-alt-text.md`.

This section applies only to WordPress. Other platforms require the equivalent
complete media/image-alt review through their own content-management surface.

Every image attachment must be reviewed, including unattached assets and images
used only through theme options, SEO-plugin settings, featured images, or custom
fields. Inventory attachment ID, title, filename, dimensions, parent, current
`_wp_attachment_image_alt`, caption, description, and known front-end usages.

- Content-bearing images need concise, factual alt text that communicates their
  purpose in context. Inspect the actual pixels and page usage before writing.
- Logos, portraits, diagrams, screenshots, and social graphics must identify the
  meaningful subject or function without repeating surrounding copy.
- Decorative or fully redundant images keep an intentionally empty alt value;
  document their attachment IDs and reason in the baseline report. Empty can be
  correct, but an unreviewed blank is never a pass.
- Never derive alt text from filenames, attachment titles, keywords, EXIF data,
  or AI guesswork without visual/context verification. Never keyword-stuff.
- Do not overwrite a useful existing alt merely to standardize wording. Repair
  missing, meaningless (`image`, `photo`, filename-only), or objectively wrong
  values and preserve unrelated media metadata.

The run passes when the complete image attachment inventory has zero unexplained
blank or meaningless alt values. Record each changed attachment ID, before/after
value, inspected usage, and any intentional decorative blank. Media changes go
through supported WordPress REST API or WP-CLI, are included in the production rollback checkpoint,
and are verified in rendered HTML where the image is publicly used.

## 5. WordPress SEO plugin and Rank Math baseline

### Selection

- **Blank/new site with no SEO owner:** install current Rank Math free from the
  official WordPress repository.
- **Established site with Rank Math:** repair its settings in place.
- **Established site with Yoast/SEOPress/AIOSEO or a custom owner:** keep and
  configure it unless the user explicitly requests migration.
- Never run two metadata/schema/sitemap owners concurrently.

### Rank Math modules — default minimum

- Link Counter
- SEO Analysis
- Sitemap
- Schema (Rich Snippets)

Keep Analytics, Content AI, AI Visibility, Instant Indexing, WooCommerce,
BuddyPress, bbPress, Web Stories, and other integrations off unless the actual site
and approved connection require them. Rank Math Analytics stays off when Google
Analytics is owned by GTM. The absence of an external Rank Math account does not
block the free local baseline; skip registration and complete the wizard.

### Rank Math settings — baseline

- advanced setup mode;
- attachments redirect to the appropriate parent/home and attachment archives are
  not indexed;
- global robots indexable with large preview directives;
- fallback Open Graph image and `summary_large_image` Twitter card;
- verified company/person knowledge-graph identity, with a logo only when an
  approved logo asset exists;
- canonical homepage title and description;
- search, date archives, password-protected content, and paginated archive
  subpages handled conservatively;
- author archives disabled/noindexed on a single-author site, explicitly reviewed
  on a real multi-author publication;
- default Page schema set to `None`/off so a service landing page is not Article;
- homepage post meta written explicitly;
- focus keyword written only when verified by research/context;
- relevant post types and taxonomies included in the sitemap, irrelevant ones off;
- HTML sitemap off until a visible HTML sitemap is intentionally designed.

Use a project-specific, idempotent config script derived from
`templates/configure-rank-math.php`. Preserve unrelated existing plugin settings by
merging the options arrays rather than replacing them wholesale.

## 6. Schema graph

### Required homepage base

The homepage must expose one connected graph containing:

- `Organization` **or** `Person` for the site publisher;
- `WebSite` linked to that publisher;
- `WebPage` linked to the WebSite and canonical URL.

Use stable canonical `@id` fragments such as `#organization`, `#person`,
`#website`, and `#webpage`; add `#logo` only when an approved logo entity exists.
Exactly one entity should own each stable ID.

### Conditional entities

| Entity | Add only when |
|---|---|
| `Service` | The visible page offers/describes that service |
| `FAQPage` | The visible page contains the same questions and answers |
| `Product` / `Offer` | The product, price, currency, and availability are visible and current |
| `LocalBusiness` | Verified NAP/location and actual local-business context exist |
| `Person` (founder/author) | The person is identified visibly or in approved project facts |
| `BreadcrumbList` | Breadcrumbs exist or the site architecture warrants them |

Use the selected platform/schema owner for the base graph. On WordPress with Rank
Math, extend its graph through `rank_math/json_ld`, remove a same-type/same-ID
plugin entity before adding the canonical project entity, and prefer one
interlinked `@graph` over unrelated blocks. A theme fallback may supply the graph
only while the chosen plugin owner is unavailable.

All JSON-LD must parse, use absolute HTTPS URLs, match visible content, and contain
no duplicate `@id` values or duplicated top-level entities.

## 7. XML sitemap and robots.txt

Operational steps and rollback live in `recipes/sitemap-and-robots.md`.

### Canonical sitemap

Declare one platform-owned sitemap index. It must return valid XML and contain at
least one child or URL entry, and every listed child sampled must return valid
XML. On WordPress when Rank Math owns the sitemap, the preferred index is:

```text
/sitemap_index.xml
```

The WordPress core `/wp-sitemap.xml` must then be disabled, redirected to the
canonical index, or otherwise demonstrably not form a second independent index.

### WordPress inclusion policy

On another platform, apply the same principle—include only intentional indexable
page/content/taxonomy types—through that platform's sitemap owner.

Include only indexable, intentional public types:

- static Pages: normally on;
- Posts: on when a blog exists or is planned and public;
- Categories: on only when archives are useful/indexable;
- Tags: off by default;
- Attachments: off;
- Authors: off on single-author sites; reviewed on multi-author publications;
- Products/CPTs/taxonomies: based on actual site architecture, never a generic
  one-size-fits-all toggle.

Images and featured images should be included when they are indexable page assets.

### robots.txt

`/robots.txt` must return successfully, must not blanket-disallow the public site,
and must include one `Sitemap:` line pointing to the chosen canonical sitemap index.
Do not put staging/private URLs in production robots output.

## 8. Internal 404 discovery

Operational steps live in `recipes/404-issues.md`. A full baseline runs a bounded
internal crawl and records both the client-error URL and the source inlinks that
made it discoverable.

The crawl passes only when:

- the exact canonical start/final host, crawler version, URL limit, start/end
  time, and URLs crawled are recorded;
- coverage completed without a licence cap, rate limit, WAF block, authentication
  wall, crash, or unexplained stop;
- every discovered internal 4xx URL has a live HTTP recheck and source-inlink
  evidence when available;
- the timestamped Markdown report contains the complete candidate table or an
  explicit complete-crawl zero-result statement;
- raw exports live under the run-specific `.claude/evidence/norml-seo-basics/{run-id}/`
  evidence folder, not as a loose client report or local Office file.

The free Screaming Frog tier is limited to 500 crawled URLs. A site that can
exceed that limit requires the licensed crawler or an already approved,
equivalently complete source. A partial/capped crawl is `BLOCKED`, never `PASS`.
The basic crawl uses no API key.

Automated output remains pending review. Do not create redirects, restore/delete
content, edit links, or change response behavior until a reviewer confirms the
issue and the owning implementation workflow receives a separate request.

## 9. Reproducibility and durability

For code-backed projects, the source of truth includes:

- project icon/social assets and manifest;
- theme integration/fallback code;
- idempotent SEO-plugin configuration script when that platform/profile uses one;
- one immutable timestamped report under
  the user-selected report folder (default `.claude/docs/seo/reports/`);
- `.claude/docs/seo/norml-seo-basics.md` as the current summary/index pointing to that
  report;
- architecture/application notes that declare output ownership;
- a Git commit pushed before/with production deploy.

Database state alone is not a reproducible implementation. Conversely, committing
a config script without executing and verifying it on the target is not completion.

## 10. Out of scope — route instead

- crawl analysis beyond the bounded internal-4xx check, plus full
  crawlability/CWV/internal-link architecture/hreflang/security analysis →
  `norml-seo-technical-analysis`;
- keyword universe/competitor selection → `keyword research` and
  `SEO strategy analysis`;
- advanced CPT/product/local/schema architecture → `norml-seo-schema`;
- bulk page titles/descriptions → `metadata writing`;
- finished SEO article publishing → `article publishing`;
- GA property/stream/tag provisioning, advanced events, conversions, ecommerce
  data layers, legal/privacy policy, and reporting dashboards → a dedicated
  measurement engagement rather than extending the presence check ad hoc.
