#!/usr/bin/env python3
"""AstraNL: summarize many texts in parallel."""
import os, sys, json
import concurrent.futures
import requests

KEY = os.environ.get("ASTRANL_AGENT_KEY")
if not KEY:
    raise SystemExit("set ASTRANL_AGENT_KEY env var")

def summarize(text: str) -> str:
    resp = requests.post(
        "https://astranl.com/capabilities/execute",
        headers={"X-Agent-Key": KEY},
        json={"intent": f"Summarize in 2 sentences: {text}",
              "capability_id": "summarize"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["result"]

if __name__ == "__main__":
    texts = sys.argv[1:] or [
        "The European Union AI Act establishes risk-based regulation.",
        "Stripe Connect lets platforms split payments between parties.",
        "Model Context Protocol is an open standard for AI tool use.",
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        for original, summary in zip(texts, ex.map(summarize, texts)):
            print(f"-- {original[:60]}\n   → {summary}\n")
