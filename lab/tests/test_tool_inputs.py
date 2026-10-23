"""Q5: MCP-style tools get validated inputs, an unknown-tool deny and a call budget."""

import unittest

from secure_agent import Agent, AgentIdentity, PolicyEngine
from secure_agent.llm import ToolCall


class ToolInputTest(unittest.TestCase):
    def test_malformed_argument_rejected_before_tool_runs(self):
        result = Agent("alice").run("lookup_customer C0001;DROP")
        self.assertEqual(result.executed, [])
        self.assertIn("invalid input", result.blocked[0][1])

    def test_vulnerable_agent_passes_malformed_argument_through(self):
        result = Agent("alice", secure=False).run("lookup_customer C0001;DROP")
        self.assertEqual(result.executed[0].args["customer_id"], "C0001;DROP")

    def test_unknown_tool_denied(self):
        policy = PolicyEngine(AgentIdentity("a", frozenset({"*"})))
        decision = policy.evaluate(ToolCall("run_shell", {"cmd": "id"}),
                                   tainted=False, calls_so_far=0)
        self.assertFalse(decision.allowed)

    def test_tool_call_budget(self):
        query = " ".join(f"lookup_customer C000{i}" for i in range(1, 9))
        result = Agent("alice").run(query)
        self.assertEqual(len(result.executed), 5)
        self.assertTrue(all(r == "tool call budget exceeded" for _, r in result.blocked))

    def test_every_decision_is_audited(self):
        agent = Agent("alice")
        agent.run("lookup_customer C0001;DROP")
        decisions = [e for e in agent.audit.events if e["event"] == "policy_decision"]
        self.assertEqual(len(decisions), 1)
        self.assertFalse(decisions[0]["allowed"])


if __name__ == "__main__":
    unittest.main()
