"""CrewAI integration for AstraNL.

Requires: pip install crewai requests
"""
import os, requests
from crewai_tools import tool

@tool("AstraNL Capability")
def astranl(capability_id: str, intent: str) -> str:
    """Call any of 15 AstraNL AI capabilities.

    capability_id: one of translate, summarize, write, code, classify,
        extract_structured, transform_format, plan_breakdown,
        compare_options, name_brainstorm, proofread, qa, explain,
        analyze_data, document_qa_legal_check.
    intent: natural language description of what to do.
    """
    key = os.environ.get("ASTRANL_AGENT_KEY")
    if not key:
        return "Error: set ASTRANL_AGENT_KEY"
    r = requests.post(
        "https://astranl.com/capabilities/execute",
        headers={"X-Agent-Key": key},
        json={"intent": intent, "capability_id": capability_id},
        timeout=30,
    )
    return r.json().get("result", r.text[:200])
