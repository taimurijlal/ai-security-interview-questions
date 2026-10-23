# 3. How would you secure a RAG application?

![RAG application security](../assets/03-rag-security.webp)

## The answer

RAG adds attack surface beyond the LLM:

- **Documents** can contain malicious instructions (poisoning, indirect injection).
- **Retrieval** can expose information across users, departments or tenants.
- **Vector databases** can be misconfigured: public endpoints, shared indexes, no auth.
- **Embeddings** are derived from sensitive text and need the same protection as the source.

Focus areas:

| Area | Control |
| --- | --- |
| Document ingestion | Validate sources, record provenance and owner, scan for embedded instructions, restrict who can add content |
| Access control | Carry document ACLs into the index; filter **at retrieval time** using the caller's identity |
| Tenant isolation | Separate indexes or mandatory tenant filters that application code can't skip |
| Retrieval filtering | Drop documents the user can't read *before* they reach the prompt, not after the answer |
| Monitoring | Log which documents were retrieved for which user and request |

The rule to state clearly: **a user from Department A should never retrieve confidential documents from Department B, even when those documents are semantically relevant to their question.** Relevance is not authorisation.

Also test whether poisoned documents can influence the application's behaviour.

## What I'd demonstrate

A RAG application with document-level permissions, adversarial test cases and evidence that access controls are enforced during retrieval.

In the lab, `alice` (support) asks about "salary bands". The vulnerable retriever returns the confidential HR document because it's the best match. The secure retriever filters by department before ranking, so the HR document never enters the prompt. `bob` (HR) still gets it.

```bash
cd lab && python -m unittest tests.test_rag_access -v
```

## Follow-ups to expect

- Why not just tell the model "don't reveal HR data"?
- How do you keep ACLs in the vector index in sync when permissions change upstream?
- Can embeddings leak the original text?
- How would you detect a poisoned document after it's already been ingested?
