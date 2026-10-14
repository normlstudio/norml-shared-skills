# Native Google Docs operations

Read [authentication](../standards/authentication.md) first. Exact live document
IDs are canonical. No private business client or sibling skill is needed.

## Connect and verify the account

Resolve `{skill-root}` to this installed package and use the chosen account:

```python
import sys
sys.path.insert(0, "{skill-root}/scripts")
from google_auth import load_credentials, verify_drive_identity
from googleapiclient.discovery import build
from doc_builder import DocBuilder
from doc_ops import select_tab, tab_end, inserted_table, fill_table_requests, update
ACCOUNT = "user@example.com"
creds = load_credentials(ACCOUNT)
drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
docs = build('docs', 'v1', credentials=creds, cache_discovery=False)
verify_drive_identity(drive, ACCOUNT)
```

Before writes, read exact Drive file metadata with `supportsAllDrives=True`.
Require native document mime type, `trashed=False`, and `capabilities.canEdit`.
Reading a Doc is not proof of Editor permission. Never choose the first
same-name folder/document; use an exact ID or disambiguate its parent and intent.

## Create a document in the requested folder

Verify destination identity and creation authority. `documents.create` creates
in My Drive; move the new file using its actual parent IDs:

```python
created = docs.documents().create(body={'title': 'Project checklist'}).execute()
DOC_ID = created['documentId']
parents = drive.files().get(fileId=DOC_ID, fields='parents').execute().get('parents', [])
drive.files().update(fileId=DOC_ID, addParents=DEST_FOLDER_ID,
                     removeParents=','.join(parents), supportsAllDrives=True,
                     fields='id,parents').execute()
```

Verify returned parents. If moving fails, retain/report the new ID; do not
silently delete it or create a second copy. Shared-drive policy can impose
additional restrictions. Native URL: `https://docs.google.com/document/d/{id}/edit`.

## Read all tabs and choose an exact target

```python
state = docs.documents().get(documentId=DOC_ID, includeTabsContent=True).execute()
tab = select_tab(state, tab_id=TAB_ID)
REVISION = state['revisionId']
end_index = tab_end(tab)
```

Tabs nest under `childTabs`; the selector traverses them all. Title selection
must be unique, optionally scoped to an exact parent ID. Duplicate titles stop
rather than selecting the first. Request `includeTabsContent=True` even for a
single default tab. A missing top-level body does not mean the document is empty.

## Build text, headings, bullets and links

Indices count UTF-16 code units, not Python characters or bytes. Body begins
at index 1; emoji/non-BMP characters need two units. The bundled builder uses
UTF-16 lengths and stamps the selected tab into every location/range.

```python
b = DocBuilder(start=end_index, tab_id=TAB_ID)
b.heading('Project setup\n', level=2)
b.text('Read the project guide. ')
a, z = b.text('Documentation')
b.text(' contains the checklist.\n')
b.link(a, z, 'https://example.com/docs')
update(docs, DOC_ID, REVISION, b.reqs, authorized=True)
```

Use TITLE, SUBTITLE, HEADING_1..HEADING_6 or NORMAL_TEXT paragraph styles.
Restore NORMAL_TEXT on newly inserted plain paragraphs near existing headings;
otherwise inherited heading style can leak. The builder restores it by default.
To create bullets, insert complete newline-terminated items, then append a
`createParagraphBullets` request with their startIndex/endIndex/tabId and
`bulletPreset='BULLET_DISC_CIRCLE_SQUARE'` before applying the same plan.
Append-in-order preserves earlier indices within a batch. Fixed-index insertion
requires reverse order. Do not mix these strategies.

## Revision control and concurrency

The helper sends `writeControl.requiredRevisionId` from the exact read used to
build the plan. A concurrent edit rejects the stale write. Re-read and re-plan;
do not attach a newer revision to old index calculations. Each stage of a
multi-stage operation reads new state/revision after the prior stage. Record
created file/tab IDs so recovery reconciles rather than duplicates them.

## Insert and fill the newly inserted table

Read exact tab/revision, insert at its derived end, then re-read cell indices.
Locate the new table by selected tab, insertion position and dimensions. Never
select the document's first table merely because it has the right dimensions.

```python
state = docs.documents().get(documentId=DOC_ID, includeTabsContent=True).execute()
tab = select_tab(state, tab_id=TAB_ID)
insertion_index = tab_end(tab)
requests = [{'insertTable': {
    'location': {'index': insertion_index, 'tabId': TAB_ID},
    'rows': 3, 'columns': 2}}]
update(docs, DOC_ID, state['revisionId'], requests, authorized=True)
state = docs.documents().get(documentId=DOC_ID, includeTabsContent=True).execute()
tab = select_tab(state, tab_id=TAB_ID)
table = inserted_table(tab, insertion_index, 3, 2)
rows = [['Step', 'Status'], ['Setup', 'Pending'], ['Review', 'Pending']]
requests = fill_table_requests(table, rows, TAB_ID)
update(docs, DOC_ID, state['revisionId'], requests, authorized=True)
```

Docs inserts a newline before the table. The locator accepts the insertion
index or its immediate next index and fails on ambiguity. Cell starts come
from fresh returned structure, not arithmetic. Filling proceeds bottom-right
to top-left so earlier cell indices stay stable. Verify the exact table afterward.

## Tab structure

Check current discovery schema for supported tab requests before use. Capture
new IDs from replies and create in the intended order where possible:

```python
state = docs.documents().get(documentId=DOC_ID, includeTabsContent=True).execute()
reply = update(docs, DOC_ID, state['revisionId'], [{'addDocumentTab': {
    'tabProperties': {'title': 'Setup', 'index': 1}}}], authorized=True)
new_tab_id = reply['replies'][0]['addDocumentTab']['tabProperties']['tabId']
```

Use exact IDs and narrow field masks for updateDocumentTabProperties. Read back
parent/sibling order; HTTP 200 is insufficient evidence of a move. Older source
tests observed pre-removal move indices and default-tab nesting restrictions.
Verify those quirks against the current API; do not blindly add 1 to all moves
or detach unrelated tabs. Deleting a tab also deletes children.

## Replacement, removal and recovery

Replacing text with deleteContentRange affects existing content. Resolve exact
revision/tab/UTF-16 range, verify the user's specific authorization and preserve
rollback evidence. Trashing/deleting tabs/ranges and other destructive requests
follow SKILL.md's boundary. Never permanently delete a file or empty Trash.
A copied Doc preserves content but not its comment threads.
If a request times out, read current state before retrying: a create/delete may
have applied. Never replay uncertain mutations or bypass revision checks.

## Read-back

Read includeTabsContent=True and traverse paragraphs, tables and nested tabs.
Verify text, named styles, links, table cells, tab order and the exact affected
IDs. Permission/revision checks do not replace verifying the actual result.

Sources: [batch updates](https://developers.google.com/workspace/docs/api/how-tos/batch-update),
[write control](https://developers.google.com/workspace/docs/api/reference/rest/v1/documents/batchUpdate),
[document tabs](https://developers.google.com/workspace/docs/api/how-tos/tabs),
[tables](https://developers.google.com/workspace/docs/api/how-tos/tables).
