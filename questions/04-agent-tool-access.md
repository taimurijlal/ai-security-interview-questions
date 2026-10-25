# 4. How would you secure an AI agent with access to tools?

![AI agent with tool access](../assets/04-agent-tool-access.webp)

## The mistake candidates make

One mistake is treating an AI agent like a traditional chatbot and focusing mainly on the prompts it receives.

Another is recommending human approval for every action without considering how that would affect the application's usefulness.

I've also seen discussions about agent security that completely overlook identity and permissions.

That's a serious omission.

## How I'd answer

I'd start by asking what the agent can actually do.

Can it only retrieve information, or can it execute code, query databases, send emails and modify cloud infrastructure?

Let's imagine an AI agent that helps an IT operations team investigate AWS security findings.

The agent can inspect resources, retrieve logs and recommend remediation actions.

I'd begin by defining its identity and access permissions.

For example, the agent might have permission to read CloudWatch logs, query security findings and inspect EC2 configurations.

But it shouldn't automatically have permission to change IAM policies or delete production resources.

I'd separate low-risk, read-only activities from higher-impact operations.

Sensitive actions should pass through an independent authorisation mechanism, with human approval where appropriate.

I'd also implement execution limits, tool allowlists, scoped credentials, logging and the ability to suspend or revoke the agent's access.

Then I'd test realistic failure scenarios.

What happens if a malicious document instructs the agent to change a security group? What if it repeatedly calls a tool? What if a compromised integration attempts to invoke another tool with greater privileges?

## Why this is a stronger answer

The risk associated with AI agents isn't simply that they might produce incorrect information.

It's that they can turn incorrect decisions into real actions.

The solution is to control the authority the agent has, rather than relying entirely on its ability to make correct decisions.

That allows organisations to benefit from automation without granting agents unrestricted power.

## What I'd demonstrate

An agent that can autonomously perform approved read-only operations but requires independently enforced approval before making privileged changes.

**In the lab:**

- `lookup_customer` (read) runs straight away, with no approval needed.
- `delete_record` (write) is denied unless a human approver says yes.
- `send_email` to a non-allowlisted domain is denied **even with approval**.
- An agent identity without the `records:write` scope can't delete, whoever approves.
- A request that tries to call tools over and over is cut off at the per-request budget.

```bash
cd lab && python -m unittest tests.test_agent_permissions -v
```

## Follow-ups to expect

- Where does the policy engine run, and what stops the agent bypassing it?
- How do you avoid approval fatigue, where humans click "yes" on everything?
- Should the agent act with the user's permissions, its own, or the intersection?
- How would you implement the kill switch in practice?
