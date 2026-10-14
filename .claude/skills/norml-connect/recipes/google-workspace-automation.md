# Connect Google Workspace automation

## 1. What and why

Read and edit native Drive/Sheets/Docs as your chosen Google identity. No
company domain, Drive mount, specific folder or service-account key is required.

## 2. Who needs it

Anyone whose authorized workflow operates live native Google files.

## 3. Prerequisites

Google Cloud CLI, Python 3.10+, access to the exact existing target files and
permission to authorize Google Cloud SDK. Choose Viewer for reading and Editor
only when writes are required. Resolve file IDs from native URLs or .gdoc/.gsheet
pointer JSON; do not ask the user to export documents.

## 4. Setup

Reuse a verified connector or an existing authorized gcloud account. Otherwise
the agent launches the provider-owned flow, leaving login/MFA/consent to the user:

```sh
gcloud auth login user@example.com --enable-gdrive-access --no-activate
```

This does not update ADC or change the globally active account. If scope
verification fails, explain the required Drive consent and reauthorize that
same account with `--force`; do not force fresh login unnecessarily.

Resolve `{skill-root}` to this installed package. Create an isolated virtualenv
outside source/synced folders and install `requirements.txt` into it. Use that
interpreter for the verifier and API work. Do not use system-pip override flags.

```sh
python3 -m venv "$HOME/.local/share/google-workspace-tools/venv"
"$HOME/.local/share/google-workspace-tools/venv/bin/python" -m pip install -r "{skill-root}/requirements.txt"
"$HOME/.local/share/google-workspace-tools/venv/bin/python" "{skill-root}/scripts/verify-google.py" \
  --account user@example.com --sheet-id '<sheet-id>' --doc-id '<doc-id>'
```

Use `--require-edit` only for workflows needing Editor. Verification reads both
files without modifying them. It takes explicit IDs to avoid inventorying other
people's documents. If the workflow needs only one service, verify that target
through its connected API; the helper's two-file check is for joint Workspace setup.

## 5. Secret storage

gcloud owns OAuth storage. Never read/copy its credential files or run the
token-print command interactively. The bundled loader captures short-lived
tokens inside the process. No custom credential schema is required.

## 6. Verification

Drive-reported email must match the exact chosen account; the native Sheet and
Doc reads must succeed. Record `can_edit` separately. Token existence, a browser
login and file visibility are weaker evidence than successful target reads.

## 7. Obstacles and fixes

- Wrong identity: stop reads and reconnect the explicitly selected account.
- Insufficient scopes: repeat only that account's Drive consent with `--force`.
- 403/404: verify target IDs, permissions and API enablement; do not borrow another account.
- API/quota error: add `--quota-project` only if the observed error requires it;
  the account needs the relevant service-usage permission there.
- Managed Python: use the virtualenv, never `--break-system-packages`.
- Organization blocks the app: seek narrow admin approval; do not bypass policy.

## 8. Administrator bootstrap

Only the target owner/admin grants file access or approves the OAuth app/API
policy. The agent uses existing supported access to prepare an exact requested
change. This package does not fabricate an OAuth-client provisioning API or
share a company folder automatically. Headless work should use the provider's
supported keyless/workload route; DWD is elevated, admin-scoped and not a laptop
default. No DWD key distribution is included.

## 9. Escalation

Report expected account, target ID, operation, sanitized status and failed
verification stage. Never send tokens, authorization codes or credential files.

Sources: [gcloud login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login),
[Sheets scopes](https://developers.google.com/workspace/sheets/api/scopes),
[Docs authorization](https://developers.google.com/workspace/docs/api/auth).
