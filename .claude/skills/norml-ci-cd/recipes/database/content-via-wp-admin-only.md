# Database strategy: `content-via-wp-admin-only`

> The content team (editors / SEO / clients) owns the database via WP admin. Devs do NOT touch the DB during normal work. Staging exists for code, but content lives only on production.

## When this applies

- Mature site with active editorial team (an editorial team publishing weekly, or a client editor)
- Production DB has thousands of posts / pages / form submissions / users
- Risk of dev-side DB sync clobbering editorial work is unacceptable
- Patterns: `local-github-staging-prod` (the most common pairing for mature sites)

## The principle

**Devs ship code. Editors ship content.** The two never mix. Staging is for code preview only; staging DB is a stale copy of prod for testing the code, not a source of truth.

## Devs do

- Push code (theme, plugins, ACF JSON schema) to staging via the normal pipeline
- Verify code works on staging using staging's stale DB copy
- Promote code to production via the normal pipeline (file deploy only — NO DB sync)
- Never `wp db import` or `wp db sync` on production

## Devs do NOT

- Run `wp post create` on prod (use the editor's WP admin or REST API via `the editorial publishing workflow` instead)
- Run `wp option update` on prod for anything content-shaped (titles, descriptions, ACF VALUES on existing fields)
- Run `wp search-replace` on prod without explicit human approval (and only for genuine URL migrations)
- Import a staging DB dump to prod

## Editors do

- Publish, edit, schedule posts via WP admin
- Update ACF field VALUES via WP admin
- Manage media library
- Adjust per-post SEO meta (RankMath)
- Reply to comments / moderate
- Manage forms (Gravity Forms, Contact Form 7, etc.)

## How code-side changes that NEED content updates work

If a code change requires NEW content on prod (e.g., a new CPT is added that needs sample posts):

1. Deploy the code (registers the CPT)
2. **Tell the editor** what's now possible and let them add content via WP admin
3. Do NOT bulk-create the content via `wp post create` on prod — that bypasses the editor's workflow and audit trail
4. If the editor wants automation help, they can use the authorized content workflow (which is content-side, not dev-side) to bulk-create via REST

## How ACF schema changes ship

This is the cleanest pattern with this strategy:

1. Dev edits ACF field group in `acf-json/` (locally)
2. Commit + push + deploy to staging
3. ACF on staging detects new JSON → editor reviews on staging
4. Deploy to prod
5. ACF on prod detects new JSON → editor reviews on prod and clicks "Sync"
6. New fields are now available, editors fill in VALUES via WP admin

No DB sync. Schema flows through code; values come from editors.

## How staging DB stays useful for code testing

Periodically (monthly / quarterly), refresh staging DB from a recent prod backup:

Use the verified export/transfer/import process in the project contract. Export rewriting
leaves production unchanged; never issue a broad remote wildcard transfer or rely on a
local `scp` invocation with two assumed remote endpoints. Disable staging side effects
before import, preserve production GUIDs and verify staging URLs/isolation afterward.

This is `staging-to-prod-full` in reverse — and it's the ONLY direction this strategy allows for full DB sync.

## Gotchas

- **The temptation to "just run one wp command on prod" is strong.** Resist. Even one-off devs commands on prod undermine the editor's trust.
- **Staging DB drift** — if it's been months since refresh, staging tests have stopped reflecting prod reality. Schedule refreshes.
- **Editors don't always announce changes.** A new plugin they activated, a setting they tweaked — invisible to dev until something breaks. Maintain a `## Editor changes since last sync` section in the project's `.claude/changelog/daily.md` and check it periodically.
- **REST API writes via the authorized content workflow are OK** when explicitly delegated — they're content-side, not dev-side. The distinction is who's running them.

## Migration path

This strategy is the maturity endpoint. Sites move TO this from `staging-to-prod-selective` as content ownership transfers to the editorial team. They rarely move away.

If the project is being decommissioned or rebuilt, the strategy may temporarily shift back to `staging-to-prod-full` for a full re-import — that's a planned transition, not a regression.

## When to refuse

- If anyone asks you to run a destructive `wp` command on prod under this strategy → refuse, point at this doc, escalate to the editor team owner

