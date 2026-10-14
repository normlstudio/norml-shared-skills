#!/usr/bin/env python3
"""Verify only public Agent-Reach baseline surfaces; no browser/social probes."""
import importlib.metadata
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    checks = {}
    checks["package"] = {"status": "ok", "version": importlib.metadata.version("agent-reach")}
    import certifi
    import feedparser
    from agent_reach.channels.web import WebChannel
    # Python.org builds may lack a default CA bundle. Keep TLS validation enabled.
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
    try:
        body = WebChannel().read("https://example.com")
        checks["public_web"] = {"status": "ok" if "Example Domain" in body else "failed"}
    except Exception as exc:
        checks["public_web"] = {"status": "failed", "error_type": type(exc).__name__, "http_status": getattr(exc, "code", None)}
    fixture = b'<rss version="2.0"><channel><title>Norml test</title><item><title>Entry</title><guid>test-1</guid></item></channel></rss>'
    parsed = feedparser.parse(fixture)
    checks["feed_parser"] = {"status": "ok" if len(parsed.entries) == 1 and parsed.entries[0].id == "test-1" else "failed", "scope": "local fixture"}
    binary = Path(sys.executable).parent / ("yt-dlp.exe" if os.name == "nt" else "yt-dlp")
    try:
        result = subprocess.run([str(binary), "--ignore-config", "--version"], capture_output=True, text=True, timeout=15)
        checks["yt_dlp"] = {"status": "ok" if result.returncode == 0 else "failed", "scope": "binary only; video extraction unverified"}
    except (OSError, subprocess.TimeoutExpired) as exc:
        checks["yt_dlp"] = {"status": "failed", "error_type": type(exc).__name__}
    checks["node_runtime"] = {"status": "present" if shutil.which("node") else "missing"}
    if shutil.which("gh"):
        try:
            result = subprocess.run(["gh", "api", "repos/Panniantong/Agent-Reach", "--jq", ".full_name"], capture_output=True, text=True, timeout=20)
            ok = result.returncode == 0 and result.stdout.strip().lower() == "panniantong/agent-reach"
            checks["public_github"] = {"status": "ok" if ok else "failed"}
        except (OSError, subprocess.TimeoutExpired) as exc:
            checks["public_github"] = {"status": "failed", "error_type": type(exc).__name__}
    else:
        checks["public_github"] = {"status": "not-installed"}
    checks["optional_social_channels"] = {"status": "not-tested"}
    print(json.dumps(checks, indent=2))
    return 1 if any(c["status"] == "failed" for c in checks.values()) else 0

if __name__ == "__main__":
    raise SystemExit(main())
