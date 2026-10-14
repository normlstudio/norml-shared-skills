#!/usr/bin/env python3
"""Read-only exact-account and existing native-file verification."""
import argparse, json, sys
from google_auth import load_credentials, verify_drive_identity

def verify_file(drive, service, file_id, kind, require_edit=False):
    mimes={'sheet':'application/vnd.google-apps.spreadsheet',
           'doc':'application/vnd.google-apps.document'}
    meta=drive.files().get(fileId=file_id, supportsAllDrives=True,
        fields='id,mimeType,trashed,capabilities(canEdit)').execute()
    if meta.get('trashed') or meta.get('mimeType') != mimes[kind]:
        raise ValueError('Target is not an active native '+kind)
    editable=bool(meta.get('capabilities',{}).get('canEdit'))
    if require_edit and not editable:
        raise PermissionError('Target lacks Editor capability')
    if kind=='sheet':
        service.spreadsheets().get(spreadsheetId=file_id,
            fields='spreadsheetId,sheets.properties.sheetId').execute()
    else:
        service.documents().get(documentId=file_id,includeTabsContent=True,
            fields='documentId,tabs.documentTab.body.content.startIndex').execute()
    return {'read':True,'can_edit':editable}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--account',required=True)
    p.add_argument('--sheet-id',required=True)
    p.add_argument('--doc-id',required=True)
    p.add_argument('--require-edit',action='store_true')
    p.add_argument('--quota-project')
    p.add_argument('--mode',choices=['gcloud','adc'],default='gcloud')
    a=p.parse_args()
    from googleapiclient.discovery import build
    creds=load_credentials(a.account,a.quota_project,a.mode)
    drive=build('drive','v3',credentials=creds,cache_discovery=False)
    verify_drive_identity(drive,a.account)
    out={'identity_matches':True}
    for kind,id_,api,version in [('sheet',a.sheet_id,'sheets','v4'),('doc',a.doc_id,'docs','v1')]:
        out[kind]=verify_file(drive,build(api,version,credentials=creds,cache_discovery=False),
                             id_,kind,a.require_edit)
    print(json.dumps(out))
    return 0

if __name__=='__main__':
    try: raise SystemExit(main())
    except Exception as exc:
        status=getattr(getattr(exc,'resp',None),'status',None)
        print(json.dumps({'ok':False,'error_type':type(exc).__name__,'http_status':status}),file=sys.stderr)
        raise SystemExit(1)
