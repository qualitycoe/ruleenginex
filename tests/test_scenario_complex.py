import unittest

from ruleenginex.constants import OperatorEnum
from ruleenginex.scenario import Scenario


class TestScenarioComplex(unittest.TestCase):
    def test_scenario_with_multiple_conditions(self):
        scenario = Scenario(
            scenario_name="Admin Access",
            rules_data=[
                {"target": "body", "prop": "role", "operator": OperatorEnum.EQUALS, "value": "admin"},
                {"target": "body", "prop": "authenticated", "operator": OperatorEnum.EQUALS, "value": True},
            ],
            response={"status": 200, "data": {"message": "Welcome, Admin!"}},
        )
        request_data = {"body": {"role": "admin", "authenticated": True}}
        self.assertTrue(scenario.evaluate(request_data))


if __name__ == "__main__":
    unittest.main()
