# 10. How would you explain AI security risk to senior leadership?

![Explaining AI risk to leadership](../assets/10-explaining-risk-to-leadership.webp)

## The answer

This question is often underestimated. A technically excellent engineer still has to explain **why a vulnerability matters**.

Don't discuss prompt injection in isolation. Translate it into a **business scenario**:

> Our support agent can read confidential customer information and send emails externally. An attacker could plant text in a support article that manipulates the agent into emailing customer data to an outside address.

Then cover, in plain language:

1. **Likelihood**: how realistic is it? Who could do it, and how hard is it?
2. **Impact**: data exposure, regulatory notification (e.g. GDPR), reputational damage, cost.
3. **Existing controls**: what already reduces the risk?
4. **Recommended treatment**: what you propose, what it costs, how long it takes.
5. **Residual risk**: what remains after the fix, and whether it's within appetite.

The outcome leadership needs: an **informed decision**, a risk they can **accept** with eyes open, and a route to **secure AI adoption**, not a reason to say "no".

## Example risk memo

> **Subject: Risk decision needed — customer support AI agent**
>
> **Scenario.** The new support agent can read customer records and send email. Content from outside the company (customer-submitted articles) can influence what it does. An attacker could use this to make it email customer data to an external address.
>
> **Likelihood: Medium.** The technique is public and needs no special access. It needs someone to get content into our knowledge base, which today any customer can do.
>
> **Impact: High.** Disclosure of customer personal data; likely regulatory notification; reputational harm.
>
> **Existing controls.** Staff review outgoing complaints; email is logged.
>
> **Recommendation.** Before launch: (1) block the agent from sending email to non-company domains; (2) require staff approval for any email the agent drafts after reading external content; (3) restrict what customer data the agent can retrieve. About two engineering weeks.
>
> **Residual risk: Low.** The agent may still give wrong *answers* influenced by bad content, but it can no longer move data out of the company on its own. We recommend accepting this and reviewing again in six months.
>
> **Decision needed:** approve the launch with these controls, or delay.

## What I'd demonstrate

A concise risk assessment that connects an AI security weakness to a business outcome and a defensible remediation decision.

## Follow-ups to expect

- How would you score this against the company's existing risk register?
- What if leadership wants to launch without the controls?
- How do you avoid either scaremongering or under-selling the risk?
- Which metrics would you report each quarter on AI risk?
