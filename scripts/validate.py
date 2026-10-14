#!/usr/bin/env python3
"""Validate package identity, anatomy, Python syntax, links and private boundaries."""
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = set('norml-ci-cd norml-page-structures norml-page-types norml-performance-audit norml-wp-architecture norml-wp-developer norml-seo-basics norml-seo-schema norml-seo-technical-analysis norml-changelog norml-connect norml-drive norml-git norml-security norml-tasks norml-skill-creator'.split())
PRIVATE = re.compile(r'Norml Drive[/\\]|norml-studio/credentials|\{norml-claude-skills\}|(?-i:/Users/[^/\s]+/)|/home/[^/\s]+/|GoogleDrive-[^/\s]+@|(?:access|go|maxtymosh)@norml\.studio|(?:time|twenty|normlstudio\.slack)\.norml\.studio|handers\.digital|antssports\.com', re.I)
SECRET = re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bxox[baprs]-[A-Za-z0-9-]{25,}\b|\bAIza[0-9A-Za-z_-]{30,}\b')


def validate():
    issues, count = [], 0
    skills = ROOT / '.claude' / 'skills'
    actual = {p.name for p in skills.iterdir() if p.is_dir()}
    if actual != EXPECTED:
        issues.append('Skill selection differs from the requested 16')
    for name in sorted(actual):
        folder = skills / name
        if folder.is_symlink():
            issues.append(name + ': source skill folder is a symlink')
            continue
        for mandatory in ['SKILL.md', 'changelog.md', 'readme.md', 'readme.data.json', 'readme.html']:
            if not (folder / mandatory).is_file():
                issues.append(name + ': missing ' + mandatory)
        entry = (folder / 'SKILL.md').read_text()
        if not re.search(r'^name:\s*' + re.escape(name) + r'\s*$', entry, re.M):
            issues.append(name + ': mismatched frontmatter name')
        if not re.search(r'^version:\s*1\.0\.0\s*$', entry, re.M):
            issues.append(name + ': unexpected initial version')
        data = json.loads((folder / 'readme.data.json').read_text())
        if data.get('skill') != name or data.get('version') != '1.0.0':
            issues.append(name + ': stale human-doc identity')
        for p in folder.rglob('*'):
            if p.is_symlink():
                issues.append(str(p.relative_to(ROOT)) + ': source symlink')
                continue
            if not p.is_file():
                if p.name in {'references', 'reference', 'misc', 'knowledge'}:
                    issues.append(name + ': generic support folder')
                continue
            count += 1
            rel = str(p.relative_to(ROOT))
            if p.is_symlink() or p.suffix in {'.pyc', '.xlsx', '.xls', '.docx', '.doc'}:
                issues.append(rel + ': forbidden artifact')
                continue
            try:
                content = p.read_text()
            except UnicodeDecodeError:
                issues.append(rel + ': unexpected binary')
                continue
            if PRIVATE.search(content):
                issues.append(rel + ': private/machine-specific boundary match')
            if SECRET.search(content):
                issues.append(rel + ': secret-like material (value suppressed)')
            if p.suffix == '.py':
                try:
                    ast.parse(content)
                except SyntaxError:
                    issues.append(rel + ': Python syntax error')
            if p.suffix == '.md':
                if p.name != 'SKILL.md' and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md', p.name):
                    issues.append(rel + ': noncanonical Markdown basename')
                for link in re.findall(r'\]\(([^)\n]+)\)', content):
                    link = link.split()[0].strip('<>')
                    if re.match(r'^[a-z]+:', link) or link.startswith('#') or '{' in link:
                        continue
                    target = unquote(link.split('#')[0])
                    if target and not (p.parent / target).exists():
                        issues.append(rel + ': unresolved local link ' + target)
    return {'ok': not issues, 'skills': len(actual), 'files': count, 'issues': issues}


if __name__ == '__main__':
    result = validate()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['ok'] else 1)
