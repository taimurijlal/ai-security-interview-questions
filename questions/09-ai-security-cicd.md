# 9. How would you integrate AI security into CI/CD?

![AI security in CI/CD](../assets/09-ai-security-in-cicd.webp)

## The answer

Don't treat AI security as a one-off assessment just before production. Build it into development so every change is checked.

Pipeline stages:

| Stage | Examples |
| --- | --- |
| Static analysis | SAST on application and agent code |
| Dependency scan | SCA on Python/JS packages, model and MCP server versions |
| Secrets detection | No API keys or tokens committed |
| Infrastructure as code | Checks on IAM, network exposure and encryption in Terraform/CDK |
| Prompt injection tests | Known direct and indirect injection payloads |
| Tool permission tests | Every tool's scope and side-effect class asserted |
| Security regression tests | Every past finding replayed as a test |
| AI evaluation datasets | Adversarial prompts with expected *safe* outcomes |

For instance: **if a developer adds a new tool capability, the pipeline should test whether that change creates an unauthorised execution path.** The lab enforces this. A test fails if any registered tool with side effects can run without approval.

**Block deployment if issues are found.**

## What I'd demonstrate

A CI/CD pipeline that fails when a known prompt injection or permission-boundary test succeeds.

See [`.github/workflows/ai-security.yml`](../.github/workflows/ai-security.yml). It runs the unit tests and the red-team suite on every push and pull request; either one failing blocks the merge.

## Follow-ups to expect

- How do you test a non-deterministic model in CI without flaky builds?
- Who owns the adversarial dataset, and how does it grow?
- How do you gate a model version upgrade, not just a code change?
- What runs on every commit vs nightly vs before a release?
