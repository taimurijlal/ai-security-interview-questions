# 3. How would you secure a RAG application?

![RAG application security](../assets/03-rag-security.webp)

## The mistake candidates make

A common mistake is focusing entirely on the LLM while ignoring the retrieval system.

Candidates might discuss prompt injection and hallucinations without examining how documents enter the knowledge base, who can access them or how retrieval permissions are enforced.

Another mistake is assuming that because information is stored in a vector database, conventional access-control requirements somehow don't apply.

## How I'd answer

I'd begin by understanding the RAG architecture.

Where do the documents come from? Who can upload or modify them? How are they processed, embedded, stored and retrieved?

Then I'd focus on two important areas: protecting the integrity of retrieved content and preventing unauthorised information access.

For example, imagine an organisation has built an internal assistant containing HR, finance and engineering documents.

An employee from the engineering department asks a question, and the retrieval system identifies a highly relevant confidential HR document.

The fact that the document is relevant doesn't mean the employee should be allowed to access it.

I'd enforce document-level access controls based on the authenticated user's permissions. Those controls must be applied during retrieval, not left to the LLM to decide whether information should be disclosed.

I'd also protect the document ingestion pipeline.

Could an attacker upload a poisoned document containing malicious instructions? Could someone alter existing documents without approval? Are documents from external sources treated differently from trusted internal content?

I'd introduce appropriate ingestion controls, provenance tracking, retrieval filtering, tenant isolation and monitoring.

Finally, I'd test whether users can retrieve information outside their permissions and whether malicious documents can influence the application's behaviour.

## Why this is a stronger answer

RAG security isn't just an LLM security problem.

It's also a data security, access-control and application security problem.

**Semantic similarity doesn't equal authorisation.**

An application can have excellent prompt injection defences and still expose confidential information because its retrieval permissions are poorly designed.

## What I'd demonstrate

A RAG application with document-level permissions, synthetic confidential documents and tests proving that unauthorised users cannot retrieve protected content.

## Follow-ups to expect

- Why not just tell the model "don't reveal HR data"?
- How do you keep ACLs in the vector index in sync when permissions change upstream?
- Can embeddings leak the original text?
- How would you detect a poisoned document after it's already been ingested?
