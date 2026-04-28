#!/usr/bin/env python3
"""AstraNL: connect via MCP SSE protocol (proper JSON-RPC).

Requires: pip install mcp
"""
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("https://astranl.com/mcp/sse") as (read, write):
        async with ClientSession(read, write) as sess:
            await sess.initialize()
            tools = await sess.list_tools()
            print(f"AstraNL exposes {len(tools.tools)} tools:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description[:80]}...")
            # Example: estimate cost without consuming wallet
            result = await sess.call_tool(
                "estimate_cost",
                {"category": "painting", "area_m2": 50, "location": "Amsterdam"}
            )
            print("\nestimate_cost result:")
            for c in result.content:
                print(c.text if hasattr(c, 'text') else c)

asyncio.run(main())
