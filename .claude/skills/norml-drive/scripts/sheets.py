"""Pure Sheets snapshot helpers; no network or mutation on import."""
import datetime as dt
from google_auth import verify_drive_identity

def column_label(index):
    if not isinstance(index,int) or isinstance(index,bool) or index < 0:
        raise ValueError('Column index must be a nonnegative integer')
    result=''
    while index >= 0:
        index,rem=divmod(index,26)
        result=chr(65+rem)+result
        index-=1
    return result

def snapshot(response, modified_time):
    out={'schema_version':1,'meta':{
        'spreadsheet_id':response['spreadsheetId'],
        'cached_at':dt.datetime.now(dt.timezone.utc).isoformat(),
        'drive_modified_time':modified_time},'tabs':[]}
    for sheet in response.get('sheets',[]):
        p=sheet['properties']
        tab={'sheet_id':p['sheetId'],'title':p['title'],'cells':{},
             'tables':sheet.get('tables',[]),
             'banded_ranges':sheet.get('bandedRanges',[]),
             'protected_ranges':sheet.get('protectedRanges',[])}
        for block in sheet.get('data',[]):
            row_offset=block.get('startRow',0)
            col_offset=block.get('startColumn',0)
            for r,row in enumerate(block.get('rowData',[])):
                for c,cell in enumerate(row.get('values',[])):
                    if not cell: continue
                    key=f'{column_label(c+col_offset)}{r+row_offset+1}'
                    tab['cells'][key]={
                        'display':cell.get('formattedValue'),
                        'entered':cell.get('userEnteredValue'),
                        'effective':cell.get('effectiveValue'),
                        'format':cell.get('effectiveFormat'),
                        'validation':cell.get('dataValidation')}
        out['tabs'].append(tab)
    return out

def _metadata(drive, spreadsheet_id):
    meta = drive.files().get(fileId=spreadsheet_id, supportsAllDrives=True,
        fields='id,mimeType,trashed,modifiedTime,capabilities(canEdit)').execute()
    if meta.get('trashed') or meta.get('mimeType') != 'application/vnd.google-apps.spreadsheet':
        raise ValueError('Target is not an active native spreadsheet')
    return meta

def pull(sheets, drive, account, spreadsheet_id):
    verify_drive_identity(drive, account)
    before = _metadata(drive, spreadsheet_id)
    response = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id,
        includeGridData=True).execute()
    after = _metadata(drive, spreadsheet_id)
    if before['modifiedTime'] != after['modifiedTime']:
        raise RuntimeError('Spreadsheet changed during snapshot; pull again')
    return snapshot(response, after['modifiedTime'])

def apply_requests(sheets, drive, account, spreadsheet_id, baseline,
                   requests, *, authorized=False, allow_destructive=False):
    if not authorized:
        raise PermissionError('Exact change must be authorized by the user')
    if baseline.get('meta', {}).get('spreadsheet_id') != spreadsheet_id:
        raise ValueError('Snapshot belongs to a different spreadsheet')
    if not requests:
        raise ValueError('No changes supplied')
    destructive = {'deleteSheet', 'deleteDimension', 'deleteRange', 'deleteTable',
                   'deleteBanding', 'deleteNamedRange'}
    if not allow_destructive and any(destructive.intersection(r) for r in requests):
        raise PermissionError('Destructive request requires exact-target authorization')
    verify_drive_identity(drive, account)
    live = _metadata(drive, spreadsheet_id)
    if not live.get('capabilities', {}).get('canEdit'):
        raise PermissionError('Selected account lacks Editor capability')
    if live['modifiedTime'] != baseline.get('meta', {}).get('drive_modified_time'):
        raise RuntimeError('Stale snapshot; pull and re-plan before applying')
    # modifiedTime is a staleness check, not a cross-call atomic lock.
    return sheets.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,
                                             body={'requests': requests}).execute()
