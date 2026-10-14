# Sheets styling

Preserve the user's existing visual system. Read current tables, banding,
validation and protected ranges first. Choose their supplied palette; no company
palette or personal dropdown preference is imposed.

Use narrow fields in `repeatCell`, `updateDimensionProperties`,
`setDataValidation` and `updateTable`. Grid ranges are zero-based and half-open.
Table IDs are strings. Supply `rowsProperties` with `*ColorStyle` fields when
creating a table; validate the current API schema before updating one.

```python
request = {'addTable': {'table': {
    'name': 'Tasks',
    'range': {'sheetId': TAB_ID, 'startRowIndex': 0, 'endRowIndex': 6,
              'startColumnIndex': 0, 'endColumnIndex': 3},
    'rowsProperties': {
        'headerColorStyle': {'rgbColor': {'red': .15, 'green': .20, 'blue': .25}},
        'firstBandColorStyle': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}},
        'secondBandColorStyle': {'rgbColor': {'red': .96, 'green': .97, 'blue': .98}}
    }
}}}
```

Native tables manage their banding. Do not layer an unrelated `addBanding` over
the same cells. Older source tests observed errors when updating table colors;
those observations do not establish a permanent restriction. Prefer current
supported field updates and test/read-back over destructive recreation. A
delete/recreate needs authorization and checks for table-reference breakage.

Tables and ordinary ranges have different dropdown presentation. Confirm the
requested style in the current UI; `showCustomUi` controls display, not a
guaranteed arrow/chip switch. Use `ONE_OF_LIST` validation with `strict=True`
when the field's allowed values are fixed. Preserve existing values.

Set row height and column widths for actual content; 21px is an optional
compact example, not a locked requirement. Wrap text when readability needs it.
Verify currency/date formats, colors, validation and formulas by reading back.

Sources: [Requests](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request),
[Tables](https://developers.google.com/workspace/sheets/api/guides/tables).
