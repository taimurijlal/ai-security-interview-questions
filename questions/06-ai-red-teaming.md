# 6. How would you perform AI red teaming?

![AI red teaming assessment](../assets/06-ai-red-teaming.webp)

## The mistake candidates make

One mistake is confusing AI red teaming with trying random jailbreak prompts until something interesting happens.

Another is measuring success by the number of prompts that cause unusual responses.

A model producing an unexpected answer isn't necessarily evidence of a meaningful security vulnerability.

## How I'd answer

I'd approach AI red teaming as a structured assessment of the application's security boundaries.

First, I'd understand the application architecture and its intended behaviour.

What data can it access? Which tools can it invoke? Which actions should never be possible without authorisation?

Then I'd define realistic attacker objectives.

For example, suppose we're assessing a financial services assistant.

An attacker might try to access another customer's information, influence the assistant through a poisoned document or manipulate a tool call into performing an unauthorised transaction.

I'd create test scenarios around those objectives.

The assessment could cover direct and indirect prompt injection, sensitive information disclosure, tool manipulation, data poisoning and excessive agency.

I'd use OWASP and MITRE ATLAS to help organise the testing.

But I'd be careful about defining what constitutes a successful attack.

If a prompt causes the model to produce an unusual response, that may be worth investigating.

However, if the same prompt causes an unauthorised database query or data disclosure, the security implications are much more significant.

I'd document the attack path, evidence, impact and recommended mitigations.

Then I'd rerun the tests after remediation.

## Why this is a stronger answer

Red teaming should help organisations understand whether attackers can compromise important security objectives.

It shouldn't become a competition to collect impressive jailbreak screenshots.

A strong AI red teaming assessment produces findings that engineering teams can reproduce, prioritise and remediate.

## What I'd demonstrate

A repeatable AI security testing exercise showing attack objectives, test cases, observed outcomes, business impact and regression results.

## Follow-ups to expect

- How do you handle non-determinism: an attack that works 1 time in 20?
- How do you decide severity for an AI finding?
- Manual vs automated red teaming: where does each fit?
- How do you avoid overfitting the defences to your own test set?
