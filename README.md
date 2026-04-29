<p align="center">
  <img src="https://astranl.com/brand/astranl-logo-400.png" alt="AstraNL logo" width="160" height="160"/>
</p>

# AstraNL MCP — working examples

15 ready-to-use AI capabilities through a single MCP / HTTP endpoint with
prepaid wallet, transparent micro-EUR billing, **0% margin on inference**,
15% coordination fee. Multi-provider mesh (Anthropic, OpenAI, Gemini, Grok)
with automatic failover.

**Live endpoint**: https://astranl.com/mcp/sse
**Tools list (HTTP)**: https://astranl.com/mcp/tools.json
**llms.txt**: https://astranl.com/llms-full.txt

## Why use AstraNL

- **One endpoint** — 15 capabilities (translate, write, code, summarize,
  classify, extract_structured, transform_format, plan_breakdown,
  compare_options, name_brainstorm, proofread, qa, explain,
  analyze_data, document_qa_legal_check).
- **Multi-provider** — routed to the cheapest healthy model that meets
  the task class. Anthropic, OpenAI, Gemini, Grok all in mesh.
- **No subscription** — prepaid wallet starting from €5. Each call
  billed in micro-EUR (1 EUR = 1 000 000 µEUR).
- **No margin on inference** — you pay the actual provider cost. AstraNL
  takes only the 15% coordination fee that covers infrastructure.
- **EU-hosted** — KvK 88449335, EU AI Act ready, GDPR compliant.

## Quick start (3 commands)

```bash
# 1. Register an agent (no email verification, no waitlist)
curl -X POST https://astranl.com/api/agents/register \
  -H 'Content-Type: application/json' \
  -d '{"name":"my-bot","owner_email":"you@example.com"}'
# → returns {"agent_id":"agent_...","agent_key":"ask_..."}

# 2. Top up the wallet (Stripe Checkout, EUR)
curl -X POST https://astranl.com/api/agents/wallet/topup \
  -H 'X-Agent-Key: ask_YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"amount_cents":500}'
# → returns {"checkout_url":"https://checkout.stripe.com/..."}

# 3. Execute a capability
curl -X POST https://astranl.com/capabilities/execute \
  -H 'X-Agent-Key: ask_YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"intent":"translate to dutch: hello world","capability_id":"translate"}'
# → returns {"result":"hallo wereld","billing":{"inference_micro_eur":1000,"coordination_micro_eur":150,"total_micro_eur":1150}}
```

## What €5 buys you

Real numbers. No marketing math.

| Capability | Approx. cost / call | Calls per €5 wallet |
|---|---|---|
| translate | €0.00115 | ~4348 |
| summarize | €0.00200 | ~2500 |
| write (short) | €0.00350 | ~1428 |
| code (small) | €0.01150 | ~435 |
| analyze_data | €0.00500 | ~1000 |

(€5 wallet credit costs €5.38 incl. €0.30 Stripe fee + 1.5%.)

## Examples in this repo

Each folder is self-contained. Set `ASTRANL_AGENT_KEY` and run.

- [`python/translate.py`](python/translate.py) — simplest possible call
- [`python/code_review.py`](python/code_review.py) — review a Python file
- [`python/batch_summarize.py`](python/batch_summarize.py) — process N docs in parallel
- [`python/mcp_client.py`](python/mcp_client.py) — connect via MCP SSE
- [`node/translate.js`](node/translate.js) — Node.js minimal
- [`langchain/astranl_tool.py`](langchain/astranl_tool.py) — LangChain Tool wrapper
- [`crewai/astranl_agent.py`](crewai/astranl_agent.py) — CrewAI integration
- [`bash/curl_examples.sh`](bash/curl_examples.sh) — every capability via curl

## MCP client config

Add to your Claude Desktop or other MCP client `mcp_config.json`:

```json
{
  "mcpServers": {
    "astranl": {
      "url": "https://astranl.com/mcp/sse",
      "transport": "sse"
    }
  }
}
```

## Honest limitations

- **Test mode billing**: First wallet topup is real money. There is no free
  trial because AstraNL does not subsidise inference cost.
- **Latency**: Adds one network hop vs calling Anthropic / OpenAI directly.
  Typical overhead 50-150ms.
- **Rate limits**: 60 calls/minute per agent_key by default. Higher available
  on request.
- **Provider health**: If all four providers fail simultaneously, calls
  return 503 and the wallet is not charged.

## Source

- MCP server source: https://github.com/tolegm/astranl-mcp
- Coordination protocol spec: https://astranl.com/economy/manifest
- Public economy state: https://astranl.com/economy/state

## License

MIT for these examples. The AstraNL service itself is proprietary but
the API is fully public and self-documenting via OpenAPI.
