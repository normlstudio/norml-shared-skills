# Database recipes — index

Four strategies. Each per-project `.claude/ci-cd.md` declares **exactly one** as `database:`.

## How to use

When promoting code or content between environments, look up the project's declared database strategy and follow the steps in `database/{slug}.md`.

## Index

| Strategy | File | One-line | When |
|---|---|---|---|
| `single-env` | [database/single-env.md](database/single-env.md) | One authoritative DB, no sync — edit on prod with backup-before | All `prod-only-*` patterns plus `local-github-prod` and `direct-prod`. |
| `staging-to-prod-full` | [database/staging-to-prod-full.md](database/staging-to-prod-full.md) | Full DB sync at launch (`wp db export` + `wp search-replace` + import) | Initial site launch from staging, OR rare full re-syncs. |
| `staging-to-prod-selective` | [database/staging-to-prod-selective.md](database/staging-to-prod-selective.md) | Only certain post types / options sync from staging | Ongoing dev — sync specific changes without clobbering prod content. |
| `content-via-wp-admin-only` | [database/content-via-wp-admin-only.md](database/content-via-wp-admin-only.md) | Content team manages DB via WP admin; devs don't touch it | Mature sites where content is owned by editors / SEO team. |

## How to pick

- **One authoritative DB (prod-only, local-github-prod, or direct-prod):** `single-env` is the only option
- **Two envs (staging + prod), first time shipping:** `staging-to-prod-full`
- **Two envs, ongoing dev with live prod content:** `staging-to-prod-selective`
- **Two envs, mature site, content owned by editors:** `content-via-wp-admin-only` (devs stay out of DB)

The dangerous combination to avoid: `staging-to-prod-full` on a live site after launch. That clobbers all prod content (posts, comments, settings) with whatever's on staging. Only use full sync at first launch.
