# One product, two planning owners

This is an illustrative project, not a claim about an existing workspace folder.

## Resolve the homes

- Product strategy/design/launch: `workspace/Products/Sample Product/.claude/tasks/`
- Plugin implementation: verified `example-org/sample-product-plugin` checkout,
  `.claude/tasks/` at its Git root.
- Shared `project_id`: `sample-product`.
- Distinct owner IDs: `sample-product-coordination`, `sample-product-plugin`.

Both configs describe the same map:

```json
{
  "workspace": {
    "owner_id": "sample-product-coordination",
    "path": "Products/Sample Product/.claude/tasks"
  },
  "repositories": [{
    "owner_id": "sample-product-plugin",
    "repository": "example-org/sample-product-plugin",
    "planning_path": ".claude/tasks"
  }]
}
```

## Organize a dump

“Make onboarding clearer, simplify the model picker, write launch content,
and maybe explore analytics later.”

- workspace goal `GOAL-01`: new customers can understand and complete setup.
- Short-term workspace `GOAL-02`: onboarding flow accepted, linked to GOAL-01.
- workspace `TASK-001`: approve the onboarding design; acceptance is the reviewed flow.
- Repo `TASK-001`: implement that accepted flow; depends on
  `sample-product-coordination::TASK-001`. It links a GitHub issue and owns the
  code steps/testing. If scope needs phases, it belongs to a repo milestone.
- Repo `TASK-002`: simplify the picker; its acceptance specifies interaction
  behavior, not just a component filename.
- workspace `TASK-002`: write launch content based on the verified behavior.
- Analytics remains an uncommitted idea/Someday task; no invented launch date.

Now selects the blocking design outcome. A project-wide query reports both
owners, with no duplication of the implementation task into the workspace backlog.
If the repo cannot be read, the result says repository coverage is unavailable.

