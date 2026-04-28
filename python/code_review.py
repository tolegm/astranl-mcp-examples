#!/usr/bin/env python3
"""AstraNL: review a Python file and get suggestions."""
import os, sys
import requests

KEY = os.environ.get("ASTRANL_AGENT_KEY")
if not KEY:
    raise SystemExit("set ASTRANL_AGENT_KEY env var")
if len(sys.argv) < 2:
    raise SystemExit("usage: code_review.py <file.py>")

source = open(sys.argv[1]).read()
resp = requests.post(
    "https://astranl.com/capabilities/execute",
    headers={"X-Agent-Key": KEY, "Content-Type": "application/json"},
    json={
        "intent": (
            f"Review this Python code for bugs, performance issues, and "
            f"style problems. Be specific. Code:\n\n{source}"
        ),
        "capability_id": "code",
    },
    timeout=60,
)
resp.raise_for_status()
print(resp.json()["result"])
