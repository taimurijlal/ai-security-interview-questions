# 10. How would you explain AI security risk to senior leadership?

![Explaining AI risk to leadership](../assets/10-explaining-risk-to-leadership.webp)

## The mistake candidates make

The biggest mistake here is answering a business question with a technical explanation.

You might spend ten minutes describing prompt injection, LLM vulnerabilities and agentic attack techniques without ever explaining what the organisation should be worried about.

Another mistake is presenting every vulnerability as critical without considering likelihood, impact or existing controls.

Senior leadership needs information that supports decisions.

## How I'd answer

I'd start with the business scenario rather than the vulnerability name.

Suppose we've identified an AI agent that can retrieve confidential customer information and send emails through an external integration.

During testing, we demonstrate that attacker-controlled content could influence the agent into attempting to send sensitive information to an unauthorised recipient.

I wouldn't begin by explaining how prompt injection works.

I'd explain the business risk.

> "Our customer support AI assistant has access to sensitive customer records and can communicate with external systems. We've identified a weakness that could allow malicious content to influence its actions, creating a potential route for unauthorised data disclosure."

Then I'd explain the conditions required for the attack to succeed, the information potentially affected and the existing controls.

I'd describe the potential impact, including customer harm, operational consequences and any relevant regulatory obligations.

Next, I'd present practical treatment options.

We could restrict the agent's permissions, prevent communication with unapproved destinations and require authorisation for sensitive operations.

I'd also explain the trade-offs.

For example, requiring human approval for every low-risk action could undermine the productivity benefits of the agent.

A more proportionate approach might allow approved read-only operations to run automatically while requiring independent approval for sensitive actions.

Finally, I'd explain the residual risk and what decision leadership needs to make.

## Why this is a stronger answer

Senior leadership doesn't need to become expert in prompt injection to make an informed security decision.

They need to understand what could happen, how serious the consequences might be, what controls are available and what those controls will cost or change.

That's the difference between identifying a technical vulnerability and managing a business risk.

## What I'd demonstrate

A concise AI security risk assessment showing the business scenario, potential impact, existing safeguards, recommended treatment and residual risk.

## Example risk memo

> **Subject: Risk decision needed — customer support AI assistant**
>
> **Scenario.** Our customer support AI assistant has access to sensitive customer records and can communicate with external systems. During testing we showed that content from outside the company could influence it into trying to email customer data to an unauthorised recipient.
>
> **Conditions for the attack.** The attacker needs to get content in front of the assistant, for example through a customer-submitted article. Today any customer can do this.
>
> **Likelihood: Medium. Impact: High.** Customer personal data could be disclosed, causing customer harm, a likely regulatory notification and reputational damage.
>
> **Existing safeguards.** Outgoing email is logged; staff review escalated tickets.
>
> **Recommended treatment.** (1) Block the assistant from emailing unapproved destinations. (2) Require independent approval for sensitive actions such as sending data or changing records. (3) Let approved read-only operations keep running automatically, so we keep the productivity benefit. About two engineering weeks.
>
> **Residual risk: Low.** Malicious content could still produce a misleading *answer*, but the assistant can no longer move customer data out of the company on its own. We recommend accepting this and reviewing again in six months.
>
> **Decision needed:** approve launch with these controls, or delay.

## Follow-ups to expect

- How would you score this against the company's existing risk register?
- What if leadership wants to launch without the controls?
- How do you avoid either scaremongering or under-selling the risk?
- Which metrics would you report each quarter on AI risk?
