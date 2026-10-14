#!/usr/bin/env python3
"""Validate a v3 planning store and render its index. No network or Git writes."""
import argparse
import hashlib
import json
import re
from pathlib import Path

QUEUES = ('now', 'next', 'someday', 'blocked', 'done')
STATUSES = {'open', 'in-progress', 'blocked', 'done', 'canceled'}
REQUIRED = {'id', 'title', 'status', 'queue', 'priority', 'rank', 'goals',
            'depends_on', 'milestone', 'plan', 'issue'}
SECTIONS = ('Outcome', 'Source', 'Scope', 'Acceptance', 'Steps',
            'Priority reason', 'Blocker', 'Next action', 'Evidence',
            'Execution claim', 'Decisions and changes')
SLUG = r'[a-z0-9]+(?:-[a-z0-9]+)*'
TASK = r'TASK-\d{3,}'


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def fingerprint(root):
    """Detect local changes between reading the store and replacing the index."""
    paths = [root / 'config.json', root / 'goals.md', root / 'tasks.md']
    paths += sorted((root / 'items').glob('*.md'))
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
            for p in paths}


def safe_path(root, relative):
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), f'Path escapes planning root: {relative}')
    return path


def metadata(path):
    raw = path.read_text(encoding='utf-8')
    require(raw.startswith('---\n'), f'{path.name}: missing frontmatter')
    parts = raw.split('\n---\n', 1)
    require(len(parts) == 2, f'{path.name}: unclosed frontmatter')
    data = {}
    for line in parts[0].splitlines()[1:]:
        require(': ' in line, f'{path.name}: expected flat key: JSON-value')
        key, value = line.split(': ', 1)
        require(key not in data, f'{path.name}: duplicate field {key}')
        try:
            data[key] = json.loads(value)
        except json.JSONDecodeError as exc:
            raise Invalid(f'{path.name}: {key} must be a JSON literal') from exc
    require(REQUIRED <= data.keys(), f'{path.name}: missing {sorted(REQUIRED - data.keys())}')
    body = parts[1]
    for section in SECTIONS:
        match = re.search(r'^## ' + re.escape(section) + r'\n(.*?)(?=^## |\Z)', body, re.M | re.S)
        require(match and match[1].strip(), f'{path.name}: missing/empty section {section}')
    return data


