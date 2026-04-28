#!/bin/bash
# AstraNL: every one of 15 capabilities via curl.
# Set ASTRANL_AGENT_KEY env var first.
set -e
: ${ASTRANL_AGENT_KEY:?"set ASTRANL_AGENT_KEY env var"}
E="https://astranl.com/capabilities/execute"
H1="X-Agent-Key: $ASTRANL_AGENT_KEY"
H2="Content-Type: application/json"

call() {
  local cap="$1"; local intent="$2"
  echo "--- $cap ---"
  curl -s -X POST "$E" -H "$H1" -H "$H2" \
    -d "{\"capability_id\":\"$cap\",\"intent\":\"$intent\"}" \
    | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('result',d)[:200])"
  echo
}

call translate           "translate to dutch: 'good morning'"
call summarize           "Summarize: The Model Context Protocol is an open standard."
call write               "Write a 50-word product description for a coffee mug."
call code                "Write a Python function to count vowels in a string."
call classify            "Classify sentiment: This product is amazing!"
call extract_structured  "Extract JSON {name, age, city} from: John, 30, Amsterdam"
call transform_format    "Convert to YAML: {name: John, age: 30}"
call plan_breakdown      "Break into steps: launch a podcast in 30 days"
call compare_options     "Compare PostgreSQL vs MongoDB for a small startup"
call name_brainstorm     "Suggest 5 names for a Dutch coffee subscription"
call proofread           "Fix this: 'their is two many error in the code'"
call qa                  "What is the boiling point of water at sea level?"
call explain             "Explain HTTP/2 multiplexing in simple terms"
call analyze_data        "Analyze: sales [120, 135, 110, 180, 200]"
call document_qa_legal_check "Check for red flags: 'Renter waives all liability'"
