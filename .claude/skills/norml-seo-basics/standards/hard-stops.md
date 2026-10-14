# Hard stops

These stops apply to every `norml-seo-basics` run. Only the user may override
a business decision; safety, target, evidence, backup, and Git requirements stay
mandatory.

## HS-1 — Production target is not uniquely verified

Stop affected operations when canonical host, CMS/account, environment and authorized
platform/source access do not agree on one exact target. Use read-only evidence;
never guess a document root or ask for plaintext credentials.

## HS-2 — Required capability/access knowledge is missing

Before mutation, verify the exact supported REST/API/CLI/admin capability and
connected identity. Keep capability, current owner and change evidence in the
project record. Missing access blocks that recipe; no private manager is required.

## HS-3 — SEO ownership is unresolved

Stop before installing/configuring GTM, analytics, metadata, schema, sitemap, or
Rank Math when another integration, SEO plugin, theme framework, mu-plugin, or
custom renderer already owns the same output. Inventory and choose one owner
first. An explicit migration requires a setting map, rollback point, old-owner
deactivation, and live duplicate-output proof.

## HS-4 — No recoverable production backup

Stop before a production platform/plugin/database/media/permalink/rewrite or code
mutation when the target lacks the applicable dated backup and recoverable
integration/code inventory. Store server backups outside the public web root.

## HS-5 — Schema would claim facts the page does not show

Stop the unsupported entity only; continue the rest of the baseline. Never create
FAQ, Review, AggregateRating, Product, Offer, LocalBusiness, address, social,
founder, or pricing claims from inference. Mark the entity as `ESCALATE` until
verified data is present and visible.

## HS-6 — A favicon would become invented branding

If there is no approved mark, monogram, or user-supplied site identity, do not
invent a logo. Repair the technical icon plumbing with an approved existing asset
when possible; otherwise mark the asset gap and continue all non-visual baseline
work.

## HS-7 — Production cannot match Git

Stop deployment when code will ship to production but the exact change cannot be
committed and pushed to the declared remote in the same turn. Do not deploy an
untracked or locally-only implementation, and do not stage unrelated work.

## HS-8 — Verification fails

Any required FAIL in `qa/acceptance-contract.md`, PHP syntax failure, plugin
checksum failure, invalid JSON-LD, broken sitemap, wrong asset MIME, visible fatal
error, or production/local drift keeps the run open. Diagnose, repair, and rerun.
Do not report completion with required failures reworded as warnings.

## HS-9 — Media alt would be guessed

Stop the alt-text mutation for any attachment whose pixels and real usage cannot
be inspected. Do not derive alt from a filename, title, keyword list, or inferred
business intent. Preserve the current value, mark the attachment `ESCALATE`, and
continue the rest of the baseline; an unreviewed blank prevents the media-alt gate
from passing but does not authorize fabricated text.

## HS-10 — Measurement identifiers or consent state are unresolved

For the Google Analytics presence check, do not provision or edit anything.
Public evidence may conclusively report present/absent without GA Admin access;
ambiguous delivery ownership becomes `ESCALATE`, and indeterminate consent/access
becomes `BLOCKED`. Never create a property, stream, Measurement ID, Google tag,
GTM tag, trigger, or published version.

For a mutable GTM/Clarity setup, stop when the GTM container, Clarity project,
canonical-domain mapping, consent owner, or required consent behavior is
ambiguous. Never create a second project or substitute an ID to keep the run
moving. Continue independent recipes.

## HS-11 — WordPress GTM would be embedded in code

Stop the GTM recipe if the proposed WordPress implementation pastes the loader,
noscript iframe, or container ID into theme, child-theme, snippet, mu-plugin, or
GitHub source. Use the approved WordPress Admin integration and prove the current
repository has no GTM embed.

## HS-12 — Search-engine property ownership or scope is unresolved

Stop Google Search Console or Bing Webmaster Tools setup when an existing
property/site or verified owner is unclear, the canonical host/scope is not
proven, DNS/platform access cannot be uniquely matched, or the proposed
verification would overwrite/remove another owner's token. For Bing, also stop
when the exact API user or canonical site record is ambiguous. Continue
independent recipes.

## HS-13 — Consent decision would be invented

Stop the affected consent and measurement recipes when the project/legal/privacy
decision, applicable audience/region, category model, or banner copy is missing.
Consent Mode does not supply that decision. Never choose basic versus advanced
mode or infer a lawful basis to keep analytics moving.

## HS-14 — 404 crawl coverage is incomplete

Stop the 404 recipe from passing when Screaming Frog/approved equivalent is
missing, the target is ambiguous or unauthorized, the site can exceed the free
500-URL cap without a licence/complete alternative, or authentication, host
instability, WAF/rate limiting, crash, or crawler error prevents complete
coverage. Record `BLOCKED` and preserve any partial evidence as partial.

Do not guess the uncrawled result and do not apply a redirect/link/content change
from an unreviewed automated candidate.

## HS-15 — Required run report cannot be persisted

Stop completion when the timestamped Markdown report cannot be written and read
back from the project-folder report path, or when the current
`.claude/docs/seo/norml-seo-basics.md` summary cannot point to it. A tracker row, chat
summary, raw crawler export, or local Office file is never a substitute.

Never overwrite an existing immutable report. Use the next unique `-rN` run-ID
suffix and append its pointer to report history.
