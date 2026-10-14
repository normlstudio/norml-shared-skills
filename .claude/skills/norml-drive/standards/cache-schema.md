# Sheets inspection cache

```json
{
  "schema_version": 1,
  "meta": {
    "spreadsheet_id": "example-sheet-id",
    "cached_at": "2026-10-13T12:00:00Z",
    "drive_modified_time": "2026-10-13T11:59:00Z"
  },
  "tabs": [{
    "sheet_id": 0,
    "title": "Tasks",
    "cells": {"A1": {"display": "Task", "entered": {"stringValue": "Task"}}},
    "tables": [],
    "banded_ranges": [],
    "protected_ranges": []
  }]
}
```

All example identifiers are synthetic. Keep raw entered/effective typed values,
displayed text and formatting separate. Matching is by exact A1 coordinate or
stable business key; C must never match CA. Sheet IDs identify tabs even after
a title changes. API ranges are zero-based and half-open. GridData startRow and
startColumn offsets must be included when converting to A1.

Store only the authorized target, not a whole account inventory. Choose a local
user-private cache directory outside Git/synced storage; mode 0700 directory and
0600 file on POSIX. On Windows use a user-only ACL and reject shared locations.
Raw protected ranges, validation, formulas and tables inform the change plan.

Refresh before applying and again after writing. Compare the current live
modifiedTime with the snapshot immediately before a write. A mismatch means
re-pull and re-plan; this is a staleness check, not a server-side compare-and-swap
lock. Never promise transactional concurrency protection across Sheets calls.
