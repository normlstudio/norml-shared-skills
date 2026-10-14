# Connect: Hyperframes

## 1. What and why

Local HTML animation CLI readiness. Authentication is separate from later operating authority.

## 2. Who needs it

The account owner or an operator explicitly authorized for this provider and target.
This is selected per task, not mandatory role-wide onboarding.

## 3. Prerequisites

A reviewed Hyperframes version, compatible Node runtime, npm, FFmpeg/ffprobe and local browser support. Optional cloud/media providers are separate.

## 4. Setup

Read upstream package engines and installation guidance for the selected release; preserve an existing Node default. Source baseline: `hyperframes@0.8.42`. Install that chosen package in an isolated local tool directory with `npm install --prefix <tool-directory> --save-exact hyperframes@0.8.42`; invoke its node_modules/.bin/hyperframes executable. Review upstream agent-skill registration separately; do not replace existing packages automatically.

## 5. Secret storage

Use the OS secret store or provider-managed protected OAuth storage. Store only
non-secret account/resource IDs and service/account references in local notes
outside Git/synced folders. Secure entry is native; never request a token in
chat or copy authentication databases. See
[connection boundaries](../standards/connection-boundaries.md).

## 6. Verification

Run --version and doctor --json, inspect individual checks and the JSON result rather than exit code alone. Readiness is separate from an actual local fixture check/render and alpha-channel verification. Use only a separately authorized tiny local fixture to test rendering; no hosted provider credits are spent.

## 7. Obstacles and fixes

Engine mismatch: select a compatible local runtime. Browser missing: use documented install route. Skill collision: preserve existing package. A MOV file alone proves neither transparency nor native-editor import.

## 8. Administrator bootstrap

No account needed for local rendering. Cloud generation/voice/model connections and any spending need their own approval.

## 9. Escalation

Provide only expected account/resource, selected client/version, failed stage,
sanitized HTTP/error code and time. The agent continues supported setup; the
user completes only unavoidable sign-in/MFA/consent or the specific missing
access approval. No secret, raw headers, callback code or private payload.

Source: [provider documentation](https://github.com/heygen-com/hyperframes). Recheck current provider setup before
first use. Public packaging tests did not authenticate a recipient account.
