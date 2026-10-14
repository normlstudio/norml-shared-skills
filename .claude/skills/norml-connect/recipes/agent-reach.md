# Connect: Agent-Reach

## 1. What & why

Install the reviewed Agent-Reach CLI and its public reading dependencies in an
isolated environment. Installation and verification are task-scoped. Baseline scope: public web, local feed parsing,
yt-dlp availability and public GitHub access. Social login is not included.

## 2. Who needs it

SEO, marketing, strategy and development teammates who need public-source
extraction. Optional by task, not a mandatory company-wide installation.

## 3. Prerequisites

Python 3.10+, a supported terminal, curl, and GitHub/network access. Node is
needed for the documented yt-dlp runtime option. Read the pinned upstream
pyproject.toml and install/CLI code before installation or upgrade. The source-reviewed revision is `da5044d26fc6adddb6554d5679c94ac22e76e428` (package 1.5.0).
Never install the unrelated same-name PyPI package. Do not register an upstream
skill over existing runtime skills.

## 4. Self-serve setup

For macOS, install under the user's local application data. If this environment
already exists, inspect its version and reuse it; do not recreate it blindly.

```bash
python3 -m venv "$HOME/.local/share/public-tools/agent-reach/venv"
"$HOME/.local/share/public-tools/agent-reach/venv/bin/python" -m pip install \
  'https://github.com/Panniantong/Agent-Reach/archive/da5044d26fc6adddb6554d5679c94ac22e76e428.zip'
"$HOME/.local/share/public-tools/agent-reach/venv/bin/agent-reach" --version
```

Windows equivalent (source-reviewed; not yet live-tested):

```powershell
$agentReachVenv = Join-Path $env:LOCALAPPDATA 'PublicTools\agent-reach\venv'
py -3 -m venv $agentReachVenv
& "$agentReachVenv\Scripts\python.exe" -m pip install 'https://github.com/Panniantong/Agent-Reach/archive/da5044d26fc6adddb6554d5679c94ac22e76e428.zip'
& "$agentReachVenv\Scripts\agent-reach.exe" --version
```

No `--system`, cookie import, optional extras, global npm installation or
upstream `skill --install` is needed for this baseline. Run upstream tools by
their venv paths; a verified non-conflicting user-local launcher is optional.
For later upgrades, inspect a specific new revision, install it deliberately,
run the same verification, and update this pin and the catalog evidence together.
Do not silently follow `main` or install all optional channels.

## 5. Where the secret goes

The baseline requires no new secrets. Reuse the existing gh connection without
copying its token. Never run secret-writing `agent-reach configure` or `setup`
commands: upstream `~/.agent-reach/config.yaml` is not a protected secret store.
Authenticated optional backends require their own supported secure connection; no cookie import or plaintext credentials are included.

## 6. Verify

Use the installed environment's Python to run the companion verifier:

```bash
"$HOME/.local/share/public-tools/agent-reach/venv/bin/python" \
  "{skill-root}/scripts/verify-agent-reach.py"
```

On Windows use its `Scripts/python.exe` against the same registered script.
It checks the package version, actually reads a public example page, parses a
local feed fixture, checks yt-dlp, and reads the public upstream GitHub repo
when gh exists. It prints only scoped statuses; it does not probe social login
or operate a browser. A failed web check means public web is not verified even
if the package is installed. A yt-dlp version check is not proof a particular
video exposes downloadable subtitles; test that exact video during the task.

Upstream `doctor --json` checks all registered backends; it is optional and is
only appropriate after inspecting/authorizing those backends. Some checks only
inspect dependencies, so a green result is not an end-to-end reading guarantee.

## 7. Obstacles & fixes

- Python SSL certificate failure → use the Python installation's maintained
  certificate setup or its certifi CA bundle; never disable TLS validation.
  A verified curl download of the pinned archive can also be installed locally.
- PEP 668 / managed Python → use the isolated venv above, not system pip flags.
- Shell cannot find agent-reach → use the exact venv binary; do not change global
  PATH or overwrite another tool just to hide the error.
- Jina HTTP 401 / anonymous network reputation blocked → observed during the
  first macOS verification. Requires a Jina-authenticated connection or a
  documented alternative. Do not report the web backend ready or create an
  account/buy access implicitly; capture Jina auth in its own this package
  recipe when that connection is requested.
- Jina challenge/rate limit → report web check failed; follow the source-capture
  skill's authorized alternative. Do not silently launch a browser.
- yt-dlp missing JS runtime config → pass `--js-runtimes node` per task when Node
  exists. Do not modify global yt-dlp configuration during catalog setup.
- Social backend not connected → baseline does not include it. Resolve the exact
  requested channel through this package and the user's browser policy.

## 8. Admin-only bootstrap

None for the public baseline. Paid services, shared accounts, proxies and social
channel enrollment are separate responsibility and access decisions. Browser
control through a CLI or MCP still needs the user's applicable authorization.

## 9. Escalation

Report the failing scoped check, installed version and reviewed revision to the
operator. Capture a reproducible connection issue here without source contents,
account lists or secrets. Do not contact others automatically.


Source: https://github.com/Panniantong/Agent-Reach
