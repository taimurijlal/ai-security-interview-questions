"""The agent loop: retrieve -> model proposes tool calls -> (policy) -> execute."""

import uuid
from dataclasses import dataclass, field
from typing import Callable

from .audit import AuditLog
from .llm import FakeLLM, ToolCall
from .policy import SUPPORT_AGENT, AgentIdentity, PolicyEngine
from .rag import retrieve
from .tools import TOOLS, ToolContext

Approver = Callable[[ToolCall], bool]


def deny_all(call: ToolCall) -> bool:
    return False


@dataclass
class AgentResult:
    trace_id: str
    answer: str
    retrieved: list[str]
    executed: list[ToolCall] = field(default_factory=list)
    blocked: list[tuple[ToolCall, str]] = field(default_factory=list)


class Agent:
    def __init__(self, user: str, *, secure: bool = True,
                 identity: AgentIdentity = SUPPORT_AGENT,
                 approver: Approver = deny_all,
                 policy: PolicyEngine | None = None):
        self.user = user
        self.secure = secure
        self.approver = approver
        self.policy = policy or PolicyEngine(identity)
        self.llm = FakeLLM()
        self.ctx = ToolContext()
        self.audit = AuditLog()

    def run(self, query: str) -> AgentResult:
        trace_id = uuid.uuid4().hex[:12]
        self.audit.record(trace_id, "request", user=self.user, query=query, secure=self.secure)

        docs = retrieve(query, self.user, enforce_acl=self.secure)
        tainted = any(d.source == "external" for d in docs)
        self.audit.record(trace_id, "retrieval",
                          docs=[{"doc_id": d.doc_id, "source": d.source,
                                 "department": d.department} for d in docs],
                          tainted=tainted)

        result = AgentResult(trace_id, self.llm.answer(query, docs), [d.doc_id for d in docs])
        for n, call in enumerate(self.llm.propose(query, docs)):
            self.audit.record(trace_id, "tool_proposed", tool=call.name, args=call.args)
            if self.secure:
                decision = self.policy.evaluate(call, tainted=tainted, calls_so_far=n)
                allowed = decision.allowed
                reason = decision.reason
                if allowed and decision.needs_approval:
                    allowed = self.approver(call)
                    reason = "approved by human" if allowed else "human approval not granted"
                self.audit.record(trace_id, "policy_decision", tool=call.name,
                                  allowed=allowed, reason=reason)
                if not allowed:
                    result.blocked.append((call, reason))
                    continue
            output = TOOLS[call.name].run(self.ctx, call.args)
            self.audit.record(trace_id, "tool_executed", tool=call.name, output=output)
            result.executed.append(call)
        return result
