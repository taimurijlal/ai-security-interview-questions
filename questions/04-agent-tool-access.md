# 4. How would you secure an AI agent with access to tools?

![AI agent with tool access](../assets/04-agent-tool-access.webp)

## The answer

This is probably the most important question to prepare for. Unlike a chatbot, an agent might execute code, query databases, send emails or change cloud infrastructure. A bad output is no longer just bad text. It's an action.

Three principles:

1. **Least privilege**: every agent has its own clearly defined identity with narrowly scoped permissions. No shared admin credentials, and no inheriting the full rights of the user or the service account.
2. **Explicit authorisation**: sensitive operations (write, delete, external send, infrastructure changes) need independent approval, **enforced outside the model**. The model can *propose* an action; a policy layer *decides*.
3. **Limit the consequences of failure**: assume the agent will eventually be manipulated, and cap the damage.

Supporting controls:

- Execution limits: max tool calls per request, rate limits, timeouts, spend caps
- Allowlists on high-risk arguments (email recipient domains, target accounts, regions)
- Monitoring and audit trails for every proposed and executed action
- An emergency shutdown that revokes the agent's credentials and stops it

## What I'd demonstrate

An agent that can perform approved read-only actions but cannot modify sensitive resources without authorisation.

In the lab:

- `lookup_customer` (read) runs straight away.
- `delete_record` (write) is denied unless a human approver says yes.
- `send_email` to a non-allowlisted domain is denied **even with approval**.
- An agent identity without the `records:write` scope can't delete, whoever approves.
- A request that would exceed the tool-call budget is cut off.

```bash
cd lab && python -m unittest tests.test_agent_permissions -v
```

## Follow-ups to expect

- Where does the policy engine run, and what stops the agent bypassing it?
- How do you avoid approval fatigue, where humans click "yes" on everything?
- Should the agent act with the user's permissions, its own, or the intersection?
- How would you implement the kill switch in practice?
