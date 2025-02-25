import unittest

from ruleenginex.constants import OperatorEnum
from ruleenginex.rules import Rules


class TestRules(unittest.TestCase):
    def test_all_rules_match(self):
        rules_data = [
            {"target": "body", "prop": "username", "operator": OperatorEnum.EQUALS, "value": "admin"},
            {"target": "body", "prop": "age", "operator": OperatorEnum.EQUALS, "value": 30},
        ]
        rules = Rules(rules_data)
        request_data = {"body": {"username": "admin", "age": 30}}
        self.assertTrue(rules.evaluate(request_data))

    def test_some_rules_fail(self):
        rules_data = [
            {"target": "body", "prop": "username", "operator": OperatorEnum.EQUALS, "value": "admin"},
            {"target": "body", "prop": "age", "operator": OperatorEnum.EQUALS, "value": 30},
        ]
        rules = Rules(rules_data)
        request_data = {"body": {"username": "admin", "age": 25}}  # Age does not match
        self.assertFalse(rules.evaluate(request_data))

    def test_empty_rules_list(self):
        rules = Rules([])
        request_data = {"body": {"username": "admin"}}
        self.assertTrue(rules.evaluate(request_data))  # No rules means always True


if __name__ == "__main__":
    unittest.main()
