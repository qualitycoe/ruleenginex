import unittest

from ruleenginex.constants import OperatorEnum
from ruleenginex.exceptions import InvalidTargetError, UnsupportedOperatorError
from ruleenginex.rule import Rule


class TestRule(unittest.TestCase):
    def test_rule_evaluation_true(self):
        rule = Rule(target="body", prop="username", operator=OperatorEnum.EQUALS, value="admin")
        request_data = {"body": {"username": "admin"}}
        self.assertTrue(rule.evaluate(request_data))

    def test_rule_evaluation_false(self):
        rule = Rule(target="body", prop="username", operator=OperatorEnum.EQUALS, value="admin")
        request_data = {"body": {"username": "user"}}
        self.assertFalse(rule.evaluate(request_data))

    def test_rule_inversion(self):
        rule = Rule(target="body", prop="username", operator=OperatorEnum.EQUALS, value="admin", invert=True)
        request_data = {"body": {"username": "admin"}}
        self.assertFalse(rule.evaluate(request_data))

    def test_rule_unsupported_operator(self):
        with self.assertRaises(UnsupportedOperatorError):
            Rule(target="body", prop="username", operator="UNSUPPORTED_OPERATOR", value="admin")

    def test_rule_missing_property(self):
        rule = Rule(target="body", prop="nonexistent", operator=OperatorEnum.EQUALS, value="value")
        request_data = {"body": {}}
        self.assertFalse(rule.evaluate(request_data))

    def test_rule_invalid_target(self):
        with self.assertRaises(InvalidTargetError):
            Rule(target="invalid_target", prop="username", operator=OperatorEnum.EQUALS, value="admin")


if __name__ == "__main__":
    unittest.main()
