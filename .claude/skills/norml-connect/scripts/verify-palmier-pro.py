#!/usr/bin/env python3
"""Verify Palmier Pro's local MCP server without printing project content."""

from __future__ import annotations

import http.client
import json
import re
import sys
from typing import Any, Dict, List, Optional


ENDPOINT_HOST = "127.0.0.1"
ENDPOINT_PORT = 19789
ENDPOINT_PATH = "/mcp"
PROTOCOL_VERSION = "2025-06-18"
TIMEOUT_SECONDS = 8


class VerificationError(RuntimeError):
    """Raised when Palmier does not satisfy the MCP connection contract."""


def decode_response(body: bytes, content_type: str) -> Optional[Dict[str, Any]]:
    text = body.decode("utf-8")
    if not text:
        return None

    if content_type.split(";", 1)[0].strip() != "text/event-stream":
        return json.loads(text)

    messages: List[Dict[str, Any]] = []
    for event in re.split(r"\r?\n\r?\n", text):
        data = "\n".join(
            line[5:].lstrip() for line in event.splitlines() if line.startswith("data:")
        )
        if not data:
            continue
        try:
            messages.append(json.loads(data))
        except json.JSONDecodeError:
            continue

    return messages[-1] if messages else None


class PalmierMCPClient:
    def __init__(self) -> None:
        self.session_id: Optional[str] = None

    def post(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": PROTOCOL_VERSION,
        }
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id

        connection = http.client.HTTPConnection(
            ENDPOINT_HOST,
            ENDPOINT_PORT,
            timeout=TIMEOUT_SECONDS,
        )
        try:
            connection.request(
                "POST",
                ENDPOINT_PATH,
                body=json.dumps(payload),
                headers=headers,
            )
            response = connection.getresponse()
            body = response.read()
            if response.status not in {200, 202}:
                raise VerificationError(
                    f"{payload.get('method', 'request')} returned HTTP {response.status}"
                )
            self.session_id = response.getheader("MCP-Session-Id") or self.session_id
            return decode_response(body, response.getheader("Content-Type", ""))
        finally:
            connection.close()


def require_result(
    message: Optional[Dict[str, Any]], method: str
) -> Dict[str, Any]:
    if not message:
        raise VerificationError(f"{method} returned no JSON-RPC response")
    if message.get("error"):
        error = message["error"]
        raise VerificationError(f"{method} failed: {error.get('message', 'unknown error')}")
    result = message.get("result")
    if not isinstance(result, dict):
        raise VerificationError(f"{method} returned no result object")
    return result


def verify() -> None:
    client = PalmierMCPClient()
    initialize = require_result(
        client.post(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {},
                    "clientInfo": {
                        "name": "norml-connect-verifier",
                        "version": "1.0.0",
                    },
                },
            }
        ),
        "initialize",
    )
    if not client.session_id:
        raise VerificationError("initialize did not assign an MCP session ID")

    client.post(
        {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
        }
    )
    tools_result = require_result(
        client.post(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {},
            }
        ),
        "tools/list",
    )
    tools = tools_result.get("tools")
    if not isinstance(tools, list) or not tools:
        raise VerificationError("tools/list returned no tools")
    if not any(tool.get("name") == "manage_project" for tool in tools):
        raise VerificationError("tools/list did not include manage_project")

    project_result = require_result(
        client.post(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "manage_project",
                    "arguments": {"action": "list"},
                },
            }
        ),
        "manage_project list",
    )
    if project_result.get("isError"):
        raise VerificationError("manage_project list returned an MCP tool error")

    server = initialize.get("serverInfo", {})
    print("Palmier Pro MCP: connected")
    print(f"  endpoint: http://{ENDPOINT_HOST}:{ENDPOINT_PORT}{ENDPOINT_PATH}")
    print(f"  protocol: {initialize.get('protocolVersion', 'unknown')}")
    print(
        "  server: "
        f"{server.get('name', 'unknown')}@{server.get('version', 'unknown')}"
    )
    print(f"  tools: {len(tools)}")
    print("  manage_project list: passed")


if __name__ == "__main__":
    try:
        verify()
    except (
        ConnectionError,
        OSError,
        TimeoutError,
        VerificationError,
        json.JSONDecodeError,
    ) as error:
        print(
            "Palmier Pro MCP: not connected — "
            f"{error}. Start Palmier Pro and retry.",
            file=sys.stderr,
        )
        raise SystemExit(1)
