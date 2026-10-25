# 7. How would you secure AI models and data in the cloud?

![AI application in AWS](../assets/07-ai-application-in-aws.webp)

## The mistake candidates make

Candidates sometimes assume that AI security requires an entirely new set of security controls.

They focus heavily on model-level risks while overlooking the cloud infrastructure, identities, APIs and data stores supporting the application.

Others assume that because they're using a managed AI service, the cloud provider is responsible for securing everything.

That's not how the shared responsibility model works.

## How I'd answer

I'd explain that AI security builds on the same cloud security principles we've been applying for years.

For an AWS-based AI application, I'd start by reviewing the architecture.

Perhaps the application uses Amazon Bedrock, Lambda, API Gateway, S3 and a retrieval system.

I'd examine how users authenticate, which IAM roles are used and what permissions each component requires.

For example, if a Lambda function only needs to invoke a specific model and retrieve documents from one S3 bucket, it shouldn't have broad access to unrelated AWS resources.

I'd review encryption, network connectivity, secrets management, logging and data handling.

I'd also investigate how inference requests and model outputs are processed, where sensitive information is stored and which services can access it.

Then I'd assess AI-specific concerns.

Can untrusted documents influence application behaviour? Can the AI application invoke privileged APIs? Are generated outputs being passed directly into downstream systems without appropriate validation?

If the application includes agents, I'd review their identities, tool permissions and approval mechanisms.

## Why this is a stronger answer

Many serious incidents involving AI applications may ultimately depend on conventional security weaknesses such as excessive IAM permissions, exposed APIs or poor secrets management.

AI introduces new risks, but it doesn't invalidate established security engineering principles.

A candidate who understands both sides is much more valuable than someone who only knows AI-specific attack terminology.

## What I'd demonstrate

A cloud security architecture review identifying excessive permissions, sensitive data exposure, weak network controls and AI-specific attack paths.

## Review checklist

| Area | Check | Common finding |
| --- | --- | --- |
| IAM | Lambda role limited to `bedrock:InvokeModel` on named model ARNs | Wildcard `bedrock:*` / `Resource: *` |
| IAM | S3 access scoped to required prefixes, read-only where possible | Full-bucket write from the inference path |
| Network | VPC endpoints for Bedrock, S3, Secrets Manager | Public egress from Lambda |
| Network | Vector DB not publicly reachable | Open security group / public endpoint |
| Data | S3 Block Public Access, SSE-KMS, bucket policy denies non-TLS | Default encryption only, no key policy review |
| Secrets | Secrets Manager with rotation; no secrets in env vars | API keys in Lambda environment |
| Logging | CloudTrail on, invocation logs to an access-restricted bucket | Prompts with PII logged to a widely readable bucket |
| Retention | Defined retention for prompts, outputs, embeddings | Indefinite retention "for debugging" |
| Edge | API Gateway auth, WAF, throttling | Unauthenticated endpoint, no rate limit (cost abuse) |
| AI-specific | Model output validated before reaching downstream systems | Generated text passed straight into SQL, shell or API calls |
| AI-specific | Agent roles separate from application roles, with approval for writes | Agent shares the Lambda's broad role |

## Follow-ups to expect

- Should you enable model-invocation logging, given it captures sensitive prompts?
- How would you stop a compromised Lambda running up a huge Bedrock bill?
- What does the shared responsibility model look like for a managed LLM service?
- How would you detect a poisoned file landing in the S3 ingestion bucket?
