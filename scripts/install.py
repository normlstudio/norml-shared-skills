#!/usr/bin/env python3
"""Copy complete public skill folders without replacing existing installations."""
import argparse
from pathlib import Path
import shutil
import sys

SOURCE = Path(__file__).resolve().parents[1] / '.claude' / 'skills'


def plan(destination, names=None):
    destination = Path(destination).expanduser().absolute()
    if any(p.is_symlink() for p in [destination, *destination.parents]):
        raise ValueError('Destination contains a symlink; choose a real isolated directory')
    if any(p.is_symlink() for p in [SOURCE, *SOURCE.parents]):
        raise ValueError('Source contains a symlink; choose a complete real package tree')
    available = {p.name: p for p in SOURCE.iterdir() if p.is_dir()}
    selected = list(dict.fromkeys(names or sorted(available)))
    if not selected or any(n not in available for n in selected):
        raise ValueError('Unknown or empty skill selection')
    plans = []
    for name in selected:
        src, dest = available[name], destination / name
        if src.is_symlink():
            raise ValueError('Source skill is a symlink: ' + name)
        if dest.exists() or dest.is_symlink():
            raise FileExistsError('Existing skill preserved: ' + name)
        if any(p.is_symlink() for p in src.rglob('*')):
            raise ValueError('Source package contains a symlink: ' + name)
        if destination.is_relative_to(src):
            raise ValueError('Destination is inside the source package')
        plans.append((src, dest))
    return plans


def install(destination, names=None, dry_run=False):
    plans = plan(destination, names)
    if dry_run:
        return [dest.name for _, dest in plans]
    Path(destination).expanduser().mkdir(parents=True, exist_ok=True)
    for source, dest in plans:
        shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    return [dest.name for _, dest in plans]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', required=True)
    parser.add_argument('--skill', action='append')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    copied = install(args.destination, args.skill, args.dry_run)
    print(('Planned' if args.dry_run else 'Installed') + ': ' + ', '.join(copied))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
