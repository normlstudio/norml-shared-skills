# Acceptance contract

`norml-seo-basics` uses a layered verification gate. A run passes only when
every applicable **Required** check passes on the final public URL. Warnings are
recorded but do not substitute for failures.

Analyze-only execution can finish with `FIX`, `BLOCKED`, or `ESCALATE`
findings when every recipe was actually assessed and reported. That means the
assessment completed; it does not turn the website result into `PASS`.

## Result rules

- **PASS** — every applicable Required check passes; warnings have an owner/next step.
- **FAIL** — one or more Required checks fail.
- **BLOCKED** — a `standards/hard-stops.md` condition prevents safe verification or repair.
- **SKIP** — a Recommended recipe was not provisioned/approved; Required work is
  unaffected and the reason is recorded.
- `N/A` requires a reason tied to site architecture; it is not a way to hide a fail.
Save machine captures under the project's `.claude/evidence/norml-seo-basics/{run-id}/`
or `.claude/qa/`, never loose in the human-facing project root.

## Gate A — target and rollback

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| A1 | Yes | Exact environment | Public host, platform mapping, canonical settings, and final redirect agree |
| A2 | Yes for writes | Capability record | Applicable platform-management capability, notes, and activity records exist |
| A3 | Yes for production writes | Platform backup | Dated, recoverable settings/data backup or version exists and is logged; server files stay outside public web root |
| A4 | Yes for code writes | Git source | Remote/branch/deploy contract known; unrelated dirty work identified |
| A5 | Yes for production code | Git/prod parity | Exact production change is committed and pushed; deployed commit recorded |

## Gate T — recipe graph, tag manager, and analytics

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| T1 | Yes | Recipe selection | Every requested/full-baseline recipe is listed with applicability and status |
| T2 | Yes | Dependency order | Every dependency is PASS/evidence-backed N/A before its dependant; no missing/circular edge or duplicate procedure |
| T3 | When selected | GTM loader | One intended `gtm.js` request and one matching noscript fallback; data layer starts |
| T4 | WordPress + GTM | Admin ownership | Approved admin integration owns GTM; repository/theme contains no embed or container ID |
| T5 | GA selected | Presence check | Public source/network states present once, absent, blocked, or duplicate; no property/stream/tag/container state is created or changed |
| T6 | GA present | Delivery ownership | One intended delivery owner is identified, or direct `gtag.js`, CMS/plugin, Site Kit, Rank Math Analytics, theme, legacy, or multi-ID ambiguity is escalated |
| T7 | Clarity selected | Clarity tag | Official Clarity tag fires once through GTM and the intended project verifies it |
| T8 | Clarity selected | No direct Clarity | No direct site/plugin/theme Clarity embed exists |
| T9 | Analytics selected | Consent state | Decision owner/mode/CMP is recorded; defaults and updates precede tag behavior; accept/reject/change tests match it |
| T10 | Search Console selected | Property ownership | Correct Domain/URL-prefix scope is verified through a durable owner without replacing another token |
| T11 | Search Console selected | Submitted sitemap | The passing canonical sitemap is submitted/readable in the correct property |
| T12 | Bing selected | Site ownership | Exact canonical HTTPS site returns `IsVerified: true`; durable proof remains live without replacing another token |
| T13 | Bing selected | Submitted sitemap | `SubmitFeed` succeeds and `GetFeeds` lists the passing canonical sitemap without an explicit error |

Preview evidence alone is not production proof for a mutable GTM/Clarity setup.
When such a workspace is changed, its version must be published and the
cache-purged public site/network must match it. The GA presence check publishes
nothing.

## Gate B — source and runtime

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| B1 | Yes when PHP changed | PHP syntax | Every changed PHP file passes the target-compatible `php -l` |
| B2 | Yes when manifest changed | Manifest JSON | Parses; name/short name/start/scope/colors/icons are valid |
| B3 | Yes when assets changed | Asset dimensions | 16/32/180/192/512 and social-card dimensions match declared roles |
| B4 | Yes | SEO ownership | Exactly one active owner for metadata/base schema/sitemap |
| B5 | Yes when Rank Math owns output | Rank Math active | Official plugin active, checksum passes, wizard/registration state valid |
| B6 | Yes when Rank Math owns output | Module scope | Minimum relevant modules on; unjustified account/product modules off |
| B7 | Yes when WordPress/Rank Math owns output | Reproducible options | Idempotent project script runs successfully twice; same hashes reuse media and changed hashes receive new URLs |
| B8 | Yes on WordPress | Site Icon | `site_icon` points to a valid square ≥512px image attachment that is not WordPress/default artwork |
| B9 | Yes | Indexability intent | Platform indexability setting and environment intent agree |
| B10 | Yes | Architecture docs | Owner, config-script path, schema types, and sitemap policy are durable |
| B11 | Yes on WordPress full runs | Media alt inventory | Every image attachment was inspected; no unexplained blank, filename-only, meaningless, or wrong alt remains |
| B12 | Yes for WordPress alt repairs | Media mutation evidence | Changed attachment IDs, before/after alt, usage context, and rendered verification are logged; intentional blank IDs have reasons |

