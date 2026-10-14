# Process — Analyze and fix

Use this process for an explicit setup, connect, configure, fix, repair, or
launch-implementation request. A read-only invocation never uses this mode.

## 1. Analyze and select first

Perform every read-only step in `processes/analyze-only.md` through evidence
reconciliation. Resolve the selected recipe graph and record the pre-change owner
for every output.

Routine fixes inside mutable selected recipes are authorized by the request. Do
not pause between indexability, metadata, sitemap, Search Console, GTM, consent,
favicon, social, schema, Rank Math, media-alt, and verification steps. Stop only
for `standards/hard-stops.md` or a business/legal/public-claim choice.

`google-analytics` and `404-issues` remain check-only in this mode. Record their
findings and route separately; never create analytics state or apply a redirect,
link edit, deletion, or restoration as an implicit continuation.

## 2. Create the rollback checkpoint

Before production mutation, capture the platform-appropriate equivalents of:

1. database/settings backup outside the public web root;
2. integration/plugin/theme/version inventory;
3. selected pre-change options, metadata, and tag-manager container version;
4. Git remote/branch/status when code exists;
5. rollback path/version in the platform activity log.

Never overwrite a previous checkpoint.

## 3. Fix ownership before implementation

Choose one owner for each output and remove/disable duplicates as an explicit
migration. In particular:

- the CMS/admin integration owns the GTM embed;
- the existing approved implementation preferably owns GA delivery through GTM,
  but this skill only audits GA; GTM owns Clarity delivery when selected;
- one mature SEO owner owns metadata/base schema/sitemap;
- the platform owns its Site Icon;
- approved project assets own favicon/social-image bytes.

On WordPress, never install Rank Math beside an established SEO plugin and never
put GTM/GA/Clarity in theme or repository code.

## 4. Execute recipes in dependency order

For each selected recipe:

1. re-check its inputs and hard stops;
2. apply its platform-specific procedure through the owning management skill;
3. verify the live result before starting a dependant;
4. record its owner, safe IDs, changed settings/code, rollback, and result.

Required order for current dependencies:

1. `indexability.md`;
2. `sitemap-and-robots.md`;
3. `google-search-console.md`;
4. `google-tag-manager.md`;
5. `consent-management.md` when selected by a dependant/applicability rule;
6. `microsoft-clarity.md` when selected;
7. `wp-rank-math.md` on WordPress when its applicability rule matches, so the
   metadata/schema owner exists before dependent settings are finalized;
8. independent metadata, Google Analytics presence, favicon, social, schema,
   404, and media-alt recipes.

If Rank Math will own social/schema output on a blank WordPress site, establish
that owner before finalizing the corresponding recipe settings, then verify the
recipes independently.

## 5. Complete inherited baseline work

Every full run executes the explicit indexability, metadata,
sitemap-and-robots, Search Console, Google Analytics presence, and bounded 404
recipes plus desktop/mobile rendering. The two check-only results remain
handoffs, not implicit fixes.

### WordPress additions

Through `supported WordPress REST API or WP-CLI` and `WordPress development workflow` as appropriate:

- install/repair the one SEO owner using `wp-rank-math.md` when applicable;
- use `templates/configure-rank-math.php` for reproducible project settings on a
  code-backed site;
- execute `wp-media-alt-text.md`: inspect every Media Library image plus real
  usage, repair only evidence-backed alt gaps, and document intentional blanks;
- configure Site Icon and media through WordPress rather than blind SQL;
- flush only relevant sitemap/rewrite/object/page/CDN caches;
- verify official plugin checksums after installation/update.

The Rank Math config script may store reproducible SEO settings. It must never
contain GTM, GA, or Clarity scripts/IDs.

## 6. Validate locally when code/assets changed

- syntax-check changed code and validate manifest JSON;
- inspect icon/social dimensions, MIME, hashes, and small-size rendering;
- run project build/tests;
- run the WordPress baseline validator locally when that profile applies;
- render desktop/mobile and capture console/page/resource failures.

Fix failures before deployment.

## 7. Commit, push, and deploy code atomically

1. Review `git status` and the targeted diff.
2. Stage only paths changed by this run.
3. Commit with a Conventional Commit whose body explains ownership.
4. Push the exact commit to the project-declared Git remote.
5. Deploy through `.claude/ci-cd.md`.

Production code may not precede Git. Admin-managed integration values are not
copied into theme code to create a commit; record them in project docs/activity
logs and preserve the admin system as owner.

## 8. Apply production platform settings

Use the verified management surface to install/activate integrations, save
options, import approved media, run idempotent configuration, and purge relevant
caches. Do not use an unapproved browser takeover when a supported API/CLI exists.

GTM workspace/tag publication is its own production mutation when a mutable GTM
or Clarity recipe requires it: use Preview first, publish a named version, and
retain the prior version for rollback. The Google Analytics presence recipe
never publishes.

## 9. Run production acceptance

Execute every applicable check in `qa/acceptance-contract.md` and each selected
recipe. Inspect source and network counts directly. One visually correct result is
not enough when two systems emit it.

On WordPress, run `scripts/validate-baseline.mjs` with expected schema and approved
asset hashes. Then run the recipe-specific GTM/GA/Clarity browser/network checks.

Any required failure keeps the task in progress. Repair and rerun rather than
reporting completion with a caveat.

## 10. Persist and hand off

Update:

- a new immutable timestamped report in the project-folder report path;
- `{project}/.claude/docs/seo/norml-seo-basics.md` as the latest-state index/summary;
- platform-management activity log and durable project notes;
- application/theme architecture docs declaring owners;
- code changelog when code changed.

Record exact integration/plugin versions, safe IDs, live URLs, selected recipes,
schema types, sitemap policy, config paths, backup/rollback, GTM versions,
commit/deploy results, QA summary, and open blocks. Never store secrets or broad
sensitive option dumps.

Do not present the implementation report as independent post-change evidence.
When a service workflow requires independent verification, its owning skill must
invoke a separate Analyze-only run after production verification.
