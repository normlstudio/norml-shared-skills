# Create a product-local skill

Read the existing product Git repository’s instructions and preserve its source ownership/name.
Use its established identity or a product-prefixed slug for collision-prone new skills. Place the
source in its project `.claude/skills/`; product-local discovery is the default.

Run [create and verify](../processes/create-and-verify.md), then add one source/discovery pointer
in the existing project context. Do not introduce a global catalog or duplicate product repo.
The presence of skills does not authorize committing or publishing the application’s entire tree.

If the method becomes useful across products, propose a reusable extraction plus a thin product
adapter under a separately grounded scope change. Preserve context/data boundaries and existing
explicit runtime adapters. Installation and publication remain independently authorized effects.
