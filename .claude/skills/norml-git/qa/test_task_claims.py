"""Behavioral checks against a real bare Git remote and independent clones."""
import concurrent.futures
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'task_claims.py'
spec = importlib.util.spec_from_file_location('task_claims', SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def command(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


class Claims(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.remote = self.root / 'shared.git'
        command('git', 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.clones = []
        for name in ('developer-one', 'developer-two'):
            repo = self.root / name
            command('git', 'clone', str(self.remote), str(repo))
            command('git', 'config', 'user.name', name, cwd=repo)
            command('git', 'config', 'user.email', name + '@example.test', cwd=repo)
            self.clones.append(repo)
        repo = self.clones[0]
        (repo / 'feature.txt').write_text('baseline\n')
        command('git', 'add', 'feature.txt', cwd=repo)
        command('git', '-c', 'user.name=developer-two', 'commit', '-m', 'feat: Developer Two implemented #42 baseline', cwd=repo)
        command('git', 'push', 'origin', 'main', cwd=repo)
        self.a, self.b = [m.Registry(p) for p in self.clones]
        self.addCleanup(self.temp.cleanup)

    def audit(self, registry, task='issue:42'):
        return registry.audit(task, 'main', keywords='baseline')['receipt']

    def claim(self, registry, task='issue:42', paths=('feature.txt',), session='worker-a'):
        return registry.claim(self.audit(registry, task), 'Developer One', session, paths, 'Fix remaining behavior only')

    def race(self, tasks, paths):
        audits = [self.audit(r, t) for r, t in zip((self.a, self.b), tasks)]
        barrier = threading.Barrier(2)
        for registry in (self.a, self.b):
            original = registry.commit
            calls = [0]
            def synchronized(parent, record, original=original, calls=calls):
                calls[0] += 1
                if calls[0] == 1:
                    barrier.wait(timeout=10)
                return original(parent, record)
            registry.commit = synchronized
        def attempt(index):
            try:
                return (True, (self.a, self.b)[index].claim(audits[index], 'Developer', 'worker-' + str(index), paths[index], 'remaining delta'))
            except m.Refusal as e:
                return (False, str(e))
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            return list(pool.map(attempt, (0, 1)))

    def test_same_task_simultaneous_first_branch_creation_has_one_owner(self):
        results = self.race(('issue:42', 'issue:42'), (('a',), ('b',)))
        self.assertEqual(sum(ok for ok, _ in results), 1)
        self.assertEqual(len(self.a.read()[1]['claims']), 1)
        self.assertIn('Busy:', next(v for ok, v in results if not ok))

    def test_different_tasks_overlapping_directories_have_one_owner(self):
        results = self.race(('issue:42', 'issue:43'), (('src',), ('src/api.py',)))
        self.assertEqual(sum(ok for ok, _ in results), 1)

    def test_disjoint_tasks_concurrent_updates_both_survive(self):
        results = self.race(('issue:42', 'issue:43'), (('src',), ('tests',)))
        self.assertTrue(all(ok for ok, _ in results))
        self.assertEqual(len(self.a.read()[1]['claims']), 2)

    def test_linked_worktree_uses_same_remote_ownership(self):
        lease = self.claim(self.a)
        linked = self.root / 'linked'
        command('git', 'worktree', 'add', '-b', 'linked', str(linked), cwd=self.clones[0])
        r = m.Registry(linked)
        self.assertEqual(r.common, self.a.common)
        with self.assertRaises(m.Refusal):
            self.claim(r, session='another-worker')
        self.assertEqual(r.check(lease['receipt'])['session'], 'worker-a')

    def test_handoff_invalidates_old_receipt_and_receiver_adopts(self):
        old = self.claim(self.a)
        new = self.a.update(old['receipt'], 'handoff', owner='Developer Two', session='worker-b')
        self.assertNotEqual(old['receipt'], new['receipt'])
        with self.assertRaises(m.Refusal):
            self.a.check(old['receipt'])
        received = self.b.adopt(old['claim']['id'], 'worker-b')
        self.assertEqual(self.b.check(received['receipt'])['owner'], 'Developer Two')
        with self.assertRaises(m.Refusal):
            self.b.adopt(old['claim']['id'], 'worker-a')

    def test_stale_heartbeat_never_releases_to_another_worker(self):
        lease = self.claim(self.a)
        def age(ledger):
            ledger['claims'][lease['claim']['id']]['updated'] = time.time() - 4000
        self.a.change(age)
        with self.assertRaises(m.Refusal):
            self.a.check(lease['receipt'])
        with self.assertRaises(m.Refusal):
            self.claim(self.b, session='worker-b')
        self.a.update(lease['receipt'], 'renew')
        self.a.check(lease['receipt'])

    def test_review_preserves_claim_until_explicit_resume(self):
        lease = self.claim(self.a)
        self.a.update(lease['receipt'], 'park', evidence='Open PR awaiting review')
        with self.assertRaises(m.Refusal):
            self.a.check(lease['receipt'])
        with self.assertRaises(m.Refusal):
            self.claim(self.b)
        self.a.update(lease['receipt'], 'renew')
        self.a.check(lease['receipt'])

    def test_scopes_reject_outside_traversal_and_globs(self):
        lease = self.claim(self.a, paths=('src',))
        self.a.check(lease['receipt'], ['src/api.py'])
        for name in ('tests/a.py', '../src/a.py', 'src/*.py', '/src', 'C:/src', '.GIT/config'):
            with self.assertRaises(m.Refusal):
                self.a.check(lease['receipt'], [name])

    def test_comma_joined_scope_requires_repeated_path_flags(self):
        for name in ('src,tests', 'src/a.py,src/b.py', 'src/a.py, src/b.py'):
            with self.subTest(scope=name):
                with self.assertRaisesRegex(m.Refusal, 'Repeat --path'):
                    m.path_scope(name)
        self.assertEqual(m.path_scope('notes with spaces.txt'), 'notes with spaces.txt')

    def test_invalid_cli_scope_never_writes_registry_or_lease(self):
        for existing in (False, True):
            if existing:
                self.claim(self.a, task='task:other', paths=('other.txt',))
            audit = self.audit(self.a, 'task:invalid')
            before = self.a.read()
            leases = self.a.cache / 'leases'
            saved = {p.name: p.read_bytes() for p in leases.glob('*.json')}
            result = subprocess.run(
                [sys.executable, str(SCRIPT), '--repo', str(self.clones[0]),
                 'claim', '--audit', audit, '--owner', 'Developer One',
                 '--session', 'invalid-cli', '--path', 'feature.txt,other.txt',
                 '--remaining', 'Remaining implementation'],
                capture_output=True, text=True)
            with self.subTest(existing_registry=existing):
                self.assertEqual(result.returncode, 2, result.stdout)
                refusal = json.loads(result.stdout)
                self.assertFalse(refusal['ok'])
                self.assertIn('Repeat --path', refusal['error'])
                self.assertEqual(self.a.read(), before)
                self.assertEqual({p.name: p.read_bytes() for p in leases.glob('*.json')}, saved)

    def test_repeated_cli_paths_protect_each_scope_and_release(self):
        repo = self.clones[0]
        paths = ('feature.txt', 'notes with spaces.txt')
        audit = self.audit(self.a, 'task:multi-path')
        result = json.loads(command(
            sys.executable, str(SCRIPT), '--repo', str(repo), 'claim',
            '--audit', audit, '--owner', 'Developer One', '--session', 'cli-worker',
            '--path', paths[0], '--path', paths[1], '--remaining', 'Remaining implementation'))
        lease = result['result']
        listed = json.loads(command(sys.executable, str(SCRIPT), '--repo', str(repo), 'list'))
        record = listed['result']['claims'][lease['claim']['id']]
        self.assertEqual(record['scopes'], list(paths))
        for path in paths:
            self.a.check(lease['receipt'], [path])
            with self.assertRaisesRegex(m.Refusal, 'Busy:'):
                self.claim(self.b, task='task:competitor', paths=(path,), session='other-cli')
        for path in paths:
            (repo / path).write_text('completed\n')
        command('git', 'add', '--', *paths, cwd=repo)
        command('git', 'commit', '-m', 'fix: finish both claimed files', cwd=repo)
        commit = command('git', 'rev-parse', 'HEAD', cwd=repo)
        command('git', 'push', 'origin', 'main', cwd=repo)
        released = json.loads(command(
            sys.executable, str(SCRIPT), '--repo', str(repo), 'release',
            '--receipt', lease['receipt'], '--integrated-commit', commit))
        self.assertEqual(released['result']['claim']['state'], 'released')

    def test_remote_failure_refuses_check_and_claim(self):
        lease = self.claim(self.a)
        self.remote.rename(self.root / 'disconnected.git')
        with self.assertRaises(m.Refusal):
            self.a.check(lease['receipt'])
        with self.assertRaises(m.Refusal):
            self.claim(self.b)

    def test_refused_push_is_not_granted_and_preserves_pending_receipt(self):
        hook = self.remote / 'hooks' / 'pre-receive'
        hook.write_text('#!/bin/sh\nexit 1\n')
        hook.chmod(0o755)
        with self.assertRaisesRegex(m.Refusal, 'Pending receipt:'):
            self.claim(self.a)
        receipts = list((self.a.cache / 'leases').glob('*.json'))
        self.assertEqual(len(receipts), 1)
        with self.assertRaises(m.Refusal):
            self.a.check(receipts[0])
        self.assertIsNone(self.a.head())

    def test_stale_audit_after_new_integrated_work_refuses(self):
        receipt = self.audit(self.a)
        repo = self.clones[0]
        (repo / 'feature.txt').write_text('more integrated work\n')
        command('git', 'commit', '-am', 'fix: latest integration', cwd=repo)
        command('git', 'push', 'origin', 'main', cwd=repo)
        with self.assertRaisesRegex(m.Refusal, 'changed after audit'):
            self.a.claim(receipt, 'Developer One', 'a', ['feature.txt'], 'remaining')

    def test_release_requires_new_related_integrated_commit(self):
        lease = self.claim(self.a)
        with self.assertRaisesRegex(m.Refusal, 'predates'):
            self.a.update(lease['receipt'], 'release', commit=lease['claim']['base_head'])
        repo = self.clones[0]
        (repo / 'feature.txt').write_text('completed\n')
        command('git', 'commit', '-am', 'fix: remaining behavior', cwd=repo)
        commit = command('git', 'rev-parse', 'HEAD', cwd=repo)
        with self.assertRaisesRegex(m.Refusal, 'integrated'):
            self.a.update(lease['receipt'], 'release', commit=commit)
        command('git', 'push', 'origin', 'main', cwd=repo)
        self.a.update(lease['receipt'], 'release', commit=commit)
        self.claim(self.b, session='next-worker')

    def test_local_head_index_and_dirty_files_unchanged(self):
        repo = self.clones[0]
        (repo / 'feature.txt').write_text('unfinished staged work\n')
        command('git', 'add', 'feature.txt', cwd=repo)
        (repo / 'extra.txt').write_text('untracked work\n')
        before = (command('git', 'rev-parse', 'HEAD', cwd=repo), command('git', 'diff', '--cached', cwd=repo), command('git', 'status', '--porcelain', cwd=repo))
        self.claim(self.a)
        after = (command('git', 'rev-parse', 'HEAD', cwd=repo), command('git', 'diff', '--cached', cwd=repo), command('git', 'status', '--porcelain', cwd=repo))
        self.assertEqual(before, after)
        self.assertEqual((repo / 'extra.txt').read_text(), 'untracked work\n')

    def test_malformed_registry_is_never_replaced(self):
        parent = self.a.head()
        tip = self.a.commit(parent, {'schema': 99, 'claims': {}})
        command('git', 'push', 'origin', tip + ':' + m.REF, cwd=self.clones[0])
        with self.assertRaisesRegex(m.Refusal, 'Unsupported'):
            self.claim(self.b)
        self.assertEqual(self.a.head(), tip)

    def test_existing_work_and_authors_are_visible_in_audit(self):
        report = self.a.audit('issue:42', 'main', keywords='baseline')
        self.assertIn('baseline', report['issue_history'])
        self.assertIn('developer-two', report['recent_history'])

    def test_case_variants_and_symlink_aliases_cannot_escape_scope(self):
        self.claim(self.a, paths=('Src',))
        with self.assertRaises(m.Refusal):
            self.claim(self.b, task='issue:43', paths=('src/api.py',))
        (self.clones[0] / 'alias').symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(m.Refusal, 'owning repository'):
            self.claim(self.a, task='issue:44', paths=('alias/other.txt',))

    def test_unknown_push_outcome_can_recover_existing_claim_receipt(self):
        original = self.a.head
        calls = [0]
        def disconnected_after_push():
            calls[0] += 1
            if calls[0] == 2:
                raise m.Refusal('Connection lost after push')
            return original()
        # Audit does not consume the injected head calls.
        audit = self.audit(self.a)
        with patch.object(self.a, 'head', disconnected_after_push):
            with self.assertRaisesRegex(m.Refusal, 'Pending receipt:'):
                self.a.claim(audit, 'Developer One', 'worker-a', ['feature.txt'], 'remaining')
        receipt = next((self.a.cache / 'leases').glob('*.json'))
        self.assertEqual(self.a.check(receipt)['session'], 'worker-a')
        with self.assertRaises(m.Refusal):
            self.claim(self.b, session='worker-b')

    def test_same_task_race_with_existing_registry_has_one_new_owner(self):
        self.claim(self.a, task='issue:99', paths=('unrelated',))
        results = self.race(('issue:42', 'issue:42'), (('a',), ('b',)))
        self.assertEqual(sum(ok for ok, _ in results), 1)
        self.assertEqual(len(self.a.read()[1]['claims']), 2)

    def test_github_transport_aliases_share_identity(self):
        self.assertEqual(m.authority('git@github.com:Example-Org/Example.git'), m.authority('https://github.com/example-org/example'))
        with self.assertRaises(m.Refusal):
            m.authority('git@bitbucket.org:example-org/example.git')

    def test_multiple_push_destinations_are_refused(self):
        repo = self.clones[0]
        command('git', 'config', '--add', 'remote.origin.pushurl', str(self.remote), cwd=repo)
        command('git', 'config', '--add', 'remote.origin.pushurl', str(self.root / 'other.git'), cwd=repo)
        with self.assertRaisesRegex(m.Refusal, 'Exactly one'):
            m.Registry(repo)

    def test_issue_snapshot_includes_cross_reference_and_excludes_number_prefix(self):
        self.a.github_host = 'example-org/example'
        def response(args, **kwargs):
            if args[:3] == ['gh', 'issue', 'view']:
                value = {'number': 42, 'state': 'OPEN', 'updatedAt': 'now'}
            elif args[:3] == ['gh', 'pr', 'list']:
                value = [{'number': 10, 'body': 'Fixes #42'}, {'number': 11, 'body': 'Fixes #420'}]
            elif args[:2] == ['gh', 'api']:
                value = [[{'source': {'issue': {'number': 12, 'pull_request': {}, 'repository_url': 'https://api.github.com/repos/example-org/example'}}}]]
                value[0][0]['source']['issue']['pull_request'] = {'url': 'https://api.github.com/repos/example-org/example/pulls/12'}
            elif args[:3] == ['gh', 'pr', 'view']:
                value = {'number': 12, 'body': 'Referenced through timeline', 'state': 'MERGED'}
            else:
                raise AssertionError(args)
            return subprocess.CompletedProcess(args, 0, json.dumps(value), '')
        with patch.object(m, 'run', response):
            issue, prs = self.a.issue_snapshot(42)
        self.assertEqual([p['number'] for p in prs], [10, 12])

    def test_changed_issue_or_pr_invalidates_audit(self):
        path = Path(self.audit(self.a))
        report = json.loads(path.read_text())
        report.update(issue={'number': 42, 'state': 'OPEN', 'updatedAt': 'old'}, prs=[])
        path.write_text(json.dumps(report))
        with patch.object(self.a, 'issue_snapshot', return_value=({'number': 42, 'state': 'OPEN', 'updatedAt': 'new'}, [])):
            with self.assertRaisesRegex(m.Refusal, 'Issue or linked PRs changed'):
                self.a.claim(path, 'Developer One', 'a', ['feature.txt'], 'remaining')


if __name__ == '__main__':
    unittest.main(verbosity=2)
