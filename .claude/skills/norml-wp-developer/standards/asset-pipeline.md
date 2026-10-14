# Asset build and release packaging

Read lockfiles and build scripts before invoking tools. Use the installed/pinned compatible
Node/Composer/PHP versions. `npm ci` installs a committed npm lockfile; do not invent lint,
watch, preview or test scripts that `package.json` does not define.

In Sage/Vite, source lives in `resources/` and built assets in `public/build/` per configuration.
Never hand-edit generated assets/manifest/theme JSON. Inspect actual manifest location and
entry keys rather than assuming Vite's defaults. Use the framework-supported Vite facade
or existing enqueue adapter; don't probe a development server in production by default.

PR validation installs dev tooling for Pint/PHPUnit/lint. The final runtime artifact installs
production-only Composer dependencies. Preserve Blade templates and runtime `resources/views`;
dropping every `resources/` file breaks rendering. Runtime helpers/custom image/icon components
must exist or be explicitly implemented before using their tags. No promise that a stock Sage
install includes them. SVG/icons/fonts/image conversion require their actual project plugins.

Deploy production Composer dependencies, built manifest/assets, PHP bootstrap/app files,
Blade templates and required public metadata. Exclude Git metadata, secrets, DB/media dumps,
node_modules, tests and CI-only state. Persistent cache/runtime storage belongs outside an
immutable release or in a deliberately shared path. Never erase it through broad rsync.

Check built references and hashed assets on an authorized running site; a successful build
is not proof of runtime/editor asset loading. See [CI/CD](ci-cd.md) for release activation.
