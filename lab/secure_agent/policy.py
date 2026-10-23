"""Policy engine: decides whether a proposed tool call may run. Lives OUTSIDE the model."""

from dataclasses import dataclass

from .llm import ToolCall
from .tools import READ, TOOLS


@dataclass(frozen=True)
class AgentIdentity:
    name: str
    scopes: frozenset[str]


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str
    needs_approval: bool = False


SUPPORT_AGENT = AgentIdentity(
    "support-agent", frozenset({"customers:read", "records:write", "email:send"})
)


class PolicyEngine:
    def __init__(self, identity: AgentIdentity, *,
                 email_domains: tuple[str, ...] = ("example.com",),
                 max_tool_calls: int = 5):
        self.identity = identity
        self.email_domains = email_domains
        self.max_tool_calls = max_tool_calls

    def evaluate(self, call: ToolCall, *, tainted: bool, calls_so_far: int) -> Decision:
        tool = TOOLS.get(call.name)
        if tool is None:
            return Decision(False, f"unknown tool {call.name!r}")
        if calls_so_far >= self.max_tool_calls:
            return Decision(False, "tool call budget exceeded")
        if tool.scope not in self.identity.scopes:
            return Decision(False, f"identity {self.identity.name} lacks scope {tool.scope}")
        if error := tool.validate(call.args):
            return Decision(False, f"invalid input: {error}")
        if tool.name == "send_email":
            domain = call.args["to"].rsplit("@", 1)[1].lower()
            if domain not in self.email_domains:
                return Decision(False, f"recipient domain {domain} not allowlisted")
        if tool.side_effect == READ:
            return Decision(True, "read-only tool within scope")
        # Untrusted content cannot grant itself authority to act.
        if tainted:
            return Decision(False, "side-effecting call proposed with untrusted content in context")
        return Decision(True, "side-effecting tool: human approval required", needs_approval=True)
