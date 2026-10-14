# Access and safety

No private credentials registry or extra skill is required.

## Resolve the exact target

Identify canonical hostname, CMS/account, environment, deployment source and
current integration owners. Compare public redirects/settings/DNS with authorized
platform access. Never guess a document root or add another property due to missing
access. Record supported capabilities in the project evidence, with no secrets.

## Connect securely

1. Reuse existing provider-supported OAuth sessions, CLIs or connected APIs.
2. Request only required resource access and scopes. Let the user complete unavoidable
   login, MFA and consent; do not request secrets in chat.
3. Store secrets in provider-managed credential storage or macOS operating-system protected credential store,
   Windows Credential Manager, or a Linux Secret Service compatible keyring.
4. Keep secrets out of prompts, source, reports, command arguments/history and logs.
   Retrieve them only into process memory when an API needs one.
5. Prefer supported API/CLI operations. Browser inspection may be used for public
   rendering; operating a provider UI requires explicit authorization and no available
   purpose-built route. An unavailable API is not permission for browser takeover.

## Service routes

- Google Search Console: use Search Console API for authorized properties/sitemaps;
  use Google's supported site-verification flow or existing verified owner for proof.
  DNS writes require the exact authoritative zone/account and preserve existing tokens.
- Tag Manager: use its API/approved connector for workspaces, tags and versions.
  Inventory existing container first. Publish only selected authorized setup changes;
  a GA presence audit never publishes or provisions analytics.
- Bing Webmaster Tools: use the documented user-scoped API key/OAuth route available
  for the account and current supported JSON API. Key-bearing URLs stay in memory
  or stdin transport; record sanitized site/verification/feed status only.
- WordPress: REST API for exposed content/media/options; WP-CLI over existing
  authorized SSH for supported operations the REST API cannot perform. Confirm
  exact wp path with read-only evidence. Use the real platform owner for GTM IDs.

## Mutation and rollback

Analyze only changes no target/provider state. Analyze and fix applies only selected
mutable recipes after backup and ownership review. Keep one owner per output and
one dated rollback point. Commit/push production code through the user's deployment
workflow, staging only this task's changes. GA and 404 discovery remain check-only.
Missing permission or a failed dependency blocks that operation, not independent work.
