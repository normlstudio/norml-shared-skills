"""Disposable local-file tests only; no real secrets or provider calls."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.dont_write_bytecode = True
SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/secrets-sweep.py'
spec = importlib.util.spec_from_file_location('sweep', SCRIPT)
sweep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sweep)

class SweepTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / 'shared-project'
        self.project.mkdir()
        self.backups = self.root / 'private-backups'
        self.token = 'ghp_' + ('synthetic' * 5)
        self.path = self.project / 'conversation.jsonl'
        self.path.write_text(json.dumps({'message': self.token}) + '\n')
    def cli(self, *args, private_backup=True):
        backup_args = ['--backup-dir', str(self.backups)] if private_backup else []
        return subprocess.run([sys.executable, str(SCRIPT), '--path', str(self.path),
                               '--report-dir', str(self.root / 'reports'), *backup_args, *args], text=True, capture_output=True)
    def test_report_has_no_value_or_preview(self):
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        output = result.stdout + ''.join(p.read_text() for p in (self.root / 'reports').glob('*'))
        self.assertNotIn(self.token, output)
        self.assertNotIn(self.token[:8], output)
    def test_dry_run_preserves_input(self):
        before = self.path.read_bytes()
        result = self.cli('--redact', '--dry-run')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(self.backups.exists())
        self.assertEqual(list(self.project.glob('*.bak*')), [])
    def test_redaction_backup_jsonl_and_idempotency(self):
        result = self.cli('--redact')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn(self.token, self.path.read_text())
        self.assertTrue(sweep.validate_jsonl(self.path.read_text()))
        backup = next(self.backups.glob('*.bak'))
        self.assertEqual(self.backups.stat().st_mode & 0o777, 0o700)
        self.assertEqual(list(self.project.glob('*.bak*')), [])
        self.assertEqual(backup.stat().st_mode & 0o777, 0o600)
        self.assertIn(self.token, backup.read_text())
        self.assertEqual(self.cli().returncode, 0)
    def test_json_failure_never_overwrites(self):
        self.path.write_text('{"message": "' + self.token + '" BROKEN}')
        before = self.path.read_bytes()
        self.assertEqual(self.cli('--redact').returncode, 1)
        self.assertEqual(self.path.read_bytes(), before)
    def test_symlink_refused(self):
        alias = self.root / 'linked.txt'
        alias.symlink_to(self.path)
        targets, errors, _ = sweep.gather_explicit([str(alias)], 50)
        self.assertEqual(targets, [])
        self.assertTrue(errors)
    def test_private_key_header_is_not_partially_redacted(self):
        text = '-----BEGIN ' + 'PRIVATE KEY-----\nsynthetic payload\n-----END PRIVATE KEY-----'
        self.path = self.project / 'key.txt'
        self.path.write_text(text)
        self.assertEqual(self.cli('--redact').returncode, 2)
        self.assertEqual(self.path.read_text(), text)
    def test_changed_input_refused(self):
        before = self.path.read_text()
        self.path.write_text('Concurrent change')
        with self.assertRaises(ValueError):
            sweep.preserve_replace(self.path, before, 'Replacement', self.backups)
        self.assertEqual(self.path.read_text(), 'Concurrent change')
    def test_default_backup_root_is_private_and_outside_shared_input(self):
        result = self.cli('--redact', private_backup=False)
        self.assertEqual(result.returncode, 0, result.stdout)
        prefix = 'Private original backups retained: '
        backup_root = Path(next(line[len(prefix):] for line in result.stdout.splitlines() if line.startswith(prefix)))
        self.addCleanup(lambda: __import__('shutil').rmtree(backup_root))
        self.assertFalse(backup_root.is_relative_to(self.project))
        self.assertEqual(backup_root.stat().st_mode & 0o777, 0o700)
        backup = next(backup_root.glob('*.bak'))
        self.assertEqual(backup.stat().st_mode & 0o777, 0o600)
        self.assertIn(self.token, backup.read_text())
        self.assertEqual(list(self.project.glob('*.bak*')), [])
    def test_source_adjacent_backup_directory_is_refused(self):
        before = self.path.read_bytes()
        result = self.cli('--redact', '--backup-dir', str(self.project / 'backups'))
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(list(self.project.rglob('*.bak')), [])
    def test_public_backup_directory_is_refused(self):
        self.backups.mkdir(mode=0o755)
        self.backups.chmod(0o755)
        before = self.path.read_bytes()
        self.assertEqual(self.cli('--redact').returncode, 1)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(list(self.backups.glob('*')), [])
    def test_english_slug_false_positive_excluded(self):
        text = 'when-a-dedicated-skill-exists-for-a-task-use-it'
        self.assertEqual(list(sweep.scan_text(text, self.path)), [])
    def test_explicit_path_required(self):
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