For plugin verification, capture version and run the relevant WP-CLI checksum
command. Never accept a plugin directory copied from an unknown source without
verification.

## Gate C — live HTTP and head

For the WordPress profile, run from the skill folder or project copy:

```bash
node scripts/validate-baseline.mjs https://example.com \
  --expect-schema=Organization,WebSite,WebPage \
  --expect-icon-sha256=<approved-icon-digests> \
  --expect-social-sha256=<approved-social-card-digest> \
  --json=.claude/evidence/norml-seo-basics/{run-id}/live-validation.json
```

Add visible conditional types, for example:

```bash
--expect-schema=Organization,WebSite,WebPage,Service,FAQPage
```

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| C1 | Yes | Homepage HTTP | Final response is 2xx HTML over HTTPS |
| C2 | Yes | Preferred host | Redirect final, canonical, OG URL, and sitemap origin agree |
| C3 | Yes | Header robots | No `X-Robots-Tag: noindex` on the public homepage |
| C4 | Yes | Title | Exactly one non-empty `<title>` |
| C5 | Yes | Description | Exactly one non-empty meta description |
| C6 | Yes | Robots meta | Exactly one and no `noindex`/`nofollow` for public launch |
| C7 | Yes | Canonical | Exactly one absolute HTTPS self-canonical |
| C8 | Yes | H1 | Exactly one visible page-primary H1 in server HTML/rendered page |
| C9 | Yes | Language/viewport | Valid `lang` and one responsive viewport meta |
| C10 | Yes | Open Graph | Exactly one type/site/title/description/url/image set; URLs valid |
| C11 | Yes | Twitter | One card plus explicit title/description/image; image valid |
| C12 | Yes | Duplicate protection | No second SEO owner emits equivalent tags or schema entities |

Title/description length guidance may produce a warning, not an automatic failure,
when the copy is accurate and intentional. Empty, generic, duplicated, or
unsupported-claim copy is a failure.

## Gate D — icon, manifest, and social assets

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| D0 | Yes | Approved identity | Rendered 16/32/180/512 pixels match a documented project identity source; no WordPress/core/host/theme placeholder or invented logo |
| D1 | Yes | Favicon links | At least one modern icon plus legacy coverage; URLs resolve |
| D2 | Yes | Apple icon | 180 × 180 image resolves with image MIME |
| D3 | Yes on WordPress | WordPress PNG icon | Generated Site Icon URLs resolve; attachment dimensions valid |
| D4 | Yes | Manifest | One manifest link returns parseable JSON with 192/512 icons |
| D5 | Yes | Manifest icons | Both icon URLs resolve with correct PNG MIME and declared sizes |
| D6 | Yes | OG/Twitter image | Absolute HTTPS URL returns 2xx image MIME, matches the approved source hash, and is 1200 × 630 unless a documented platform exception applies |
| D7 | Warning | Theme color | Theme/manifest colors intentionally match approved site palette |
| D8 | Yes for fixes | Source/live parity | At least one live favicon hash and the social-card hash match committed approved assets; changed bytes use fresh public URLs |
| D9 | Yes | Root favicon fallback | `/favicon.ico` returns 2xx non-empty `image/*` bytes, not HTML, and matches the approved icon family during a fix run |

An HTTP 200 serving HTML for an icon URL is a failure even if the browser appears
to show a cached favicon.

## Gate E — schema

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| E1 | Yes | JSON syntax | Every `application/ld+json` block parses |
| E2 | Yes | Base graph | Expected Organization-or-Person, WebSite, and WebPage types exist |
| E3 | Yes | Stable identity | Absolute canonical `@id` values; no duplicate IDs |
| E4 | Yes | Graph links | Publisher/site/page/provider references resolve coherently; logo links exist only for an approved logo asset; Site Icon bytes are rejected as an Organization logo unless explicit dual-role approval is documented and passed to the validator |
| E5 | Yes | Visible parity | Every conditional entity/property matches visible approved facts |
| E6 | Yes | No duplicates | Plugin and theme do not emit duplicate same-purpose entities |
| E7 | Yes if conditional type expected | Conditional schema | Expected Service/FAQ/Product/etc. type exists and is complete enough for its purpose |

