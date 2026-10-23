# AI Security Engineer Interview Questions (2026)

Ten scenario-based questions that keep coming up in AI Security Engineer and Agentic AI Security Engineer job descriptions, with model answers, diagrams, and a small runnable lab you can use as your "show, don't tell" evidence.

> Knowing AI security terminology and knowing how to secure an AI application are two very different things.

## Why this repo exists

The hiring manager's real question is rarely "what is prompt injection?". It is:

> *"We're deploying an AI agent that can access customer information, retrieve internal documents and execute actions through APIs. How would you secure it?"*
> …followed by: *"What would you actually implement to stop it accessing information it shouldn't, or performing an unauthorised action?"*

Most of what employers ask for is **not new**: threat modelling, secure coding, cloud security, Python, IAM, security architecture. It is traditional security engineering applied to LLMs, RAG, MCP and agents. If you already know AppSec, cloud or IAM, you don't start from scratch. You learn where AI systems introduce new risks and apply what you know.

### The market signal

From the UK Government's *Cyber Security Skills in the UK Labour Market 2026* report:

| Signal | Figure |
| --- | --- |
| Core cyber job postings asking for AI skills | ~4% → **~9%** in one year |
| Cyber firms expecting AI-skill needs to grow (next 12 months) | **73%** |
| Employment in UK cyber firms offering AI security services | 9,740 → 14,720 (**+51%**) |

These aren't all dedicated AI Security Engineer roles, but they show AI security becoming a core part of the industry.

## The 10 questions

| # | Question | Diagram | Lab evidence |
| --- | --- | --- | --- |
| 1 | [How would you threat model an AI application?](questions/01-threat-modelling.md) | <img src="assets/01-threat-model.webp" width="220"> | [Threat model](lab/README.md#threat-model) |
| 2 | [What is prompt injection, and how would you prevent it?](questions/02-prompt-injection.md) | <img src="assets/02-prompt-injection.webp" width="220"> | `test_prompt_injection.py` |
| 3 | [How would you secure a RAG application?](questions/03-rag-security.md) | <img src="assets/03-rag-security.webp" width="220"> | `test_rag_access.py` |
| 4 | [How would you secure an AI agent with access to tools?](questions/04-agent-tool-access.md) | <img src="assets/04-agent-tool-access.webp" width="220"> | `test_agent_permissions.py` |
| 5 | [What security risks does MCP introduce?](questions/05-mcp-security.md) | <img src="assets/05-mcp-integration-security.webp" width="220"> | `test_tool_inputs.py` |
| 6 | [How would you perform AI red teaming?](questions/06-ai-red-teaming.md) | <img src="assets/06-ai-red-teaming.webp" width="220"> | `python -m secure_agent.redteam` |
| 7 | [How would you secure AI models and data in the cloud?](questions/07-cloud-ai-security.md) | <img src="assets/07-ai-application-in-aws.webp" width="220"> | [AWS review checklist](questions/07-cloud-ai-security.md#review-checklist) |
| 8 | [How would you detect and investigate an AI security incident?](questions/08-incident-investigation.md) | <img src="assets/08-incident-investigation.webp" width="220"> | `test_incident_trace.py` |
| 9 | [How would you integrate AI security into CI/CD?](questions/09-ai-security-cicd.md) | <img src="assets/09-ai-security-in-cicd.webp" width="220"> | [`.github/workflows/ai-security.yml`](.github/workflows/ai-security.yml) |
| 10 | [How would you explain AI security risk to senior leadership?](questions/10-explaining-risk-to-leadership.md) | <img src="assets/10-explaining-risk-to-leadership.webp" width="220"> | [Risk memo example](questions/10-explaining-risk-to-leadership.md#example-risk-memo) |

Each question page has the same shape:

1. **The answer**: how to approach it out loud.
2. **What I'd demonstrate**: the concrete artefact that proves you can do it.
3. **Follow-ups to expect**: where a good interviewer will push next.

## The lab: one project, ten answers

The single best piece of prep: build **one** realistic AI application with an LLM, RAG, tools and an agent. Deliberately introduce weaknesses, exploit them in a controlled environment, then fix them.

[`lab/`](lab/) is a minimal, dependency-free version of that project. It runs the same agent in two modes:

- `secure=False`: the naive build. Prompt injection exfiltrates data, retrieval ignores permissions, tools run unchecked.
- `secure=True`: controls enforced **outside the model**. Retrieval-time ACLs, scoped agent identity, a policy engine, taint tracking for untrusted content, recipient allowlists, human approval and an audit trail.

```bash
cd lab
python -m secure_agent.redteam          # attack table: vulnerable vs secure
python -m unittest discover -s tests -t .
```

The model in the lab is a deterministic stand-in that **obeys any instructions it reads**. That's deliberate: the controls have to hold even when the model is fully compromised.

## Final advice

> Don't prepare for an AI Security Engineer interview by trying to sound like an AI expert. Prepare by becoming a security engineer who genuinely understands how AI systems work.

## References

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Model Context Protocol specification: security best practices](https://modelcontextprotocol.io/)
- [AWS: Security in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)
