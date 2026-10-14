# Google Sheets operations

Read [authentication](../standards/authentication.md) first. In examples,
`ACCOUNT` is the explicit chosen account and `CACHE_DIR` is a restricted local
cache folder outside the repository and synced storage. Refresh before writes;
never treat a cache as canonical. Before any destructive request, follow
the approval boundary in SKILL.md. A single batch is not a cross-API transaction.

## Pull full state into a private cache

```python
import json, pathlib, sys
sys.path.insert(0, "{skill-root}/scripts")
from google_auth import load_credentials
from googleapiclient.discovery import build
from sheets import pull, apply_requests

creds = load_credentials(ACCOUNT)
sheets = build('sheets', 'v4', credentials=creds, cache_discovery=False)
drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
cache = pull(sheets, drive, ACCOUNT, SID)
cache_dir = pathlib.Path(CACHE_DIR)
cache_dir.mkdir(parents=True, exist_ok=True)
cache_dir.chmod(0o700)
cache_path = cache_dir / (SID + '.json')
cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
cache_path.chmod(0o600)
```

The bundled helper verifies identity/native type and reads every GridData block,
including row/column offsets. It retains typed values, formulas and protected
ranges. Snapshot extraction is schema-versioned. Reject a snapshot taken while
the file was changing. The live API file remains canonical.

## Find a Table by name (NEVER hardcode ranges)

Spreadsheets grow over time as tasks get added, and layouts differ per project. **Never hardcode row positions** in code or formulas. Find Tables by name and use their current `range` from the API; in formulas, always use structured refs (`Invoices[Amount]`).

```python
def find_table(svc, spreadsheet_id, sheet_title, table_name):
    ss = svc.spreadsheets().get(
        spreadsheetId=spreadsheet_id,
        fields='sheets(properties(title),tables)',
    ).execute()
    for sh in ss['sheets']:
        if sh['properties']['title'] == sheet_title:
            for t in sh.get('tables', []):
                if t.get('name') == table_name:
                    return t  # has tableId, range, rowsProperties, columnProperties
    return None

# Use:
table = find_table(svc, SID, 'Dashboard', 'Invoices')
r = table['range']
header_row_1idx = r['startRowIndex'] + 1
footer_row_1idx = r['endRowIndex']  # endRowIndex is exclusive
body_first_1idx = r['startRowIndex'] + 2  # skip header
body_last_1idx  = r['endRowIndex'] - 1    # exclude footer
```

In formulas — always:
```
✓ =SUMIFS(Invoices[Amount], Invoices[Status], "paid")
✗ =SUMIFS(J119:J124, H119:H124, "paid")
```

When placing a NEW Table, anchor relative to an existing Table's footer:
```python
parent = find_table(svc, SID, 'Dashboard', 'Dashboard workload')
new_start_row = parent['range']['endRowIndex'] + 2  # 1 blank gap then start
```

## Inspect — read cache + answer a question

```python
import json, pathlib, re

def load_cache(spreadsheet_id):
    p = pathlib.Path(CACHE_DIR) / f'{spreadsheet_id}.json'
    if not p.exists():
        raise FileNotFoundError(f'No cache for {spreadsheet_id}. Run pull first.')
    return json.loads(p.read_text())

def find_rows_by_member(cache, tab_title, member_name, member_col='C'):
    tab = next(t for t in cache['tabs'] if t['title'] == tab_title)
    rows = []
    for cell, value in tab['cells'].items():
        if re.fullmatch(re.escape(member_col) + r'\d+', cell) and value.get('display') == member_name:
            row_num = int(cell[len(member_col):])
            task_cell = f'D{row_num}'
            rows.append({'row': row_num, 'task': tab['cells'].get(task_cell, {}).get('display', '')})
    return rows
```

## Two formula-write paths — pick the right one

The Sheets API has two ways to write formulas, with different parsers:

1. **`spreadsheets.batchUpdate` → `updateCells` → `userEnteredValue.formulaValue`** — strict protobuf parser. **Rejects structured table references** (e.g. `Table_Name[Column]`) with `Formula parse error`, even though the same formula works in the UI. Fine for plain SUMIFS / cell-range formulas.

2. **`spreadsheets.values.update` (or `batchUpdate`) with `valueInputOption='USER_ENTERED'`** — UI-equivalent parser. **Accepts structured table refs**, named ranges, and everything else Sheets supports.

**Rule of thumb:** if your formula uses anything beyond plain `'Sheet'!A1:A10` references — structured table refs, named ranges, certain newer functions — use the `values` endpoint with `USER_ENTERED`. For pure cell-range formulas, either path works.

