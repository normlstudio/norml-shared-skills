import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS=Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(SCRIPTS))
from google_auth import load_credentials, verify_drive_identity
spec=importlib.util.spec_from_file_location('reader',SCRIPTS/'verify-google-read.py')
reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)

class GoogleBoundaries(unittest.TestCase):
    def test_explicit_account_required(self):
        with self.assertRaises(ValueError):load_credentials('')
    def test_exact_gsc_target(self):
        rows=[{'siteUrl':'https://example.com/','permissionLevel':'siteFullUser'}]
        self.assertTrue(reader.target_visible('gsc',rows,'https://example.com/'))
        self.assertFalse(reader.target_visible('gsc',rows,'http://example.com/'))
        self.assertFalse(reader.target_visible('gsc',[], 'https://example.com/'))
    def test_unverified_property_refused(self):
        self.assertFalse(reader.target_visible('gsc',[{'siteUrl':'sc-domain:example.com',
            'permissionLevel':'siteUnverifiedUser'}],'sc-domain:example.com'))
    def test_exact_analytics_property(self):
        rows=[{'propertySummaries':[{'property':'properties/123'}]}]
        self.assertTrue(reader.target_visible('analytics',rows,'properties/123'))
        self.assertFalse(reader.target_visible('analytics',rows,'properties/12'))
    def test_mismatched_identity_refused(self):
        class Drive:
            def about(self):return self
            def get(self,**kw):return self
            def execute(self):return {'user':{'emailAddress':'other@example.com'}}
        with self.assertRaises(RuntimeError):verify_drive_identity(Drive(),'user@example.com')

if __name__=='__main__':unittest.main()
