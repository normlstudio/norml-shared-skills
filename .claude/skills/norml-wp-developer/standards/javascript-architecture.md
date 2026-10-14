# JavaScript architecture

Retain the inherited project's framework/module format. Sage examples use Alpine as an
explicit stack choice; new native editor blocks may use WordPress React packages.
Do not introduce a second framework during an unrelated feature.

- One scoped module per behavior; import through the existing main/editor entry.
- Declare state and lifecycle, including event/listener/widget cleanup.
- Pass server values via safe serialization (`@js` in Blade), not interpolated strings.
- Match ARIA state, keyboard interaction, focus management and DOM visibility.
- Respect reduced motion; animations may not hide essential content when disabled.
- Fetch remote data asynchronously with timeout/error/empty states; no synchronous render calls.
- Endpoints validate input, capabilities and nonces; user data never becomes unsafe HTML.
- Add sliders/animation libraries only when needed, with project authorization and bundle review.

For Alpine register `Alpine.data()` modules before starting one Alpine instance. Use `x-cloak`
with a scoped stylesheet to prevent flashes; include a collapse plugin only if installed.
Use unique component IDs and prevent duplicate initialization in the editor. The full
[component guide](component-system.md) supplies the concrete Blade/Alpine example.
