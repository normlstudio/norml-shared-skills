#!/usr/bin/env python3
"""Isolated integrity/recovery tests; never read or mutate real task stores."""
import importlib.util
import json
import re
import tempfile
import sys
sys.dont_write_bytecode = True
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('planning', SKILL / 'scripts/planning.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class PlanningTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'items').mkdir()
        self.cfg = {
            'schema_version': 3, 'storage': 'workspace',
            'locations': {'workspace': None, 'repositories': []},
            'planning': {'lane': 'quick', 'commit_docs': False,
                         'canonical_system': 'norml-tasks', 'active_milestones': []},
            'github': {'enabled': False, 'repository': None,
                       'task_scope': 'all-concrete', 'category_labels': {}},
            'workflow': {'research_when_needed': True, 'verify_before_complete': True,
                         'auto_advance': False}}
        self.cfg.update(project_id='sample', owner_id='sample-workspace')
        self.cfg['locations']['workspace'] = {'owner_id':'sample-workspace', 'path':'Products/Sample/.claude/tasks'}
        self.save_config()
        (self.root / 'goals.md').write_text('# Goals\n\n### GOAL-01 — Accepted outcome\n')
        self.item()

    def save_config(self):
        (self.root / 'config.json').write_text(json.dumps(self.cfg))

    def item(self, number=1, **overrides):
        example = (SKILL / 'examples/organizing-a-thought-dump.md').read_text()
        raw = re.search(r'```markdown\n(.*?)\n```', example, re.S)[1]
        meta, body = raw.split('\n---\n',1)
        data = {k:json.loads(v) for k,v in (x.split(': ',1) for x in meta.splitlines()[1:])}
        data['id'] = f'TASK-{number:03d}'
        data['goals'] = ['GOAL-01']
        data['queue'] = 'next'
        data.update(overrides)
        path = self.root / f'items/task-{number:03d}-sample.md'
        path.write_text('---\n'+'\n'.join(f'{k}: {json.dumps(v)}' for k,v in data.items())+'\n---\n'+body)
        return path

    def load(self):
        return p.load_store(self.root)

    def test_workspace_roundtrip_is_deterministic(self):
        before = p.fingerprint(self.root)
        cfg, items, ext = self.load()
        rendered = p.render(cfg,items)
        p.write_index(self.root,rendered,before)
        self.assertEqual(rendered,(self.root/'tasks.md').read_text())
        self.assertEqual([], ext)
        self.assertIn('(items/task-001-sample.md)',rendered)

    def test_legacy_store_never_overwritten(self):
        self.cfg['schema_version'] = 2
        self.save_config()
        (self.root/'tasks.md').write_text('Unmigrated user work')
        with self.assertRaisesRegex(p.Invalid, 'Legacy'):
            self.load()
        self.assertEqual('Unmigrated user work',(self.root/'tasks.md').read_text())

    def test_detects_cycle(self):
        self.item(depends_on=['TASK-002'])
        self.item(2,depends_on=['TASK-001'])
        with self.assertRaisesRegex(p.Invalid, 'cycle'):
            self.load()

    def test_missing_dependency(self):
        self.item(depends_on=['TASK-999'])
        with self.assertRaisesRegex(p.Invalid, 'missing local dependency'):
            self.load()

    def test_duplicate_ids(self):
        (self.root/'items/task-001-duplicate.md').write_text((self.root/'items/task-001-sample.md').read_text())
        with self.assertRaisesRegex(p.Invalid, 'Duplicate ID'):
            self.load()

    def test_status_queue_mismatch(self):
        self.item(status='done',queue='now')
        with self.assertRaisesRegex(p.Invalid, 'terminal'):
            self.load()

    def test_external_reference_is_unverified(self):
        self.cfg['locations']['repositories']=[{'owner_id':'sample-repo','repository':'example-org/sample','planning_path':'.claude/tasks'}]
        self.save_config()
        self.item(depends_on=['sample-repo::TASK-001'])
        self.assertEqual(['sample-repo::TASK-001'],self.load()[2])

    def test_unknown_owner_fails(self):
        self.item(depends_on=['unknown::TASK-001'])
        with self.assertRaisesRegex(p.Invalid,'unmapped external owner'):
            self.load()

    def test_changed_item_prevents_index_overwrite(self):
        before=p.fingerprint(self.root)
        cfg,items,_=self.load()
        self.item(title='Another session changed this')
        with self.assertRaisesRegex(p.Invalid,'changed since read'):
            p.write_index(self.root,p.render(cfg,items),before)
        self.assertFalse((self.root/'tasks.md').exists())

    def test_path_traversal_rejected(self):
        self.cfg['locations']['workspace']['path']='../../.claude/tasks'
        self.save_config()
        with self.assertRaisesRegex(p.Invalid,'portable planning path'):
            self.load()

    def test_missing_plan_rejected(self):
        (self.root/'milestones/launch').mkdir(parents=True)
        (self.root/'milestones/launch/state.md').write_text('Planned')
        self.item(milestone='launch',plan='01-01')
        with self.assertRaisesRegex(p.Invalid,'plan file'):
            self.load()

    def test_repository_mirror_identity(self):
        self.cfg.update(storage='repository',owner_id='sample-repo')
        self.cfg['locations']['repositories']=[{'owner_id':'sample-repo','repository':'example-org/sample','planning_path':'.claude/tasks'}]
        self.cfg['github'].update(enabled=True, repository='example-org/sample')
        self.cfg['planning']['commit_docs']=True
        self.save_config()
        self.item(issue='https://github.com/example-org/sample/issues/1')
        self.load()
        self.item(issue='https://github.com/other-org/sample/issues/1')
        with self.assertRaisesRegex(p.Invalid,'issue repository mismatch'):
            self.load()

    def test_local_repository_needs_no_hosted_identity_when_mirror_disabled(self):
        self.cfg.update(storage='repository', owner_id='sample-repo')
        self.cfg['locations']['repositories'] = [{'owner_id': 'sample-repo',
            'repository': None, 'planning_path': '.claude/tasks'}]
        self.cfg['planning']['commit_docs'] = True
        self.save_config()
        self.load()
        self.cfg['locations']['repositories'][0].pop('repository')
        self.save_config()
        self.load()

    def test_enabled_mirror_refuses_missing_repository_identity(self):
        self.cfg.update(storage='repository', owner_id='sample-repo')
        self.cfg['locations']['repositories'] = [{'owner_id': 'sample-repo',
            'repository': None, 'planning_path': '.claude/tasks'}]
        self.cfg['github'].update(enabled=True, repository=None)
        self.cfg['planning']['commit_docs'] = True
        self.save_config()
        with self.assertRaisesRegex(p.Invalid, 'verified repository identity'):
            self.load()

    def test_now_requires_completed_prerequisites(self):
        self.item(queue='now',depends_on=['TASK-002'])
        self.item(2)
        with self.assertRaisesRegex(p.Invalid,'unfinished local prerequisite'):
            self.load()

    def test_goal_mention_is_not_a_definition(self):
        (self.root/'goals.md').write_text('A mention of GOAL-01 without a definition')
        with self.assertRaisesRegex(p.Invalid,'missing goal'):
            self.load()

    def test_title_cannot_inject_table_or_link(self):
        self.item(title='A | [bad](other)\nrow')
        cfg,items,_=self.load()
        rendered=p.render(cfg,items)
        self.assertIn('A &#124; &#91;bad&#93;(other) row',rendered)


if __name__=='__main__':
    unittest.main()