Do not use a schema validator's green result to excuse false content. Syntax and
visible-fact parity are separate requirements.

## Gate F — sitemap and robots

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| F1 | Yes | Canonical index | Declared canonical sitemap index returns 2xx valid XML with ≥1 `<loc>` |
| F2 | Yes | Child maps | Every sampled/listed child tested returns 2xx valid XML |
| F3 | Yes | Sitemap policy | Only intentional indexable post types/taxonomies appear |
| F4 | Yes on WordPress | Core duplicate | `/wp-sitemap.xml` is disabled/redirected, or its deliberate ownership is documented instead of Rank Math |
| F5 | Yes | robots.txt | Returns successfully, no public `Disallow: /`, canonical `Sitemap:` line present |
| F6 | Yes | URL origin | Sitemap and robots URLs use the preferred HTTPS host |
| F7 | Search Console selected | Search Console state | Correct verified property accepts/reads the canonical sitemap; Security Issues and Manual Actions were reviewed |
| F8 | Bing selected | Bing Webmaster state | Exact verified site lists the canonical sitemap; current feed/diagnostic state was reviewed and recorded |

## Gate G — browser and regression

Use an isolated Playwright/browser context; never take over the user's current tab.

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| G1 | Yes | Desktop render | Intended homepage renders; no fatal/login/maintenance page |
| G2 | Yes | Mobile render | Intended homepage renders at 375px; no horizontal overflow |
| G3 | Yes | Console/page errors | No uncaught error caused by this change |
| G4 | Yes | Resource failures | No baseline icon/manifest/social/theme resource fails |
| G5 | Yes | Visible/schema parity | H1, service, offer, FAQ, person/entity facts agree with schema |
| G6 | Yes | Cache-purged repeat | Fresh context/source still returns the new canonical output |
| G7 | Yes when media is visible | Rendered image alt | Changed content-bearing attachments render the reviewed alt; intentional decorative images render empty alt |

## Gate H — final reconciliation

Compare the applicable states side by side:

1. intended baseline in `norml-seo-basics.md`;
2. immutable timestamped report and machine evidence;
3. source/config committed to Git;
4. platform/plugin/admin state;
5. cache-purged public response;
6. summarized Care cycle, when applicable.

They must agree on title, description, canonical, owner, identity, schema types,
sitemap policy, and asset URLs. If any layer differs, the task remains FAIL until
reconciled.

## Gate I — crawl and report

| ID | Required | Check | Pass condition |
|---|---:|---|---|
| I1 | Yes on full runs | 404 crawler identity | Exact canonical start/final host, Screaming Frog/equivalent version, licence/cap, timestamps, and URLs crawled are recorded |
| I2 | Yes on full runs | Crawl completeness | Crawl finished without cap/block/error; otherwise recipe is explicitly `BLOCKED`, never a partial pass |
| I3 | Yes when 4xx found | Candidate evidence | Every internal 4xx has response code, URL, source inlink(s) when available, and a separate live recheck |
| I4 | Yes | Immutable report | Timestamped full Markdown report exists in the project report folder and is readable after write |
| I5 | Yes | Current index | `.claude/docs/seo/norml-seo-basics.md` points to the immutable report instead of replacing its history |

The crawl and GA presence recipe are check-only. Their evidence cannot satisfy a
separate fix/change request, and no automated candidate becomes a confirmed issue
without review.

## Minimal final evidence

Record without secrets:

- checked URL and timestamp;
- validator PASS/WARN/FAIL counts and JSON artifact path;
- platform integration/plugin version and checksum result when applicable;
- Site Icon setting/attachment ID and public URL when applicable;
- WordPress Media Library image count, reviewed count, changed attachment IDs,
  and documented intentional decorative blanks when applicable;
- approved identity source plus favicon/social SHA-256 evidence and rendered
  16/32/180/512 proof;
- schema types and duplicate-ID count;
- sitemap index plus tested child count;
- 404 crawl version/cap/coverage, URL count, raw evidence path, internal 4xx
  count, and source-inlink table;
- robots sitemap line;
- Google Search Console and Bing property/site scope, ownership, and sitemap
  status when selected;
- desktop/mobile/browser result;
- immutable report path plus current-index pointer;
- backup path (write mode), commit, push, and deployed environment;
- remaining escalations with an owner, never a time estimate.