def load_store(root):
    root = root.resolve()
    cfg = json.loads((root / 'config.json').read_text(encoding='utf-8'))
    require(cfg.get('schema_version') == 3, 'Legacy/unknown store: explicit upgrade required; index left untouched')
    for field in ('project_id', 'owner_id'):
        require(isinstance(cfg.get(field), str) and re.fullmatch(SLUG, cfg[field]), f'Invalid {field}')
        require(not cfg[field].startswith('replace-'), f'Unresolved {field}')
    require(cfg.get('storage') in ('workspace', 'repository'), 'Invalid storage')
    planning = cfg.get('planning', {})
    require(planning.get('canonical_system') == 'norml-tasks', 'Another system owns planning')
    require(planning.get('lane') in ('quick', 'project'), 'Invalid planning lane')
    require(type(planning.get('commit_docs')) is bool, 'commit_docs must be boolean')
    active = planning.get('active_milestones')
    require(isinstance(active, list) and len(active) == len(set(active)), 'Invalid/duplicate active milestones')
    for slug in active:
        require(isinstance(slug, str) and re.fullmatch(SLUG, slug), 'Invalid milestone slug')
        require(safe_path(root, f'milestones/{slug}/state.md').is_file(), f'Missing milestone state: {slug}')
    locations = cfg.get('locations', {})
    require('workspace' in locations and isinstance(locations.get('repositories'), list), 'Missing location map')
    owners = []
    entries = ([locations['workspace']] if locations['workspace'] is not None else []) + locations['repositories']
    for entry in entries:
        require(isinstance(entry, dict), 'Invalid location entry')
        oid = entry.get('owner_id')
        require(isinstance(oid, str) and re.fullmatch(SLUG, oid), 'Invalid mapped owner')
        owners.append(oid)
        path = entry.get('planning_path', entry.get('path'))
        require(isinstance(path, str) and not Path(path).is_absolute() and '..' not in Path(path).parts
                and '\\' not in path and ':' not in path and not path.startswith('~')
                and (path == '.claude/tasks' or path.endswith('/.claude/tasks')), 'Invalid portable planning path')
        if entry.get('repository') is not None:
            require(isinstance(entry['repository'], str) and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', entry['repository']), 'Invalid mapped repository')
    require(len(owners) == len(set(owners)), 'Duplicate mapped owner IDs')
    require(cfg['owner_id'] in owners, 'Current owner is absent from location map')
    github = cfg.get('github', {})
    require(type(github.get('enabled')) is bool, 'github.enabled must be boolean')
    if cfg['storage'] == 'workspace':
        require(locations['workspace'] is not None and locations['workspace']['owner_id'] == cfg['owner_id'], 'workspace owner mismatch')
        require(not github['enabled'] and not planning['commit_docs'], 'workspace cannot enable GitHub/Git publication')
    else:
        own_repo = [e for e in locations['repositories'] if e['owner_id'] == cfg['owner_id']]
        require(len(own_repo) == 1, 'Repository owner missing')
        if github['enabled']:
            require(isinstance(own_repo[0].get('repository'), str), 'GitHub mirroring requires a verified repository identity')
            require(github.get('repository') == own_repo[0]['repository'], 'GitHub repository mismatch')
    require((root / 'items').is_dir() and not (root / 'items').is_symlink(), 'Missing/linked items directory')
    goals = (root / 'goals.md').read_text(encoding='utf-8')
    declared_goals = re.findall(r'^### (GOAL-\d+)\b', goals, re.M)
    require(len(declared_goals) == len(set(declared_goals)), 'Duplicate goal IDs')
    goal_ids = set(declared_goals)
    items, external = {}, set()
    for path in sorted((root / 'items').glob('*.md')):
        require(not path.is_symlink(), 'Task symlinks are not supported')
        data = metadata(path)
        tid = data['id']
        require(isinstance(tid, str) and re.fullmatch(TASK, tid), f'{path.name}: invalid task ID')
        require(tid not in items, f'Duplicate ID: {tid}')
        require(re.fullmatch(tid.lower() + '-' + SLUG + r'\.md', path.name), f'{tid}: filename/ID mismatch')
        require(isinstance(data['title'], str) and data['title'].strip(), f'{tid}: empty title')
        require(data['status'] in STATUSES and data['queue'] in QUEUES, f'{tid}: invalid status/queue')
        require(data['priority'] in ('P0', 'P1', 'P2', 'P3'), f'{tid}: invalid priority')
        require(type(data['rank']) is int and data['rank'] > 0, f'{tid}: invalid rank')
        status, queue = data['status'], data['queue']
        require((status == 'blocked') == (queue == 'blocked'), f'{tid}: blocked status/queue mismatch')
        require((status in ('done', 'canceled')) == (queue == 'done'), f'{tid}: terminal status/queue mismatch')
        require(status != 'in-progress' or queue == 'now', f'{tid}: in-progress requires Now')
        for field, pattern in [('goals', r'GOAL-\d+'), ('depends_on', TASK)]:
            refs = data[field]
            require(isinstance(refs, list) and all(isinstance(x, str) for x in refs), f'{tid}: invalid {field}')
            require(len(refs) == len(set(refs)), f'{tid}: duplicate {field}')
            for ref in refs:
                require(re.fullmatch(r'(?:' + SLUG + r'::)?' + pattern, ref), f'{tid}: invalid reference {ref}')
                owner, local = ref.split('::', 1) if '::' in ref else (cfg['owner_id'], ref)
                if owner != cfg['owner_id']:
                    require(owner in owners, f'{tid}: unmapped external owner {owner}')
                    external.add(ref)
                elif field == 'goals':
                    require(local in goal_ids, f'{tid}: missing goal {local}')
        milestone, plan = data['milestone'], data['plan']
        require(milestone is None or isinstance(milestone, str) and re.fullmatch(SLUG, milestone), f'{tid}: invalid milestone')
        if milestone:
            require(safe_path(root, f'milestones/{milestone}/state.md').is_file(), f'{tid}: missing milestone')
        require(plan is None or isinstance(plan, str) and re.fullmatch(r'\d{2}-\d{2}', plan), f'{tid}: invalid plan')
        if plan:
            require(milestone is not None, f'{tid}: plan without milestone')
            matches = list((root / 'milestones' / milestone / 'phases').glob(f'{plan[:2]}-*/{plan}-plan.md'))
            require(len(matches) == 1, f'{tid}: missing/ambiguous plan file')
        if data['issue'] is not None:
            require(isinstance(data['issue'], str) and re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/[1-9]\d*', data['issue']), f'{tid}: invalid issue URL')
            require(cfg['storage'] == 'repository' and '/'.join(data['issue'].split('/')[3:5]) == own_repo[0]['repository'], f'{tid}: issue repository mismatch')
        data['path'] = path.relative_to(root).as_posix()
        items[tid] = data
    issues = [x['issue'] for x in items.values() if x['issue']]
    require(len(issues) == len(set(issues)), 'Multiple tasks point to the same issue')
    graph = {}
    for tid, data in items.items():
        deps = [r.split('::')[-1] for r in data['depends_on'] if '::' not in r or r.split('::')[0] == cfg['owner_id']]
        require(all(d in items for d in deps), f'{tid}: missing local dependency')
        graph[tid] = deps
    visited, visiting = set(), set()
    def visit(tid):
        require(tid not in visiting, f'Dependency cycle involving {tid}')
        if tid in visited:
            return
        visiting.add(tid)
        for dep in graph[tid]:
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)
    for tid in graph:
        visit(tid)
    for tid, deps in graph.items():
        if items[tid]['queue'] == 'now':
            require(all(items[d]['status'] == 'done' for d in deps), f'{tid}: Now has an unfinished local prerequisite')
    return cfg, items, sorted(external)


def cell(value):
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')


def render(cfg, items):
    lines = [f"# Tasks — {cfg['owner_id']}", '', '> Navigation generated from canonical task files. Change the item first, then rebuild this index.', '',
             'Goals: [goals.md](goals.md). Locations and active milestones: [config.json](config.json).', '', '## Active milestones', '']
    for slug in cfg['planning']['active_milestones']:
        lines.append(f'- [{slug}](milestones/{slug}/state.md)')
    if not cfg['planning']['active_milestones']:
        lines.append('None')
    for queue in QUEUES:
        lines += ['', f'## {queue.title()}', '', '| Task | Priority | Status | Goals | Depends on | Issue |', '|---|---|---|---|---|---|']
        for task in sorted((x for x in items.values() if x['queue'] == queue), key=lambda x: (x['rank'], x['id'])):
            issue = f"[issue]({task['issue']})" if task['issue'] else '—'
            lines.append(f"| [{task['id']} — {cell(task['title'])}]({task['path']}) | {task['priority']} | {task['status']} | {cell(', '.join(task['goals'])) or '—'} | {cell(', '.join(task['depends_on'])) or '—'} | {issue} |")
    return '\n'.join(lines) + '\n'


def write_index(root, text, before):
    require(fingerprint(root) == before, 'Store changed since read; re-read before writing index')
    target = root / 'tasks.md'
    require(not target.is_symlink(), 'Index symlink is not supported')
    temp = root / '.tasks-index.tmp'
    with temp.open('x', encoding='utf-8') as handle:
        handle.write(text)
    try:
        require(fingerprint(root) == before, 'Store changed during render; index left untouched')
        temp.replace(target)
    finally:
        temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['check', 'index'])
    parser.add_argument('root', type=Path, help='Owner .claude/tasks directory')
    parser.add_argument('--write', action='store_true', help='Replace only tasks.md (index action only)')
    args = parser.parse_args()
    try:
        require(not args.write or args.action == 'index', '--write requires index action')
        before = fingerprint(args.root)
        cfg, items, external = load_store(args.root)
        rendered = render(cfg, items)
        if args.action == 'index':
            if args.write:
                write_index(args.root, rendered, before)
                print(f'Index written: {len(items)} task(s)')
            else:
                print(rendered, end='')
        else:
            require((args.root / 'tasks.md').read_text(encoding='utf-8') == rendered, 'Index is stale; run index --write')
            print(f'Local structure OK: {len(items)} task(s); domain acceptance not evaluated')
        if external:
            print('UNVERIFIED external references (read their canonical stores): ' + ', '.join(external))
    except (Invalid, OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'Planning check failed: {exc}\n')


if __name__ == '__main__':
    main()
