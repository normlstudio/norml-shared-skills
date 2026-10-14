# Norml Shared Skills

Sixteen standalone development, SEO and workflow skills from Norml Studio.
Every package uses a `norml-` name and includes runtime instructions, supporting
procedures, a Markdown guide and a rendered visual guide. No private ecosystem
installation is required.

## Install

Start in the project where you want the skills. With Node 22 or newer, choose
one runtime:

```sh
npx skills@latest add normlstudio/norml-shared-skills --agent claude-code --skill '*' --copy --yes
```

```sh
npx skills@latest add normlstudio/norml-shared-skills --agent codex --skill '*' --copy --yes
```

To select one skill, replace `'*'` with its name, for example
`norml-wp-architecture`. These commands are project-local; global installation
requires adding `--global`. Review existing same-name packages before using
third-party installers that may replace them. This collection's own installer
refuses collisions.

From a downloaded ZIP or clone, Python 3.10+ provides an alternative:

```sh
python3 scripts/install.py --destination /path/to/project/.claude/skills
```

Or choose specific packages with repeated `--skill` flags:

```sh
python3 scripts/install.py --destination /path/to/project/.claude/skills \
  --skill norml-ci-cd --skill norml-wp-architecture
```

Choose the runtime's supported project skill directory as destination. The
manual installer copies complete folders, rejects source/destination symlinks
and preflights existing packages. It installs no dependencies, credentials,
MCP servers or hooks. Reload/start an agent session after installation.

## Included skills

| Source capability | Public package | Purpose |
|---|---|---|
| Dev CI/CD | [norml-ci-cd](.claude/skills/norml-ci-cd/readme.md) | Deployment, database and recovery contracts |
| Dev page structures | [norml-page-structures](.claude/skills/norml-page-structures/readme.md) | Bundled page/block catalog |
| Dev page types | [norml-page-types](.claude/skills/norml-page-types/readme.md) | Page families and eligible intersections |
| Dev performance audit | [norml-performance-audit](.claude/skills/norml-performance-audit/readme.md) | Measured performance diagnosis |
| Dev WP architecture | [norml-wp-architecture](.claude/skills/norml-wp-architecture/readme.md) | WordPress data models and templates |
| Dev WP developer | [norml-wp-developer](.claude/skills/norml-wp-developer/readme.md) | Sage and inherited-theme workflows |
| SEO basics | [norml-seo-basics](.claude/skills/norml-seo-basics/readme.md) | Fifteen baseline SEO recipes |
| SEO schema | [norml-seo-schema](.claude/skills/norml-seo-schema/readme.md) | JSON-LD and WordPress schema mapping |
| SEO technical analysis | [norml-seo-technical-analysis](.claude/skills/norml-seo-technical-analysis/readme.md) | Eight-area evidence-based audit |
| Dev changelog | [norml-changelog](.claude/skills/norml-changelog/readme.md) | Durable decisions and change history |
| Norml Connect | [norml-connect](.claude/skills/norml-connect/readme.md) | Provider setup and exact-target verification |
| Norml Drive | [norml-drive](.claude/skills/norml-drive/readme.md) | Live Google Sheets/Docs operations |
| Norml Git | [norml-git](.claude/skills/norml-git/readme.md) | Git, shared claims and worktree preservation |
| Norml Security | [norml-security](.claude/skills/norml-security/readme.md) | Protected storage and local leak checks |
| Norml Tasks | [norml-tasks](.claude/skills/norml-tasks/readme.md) | Local planning and optional issue mirroring |
| Norml Skill Creator | [norml-skill-creator](.claude/skills/norml-skill-creator/readme.md) | Portable creation and migration workflows |

## First use

Name the exact project, account/resource and requested result. Read project
instructions before implementation. SKILL.md selects that package's procedures;
readme.md is the human reference and readme.html is the visual guide. Optional
bundled handoffs do not require private sibling skills.

Examples:

- Use norml-wp-architecture to review this repository's data model.
- Use norml-seo-basics to run an analyze-only baseline for this site.
- Use norml-tasks to organize this backlog without issue mirroring.
- Use norml-connect to verify my Google account against these native file IDs.

## Public boundary

There is no company Drive root, internal credential registry, client/account
data, production secret, compulsory normlstudio hosting or whole-tree
publish policy. Your own project conventions and approval rules govern use.
Reusable catalogs/templates are bundled. Private screenshots, local caches,
source classification ledgers and auth state are excluded.

Secrets belong in the OS/provider protected store. Authentication does not
authorize messages, campaigns, DNS changes, purchases or production deployment.
Destructive work requires exact-target authority and recovery. Native Google
files stay live-ID based, with no stale Office-file fallback.

## Validate

```sh
python3 scripts/validate.py
python3 -m unittest discover -s qa
```

Validation checks all sixteen identities, required docs, links, Python syntax
and private/secret boundaries. Fixtures cover install collisions/symlinks,
remote-claim concurrency, planning, private security backups, exact Google
identity, typed snapshots and revision-protected document edits. Visual guides
were checked at desktop/mobile widths.

Installation is checked in disposable projects for Claude Code and Codex.
That verifies delivered files/supporting material; it does not prove every
workflow ran end-to-end inside each runtime. No recipient account, production
site/deploy or paid provider operation was exercised. Verify provider access
and current requirements at first use.

## Inside the collection

```text
.claude/skills/<norml-name>/
  SKILL.md                 runtime router
  recipes/, standards/     operating procedures and contracts
  templates/, scripts/     helpers where applicable
  qa/                      local checks where applicable
  readme.md                human reference
  readme.data.json          visual-guide data
  readme.html               generated visual guide
  changelog.md             public history
  LICENSE                  portable license attribution
scripts/install.py         collision-safe manual installation
scripts/validate.py        collection validation
```

Version: 1.0.0. License: [MIT](LICENSE).
Source: [normlstudio/norml-shared-skills](https://github.com/normlstudio/norml-shared-skills).
