# Database strategy: staging-to-prod-full

Full replacement is for initial launch or an explicitly reviewed replacement where losing
production-only state is acceptable. Routine promotion of an ongoing site must use selective
migration or editor-owned content. Users/orders/submissions/comments/editor work can be lost.

## Pre-flight

1. Verify exact source/target site roots, database identity, URLs, table scope and owner.
2. Obtain exact replacement authorization; inventory production-only state and prevent
   concurrent writes for the cutover as the project requires.
3. Complete and verify recoverable production DB/files/media backups and staging backup.
4. Prove restore in an isolated environment. Stop on missing backup or an ambiguous target.
5. Verify the same code/plugins/content types are supported by the destination runtime.

## Serialization-safe export and import

Illustrative commands: substitute only verified project values. Use a private directory
outside the web root and never publish dumps or output containing user records.

```bash
# Execute on source against its verified site root. --export leaves staging unchanged.
wp --path={staging-site-root} search-replace \
  'https://staging.example.com' 'https://example.com' \
  --skip-columns=guid --all-tables-with-prefix --dry-run
wp --path={staging-site-root} search-replace \
  'https://staging.example.com' 'https://example.com' \
  --skip-columns=guid --all-tables-with-prefix --export={private-rewritten-dump}
```

Inspect plugin-specific serialization and multisite scope before using broad table flags.
For a second path/domain rewrite, use an isolated temporary WordPress/database workspace;
never `sed` a WordPress SQL dump. Transfer via one supported local/remote endpoint per
command, or run the transfer from one verified remote host. Standard rsync cannot transfer
between two remote endpoints in a single command.

```bash
# On target, only after reviewed destructive-replacement authorization and backup.
wp --path={production-site-root} db import {private-rewritten-dump}
```

Reset/drop only when the approved replacement plan explicitly requires it; an import itself
may overwrite/drop tables depending on its SQL. Sync approved media incrementally without
deleting destination-only files. Run only relevant cache hooks; do not assume Acorn exists.

## Verification and recovery

Check production home, primary action, contact flow, an archive and a detail page. Verify
media, routing, admin editor, supported plugins, production indexing and canonical URLs.
Confirm schema and counts match approved migration scope, and all intentionally protected
state survives. Read-back any settings. Record checks and actual cutover revision.

If broken, restore the verified pre-cutover data/media and matching code revision, clear
caches and verify recovery. Preserve encrypted backup evidence under project retention rules.

See [selective migration](staging-to-prod-selective.md) for ongoing sites and
[backup catalog](../backup.md) for recovery planning.
