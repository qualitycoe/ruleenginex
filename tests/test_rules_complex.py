import unittest

from ruleenginex.constants import OperatorEnum
from ruleenginex.rules import Rules


class TestRulesComplex(unittest.TestCase):
    def test_rules_with_nested_data(self):
        rules_data = [
            {"target": "body", "prop": "user.details.age", "op": "EQUALS", "value": 30},
            {"target": "body", "prop": "user.details.name", "op": "EQUALS", "value": "Alice"},
        ]
        rules = Rules(rules_data)
        request_data = {"body": {"user": {"details": {"age": 30, "name": "Alice"}}}}
        self.assertTrue(rules.evaluate(request_data))

    def test_rules_with_mixed_data_types(self):
        rules_data = [
            {"target": "body", "prop": "count", "op": "EQUALS", "value": 100},
            {"target": "body", "prop": "is_active", "op": "EQUALS", "value": False},
            {"target": "body", "prop": "tags", "op": "ARRAY_INCLUDES", "value": "featured"},
        ]
        rules = Rules(rules_data)
        request_data = {"body": {"count": 100, "is_active": False, "tags": ["featured", "popular"]}}
        self.assertTrue(rules.evaluate(request_data))

    def test_rules_with_conflicting_conditions(self):
        rules_data = [
            {"target": "body", "prop": "status", "op": "EQUALS", "value": "active"},
            {"target": "body", "prop": "status", "op": "EQUALS", "value": "inactive"},
        ]
        rules = Rules(rules_data)
        request_data = {"body": {"status": "active"}}
        self.assertFalse(rules.evaluate(request_data))  # Conflicting rules


if __name__ == "__main__":
    unittest.main()
