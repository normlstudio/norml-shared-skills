# Add or extend a page type

Read this file before catalog maintenance. It is the durable version of the
creation request: a page type is a **set of related pages**, usually understood
through archive/single relationships, with as much justified depth as needed.
The catalog is client-agnostic and helps propose architecture and future pages.
It is not a collection of client URLs or a second block/layout catalog.

## Locked package shape

```text
norml-page-types/
├── SKILL.md                         runtime instructions and quick family index
├── index.md                         complete linked table of families and members
├── add-page-type.md                 this authoring contract
├── page-types/
│   └── {family}/
│       ├── {family}.md               entire family: purpose, fit, model, all branches
│       ├── archive.md               when this family has a hub/archive
│       ├── single.md                when this family has a detail destination
│       ├── {meaningful-child}.md    one member specification
│       └── {axis}-by-{axis}.md      one supported intersection specification
├── standards/architecture.md        shared vocabulary and relationship rules
├── standards/project-patterns.md    source extraction and locale distinctions
├── standards/pattern-notes.md     dated public precedents and review limits
├── templates/                       family and member source templates
├── qa/catalog-cases.md              matching/extension acceptance cases
├── changelog.md
└── readme.md + readme.data.json + readme.html
```

**One folder per family. All family members are flat in that folder.** Do not
create archive/single subfolders, client/entity instances, depth folders, or a
catch-all misc drawer. The overview basename must equal its folder slug.
`archive.md`/`single.md` are useful conventions, not forced empty files for
singletons. Descriptive member names are allowed. The folder holds any number
of real member contracts; do not cap it at two files.

Examples: industries contains its overview, archive, single, industry-by-service,
industry-by-location and subindustry. Services contains a service-location
member and points to the industry-service member’s canonical home. About Us can
be the logical archive for team-member singles without a separate Team listing.

## Decide new family or new member

1. Read SKILL.md, index.md and standards/architecture.md; search names and aliases.
2. Read the nearest family and its member files. Classify the actual entity,
   visitor job, lifecycle and relationships, not just its nav label.
3. A different presentation of the same family is a member/variant or project
   decision. A new collection/purpose/lifecycle that cannot fit the existing
   family is a candidate family. A renamed archive label is not a new family.
4. Before Git edits, follow `project Git workflow` collaboration and ownership checks in
   the real source repository. Resolve overlapping active work; never fork the
   skill into runtime adapter directories or Drive.
5. Resolve material missing facts or ownership while continuing independent
   reading. An empty shell is not a usable catalog addition.

## Author a new family

1. Select a lowercase kebab-case slug; validate proposed Markdown paths with
   the hub’s `scripts/lint-markdown-filenames.sh` before creation.
2. Create `page-types/{family}/{family}.md` from [the family template](templates/family.md).
   Explain purpose, why/when it fits, when to skip/embed, canonical entity,
   candidate model, complete member table, relationships/depth, evidence and
   handoff. Keep model decisions conditional and delegate actual CMS mapping.
3. Create one file per actual reusable member from [the page template](templates/page.md).
   Include family/member ID, logical role, illustrative route, parents, purpose,
   content responsibility, links, eligibility/omission, model/structure handoff.
   Do not prescribe block order, tokens, UI or copied implementation code.
4. For collections, evaluate archive/hub and single together. If one is absent,
   state why and whether it is embedded-only, disabled or not applicable.
   About Us can be an archive/hub logically and a singleton Page technically.
5. Add every category, child and intersection in the same flat folder. Describe
   navigation, URL, entity and CMS hierarchy separately. For combinations name
   both parents, canonical tuple, eligibility and one owning family/member.
   A reverse orientation links to the original; it is not a second page.
6. When deriving from projects, read [project-pattern rules](standards/project-patterns.md)
   and [the precedent review](standards/pattern-notes.md). Add dated public-source
   evidence, verify final page content/role and label unobserved generalizations.
   Sitemap presence alone does not prove a working destination or integration.
7. Specify content sources and differences that make each member useful. A
   new family must remain portable across clients; project facts stay outside.
   Label examples/defaults as such, and cite sources for externally asserted
   technical behavior. Do not claim a client variant has been live-tested.
8. Link matching `norml-page-structures` specifications when they really apply;
   explicitly flag absent/mismatched variants. A new family does not silently
   add required blocks to that sibling. Route structure work there separately.

## Extend an existing family

Read its same-name overview and the existing related members first. Add the new
member flat alongside them; update relationships and the local table. Keep the
existing meaning and stable member IDs. A third dimension or deeper branch
needs an explicit contract and evidence gate; do not infer it from two-axis
support. Respect project-specific forbidden combinations.

## Reconcile discovery and verify

- Update the full row in root index.md: linked overview, fit/skip conditions,
  all member links and branches. Update SKILL.md’s quick index and local table.
- Ensure every member is reachable from both the root index and family overview.
  Do not hide a procedure in an unindexed file. Cross-family reverse references
  resolve to the same canonical member, not a duplicate definition.
- Run [catalog cases](qa/catalog-cases.md), relative-link/coverage checks and
  the hub’s Markdown filename, semantic-folder and portable-path lints.
- Check archive/single dispositions, singleton exceptions, route collisions,
  inherited-model compatibility and content uniqueness responsibilities.
- Bump semantic version and append changelog. Update the owner’s root changelog
  for a new family/taxonomy change. Use `human documentation maintenance` for current human guides.
- Use `package maintenance` for any changed package description/discovery;
  `project Git workflow` owns publication, exact staging and shared claim release.

Done means a useful complete family/member contract, reconciled indexes and
verified discovery/docs. Catalog publication is not page implementation or a
verified client content model. Record unresolved downstream work honestly.
