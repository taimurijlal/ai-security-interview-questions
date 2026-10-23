# Lab: one AI agent, vulnerable and secured

A small, dependency-free Python project that gives you concrete evidence for most of the ten questions. Python 3.10+, standard library only.

```bash
cd lab
python -m secure_agent.redteam              # attack table, vulnerable vs secure
python -m unittest discover -s tests -t .   # full test suite
```

## Architecture

```
user ──► Agent.run(query)
           │
           ├─ rag.retrieve()        documents.py  (ACL filter in secure mode)
           │
           ├─ FakeLLM.propose()     llm.py        (obeys ANY instruction it reads)
           │
           ├─ PolicyEngine.evaluate()  policy.py  (secure mode only, outside the model)
           │     scope ─► input validation ─► allowlists ─► taint ─► human approval
           │
           ├─ tools.TOOLS[...].run()   tools.py   (lookup_customer / delete_record / send_email)
           │
           └─ AuditLog.record()        audit.py   (JSON events, one trace_id per request)
```

`FakeLLM` is a deterministic stand-in for a real model that is **completely** vulnerable to prompt injection. Swapping in a real LLM makes the model harder to fool but changes nothing about the controls. That's the point: security is enforced by the system around the model.

## Threat model

Example application: a customer support agent with a RAG knowledge base and three tools.

**Assets:** customer records, confidential HR documents, the company's email reputation, data integrity.
**Attacker-controlled inputs:** user prompts, customer-submitted knowledge-base articles (`source="external"`), tool arguments derived from either.

| # | Threat (STRIDE / OWASP LLM) | Attack path | Impact | Control in this lab | Test |
| --- | --- | --- | --- | --- | --- |
| T1 | Indirect prompt injection → exfiltration (Info disclosure / LLM01) | Poisoned article `sup-003` tells the model to `send_email` to attacker | Customer/HR data leaves the company | Taint tracking: no side-effecting calls with external content in context; recipient domain allowlist | `test_prompt_injection` |
| T2 | Cross-department retrieval (Info disclosure / LLM02) | Support user asks about salary bands | Confidential HR data disclosed | ACL filter at retrieval time, before ranking | `test_rag_access` |
| T3 | Excessive agency (Elevation of privilege / LLM06) | User or injected text asks the agent to `delete_record` | Data loss | Scoped agent identity; human approval for write/external tools | `test_agent_permissions` |
| T4 | Tool argument injection (Tampering) | `lookup_customer C0001;DROP` | Downstream injection | Per-tool input validation (MCP-style schema) | `test_tool_inputs` |
| T5 | Resource abuse (DoS / LLM10) | Prompt triggers many tool calls | Cost, downstream load | Tool-call budget per request | `test_tool_inputs` |
| T6 | Repudiation / no forensics | Agent acts, nobody can say why | Can't investigate or contain | Structured audit trail with trace IDs | `test_incident_trace` |

## Exercises to extend it

- Swap `FakeLLM` for a real model (e.g. via Amazon Bedrock) and check the tests still pass.
- Add an output filter that redacts customer IDs from answers to unauthenticated users.
- Add a new `refund_payment` tool and watch `test_every_side_effecting_tool_needs_approval` force you to classify it.
- Turn `PolicyEngine` into an MCP proxy that sits between a client and real MCP servers.
- Write a detection rule over the JSONL audit log: alert on any denied `send_email` with `tainted=true`.
