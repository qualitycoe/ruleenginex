import unittest

from ruleenginex.rules import Rules


class TestRules(unittest.TestCase):
    def test_all_rules_match(self):
        rules = [
            {"target": "body", "prop": "username", "op": "EQUALS", "value": "admin"},
            {"target": "body", "prop": "age", "op": "EQUALS", "value": 30},
        ]
        rules = Rules(rules)
        request_data = {"body": {"username": "admin", "age": 30}}
        self.assertTrue(rules.evaluate(request_data))

    def test_some_rules_fail(self):
        rules = [
            {"target": "body", "prop": "username", "op": "EQUALS", "value": "admin"},
            {"target": "body", "prop": "age", "op": "EQUALS", "value": 30},
        ]
        rules = Rules(rules)
        request_data = {"body": {"username": "admin", "age": 25}}  # Age does not match
        self.assertFalse(rules.evaluate(request_data))

    def test_empty_rules_list(self):
        rules = Rules([])
        request_data = {"body": {"username": "admin"}}
        self.assertTrue(rules.evaluate(request_data))  # No rules means always True


if __name__ == "__main__":
    unittest.main()
