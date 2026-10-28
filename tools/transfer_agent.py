"""
HO-4.1.3 - Observe an LLM-powered agent automating a repetitive test task (LedgerLeaf Bank)

Task the agent gets: check the US-05 transfer-amount rules against the RUNNING app via its API,
choose its own test values, run them, and write a short defect report.

The agent loop:  LLM decides -> calls a tool -> sees the result -> decides again ... -> final report.
Tools are plain Python functions; the LLM (Ollama, local) only chooses which tool to call with which arguments.

Usage (app running in another window, Ollama running):
    python tools/transfer_agent.py
    python tools/transfer_agent.py --model llama3.1:8b --max-steps 15
"""
import argparse
import json
import pathlib
import requests

APP = "http://127.0.0.1:5000"
OLLAMA = "http://localhost:11434/api/chat"
DEMO = {"email": "alex.tester@ledgerleaf.test", "from_account": "100-001", "to_account": "100-002"}

RULES = ("US-05 transfer amount rules: minimum $0.01; maximum $5,000.00 per transfer, INCLUSIVE "
         "(exactly 5000.00 must be accepted); at most two decimal places; the amount must be positive; "
         "the amount cannot exceed the balance of the source account (100-001 has $12,500.00 after a reset).")


# ------------------------------------------------------------------ tools
def reset_data() -> str:
    """Restore the demo data (balances back to the start values)."""
    requests.post(f"{APP}/api/test/reset", timeout=10)
    return "Demo data reset. 100-001 = $12,500.00, 100-002 = $800.00."


def transfer(amount: str) -> str:
    """Transfer AMOUNT from 100-001 to 100-002 via POST /api/transfers and return the HTTP result."""
    r = requests.post(f"{APP}/api/transfers", json={**DEMO, "amount": amount}, timeout=10)
    return json.dumps({"amount": amount, "http_status": r.status_code, "body": r.json()})


TOOLS = {"reset_data": reset_data, "transfer": transfer}
TOOL_SPECS = [
    {"type": "function", "function": {
        "name": "reset_data", "description": reset_data.__doc__,
        "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {
        "name": "transfer", "description": transfer.__doc__ + " HTTP 201 = accepted, 400 = rejected.",
        "parameters": {"type": "object", "properties": {
            "amount": {"type": "string", "description": "Amount as text, e.g. '5000.00' or '-1'"}},
            "required": ["amount"]}}},
]

SYSTEM = ("You are a software test agent for LedgerLeaf Bank. " + RULES +
          " Use the tools to test the amount boundaries and invalid values one by one: call reset_data "
          "before each transfer. After testing, reply with a final report as a Markdown table "
          "| Amount | Expected | Actual HTTP status | Pass/Fail | and list every failure as a defect. "
          "Expected: accepted = HTTP 201, rejected = HTTP 400.")


def chat(model, messages):
    r = requests.post(OLLAMA, json={"model": model, "messages": messages, "tools": TOOL_SPECS,
                                    "stream": False, "options": {"temperature": 0}}, timeout=600)
    r.raise_for_status()
    return r.json()["message"]


GUIDED = (" Test exactly these amounts, one at a time, calling reset_data before each: "
          "0.00, 0.01, 4999.99, 5000.00, 5000.01, -1, 10.005, 12500.01. "
          "Do NOT write the final report until all 8 amounts have been tested.")


def run(model, max_steps, chat_fn=chat, guided=False):
    task = "Test the transfer amount rules of US-05 now." + (GUIDED if guided else "")
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": task}]
    mode = "guided" if guided else "open"
    log = [f"# HO-4.1.3 agent run ({model}, {mode})", ""]
    for step in range(1, max_steps + 1):
        msg = chat_fn(model, messages)
        messages.append(msg)
        calls = msg.get("tool_calls") or []
        if not calls:                                   # no tool call -> the agent is done
            print(f"\n=== FINAL REPORT (step {step}) ===\n{msg.get('content', '')}")
            log += ["## Final report", msg.get("content", "")]
            break
        for c in calls:
            name = c["function"]["name"]
            args = c["function"].get("arguments") or {}
            if isinstance(args, str):
                args = json.loads(args or "{}")
            result = TOOLS[name](**args) if name in TOOLS else f"Unknown tool {name}"
            print(f"[step {step}] {name}({args}) -> {result}")
            log.append(f"- step {step}: `{name}({args})` → {result}")
            messages.append({"role": "tool", "tool_name": name, "content": result})
    else:
        print(f"\nStopped after {max_steps} steps without a final report.")
        log.append(f"Stopped after {max_steps} steps without a final report.")
    out = pathlib.Path(__file__).resolve().parents[1] / "reports" / f"4.1.3-agent-run_{model.replace(':', '-')}_{mode}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"\nLog written to {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama3.1:8b")
    ap.add_argument("--max-steps", type=int, default=25)
    ap.add_argument("--guided", action="store_true", help="give the agent an explicit list of amounts to test")
    a = ap.parse_args()
    run(a.model, a.max_steps, guided=a.guided)
