# Authentication for native Google files

Reuse an authorized Google connector if it already supports the requested
native-file operations and exact identity. This package's Python examples use
the bundled `scripts/google_auth.py`; it needs Google API Python clients from
`requirements.txt` installed in an isolated virtualenv.

For the bundled gcloud route, the agent runs:

```sh
gcloud auth login user@example.com --enable-gdrive-access --no-activate
```

The user handles provider login/MFA/consent. No company domain is required and
ADC is not overwritten. This profile has broad Drive edit scope; Google offers
no no-delete edit scope, so operation safeguards remain necessary. Use a
read-only provider connector/scopes when only reading is needed. Do not expand
an existing grant silently. App policy/API enablement/file sharing remain
owner/admin actions, distinct from login. No service-account key is required.

Resolve `{skill-root}` to this package when using the recipe snippets. In Python:

```python
import sys
sys.path.insert(0, "{skill-root}/scripts")
from google_auth import load_credentials, verify_drive_identity
from googleapiclient.discovery import build
ACCOUNT = "user@example.com"  # explicitly chosen non-secret identity
creds = load_credentials(ACCOUNT)
drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
verify_drive_identity(drive, ACCOUNT)
sheets = build('sheets', 'v4', credentials=creds, cache_discovery=False)
docs = build('docs', 'v1', credentials=creds, cache_discovery=False)
```

gcloud stores refresh material; the helper captures short-lived tokens inside
the process. Never print tokens or read/copy OAuth databases. On an explicitly
selected existing ADC route use `mode='adc'` and verify the Drive identity
before operating. A correct Cloud login does not prove Workspace scopes.

Check exact file metadata with `supportsAllDrives=True`, expected native mime
type, `trashed=False` and `capabilities.canEdit` where writes are needed. A
read-only identity/resource check creates no files. Revoke or reconnect only
the selected account through the provider when authorized; preserve others.

Sources: [gcloud login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login),
[Drive authorization](https://developers.google.com/workspace/drive/api/guides/api-specific-auth).
