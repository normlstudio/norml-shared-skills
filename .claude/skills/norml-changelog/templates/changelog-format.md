# Project changelog format

Use the existing project date/naming convention, or default to `MMM D, YYYY`.
One date section per day; merge parallel-session updates carefully.

```markdown
# Changelog — {project}

Verified changes, decisions and integrations. Recent work stays detailed;
older routine work may be summarized. Security and breaking changes stay intact.

## Oct 13, 2026 — Archive filtering

### Content
- Added the `resource_type` taxonomy and connected the archive filter.
- [DECISION] Resource types use a controlled hierarchical vocabulary so editors
  can group resources consistently; freeform attributes stay custom fields.

### Integration
- [INTEGRATION] The authorized content service owns resource metadata; the
  importer reads verified source records and updates mapped WordPress fields.
  Authentication uses the provider/OS protected store; no secret values in docs.

### Verification
- Confirmed filtering, pagination and empty state on staging.
- Production deploy remains pending; no production verification claimed.
```

## Compression

Keep at least the newest 20 date sections in full. After 50 sections, group eligible
routine work older than 30 days into weekly summaries. Preserve verbatim decisions,
integration entries, security fixes, breaking changes and their rationale.
Never convert deferred or unverified work into a completed change during compression.

```markdown
## Week of Sep 7, 2026 — Archive maintenance

- Repaired archive queries, pagination and filter empty states.
- [DECISION] Shared content identity remains in the site-core plugin so changing
  themes does not orphan the collection.
```
