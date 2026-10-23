"""A deterministic stand-in for an LLM that is fully susceptible to prompt injection.

It obeys tool-call instructions found ANYWHERE in its prompt: the user's
request or retrieved documents. That is the worst case on purpose. The
security controls in this lab must hold even when the model is compromised.
"""

import re
from dataclasses import dataclass, field

from .documents import Document


@dataclass
class ToolCall:
    name: str
    args: dict = field(default_factory=dict)


_PATTERNS = [
    (re.compile(r"send_email to (\S+@[\w.-]+\w)"), "send_email", "to"),
    (re.compile(r"lookup_customer (\S+)"), "lookup_customer", "customer_id"),
    (re.compile(r"delete_record (\S+)"), "delete_record", "record_id"),
]


class FakeLLM:
    def propose(self, query: str, context: list[Document]) -> list[ToolCall]:
        prompt = "\n".join([query, *(d.text for d in context)])
        calls = []
        for pattern, tool, arg in _PATTERNS:
            for match in pattern.finditer(prompt):
                args = {arg: match.group(1)}
                if tool == "send_email":
                    # Exfiltrate whatever the model can see.
                    args["body"] = " ".join(d.text for d in context)
                calls.append(ToolCall(tool, args))
        return calls

    def answer(self, query: str, context: list[Document]) -> str:
        if not context:
            return "I couldn't find anything relevant."
        return "Based on: " + " | ".join(d.text for d in context)
