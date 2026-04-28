#!/usr/bin/env python3
"""AstraNL: simplest possible translate call.

Set ASTRANL_AGENT_KEY environment variable first.
Get a key from: https://astranl.com/agents (or POST /api/agents/register)
"""
import os
import requests

KEY = os.environ.get("ASTRANL_AGENT_KEY")
if not KEY:
    raise SystemExit("set ASTRANL_AGENT_KEY env var")

resp = requests.post(
    "https://astranl.com/capabilities/execute",
    headers={"X-Agent-Key": KEY, "Content-Type": "application/json"},
    json={
        "intent": "translate to dutch: 'Hello world, today is a great day'",
        "capability_id": "translate",
    },
    timeout=30,
)
resp.raise_for_status()
data = resp.json()
print("result:", data["result"])
print("billing:", data.get("billing"))
print("wallet remaining (µEUR):", data.get("wallet_balance_micro_eur"))
