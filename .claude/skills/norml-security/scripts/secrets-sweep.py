#!/usr/bin/env python3
"""Explicit local-path leak detection with opt-in redaction; no secret previews."""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Pattern catalog
# ---------------------------------------------------------------------------
#
# Each entry: (id, confidence, regex, category, description)
#
# Confidence levels:
#   high   — auto-redact when --redact is on; vanishingly small false-positive
#            rate (service-prefixed keys, SSH key blocks, shell secrets-on-argv).
#   medium — report only; user reviews before redaction (contextual, can
#            false-positive on legitimate strings of similar shape).
#
# Patterns are evaluated in order; for overlapping matches, first-wins.
PATTERNS = [
    # --- High confidence: service-prefixed API keys ---
    ("anthropic_key", "high",
     r"sk-ant-[A-Za-z0-9_-]{20,}",
     "anthropic_api_key",
     "Anthropic API key"),
    # OpenAI keys: contiguous alphanumeric (no hyphens) after `sk-` or `sk-proj-`.
    # Underscores allowed for newer project-scoped keys. Hyphens explicitly
    # excluded — `sk-` followed by hyphens matches English-word substrings
    # like `sk-exists-for-a-task-use-it`, which was a real false-positive
    # against memory file slugs.
    ("openai_key", "high",
     r"sk-(?:proj-)?[A-Za-z0-9_]{20,}",
     "openai_api_key",
     "OpenAI API key (incl. project-scoped)"),
    ("github_pat_classic", "high",
     r"ghp_[A-Za-z0-9]{30,}",
     "github_pat",
     "GitHub personal access token (classic)"),
    ("github_pat_finegrained", "high",
     r"github_pat_[A-Za-z0-9_]{20,}",
     "github_pat",
     "GitHub personal access token (fine-grained)"),
    ("github_oauth", "high",
     r"gho_[A-Za-z0-9]{30,}",
     "github_token",
     "GitHub OAuth token"),
    ("github_app", "high",
     r"(?:ghs_|ghu_|ghr_)[A-Za-z0-9]{30,}",
     "github_token",
     "GitHub app/user/refresh token"),
    ("slack_bot", "high",
     r"xoxb-[A-Za-z0-9-]{20,}",
     "slack_token",
     "Slack bot token"),
    ("slack_user", "high",
     r"xoxp-[A-Za-z0-9-]{20,}",
     "slack_token",
     "Slack user token"),
    ("slack_app", "high",
     r"xoxa-[A-Za-z0-9-]{20,}",
     "slack_token",
     "Slack app token"),
    ("slack_refresh", "high",
     r"xoxe\.xoxp-[A-Za-z0-9-]{20,}",
     "slack_token",
     "Slack refresh token"),
    ("aws_access_key", "medium",
     r"AKIA[0-9A-Z]{16}",
     "aws_credential",
     "AWS access key ID"),
    ("google_api", "high",
     r"AIza[0-9A-Za-z_-]{35}",
     "google_api_key",
     "Google API key"),
    ("stripe_live", "high",
     r"sk_live_[A-Za-z0-9]{20,}",
     "stripe_key",
     "Stripe live secret key"),
    ("stripe_test", "high",
     r"sk_test_[A-Za-z0-9]{20,}",
     "stripe_key",
     "Stripe test secret key"),
    ("twilio_account_sid_with_token", "medium",
     r"(?<![A-Za-z0-9])AC[0-9a-f]{32}(?![A-Za-z0-9])",
     "twilio_credential",
     "Twilio account SID (heuristic — may need pairing with auth token)"),

    # --- High confidence: SSH private key blocks ---
    # The `[^\n]+?` between BEGIN/END means we only match within a single file
    # line. This is correct for .jsonl transcripts (where the entire key block
    # is JSON-encoded on one physical line with embedded `\n` escapes) and
    # avoids collapsing multiple JSON records together. Plain-text files with
    # multi-line key blocks are picked up by `ssh_private_key_header` below
    # (header-line-only — enough to flag the file for manual review).
    ("ssh_private_key", "high",
     r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----[^\n]+?-----END (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----",
     "ssh_private_key",
     "SSH/PGP private key block (single-line / JSON-encoded)"),
    ("ssh_private_key_header", "high",
     r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----",
     "ssh_private_key_header",
     "SSH/PGP private key header (flags multi-line block — content not redacted by this pattern)"),

    # --- High confidence: shell artifacts with secret-on-argv ---
    # `security add-generic-password ... -w <value>` where <value> is non-empty
    # AND looks like an actual password (≥4 non-quote, non-backslash chars).
    # Filters out the safe `-w<EOL>` form and the false-positive `-w "}` form
    # where the regex would otherwise overrun into JSON syntax.
    ("keychain_inline", "high",
     r"security\s+add-generic-password\s+(?:[^\n\"]*?\s)?-w\s+[A-Za-z0-9][^\s\"\\]{3,}",
     "shell_secret_on_argv",
     "macOS Keychain `security add-generic-password ... -w <inline-value>`"),

    # `curl -u USER:PASS` where PASS isn't a variable
    ("curl_basic_auth_literal", "high",
     r"curl\s+(?:[^\n]*?\s)?-u\s+[\w.-]+:[^\s$\"'\n]{8,}",
     "shell_secret_on_argv",
     "curl basic auth with literal password on argv"),

    # `Authorization: Bearer <token>` in HTTP-request-shaped text where token is non-trivial
    ("bearer_token", "high",
     r"(?i)Authorization:\s*Bearer\s+[A-Za-z0-9_\-.=]{20,}",
     "bearer_token",
     "HTTP Authorization Bearer token"),

    # --- Medium confidence: contextual / shape-based ---
    # WordPress Application Password format: 6 groups of 4 alphanums separated by single spaces.
    # Very specific shape — but legitimate strings of this shape DO exist.
    # Report only; user decides.
    ("wp_app_pwd_format", "medium",
     r"(?<![A-Za-z0-9])[A-Za-z0-9]{4} [A-Za-z0-9]{4} [A-Za-z0-9]{4} [A-Za-z0-9]{4} [A-Za-z0-9]{4} [A-Za-z0-9]{4}(?![A-Za-z0-9])",
     "wp_app_password",
     "WordPress Application Password (24 chars, formatted)"),

    # NOTE: A `wp_app_pwd_compact` pattern (bare 24-char alphanum) was tried
    # and removed — false-positive rate was ~99.99% (matches every UUID,
    # truncated hash, base64 chunk in transcripts). The formatted version
    # above (six groups of 4 chars separated by single spaces) is the natural
    # form WordPress shows users; that's the catchable shape.

    # JWT-shaped tokens (header.payload.signature)
    ("jwt_token", "medium",
     r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
     "jwt",
     "JWT (JSON Web Token)"),
]


REDACTION_MARKER_FMT = "<REDACTED:norml-security:{date}:{category}>"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def short_preview(matched: str, side: int = 4) -> str:
    """Return 'abcd...wxyz' style preview; full asterisks for very short matches."""
    s = matched
    if len(s) <= side * 2 + 3:
        return "<hidden>"
    return "<hidden>"


def make_marker(category: str) -> str:
    return REDACTION_MARKER_FMT.format(
        date=datetime.now().strftime("%Y-%m-%d"),
        category=category,
    )


# Files whose names suggest they hold example/placeholder secrets — used to
# downgrade false-positive risk. Currently only the skill docs themselves.
def is_skill_doc(path: Path) -> bool:
    parts = str(path).replace("\\", "/")
    return ("/.claude/skills/" in parts
            and path.suffix in (".md",))


def scan_text(content: str, path: Path):
    """
    Yield (pattern_id, confidence, category, span_start, span_end, preview)
    for each match, skipping spans inside an existing REDACTED marker.
    """
    redacted_spans = [m.span() for m in re.finditer(
        r"<REDACTED:norml-security:[^>]+>", content)]

    def inside_redacted(start: int, end: int) -> bool:
        for rs, re_ in redacted_spans:
            if rs <= start < re_ or rs < end <= re_:
                return True
        return False

    # Track spans we've already reported to avoid double-counting overlaps
    reported = []

    def overlaps_reported(start: int, end: int) -> bool:
        for rs, re_ in reported:
            if not (end <= rs or start >= re_):
                return True
        return False

    skill_doc = is_skill_doc(path)

    for pid, conf, regex, category, _desc in PATTERNS:
        for m in re.finditer(regex, content):
            if inside_redacted(m.start(), m.end()):
                continue
            if overlaps_reported(m.start(), m.end()):
                continue
            # Skill docs: skip medium-confidence matches (likely placeholders /
            # examples). High-confidence still applies — real keys in docs are
            # real keys.
            reported.append((m.start(), m.end()))
            yield pid, conf, category, m.start(), m.end(), short_preview(m.group())


def redact_text(content: str, path: Path, high_only: bool = True) -> tuple[str, int]:
    """
    Return (new_content, count_redacted).
    Replaces matched spans with REDACTION markers. Idempotent — skips spans
    already inside a REDACTED marker.
    """
    findings = list(scan_text(content, path))
    if not findings:
        return content, 0

    if high_only:
        findings = [f for f in findings if f[1] == "high"]
    if not findings:
        return content, 0

    # Apply replacements from the end backwards so offsets stay valid
    findings_sorted = sorted(findings, key=lambda f: f[3], reverse=True)
    new_content = content
    count = 0
    for pid, conf, category, start, end, _preview in findings_sorted:
        marker = make_marker(category)
        new_content = new_content[:start] + marker + new_content[end:]
        count += 1
    return new_content, count


def validate_jsonl(content: str) -> bool:
    """Return True if every non-empty line parses as JSON."""
    for line in content.split("\n"):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError:
            return False
    return True



TEXT_SUFFIXES = {'.json', '.jsonl', '.md', '.txt', '.log', '.sh', '.py', '.ps1', '.yaml', '.yml'}


def gather_explicit(paths, limit):
    targets, errors, skipped, seen = [], [], [], set()
    for raw in paths:
        root = Path(raw).expanduser()
        if root.is_symlink() or not root.exists():
            errors.append(str(root) + ': missing/symlink root refused')
            continue
        candidates = [root] if root.is_file() else list(root.rglob('*'))
        for candidate in candidates:
            if candidate.is_symlink():
                errors.append(str(candidate) + ': symlink refused')
                continue
            if not candidate.is_file():
                continue
            if candidate.suffix not in TEXT_SUFFIXES:
                skipped.append(str(candidate) + ': unsupported suffix')
                continue
            try:
                resolved = candidate.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                if candidate.stat().st_size > limit * 1024 * 1024:
                    skipped.append(str(candidate) + ': exceeds size ceiling')
                    continue
                targets.append(candidate)
            except OSError:
                errors.append(str(candidate) + ': unavailable metadata')
    return targets, errors, skipped


def private_backup_root(configured, scan_roots):
    """Keep original plaintext outside every selected input tree."""
    import stat
    import tempfile
    if configured:
        root = Path(configured).expanduser()
        if root.is_symlink():
            raise ValueError('Symlink backup directory refused')
        root.mkdir(parents=True, mode=0o700, exist_ok=True)
    else:
        root = Path(tempfile.mkdtemp(prefix='secret-sweep-backups-'))
    root = root.resolve()
    for selected in scan_roots:
        selected = Path(selected).expanduser().resolve()
        boundary = selected if selected.is_dir() else selected.parent
        if root == boundary or root.is_relative_to(boundary):
            raise ValueError('Backup directory must be outside every scanned input tree')
    metadata = root.stat()
    if not stat.S_ISDIR(metadata.st_mode) or stat.S_IMODE(metadata.st_mode) & 0o077:
        raise ValueError('Backup directory must have private permissions (700)')
    if hasattr(os, 'getuid') and metadata.st_uid != os.getuid():
        raise ValueError('Backup directory must be owned by the current user')
    return root


def preserve_replace(path, content, replacement, backup_root):
    import stat
    import tempfile
    metadata = path.stat()
    if path.is_symlink() or metadata.st_nlink != 1:
        raise ValueError('Symlink/hard-link input refused')
    if path.read_text(encoding='utf-8') != content:
        raise ValueError('Input changed after read; no overwrite')
    backup_root = private_backup_root(backup_root, [path])
    backup = backup_root / (str(time.time_ns()) + '-' + path.name + '.bak')
    with backup.open('x', encoding='utf-8') as handle:
        backup.chmod(0o600)
        handle.write(content)
    fd, temporary = tempfile.mkstemp(prefix='.redacted-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            handle.write(replacement)
        os.chmod(temporary, stat.S_IMODE(metadata.st_mode))
        if path.is_symlink() or path.stat().st_nlink != 1 or path.read_text(encoding='utf-8') != content:
            raise ValueError('Input changed during write; no overwrite')
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return backup


def main(argv=None):
    import tempfile
    parser = argparse.ArgumentParser(description='Scan explicit local text paths; values and previews stay hidden.')
    parser.add_argument('--path', action='append', required=True, help='Repeat for each authorized file/directory')
    parser.add_argument('--redact', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--include-medium', action='store_true')
    parser.add_argument('--max-file-mb', type=int, default=50)
    parser.add_argument('--report-dir')
    parser.add_argument('--backup-dir', help='Explicit private non-synced directory outside input trees; default: private OS temporary directory')
    args = parser.parse_args(argv)
    if args.max_file_mb <= 0 or (args.dry_run and not args.redact):
        parser.error('Positive size ceiling required; --dry-run requires --redact')
    targets, errors, skipped = gather_explicit(args.path, args.max_file_mb)
    rows, remaining_high, redactions = [], 0, 0
    backup_root = None
    for path in targets:
        try:
            content = path.read_text(encoding='utf-8')
            findings = list(scan_text(content, path))
            rows.extend(f'{path}: {pid} confidence={confidence} category={category}'
                        for pid, confidence, category, *_ in findings)
            actionable = [f for f in findings if f[0] != 'ssh_private_key_header'
                          and (f[1] == 'high' or args.include_medium)]
            high = sum(f[1] == 'high' for f in findings)
            remaining_high += high
            if not args.redact or not actionable:
                continue
            replacement = content
            for pid, confidence, category, begin, end, _ in sorted(actionable, key=lambda f: f[3], reverse=True):
                replacement = replacement[:begin] + make_marker(category) + replacement[end:]
            if path.suffix == '.jsonl' and not validate_jsonl(replacement):
                raise ValueError('Redacted JSONL would be invalid')
            if path.suffix == '.json':
                json.loads(replacement)
            if not args.dry_run:
                if backup_root is None:
                    backup_root = private_backup_root(args.backup_dir, args.path)
                preserve_replace(path, content, replacement, backup_root)
                remaining_high -= sum(f[1] == 'high' for f in actionable)
            redactions += len(actionable)
        except (OSError, UnicodeError, ValueError):
            errors.append(str(path) + ': read/write/integrity/concurrent-change refusal')
    if args.report_dir:
        report_root = Path(args.report_dir).expanduser()
        if report_root.is_symlink():
            parser.error('Symlink report directory refused')
        report_root.mkdir(parents=True, exist_ok=True)
    else:
        report_root = Path(tempfile.mkdtemp(prefix='secret-sweep-report-'))
    report = report_root / ('sweep-' + str(time.time_ns()) + '.txt')
    summary = f'Scanned={len(targets)} findings={len(rows)} unresolved-high={remaining_high} errors={len(errors)} skipped={len(skipped)} redaction-spans={redactions}'
    with report.open('x', encoding='utf-8') as handle:
        report.chmod(0o600)
        handle.write(summary + '\n' + '\n'.join(rows + errors + skipped) + '\n')
    print(summary)
    print('Report: ' + str(report))
    if backup_root is not None:
        print('Private original backups retained: ' + str(backup_root))
    return 1 if errors else 2 if remaining_high else 0


if __name__ == '__main__':
    sys.exit(main())
