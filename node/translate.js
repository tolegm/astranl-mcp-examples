#!/usr/bin/env node
// AstraNL: minimal Node.js translate call
// Set ASTRANL_AGENT_KEY env var first.
const key = process.env.ASTRANL_AGENT_KEY;
if (!key) { console.error('set ASTRANL_AGENT_KEY env var'); process.exit(1); }

const resp = await fetch('https://astranl.com/capabilities/execute', {
  method: 'POST',
  headers: { 'X-Agent-Key': key, 'Content-Type': 'application/json' },
  body: JSON.stringify({
    intent: "translate to dutch: 'Hello, today is a great day'",
    capability_id: 'translate',
  }),
});
const data = await resp.json();
console.log('result:', data.result);
console.log('billing:', data.billing);
