"""Q4 / Q9: least privilege, explicit authorisation, limited blast radius."""

import unittest

from secure_agent import Agent, AgentIdentity, PolicyEngine
from secure_agent.llm import ToolCall
from secure_agent.tools import READ, TOOLS


class AgentPermissionsTest(unittest.TestCase):
    def test_read_only_tool_runs_without_approval(self):
        result = Agent("alice").run("lookup_customer C0042")
        self.assertEqual([c.name for c in result.executed], ["lookup_customer"])

    def test_write_requires_human_approval(self):
        agent = Agent("alice")
        result = agent.run("delete_record R-17")
        self.assertIn("R-17", agent.ctx.records)
        self.assertEqual(result.blocked[0][1], "human approval not granted")

    def test_write_runs_once_approved(self):
        agent = Agent("alice", approver=lambda call: True)
        agent.run("delete_record R-17")
        self.assertNotIn("R-17", agent.ctx.records)

    def test_identity_without_scope_cannot_write_even_if_approved(self):
        read_only = AgentIdentity("faq-bot", frozenset({"customers:read"}))
        agent = Agent("alice", identity=read_only, approver=lambda call: True)
        result = agent.run("delete_record R-17")
        self.assertIn("R-17", agent.ctx.records)
        self.assertIn("lacks scope records:write", result.blocked[0][1])

    def test_external_recipient_denied_even_if_approved(self):
        policy = PolicyEngine(AgentIdentity("a", frozenset({"email:send"})))
        decision = policy.evaluate(ToolCall("send_email", {"to": "x@evil.example"}),
                                   tainted=False, calls_so_far=0)
        self.assertFalse(decision.allowed)

    def test_every_side_effecting_tool_needs_approval(self):
        """Guards CI: a newly added tool must not create an unapproved execution path."""
        everything = AgentIdentity("all", frozenset(t.scope for t in TOOLS.values()))
        policy = PolicyEngine(everything)
        valid_args = {"delete_record": {"record_id": "R-1"},
                      "send_email": {"to": "a@example.com"},
                      "lookup_customer": {"customer_id": "C0001"}}
        for tool in TOOLS.values():
            if tool.side_effect == READ:
                continue
            with self.subTest(tool=tool.name):
                self.assertIn(tool.name, valid_args, "add valid sample args for new tools")
                decision = policy.evaluate(ToolCall(tool.name, valid_args[tool.name]),
                                           tainted=False, calls_so_far=0)
                self.assertTrue(decision.needs_approval or not decision.allowed)


if __name__ == "__main__":
    unittest.main()
