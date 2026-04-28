"""LangChain Tool wrapper for AstraNL capabilities.

Requires: pip install langchain requests
"""
import os, requests
from langchain.tools import Tool

def _astranl_call(capability_id: str, intent: str) -> str:
    key = os.environ.get("ASTRANL_AGENT_KEY")
    if not key:
        return "Error: set ASTRANL_AGENT_KEY env var"
    resp = requests.post(
        "https://astranl.com/capabilities/execute",
        headers={"X-Agent-Key": key},
        json={"intent": intent, "capability_id": capability_id},
        timeout=30,
    )
    if resp.status_code != 200:
        return f"AstraNL error {resp.status_code}: {resp.text[:200]}"
    return resp.json().get("result", "")

# A tool per capability — picks just three to demonstrate
astranl_translate = Tool(
    name="astranl_translate",
    description="Translate text between languages. Input: 'translate to <lang>: <text>'",
    func=lambda x: _astranl_call("translate", x),
)
astranl_summarize = Tool(
    name="astranl_summarize",
    description="Summarize text into key points or TL;DR",
    func=lambda x: _astranl_call("summarize", x),
)
astranl_classify = Tool(
    name="astranl_classify",
    description="Classify text into categories or extract sentiment/tags",
    func=lambda x: _astranl_call("classify", x),
)

if __name__ == "__main__":
    print(astranl_translate.run("translate to dutch: 'good morning'"))