The downside of `values.update`: you can't bundle it with format/structure changes in a single transaction the way `batchUpdate` can. So the typical pattern is:
1. `batchUpdate` for structural changes (insert/delete rows, formatting, copyPaste)
2. `values.update` (USER_ENTERED) for cell values + formulas with structured refs

## Apply the authorized plan

```python
# These booleans reflect actual user authorization for exact reviewed targets;
# never infer destructive authorization merely from a generic cleanup request.
reply = apply_requests(sheets, drive, ACCOUNT, SID, cache, requests,
                       authorized=True, allow_destructive=False)
cache = pull(sheets, drive, ACCOUNT, SID)
```

The helper checks account, native type, Editor capability, snapshot target and
live modifiedTime immediately before batching. A stale snapshot stops the write.
This guard is not a server-side atomic lock: Sheets lacks compare-and-swap across
these calls. A request that clears/overwrites existing values also needs explicit
review even if its operation name is not a `delete*` request. Use bounded fields
and exact ranges. Protected ranges require respect for the user's intended
ownership, not just API permission.

For a separate `values.update` formula write, repeat the same live identity,
capability and freshness checks against a newly pulled baseline. Read back
formula and effective value. Do not claim two separate endpoints are one transaction.

## Row-find by content

When row numbers shift because of inserts/deletes, always re-find by content (member + task) rather than hardcoding:

```python
def find_row(tab_cells, member_col, member_value, task_col, task_value):
    for cell, val in tab_cells.items():
        if re.fullmatch(re.escape(member_col) + r'\d+', cell) and val.get('display') == member_value:
            row = int(cell[len(member_col):])
            if tab_cells.get(f'{task_col}{row}', {}).get('display') == task_value:
                return row
    return None
```

## Tables and banding

Read existing `tables` and `bandedRanges` before styling. Avoid overlapping
`addTable`/`addBanding` ownership. Treat delete/recreate of a table as a structural
change needing review, because references and table IDs can change even when
cell values survive. Use narrow field masks and read back. Older source testing
observed 500s for some table-style updates; this is not a permanent API contract.
Check the current request schema and test against an authorized scratch target.
See [styling](../standards/styling.md).

## Formula safety — avoid circular SUMIF

`SUMIF('Sheet'!C:C, A54, 'Sheet'!I:I)` where cell C54 is inside the sum range will **circularly reference itself** and return `#REF!`. This happens when the Allocated Resources table (which has its own column C = Fact hours) sits in the same sheet as the main table.

**Fix:** bound the range explicitly.
```python
f"=SUMIF('Mar 25 – Apr 24'!C2:C45, A{row}, 'Mar 25 – Apr 24'!I2:I45)"
```

Row 45 in this example is a safe upper bound below the main table and above the Allocated Resources area.

## Inserting a row inside a table (push row 22 down, add new row 22)

```python
{'insertDimension': {
    'range': {'sheetId': TAB_SID, 'dimension': 'ROWS',
              'startIndex': 21, 'endIndex': 22},  # 0-indexed
    'inheritFromBefore': True,  # copy styles from row above (important for banded range)
}}
```

## Deleting rows — descending order for index stability

```python
# Delete rows 28, 24, 23 (in original numbering). Process highest→lowest.
for r in sorted([28, 24, 23], reverse=True):
    reqs.append({'deleteDimension': {
        'range': {'sheetId': TAB_SID, 'dimension': 'ROWS',
                  'startIndex': r-1, 'endIndex': r}
    }})
```

In a single `batchUpdate`, requests execute sequentially with **post-previous-request** indices. Descending order means each delete doesn't shift the targets of later deletes.

## Updating a single cell (by 1-indexed row + col-letter)

```python
def col_letter_to_idx(letter):
    # 'A' -> 0, 'B' -> 1, ..., 'AA' -> 26
    idx = 0
    for c in letter:
        idx = idx * 26 + (ord(c.upper()) - 65 + 1)
    return idx - 1

def update_cell_req(sheet_id, a1):
    # e.g., 'I10' -> row 10, col I
    import re
    m = re.match(r'([A-Z]+)(\d+)', a1)
    col, row = m.group(1), int(m.group(2))
    col_idx = col_letter_to_idx(col)
    def make(value_type, value):
        return {'updateCells': {
            'range': {'sheetId': sheet_id,
                      'startRowIndex': row-1, 'endRowIndex': row,
                      'startColumnIndex': col_idx, 'endColumnIndex': col_idx+1},
            'rows': [{'values': [{'userEnteredValue': {value_type: value}}]}],
            'fields': 'userEnteredValue',
        }}
    return make
```

## Appending a row at the end of a table (without shifting other tables)

```python
# To add a row to the end of the Project workload table without disturbing Allocated Resources below,
# insert at the row BEFORE the footer (or the last row of the table range).
# Find current table range from the chosen tab's tables metadata['range'] and insert at end_row - 1.
```
