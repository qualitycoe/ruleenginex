import unittest

from ruleenginex.scenario import Scenario


class TestScenario(unittest.TestCase):
    def test_scenario_match(self):
        scenario = Scenario(
            scenario_name="Valid Login",
            rules_data=[{"target": "body", "prop": "username", "op": "EQUALS", "value": "admin"}],
            response={"status": 200, "data": {"message": "Login successful"}},
        )
        request_data = {"body": {"username": "admin"}}
        self.assertTrue(scenario.evaluate(request_data))

    def test_scenario_no_match(self):
        scenario = Scenario(
            scenario_name="Invalid Login",
            rules_data=[{"target": "body", "prop": "username", "op": "EQUALS", "value": "admin"}],
            response={"status": 403, "data": {"error": "Unauthorized"}},
        )
        request_data = {"body": {"username": "user"}}  # Does not match
        self.assertFalse(scenario.evaluate(request_data))

    def test_scenario_response(self):
        expected_response = {"status": 200, "data": {"message": "Login successful"}}
        scenario = Scenario(
            scenario_name="Valid Login",
            rules_data=[{"target": "body", "prop": "username", "op": "EQUALS", "value": "admin"}],
            response=expected_response,
        )
        self.assertEqual(scenario.get_response(), expected_response)


if __name__ == "__main__":
    unittest.main()
