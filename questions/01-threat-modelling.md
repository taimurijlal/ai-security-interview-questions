# 1. How would you threat model an AI application?

![AI application threat model](../assets/01-threat-model.webp)

## The mistake candidates make

One mistake I'd avoid is immediately reciting a list of vulnerabilities from the OWASP Top 10 for LLM Applications.

Prompt injection, sensitive information disclosure, excessive agency, supply chain vulnerabilities ...

All valid concerns, but listing them doesn't demonstrate that you know how to threat model a real system.

I've seen this problem in traditional cybersecurity interviews as well. Someone knows the threats, but struggles when asked to apply that knowledge to a specific architecture.

## How I'd answer

I'd start by asking the interviewer a few questions about the application.

What is the application supposed to do? Who uses it? What information does it process? Does it simply generate responses, or can it execute actions?

Let's imagine we're discussing a customer support application that uses an LLM, a RAG knowledge base and several external tools.

I'd map the architecture, identifying the application components, data flows, entry points, identities and trust boundaries.

Then I'd focus on what an attacker might control.

For example, an attacker might control a user prompt, a document retrieved from the knowledge base or the response returned by an external tool.

I'd examine whether those lower-trust inputs could influence privileged operations or cause unauthorised data access.

I'd also look beyond AI-specific threats. Could users retrieve documents belonging to other customers? Are service accounts overprivileged? Are APIs properly authenticated?

I'd use STRIDE to structure the assessment and AI-specific guidance from OWASP and MITRE ATLAS to identify additional attack scenarios.

Finally, I'd prioritise findings based on exploitability, business impact and existing controls.

## Why this is a stronger answer

Threat modelling isn't about knowing the largest number of vulnerabilities. It's about understanding how a system could be compromised and identifying the controls that matter most.

A public chatbot that answers general questions has a very different risk profile from an AI agent that can modify customer records or execute cloud infrastructure changes.

The interviewer wants to see whether you understand that distinction.

## What I'd demonstrate

A threat model showing the architecture, trust boundaries, realistic attack paths, risk ratings and recommended controls.

## Follow-ups to expect

- Where exactly is the trust boundary between the retrieved context and the model?
- Which threat would you fix first, and why?
- How does the threat model change when you give the assistant a tool that writes data?
- How would you keep the threat model current as the system changes?
