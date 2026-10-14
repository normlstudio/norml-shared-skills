# MVP mode

`mode: mvp-mode`

MVP mode is a cross-cutting delivery posture for an early product or site whose
real feedback loop lives on its production URL. It is intentionally **not a
deployment recipe**: the project's `pattern:` or custom topology still says how
and where it ships. This mode only removes local-first and staging ceremony that
does not currently improve the product.

## Use when

- The user explicitly says the project is in MVP mode, wants it live now, or
  says local parity is not important.
- Production is the deliberate acceptance surface for a small, reversible
  increment.
- The project still has a known deployment target, an exact GitHub source
  revision, a rollback path, and a live verification path.

Do not infer MVP mode merely because a project is new. Record it in the nearest
`.claude/ci-cd.md` as a deliberate project decision.

## Contract

MVP mode changes delivery ceremony:

- **Production-first feedback.** Verify the real URL after every deploy; a
  local render is optional unless it is the cheapest useful diagnostic.
- **No staging requirement.** Absence of staging is accepted and does not block
  a release.
- **No local-parity requirement.** Builds and automated checks may run locally,
  in CI, or on the production build host. Local setup is not a release gate.
- **Smallest safe increment.** Ship one coherent product outcome or deployment
  foundation at a time, keeping rollback obvious.
- **Visible debt.** Record deliberate MVP compromises in the project contract's
  known-gotchas/debt section instead of silently normalizing them.

MVP mode does not change these invariants:

- The exact production revision is committed and pushed to the canonical
  the configured Git repository repository in the same turn as deployment.
- Secrets remain in the OS-native secret store and the approved production
  runtime store; never in Git, chat, build logs, or planning files.
- Destructive database or state operations retain their explicit human gate.
- A data-changing deploy retains the project's backup/restore gate. A stateless
  code-only deploy may proceed without manufacturing a local data copy.
- Auth, tenancy, permissions, and other security boundaries are not mocked away
  merely to get a green page.
- The deployed revision must be identifiable and rollback must point to a known
  prior revision/image/configuration.
- Production smoke verification is mandatory and must exercise the changed
  surface, not only return an HTTP status.

## Production loop

1. Read the project `.claude/ci-cd.md`, its declared deployment pattern/custom
   topology, protected credential reference, and this mode.
2. Resolve one exact production target and one rollback unit (Git SHA, image
   tag, release, or equivalent).
3. Run the smallest relevant automated gate. It may run on the build host; do
   not require a local environment only for ceremony.
4. Commit and push the exact revision through `standard scoped Git operations` before it becomes
   live. Stage only the files owned by this change.
5. Build and deploy that immutable revision through the project's declared
   production command.
6. Verify the live URL with the relevant render/smoke workflow, including
   console, page errors, failed requests, rendered dimensions, and a screenshot
   for UI work.
7. Record the live revision and any intentional MVP debt in the project
   contract/changelog.

If the production check fails, diagnose and roll forward with a new exact
revision when safe. Roll back to the recorded previous unit when the live state
is materially broken and a forward fix is not already proven.

## Leaving MVP mode

Replace `mode: mvp-mode` with `mode: standard` (or a future named mode) when the
project needs staging as a release gate, local parity becomes operationally
valuable, or production-first iteration is no longer the accepted risk posture.
Changing modes does not require changing the deployment pattern unless the
topology itself also changes.
