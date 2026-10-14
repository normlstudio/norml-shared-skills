# Connect: Google Apps Script (read-only)

## 1. What & why

Connect an explicitly authorized Google identity to inspect Apps Script source,
versions, and deployments through Google's `clasp` CLI. Connection does not
authorize source changes, script execution, trigger changes, or deployment.

## 2. Who needs it

Developers investigating an existing Apps Script project.

## 3. Prerequisites

Node.js 20 or newer, the exact script ID, and an authorized Google identity
with access to that script. The user completes Google login/MFA/consent.

## 4. Self-serve setup

Create a separate temporary audit directory, never inside the live source
checkout. Add `.clasp.json` containing the exact `scriptId` and `rootDir: "."`.
Add an `appsscript.json` containing only this audit's consent scopes:

```json
{
  "timeZone": "Etc/UTC",
  "runtimeVersion": "V8",
  "oauthScopes": [
    "https://www.googleapis.com/auth/script.projects.readonly",
    "https://www.googleapis.com/auth/script.deployments.readonly",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
  ]
}
```

From that directory, start Google's loopback authorization flow:

```bash
npx --yes @google/clasp@3.4.1 --user '{unique-audit-profile}' login --use-project-scopes
```

The user selects the explicitly requested identity. Do not add
`--include-clasp-scopes`: default clasp scopes include writes. This temporary
manifest is a consent request, not the production manifest; never push it.
Preserve existing named profiles and never change the default profile.

## 5. Where the secret goes

This recipe explicitly delegates OAuth to the Google-maintained clasp CLI,
using provider-managed protected OAuth storage.
Clasp owns its default `~/.clasprc.json` store. Agents must never read, parse,
copy, sync, or hand-edit it. Use only clasp login/use/logout commands; never
use a custom `--auth` file. Keep permissions owner-only. Store non-secret
profile, account, script ID, and verification metadata in private local notes outside Git/synced storage.

## 6. Verify

Require the login output to identify the expected email, then from the isolated
audit directory run:

```bash
npx --yes @google/clasp@3.4.1 --user '{unique-audit-profile}' list-deployments
npx --yes @google/clasp@3.4.1 --user '{unique-audit-profile}' pull
```

Connected means the expected identity plus successful exact-target API reads.
Pull writes only the isolated local snapshot; do not overwrite a working tree.
Inspect snapshot content for embedded secrets before displaying or sharing it.

## 7. Obstacles & fixes

**Google returns a generic 400 during consent, then "This app is blocked" →
OAuth authorization has not completed; this does not establish missing access
to the script → Stop login retries. Have the authorized Workspace administrator
inspect the exact OAuth client under Security → Access and data control → API
controls → Manage third-party app access. A screenshot alone cannot distinguish
Workspace policy, account protection, or Google's OAuth-client restrictions.
Do not broadly trust all apps, disable protection, or claim that changing the
Apps Script API switch fixes a pre-consent block. Review narrow app/scope access
before any policy change.**

**Wrong identity in login output → Google selected another session → Stop target
reads, log out only this named profile, and repeat consent with the correct user.**

**Apps Script API disabled for the user → Dashboard API-access switch is off →
Ask the user to enable it at `https://script.google.com/home/usersettings`, then
retry. Do not change the switch through browser automation.**

**403/404 for the exact script → Authentication is not project authorization →
Verify the script ID and ask its owner for the narrow access needed.**

**OAuth blocked by Workspace policy → Third-party app access is restricted →
Escalate to the Workspace admin; never bypass the policy.**

## 8. Admin-only bootstrap

Only the owner/admin grants project access or approves clasp under Workspace
app-access policy. Do not grant broad Cloud IAM or create a service-account key
to bypass missing script access. Clasp is Google-maintained but its repository
states it is not an officially supported Google product.

## 9. Escalation

Report sanitized error, expected identity, exact target, and requested read-only
scopes. Never share tokens, callback codes, or credential files. Revoke through
Google Account permissions or the named clasp profile's logout command when
authorized; never log out unrelated accounts.

Sources: [clasp](https://github.com/google/clasp),
[source read scopes](https://developers.google.com/apps-script/api/reference/rest/v1/projects/getContent),
[deployment read scopes](https://developers.google.com/apps-script/api/reference/rest/v1/projects.deployments/list).


This route is source-reviewed; recipient login and exact script reads remain unverified until run.
