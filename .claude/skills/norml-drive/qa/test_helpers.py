import importlib.util, pathlib, sys, unittest
SCRIPTS=pathlib.Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(SCRIPTS))
from sheets import column_label, snapshot, apply_requests
from doc_ops import select_tab, inserted_table, update
spec=importlib.util.spec_from_file_location('builder',SCRIPTS/'doc_builder.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)

class Helpers(unittest.TestCase):
    def test_wide_columns(self):
        self.assertEqual([column_label(x) for x in [0,25,26,51,52,701,702]],
                         ['A','Z','AA','AZ','BA','ZZ','AAA'])
    def test_offset_formula(self):
        resp={'spreadsheetId':'test','sheets':[{'properties':{'sheetId':7,'title':'Tasks'},
            'data':[{'startRow':4,'startColumn':52,'rowData':[{'values':[{
                'formattedValue':'2','userEnteredValue':{'formulaValue':'=1+1'}}]}]}]}]}
        cell=snapshot(resp,'time')['tabs'][0]['cells']['BA5']
        self.assertEqual(cell['entered'],{'formulaValue':'=1+1'})
    def test_unicode_and_tab(self):
        b=builder.DocBuilder(tab_id='t.test')
        self.assertEqual(b.text('A😀\n'),(1,5))
        self.assertEqual(b.reqs[0]['insertText']['location']['tabId'],'t.test')
        self.assertEqual(b.reqs[1]['updateParagraphStyle']['range']['endIndex'],5)
    def test_duplicate_title_rejected(self):
        document={'tabs':[{'tabProperties':{'tabId':n,'title':'Setup'}} for n in ['a','b']]}
        with self.assertRaises(ValueError):select_tab(document,title='Setup')
        self.assertEqual(select_tab(document,tab_id='b')['tabProperties']['tabId'],'b')
    def test_new_table_selected_after_old(self):
        old={'rows':3,'columns':2}; new={'rows':3,'columns':2}
        tab={'documentTab':{'body':{'content':[{'startIndex':2,'table':old},
             {'startIndex':101,'table':new}]}}}
        self.assertIs(inserted_table(tab,100,3,2),new)
        with self.assertRaises(ValueError):inserted_table(tab,50,3,2)
    def test_revision_required_and_transmitted(self):
        class Docs:
            def documents(self):return self
            def batchUpdate(self,**kw):self.body=kw['body'];return self
            def execute(self):return {}
        docs=Docs()
        with self.assertRaises(ValueError):update(docs,'id',None,[{}],authorized=True)
        update(docs,'id','revision',[{'insertText':{'text':'hello'}}],authorized=True)
        self.assertEqual(docs.body['writeControl'],{'requiredRevisionId':'revision'})
    def test_sheet_staleness_and_permission_guard(self):
        class Drive:
            def __init__(self,editable=True):self.editable=editable
            def about(self):self.op='about';return self
            def files(self):self.op='file';return self
            def get(self,**kw):return self
            def execute(self):
                if self.op=='about':return {'user':{'emailAddress':'user@example.com'}}
                return {'mimeType':'application/vnd.google-apps.spreadsheet',
                        'modifiedTime':'new','capabilities':{'canEdit':self.editable}}
        baseline={'meta':{'spreadsheet_id':'id','drive_modified_time':'old'}}
        requests=[{'updateCells':{}}]
        with self.assertRaises(RuntimeError):
            apply_requests(None,Drive(),'user@example.com','id',baseline,requests,authorized=True)
        baseline['meta']['drive_modified_time']='new'
        with self.assertRaises(PermissionError):
            apply_requests(None,Drive(False),'user@example.com','id',baseline,requests,authorized=True)
        with self.assertRaises(PermissionError):
            apply_requests(None,Drive(),'user@example.com','id',baseline,[{'deleteSheet':{}}],authorized=True)

if __name__=='__main__': unittest.main()
