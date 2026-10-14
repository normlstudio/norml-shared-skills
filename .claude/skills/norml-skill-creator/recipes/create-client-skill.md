# Create a client procedure or flow-test package

1. Resolve canonical client/project, approved slug and existing source owner from verified context.
2. Reuse its private collection or requested project-scoped destination; no mandatory host owner.
3. Prefix collision-prone names with the verified client slug. Folder/frontmatter identity agrees.
4. Read current architecture/source before building with
   [create and verify](../processes/create-and-verify.md).

A client flow includes verified prerequisites, roles, environment, source-of-truth boundaries,
entities/join keys, ordered state transitions, failure paths, downstream effects and expected
outcomes. Tests use permitted fixtures/effects and record actual evidence. Include negative cases,
cleanup/rollback and conditions preventing PASS. Undefined variants remain explicit blockers.
Shared mechanics can be locally bundled or use an available adapter; private client facts stay
in this client package. Never duplicate a conflicting test manual outside its canonical procedure.

Resolve installed source root separately from project data root. Cwd must not choose a client.
Local package creation does not authorize charges, refunds, customer writes, remote publication or
client data migration. Client access/distribution is explicit; global discovery grants no cross-client
operating permission. A new collection index records actual skills and source provenance only.
