# Explicitly scoped local leak sweep

Use Python 3.10+. Choose exact authorized files/directories; paths are never defaulted to a home,
transcript tree, temporary directory or credentials registry. No secret values or previews are emitted.

```bash
python3 "{skill-root}/scripts/secrets-sweep.py" --path "{scan-root}"
python3 "{skill-root}/scripts/secrets-sweep.py" --path "{scan-root}" --redact --dry-run
python3 "{skill-root}/scripts/secrets-sweep.py" --path "{scan-root}" --redact
```

Multiple roots repeat `--path`. The report contains pattern/confidence/category/count and paths.
Directory recursion covers selected text suffixes; `--max-file-mb` sets the size ceiling. Unknown
encoding, symlinks, non-regular files or changed content are reported, never silently redacted.
The default report is restricted local temporary output; `--report-dir` is an explicitly chosen
private output directory. Original plaintext backups never sit beside scanned files.
Actual redaction uses a separate private OS temporary directory by default, retained and printed
after the run. To choose persistent backup storage, pass `--backup-dir "{private-backup-dir}"`
with an explicit private, non-synced directory outside every selected input tree. It must be owned
by the current user with 700 permissions; each original backup is 600. `--report-dir` controls
reports only and never selects where original plaintext backups go. Do not choose shared/synced
folders for either output. Verify backup files before authorizing exact-path cleanup; retained
backups are never automatically aged out or deleted by the scanner.

Report-only finds candidates; review private context before redacting. `--include-medium` expands
opt-in redaction to higher-false-positive JWT/formatted app-password shapes. `--redact --dry-run`
changes no inputs but does create the non-secret report. Private-key header findings cannot safely
redact a multiline key block and stay report-only with a nonzero unresolved result. Rotate/revoke
actual exposed keys; redaction is not cryptographic revocation.

Before actual writes, the helper checks content still matches its read snapshot, refuses multiple
hard links, creates a restricted original backup, preserves mode and validates JSON/JSONL output.
Do not treat it as a distributed writer lock. Stop concurrent writers before redaction. JSON safety
is syntax, not preservation of every application's semantics; review high-confidence false positives.

Exit 0: no unresolved selected high findings/errors; 2: candidate high findings remain; 1: errors.
Backups still contain the original secrets: restrict access, verify sanitized files/readback, then
remove only approved exact backup paths. No automatic age-based deletion. The helper does not scan
Git history, cloud services, secret stores or all possible secret formats; skipped/oversize coverage
is explicit. Run [isolated tests](../qa/test-sweep.py); never use live secrets/user files as fixtures.
