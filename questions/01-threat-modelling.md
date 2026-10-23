# 1. How would you threat model an AI application?

![AI application threat model](../assets/01-threat-model.webp)

## The answer

Start with the **architecture**, not a list of vulnerabilities.

Take a customer support application that uses an LLM, a RAG knowledge base and several external tools. Map:

- **Components**: web app, LLM, retrieval system, vector DB, tools/APIs, data sources
- **Data flows**: what goes into the prompt, what comes back out, where it's stored
- **Identities**: who the end user is, what identity the agent and each tool runs as
- **Entry points**: user prompts, document ingestion, tool responses, admin consoles
- **Trust boundaries**: every point where data of one trust level becomes input to something with more authority

Then ask: **what can an attacker control?** In an AI system that's much more than the chat box:

| Attacker-controllable input | Example |
| --- | --- |
| User prompts | Direct injection, jailbreaks |
| Retrieved documents | A poisoned knowledge-base article |
| Tool responses | A third-party API or MCP server returning instructions |
| Ingested data | Uploaded files, scraped web pages, emails |

Combine traditional methods with AI-specific guidance:

- **STRIDE** for each component and data flow
- **OWASP Top 10 for LLM Applications** (prompt injection, sensitive information disclosure, excessive agency, and so on)
- **MITRE ATLAS** for adversary techniques against ML systems

For each threat, record the attack path, the business impact and the control that mitigates it.

## What I'd demonstrate

A threat model that identifies **realistic attack paths**, their **business impact** and the **controls** required to mitigate them. See the lab's [threat model](../lab/README.md#threat-model) for a worked example.

## Follow-ups to expect

- Where exactly is the trust boundary between the retrieved context and the model?
- Which threat would you fix first, and why?
- How does the threat model change when you give the assistant a tool that writes data?
- How would you keep the threat model current as the system changes?
