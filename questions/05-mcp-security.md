# 5. What security risks does MCP introduce?

![MCP integration security](../assets/05-mcp-integration-security.webp)

## The answer

The Model Context Protocol (MCP) lets AI applications connect to tools and external capabilities through a standard client/server interface.

**The protocol itself isn't automatically insecure.** The risk depends on how servers, tools, credentials and trust relationships are implemented. What to examine:

| Risk | What it looks like |
| --- | --- |
| Malicious tool responses | A server returns text containing instructions: indirect prompt injection via tools |
| Overly broad permissions | A "database" MCP server connecting with a full read/write admin account |
| Credential exposure | Tokens in config files, passed through to the model, or shared across users |
| Unauthorised tool invocation | The model calls a tool the user never intended, or with attacker-supplied arguments |
| Third-party server trust | An unvetted external server; tool descriptions that change after approval |

Concrete example: **an MCP server offering database access shouldn't automatically inherit unrestricted database permissions.** Give it a dedicated, read-only, schema-limited credential, and validate every argument it receives.

Controls: an allowlist of approved servers, pinned versions, scoped per-server credentials, schema validation on tool inputs, tool responses treated as untrusted content, and auditing of every invocation.

## What I'd demonstrate

An MCP integration with scoped credentials, validated tool inputs and auditable tool execution.

The lab models each tool like an MCP tool: a name, a required scope, a side-effect class and an input validator. `lookup_customer` only accepts IDs matching `C` plus four digits. Injection payloads such as `C0001;DROP` are rejected before the tool runs, and every decision is written to the audit log.

```bash
cd lab && python -m unittest tests.test_tool_inputs -v
```

## Follow-ups to expect

- How would you vet a third-party MCP server before allowing it?
- What happens if a server changes its tool descriptions after you approved it?
- How should OAuth tokens flow between the user, the MCP client and the server?
- Local (stdio) vs remote MCP servers: what changes in your threat model?
