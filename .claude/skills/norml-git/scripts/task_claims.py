#!/usr/bin/env python3
"""Shared task ownership using ordinary fast-forward Git pushes. Stdlib only."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import uuid

REF = 'refs/heads/norml/task-claims'
FILE = 'claims.json'
SCHEMA = 1

class Refusal(Exception):
    pass

def run(argv, *, cwd=None, data=None, env=None, okay=False):
    result = subprocess.run(argv, cwd=cwd, input=data, text=True, capture_output=True, env=env, timeout=60)
    if result.returncode and not okay:
        # Avoid echoing credential-bearing remote URLs or arbitrary server output.
        raise Refusal(f'{argv[0]} {argv[1]} failed (exit {result.returncode}); verify access and retry. No ownership assumed.')
    return result

def git(repo, *args, data=None, okay=False):
    return run(['git', '-C', str(repo), *args], data=data, okay=okay)

def path_scope(value):
    if ',' in value:
        raise Refusal('Scopes cannot contain commas. Repeat --path for each file or directory.')
    if not value or '\\' in value or value.startswith('/') or any(c in value for c in ':*?[]\x00\n\r'):
        raise Refusal('Scopes must be literal repository-relative files or directories, without globs.')
    if value == '.':
        return value
    parts = value.rstrip('/').split('/')
    if any(p in ('', '.', '..') or p.casefold() == '.git' for p in parts):
        raise Refusal('Unsafe file scope.')
    return '/'.join(parts)

def overlaps(a, b):
    # Conservative across macOS/Windows/Linux: spelling case cannot evade a claim.
    a, b = a.casefold(), b.casefold()
    return a == '.' or b == '.' or a == b or a.startswith(b + '/') or b.startswith(a + '/')

def authority(url):
    match = re.fullmatch(r'(?:git@github\.com:|https://github\.com/)([^/]+)/([^/]+?)(?:\.git)?/?', url)
    if match:
        return 'github.com/' + '/'.join(match.groups()).lower()
    if Path(url).is_absolute() or url.startswith('file://'):
        return str(Path(url.removeprefix('file://')).resolve())
    raise Refusal('Use the canonical GitHub remote; filesystem remotes are supported for isolated tests only.')

class Registry:
    def __init__(self, repo, remote='origin'):
        self.repo = Path(git(repo, 'rev-parse', '--show-toplevel').stdout.strip()).resolve()
        self.remote = remote
        # Pin both URLs; a split fetch/push origin is not one authority.
        fetches = git(self.repo, 'remote', 'get-url', '--all', remote).stdout.splitlines()
        pushes = git(self.repo, 'remote', 'get-url', '--push', '--all', remote).stdout.splitlines()
        if len(fetches) != 1 or len(pushes) != 1:
            raise Refusal('Exactly one fetch and push destination is required. Resolve the canonical remote first.')
        fetch, push = fetches[0], pushes[0]
        if authority(fetch) != authority(push):
            raise Refusal('Fetch and push URLs differ. Resolve the canonical remote first.')
        self.url = fetch
        self.github_host = None
        self.identity = hashlib.sha256(authority(fetch).encode()).hexdigest()
        self.common = Path(git(self.repo, 'rev-parse', '--path-format=absolute', '--git-common-dir').stdout.strip())
        self.cache = self.common / 'norml' / 'task-claims'

    def scope(self, value):
        value = path_scope(value)
        path = self.repo
        if value != '.':
            for part in value.split('/'):
                path = path / part
                if path.is_symlink() or (path.is_dir() and (path / '.git').exists()):
                    raise Refusal('Claim the owning repository directly, not a symlink or nested checkout.')
        return value

    def head(self):
        rows = git(self.repo, 'ls-remote', '--heads', self.remote, REF).stdout.splitlines()
        return rows[0].split()[0] if rows else None

    def read(self):
        head = self.head()
        if not head:
            return None, {'schema': SCHEMA, 'claims': {}}
        # Fetch exact tip without sharing FETCH_HEAD or a tracking ref between processes.
        git(self.repo, 'fetch', '--quiet', '--no-tags', '--no-write-fetch-head', self.remote, head)
        try:
            record = json.loads(git(self.repo, 'show', head + ':' + FILE).stdout)
        except (ValueError, TypeError):
            raise Refusal('Registry is unreadable. Do not reset or replace it.')
        if not isinstance(record, dict) or record.get('schema') != SCHEMA or not isinstance(record.get('claims'), dict):
            raise Refusal('Unsupported registry schema. Do not overwrite it.')
        return head, record

    def commit(self, parent, record):
        blob = git(self.repo, 'hash-object', '-w', '--stdin', data=json.dumps(record, sort_keys=True) + '\n').stdout.strip()
        tree = git(self.repo, 'mktree', data=f'100644 blob {blob}\t{FILE}\n').stdout.strip()
        args = ['commit-tree', tree]
        if parent:
            args += ['-p', parent]
        return git(self.repo, *args, data='chore(coordination): update task ownership\n').stdout.strip()

    def change(self, mutate):
        for _ in range(6):
            before, record = self.read()
            updated = copy.deepcopy(record)
            result = mutate(updated)
            tip = self.commit(before, updated)
            git(self.repo, 'push', '--porcelain', '--no-follow-tags', self.remote, tip + ':' + REF, okay=True)
            # Ambiguous network result: observe exact commit/descendants rather than assuming failure.
            after = self.head()
            if after == tip:
                return result, tip
            if after:
                git(self.repo, 'fetch', '--quiet', '--no-tags', '--no-write-fetch-head', self.remote, after)
                if git(self.repo, 'merge-base', '--is-ancestor', tip, after, okay=True).returncode == 0:
                    return result, after
            if after == before:
                raise Refusal('Registry push was not accepted. No claim granted; verify permissions/hooks.')
            # A concurrent winner advanced the branch: re-read and re-check its claims.
        raise Refusal('Registry stayed busy. Retry later; do not start implementation.')

    def github(self):
        if self.github_host:
            return self.github_host
        match = re.fullmatch(r'(?:git@github\.com:|https://github\.com/)([^/]+)/([^/]+?)(?:\.git)?/?', self.url)
        if not match:
            raise Refusal('Issue audit requires a verified GitHub remote; local test remotes support native task IDs only.')
        # Resolve repository renames/owner redirects for timeline comparisons.
        host = '/'.join(match.groups())
        self.github_host = json.loads(run(['gh', 'repo', 'view', host, '--json', 'nameWithOwner']).stdout)['nameWithOwner']
        return self.github_host

    def base_head(self, base):
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._/-]*', base) or '..' in base or base.startswith('norml/task-claims'):
            raise Refusal('Use an explicit ordinary integration branch name.')
        rows = git(self.repo, 'ls-remote', '--heads', self.remote, 'refs/heads/' + base).stdout.splitlines()
        if not rows:
            raise Refusal('Integration branch not found on the canonical remote.')
        head = rows[0].split()[0]
        git(self.repo, 'fetch', '--quiet', '--no-tags', '--no-write-fetch-head', self.remote, head)
        return head

    def receipt(self, kind, record):
        folder = self.cache / kind
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / (uuid.uuid4().hex + '.json')
        # IDs are generated here, never source-controlled filenames.
        path.write_text(json.dumps(record, indent=2) + '\n')
        return str(path)

    def issue_snapshot(self, issue):
        host = self.github()
        fields = 'number,title,state,mergedAt,url,body,headRefName,author,updatedAt'
        issue_data = json.loads(run(['gh', 'issue', 'view', str(issue), '--repo', host,
                                    '--json', 'number,title,state,body,assignees,updatedAt']).stdout)
        candidates = json.loads(run(['gh', 'pr', 'list', '--repo', host, '--state', 'all', '--limit', '100',
                                     '--search', f'"#{issue}" in:body', '--json', fields]).stdout)
        if len(candidates) == 100:
            raise Refusal('PR search reached its limit. Complete the audit manually before claiming.')
        pattern = re.compile(r'(?<![\w])#' + str(issue) + r'(?!\d)')
        prs = {p['number']: p for p in candidates if pattern.search(p.get('body', ''))}
        pages = json.loads(run(['gh', 'api', f'repos/{host}/issues/{issue}/timeline', '--paginate', '--slurp']).stdout)
        for page in pages:
            for event in page:
                source = event.get('source', {}).get('issue', {})
                if not source.get('pull_request') or source.get('repository_url', '').lower() != ('https://api.github.com/repos/' + host).lower():
                    continue
                number = source['number']
                if number not in prs:
                    prs[number] = json.loads(run(['gh', 'pr', 'view', str(number), '--repo', host, '--json', fields]).stdout)
        return issue_data, [prs[n] for n in sorted(prs)]

    def audit(self, task, base, issue=None, keywords=None):
        base_head = self.base_head(base)
        head, registry = self.read()
        issue_data, prs = None, []
        if issue:
            issue_data, prs = self.issue_snapshot(issue)
            query = '#' + str(issue)
        else:
            if not keywords:
                raise Refusal('Native tasks require --keywords for the prior-work audit.')
            query = keywords
            if authority(self.url).startswith('github.com/'):
                prs = json.loads(run(['gh', 'pr', 'list', '--repo', self.github(), '--state', 'all', '--limit', '100',
                                      '--search', keywords, '--json', 'number,title,state,mergedAt,url,body,headRefName,author,updatedAt']).stdout)
                if len(prs) == 100:
                    raise Refusal('PR search reached its limit. Narrow the native-task keywords.')
        history = git(self.repo, 'log', base_head, '--format=%h %an %s', '--fixed-strings', '--grep=' + query, '-n', '100').stdout
        recent = git(self.repo, 'log', base_head, '-n', '35', '--format=%h %an %s').stdout
        record = {'id': uuid.uuid4().hex, 'schema': SCHEMA, 'remote': self.identity,
                  'task': task, 'base': base, 'base_head': base_head, 'registry_head': head,
                  'created': time.time(), 'issue': issue_data, 'prs': prs,
                  'issue_history': history, 'recent_history': recent,
                  'claims': registry['claims'], 'worktrees': git(self.repo, 'worktree', 'list', '--porcelain').stdout}
        record['receipt'] = self.receipt('audits', record)
        return record

    def claim(self, receipt, owner, session, scopes, remaining):
        audit = json.loads(Path(receipt).read_text())
        if audit.get('remote') != self.identity or audit.get('schema') != SCHEMA or time.time() - audit['created'] > 900:
            raise Refusal('Audit is stale or belongs to another remote. Re-run audit.')
        if self.base_head(audit['base']) != audit['base_head']:
            raise Refusal('Integration branch changed after audit. Re-audit before claiming.')
        if audit.get('issue'):
            issue_data, prs = self.issue_snapshot(audit['issue']['number'])
            if issue_data != audit['issue'] or prs != audit['prs']:
                raise Refusal('Issue or linked PRs changed after audit. Re-audit before claiming.')
        if (audit.get('issue') or {}).get('state') == 'CLOSED':
            raise Refusal('Issue is closed. Audit the result and use a new follow-up task.')
        if not remaining.strip() or not owner.strip() or not session.strip():
            raise Refusal('Owner, distinct session and exact remaining work are required.')
        scopes = sorted(set(self.scope(s) for s in scopes))
        if not scopes:
            raise Refusal('At least one file/directory boundary is required.')
        claim_id = uuid.uuid4().hex
        record = {'id': claim_id, 'task': audit['task'], 'owner': owner, 'session': session,
                  'scopes': scopes, 'remaining': remaining, 'base': audit['base'],
                  'base_head': audit['base_head'], 'created': time.time(),
                  'updated': time.time(), 'state': 'active', 'epoch': 1}
        local = {'id': claim_id, 'remote': self.identity, 'session': session, 'epoch': 1}
        # Persist before the remote mutation. A crash/unknown push outcome must
        # remain recoverable without granting a second owner.
        lease = self.receipt('leases', local)
        def add(ledger):
            for other in ledger['claims'].values():
                if other['state'] == 'released':
                    continue
                if other['task'] == record['task'] or any(overlaps(a, b) for a in scopes for b in other['scopes']):
                    raise Refusal(f"Busy: {other['task']} is held by {other['owner']} / {other['session']} ({other['state']}). Coordinate with that owner; do not duplicate work.")
            ledger['claims'][claim_id] = record
            return record
        try:
            result, head = self.change(add)
        except (Refusal, OSError, subprocess.TimeoutExpired) as e:
            raise Refusal(f'{e} Pending receipt: {lease}. Check it after reconnecting; never assume ownership.')
        return {'claim': result, 'receipt': lease, 'registry_head': head}

    def adopt(self, claim_id, session):
        # Explicitly assigned sessions can resume on another computer. Receipts
        # are bookkeeping, not a security boundary against repository writers.
        _, ledger = self.read()
        record = ledger['claims'].get(claim_id)
        if not record or record['state'] == 'released' or record['session'] != session:
            raise Refusal('No live claim assigned to this session.')
        local = {'id': claim_id, 'remote': self.identity, 'session': session, 'epoch': record['epoch']}
        return {'claim': record, 'receipt': self.receipt('leases', local)}

    def owned(self, receipt, ledger):
        local = json.loads(Path(receipt).read_text())
        record = ledger['claims'].get(local.get('id'))
        if local.get('remote') != self.identity or not record or record['state'] == 'released' or record['session'] != local.get('session') or record['epoch'] != local.get('epoch'):
            raise Refusal('This receipt no longer owns the task. Stop and coordinate.')
        return local, record

    def update(self, receipt, action, **kwargs):
        def edit(ledger):
            local, record = self.owned(receipt, ledger)
            record['updated'] = time.time()
            if action == 'renew':
                record['state'] = 'active'
            elif action == 'park':
                if not kwargs['evidence'].strip():
                    raise Refusal('Parking needs evidence or a concrete blocker.')
                record['state'] = 'review'
                record['evidence'] = kwargs['evidence']
            elif action == 'handoff':
                if not kwargs['owner'].strip() or not kwargs['session'].strip() or kwargs['session'] == record['session']:
                    raise Refusal('Handoff requires an owner and a distinct target session.')
                record.update(owner=kwargs['owner'], session=kwargs['session'], epoch=record['epoch'] + 1, state='active')
            elif action == 'release':
                commit = kwargs['commit']
                base = self.base_head(record['base'])
                if not re.fullmatch(r'[0-9a-f]{40,64}', commit) or git(self.repo, 'merge-base', '--is-ancestor', commit, base, okay=True).returncode:
                    raise Refusal('Release requires a commit actually integrated into the shared base. Park local work instead.')
                if git(self.repo, 'merge-base', '--is-ancestor', commit, record['base_head'], okay=True).returncode == 0:
                    raise Refusal('This commit predates the claim. Supply the integrated implementation commit.')
                changed = git(self.repo, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only', '-r', commit).stdout.splitlines()
                if not any(overlaps(p, s) for p in changed for s in record['scopes']):
                    raise Refusal('The integrated commit does not touch the claimed scope.')
                record.update(state='released', evidence=commit)
            return record
        result, head = self.change(edit)
        if action == 'handoff':
            local = {'id': result['id'], 'remote': self.identity, 'session': result['session'], 'epoch': result['epoch'], 'registry_head': head}
            return {'claim': result, 'receipt': self.receipt('leases', local)}
        return {'claim': result, 'registry_head': head}

    def check(self, receipt, paths=()):
        _, ledger = self.read()
        _, record = self.owned(receipt, ledger)
        if time.time() - record['updated'] > 1800 or record['state'] != 'active':
            raise Refusal('Ownership is paused or heartbeat is stale. Renew/check before editing; it is not free to others.')
        for p in paths:
            p = self.scope(p)
            if not any(scope == '.' or p.casefold() == scope.casefold() or p.casefold().startswith(scope.casefold() + '/') for scope in record['scopes']):
                raise Refusal('Path is outside this claim: ' + p)
        return record

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', default='.')
    p.add_argument('--remote', default='origin')
    sub = p.add_subparsers(dest='action', required=True)
    audit = sub.add_parser('audit')
    key = audit.add_mutually_exclusive_group(required=True)
    key.add_argument('--issue', type=int)
    key.add_argument('--task')
    audit.add_argument('--base', required=True)
    audit.add_argument('--keywords')
    sub.add_parser('list')
    adopt = sub.add_parser('adopt')
    adopt.add_argument('--id', required=True)
    adopt.add_argument('--session', required=True)
    claim = sub.add_parser('claim')
    claim.add_argument('--audit', required=True)
    claim.add_argument('--owner', required=True)
    claim.add_argument('--session', required=True)
    claim.add_argument('--path', action='append', required=True)
    claim.add_argument('--remaining', required=True)
    for name in ('check', 'renew', 'park', 'handoff', 'release'):
        command = sub.add_parser(name)
        command.add_argument('--receipt', required=True)
        if name == 'check':
            command.add_argument('--path', action='append', default=[])
        if name == 'park':
            command.add_argument('--evidence', required=True)
        if name == 'handoff':
            command.add_argument('--owner', required=True)
            command.add_argument('--session', required=True)
        if name == 'release':
            command.add_argument('--integrated-commit', required=True)
    a = p.parse_args()
    r = Registry(a.repo, a.remote)
    if a.action == 'audit':
        if a.issue is not None and a.issue <= 0:
            raise Refusal('Issue number must be positive.')
        if a.task is not None and not re.fullmatch(r'[a-z0-9][a-z0-9._:-]*', a.task):
            raise Refusal('Native task IDs must be stable lowercase slugs or provider IDs, without spaces.')
        task = 'issue:' + str(a.issue) if a.issue else 'task:' + a.task
        result = r.audit(task, a.base, a.issue, a.keywords)
    elif a.action == 'list':
        head, record = r.read()
        result = {'head': head, **record}
    elif a.action == 'adopt':
        result = r.adopt(a.id, a.session)
    elif a.action == 'claim':
        result = r.claim(a.audit, a.owner, a.session, a.path, a.remaining)
    elif a.action == 'check':
        result = r.check(a.receipt, a.path)
    else:
        result = r.update(a.receipt, a.action, evidence=getattr(a, 'evidence', None),
                          owner=getattr(a, 'owner', None), session=getattr(a, 'session', None),
                          commit=getattr(a, 'integrated_commit', None))
    print(json.dumps({'ok': True, 'result': result}, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (Refusal, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        print(json.dumps({'ok': False, 'error': str(e)}))
        sys.exit(2)
