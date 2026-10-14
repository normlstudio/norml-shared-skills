import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('install', Path(__file__).resolve().parents[1] / 'scripts/install.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class Install(unittest.TestCase):
    def test_complete_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp).resolve() / 'skills'
            names = module.install(target)
            self.assertEqual(len(names), 16)
            for name in names:
                self.assertEqual((target / name / 'SKILL.md').read_bytes(),
                                 (module.SOURCE / name / 'SKILL.md').read_bytes())
                self.assertTrue((target / name / 'readme.html').is_file())

    def test_collision_preflight_preserves_all(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp).resolve() / 'skills'
            (target / 'norml-drive').mkdir(parents=True)
            (target / 'norml-drive' / 'marker').write_text('keep')
            with self.assertRaises(FileExistsError):
                module.install(target, ['norml-connect', 'norml-drive'])
            self.assertFalse((target / 'norml-connect').exists())
            self.assertEqual((target / 'norml-drive' / 'marker').read_text(), 'keep')

    def test_reject_unknown_and_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp).resolve() / 'skills'
            with self.assertRaises(ValueError):
                module.install(target, ['../outside'])
            real = Path(tmp).resolve() / 'real'
            real.mkdir()
            target.symlink_to(real, target_is_directory=True)
            with self.assertRaises(ValueError):
                module.install(target, ['norml-drive'])
            self.assertEqual(list(real.iterdir()), [])

    def test_source_skill_symlink_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            source, external = root / 'source', root / 'external'
            source.mkdir(); external.mkdir()
            (external / 'SKILL.md').write_text('external')
            (source / 'norml-outside').symlink_to(external, target_is_directory=True)
            with patch.object(module, 'SOURCE', source):
                with self.assertRaises(ValueError):
                    module.install(root / 'target', ['norml-outside'])
            self.assertFalse((root / 'target').exists())


if __name__ == '__main__':
    unittest.main()
