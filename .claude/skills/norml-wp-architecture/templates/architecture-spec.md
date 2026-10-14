# WordPress architecture spec — {collection or singleton}

- Source request and verified current model: {evidence}
- Primitive/internal identifier: {page / post / CPT / other}
- Rationale and accepted override: {one-off/repeatable/editorial and consequences}
- Public / publicly queryable / REST/editor access: {explicit values}
- Hierarchy / supports: {needed behavior only}
- Taxonomies: {names, hierarchical/flat, controlled vocabulary, public archives}
- Fields: {typed definitions, relationships, ownership and editing source}
- Archive: {exact URL and template slot, or none}
- Single: {exact URL and template slot, or no public single}
- Existing-route collisions/redirects: {verified finding or unchecked}
- Code/schema owner: {site-core plugin / theme / child / mu-plugin}
- Dependencies and portability tradeoff: {ACF license/version or none; future theme change}
- Permalink flush: {required after registration change; once, never every request}
- Rendering handoff: {builder/template and dynamic content binding}
- Structure/content acceptance: {required blocks, conditions, editor source, rendered evidence}
- Outstanding decisions/access: {explicit unresolved items}
