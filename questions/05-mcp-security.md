# 5. What security risks does MCP introduce?

![MCP integration security](../assets/05-mcp-integration-security.webp)

## The mistake candidates make

Some candidates talk about MCP as though it's inherently insecure.

Others explain how the protocol works but never discuss authentication, authorisation or the trust relationships between the AI application and connected servers.

Knowing how to connect an MCP server isn't the same as knowing how to secure one.

## How I'd answer

I'd explain that the Model Context Protocol provides a standardised way for AI applications to interact with external tools and data sources.

The security implications depend on how those integrations are implemented.

For example, imagine an organisation connects its AI assistant to three MCP servers.

One provides access to internal documentation, another integrates with a ticketing platform and the third can query a production database.

I'd start by understanding who operates each server, how the client authenticates and what permissions the server has.

I'd also examine the trustworthiness of tool descriptions and responses.

A malicious or compromised MCP server could provide misleading tool metadata or return content containing instructions intended to manipulate the AI application.

I'd assess whether the application distinguishes untrusted tool output from trusted instructions.

Then I'd examine the controls around tool execution.

Does the server validate the caller's permissions? Are tool arguments validated? Are credentials properly scoped? Can sensitive information be sent to unapproved destinations?

For the database integration, I'd ensure the MCP server uses appropriately restricted credentials and independently checks whether a requested operation is authorised.

I'd also implement logging, approved server registries and appropriate monitoring.

## Why this is a stronger answer

MCP simplifies connectivity between AI applications and external systems.

But every new integration introduces a trust relationship that needs to be understood and controlled.

An AI application might be securely configured while relying on an external MCP server with excessive database permissions.

That's why I'd assess the entire integration rather than treating the protocol itself as the security boundary.

## What I'd demonstrate

An MCP integration with scoped credentials, server-side authorisation, input validation and audit logging, along with tests showing that unauthorised operations are rejected.

## Follow-ups to expect

- How would you vet a third-party MCP server before allowing it?
- What happens if a server changes its tool descriptions after you approved it?
- How should OAuth tokens flow between the user, the MCP client and the server?
- Local (stdio) vs remote MCP servers: what changes in your threat model?
