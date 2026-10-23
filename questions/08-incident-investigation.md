# 8. How would you detect and investigate an AI security incident?

![AI security incident investigation](../assets/08-incident-investigation.webp)

## The answer

Start by identifying the **telemetry** you need. Traditional application logs may show *that* an agent did something, but not *why*.

For AI systems you need visibility into:

| Source | Answers |
| --- | --- |
| Application logs | Who made the request, when, from where |
| LLM interactions | The user request, retrieved context, model output (where appropriate) |
| Tool execution logs | Which tools were proposed, allowed, denied and executed, with which arguments |
| API / cloud logs | What actually changed in downstream systems (CloudTrail etc.) |
| Identity logs | Which identity/credential was used, and what it was allowed to do |

All of it tied together with a **correlation / trace ID** per request.

Example: an agent unexpectedly accesses sensitive customer records. The investigation reconstructs:

1. **The initiating input**: which user request started it?
2. **The influence**: which input or retrieved document steered the behaviour?
3. **The enabling permission**: which identity and permission allowed the action?
4. **The impact**: which resources were touched, and was data exfiltrated?

Then contain (revoke the agent's credentials, quarantine the poisoned document, disable the tool) and remediate the root cause.

**Preserve evidence while respecting privacy and data-retention requirements.** Prompt logs are often sensitive data in their own right.

## What I'd demonstrate

An incident investigation that traces an unauthorised action from its initiating input to the affected resource.

The lab writes structured JSON audit events (`request`, `retrieval`, `tool_proposed`, `policy_decision`, `tool_executed`) with a shared `trace_id`. The test replays the injection attack and reconstructs the root cause from the log alone: the attempted `send_email` traces back to document `sup-003` from an external source.

```bash
cd lab && python -m unittest tests.test_incident_trace -v
```

## Follow-ups to expect

- How long would you keep full prompt and response logs, and who can read them?
- How do you tell a hallucinated action from an injected one?
- What detections would you write to catch this earlier?
- What's in your containment playbook for a compromised agent?
