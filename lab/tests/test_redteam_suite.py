"""Q6: every red-team scenario works against the naive build and fails against the secure one."""

import unittest

from secure_agent.redteam import SCENARIOS, run_scenario


class RedTeamSuiteTest(unittest.TestCase):
    def test_scenarios(self):
        for scenario in SCENARIOS:
            with self.subTest(scenario=scenario.name):
                self.assertTrue(run_scenario(scenario, secure=False), "attack should land on vulnerable build")
                self.assertFalse(run_scenario(scenario, secure=True), "attack should be blocked")


if __name__ == "__main__":
    unittest.main()
