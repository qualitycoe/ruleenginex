import unittest
from ruleenginex.constants import OperatorEnum
from ruleenginex.rule import Rule


class TestRuleComplex(unittest.TestCase):
    def test_rule_evaluates_nested_dicts(self):
        rule = Rule(target="body", prop="user.details.age", operator=OperatorEnum.EQUALS, value=30)
        request_data = {"body": {"user": {"details": {"age": 30}}}}
        self.assertTrue(rule.evaluate(request_data))
        self.assertFalse(rule.evaluate({"body": {"user": {"details": {"age": 25}}}}))

    def test_rule_handles_empty_values(self):
        rule = Rule(target="body", prop="username", operator=OperatorEnum.NULL, value=None)
        self.assertTrue(rule.evaluate({"body": {"username": None}}))
        self.assertFalse(rule.evaluate({"body": {"username": "admin"}}))

    def test_rule_handles_varied_data_types(self):
        rule1 = Rule(target="body", prop="count", operator=OperatorEnum.EQUALS, value=5)
        rule2 = Rule(target="body", prop="is_active", operator=OperatorEnum.EQUALS, value=True)
        rule3 = Rule(target="body", prop="roles", operator=OperatorEnum.ARRAY_INCLUDES, value="admin")

        request_data = {"body": {"count": 5, "is_active": True, "roles": ["admin", "user"]}}
        self.assertTrue(rule1.evaluate(request_data))
        self.assertTrue(rule2.evaluate(request_data))
        self.assertTrue(rule3.evaluate(request_data))

    def test_rule_handles_partial_data(self):
        rule = Rule(target="body", prop="settings.theme", operator=OperatorEnum.EQUALS, value="dark")
        request_data = {"body": {"settings": {}}}  # Missing theme
        self.assertFalse(rule.evaluate(request_data))

    def test_rule_jsonpath_array_evaluation(self):
        rule = Rule(target="body", prop="$.users[*].name", operator=OperatorEnum.ARRAY_INCLUDES, value="Alice")
        request_data = {"body": {"users": [{"name": "Alice"}, {"name": "Bob"}]}}
        assert rule.evaluate(request_data) is True
        assert rule.evaluate({"body": {"users": [{"name": "Charlie"}]}}) is False

    def test_rule_object_path_evaluation(self):
        rule = Rule(target="body", prop="user.details.age", operator=OperatorEnum.EQUALS, value=30)
        request_data = {"body": {"user": {"details": {"age": 30}}}}
        assert rule.evaluate(request_data) is True
        assert rule.evaluate({"body": {"user": {"details": {"age": 25}}}}) is False

    def test_rule_jsonpath_evaluation(self):
        rule = Rule(target="body", prop="$.user.details.age", operator=OperatorEnum.EQUALS, value=30)
        request_data = {"body": {"user": {"details": {"age": 30}}}}
        assert rule.evaluate(request_data) is True
        assert rule.evaluate({"body": {"user": {"details": {"age": 25}}}}) is False

    def test_rule_empty_property_uses_entire_target(self):
        rule = Rule(target="body", prop=None, operator=OperatorEnum.VALID_JSON_SCHEMA, value={"type": "object"})
        request_data = {"body": {"user": "Alice", "age": 30}}
        assert rule.evaluate(request_data) is True  # The entire body should match schema

    def test_rule_empty_string_property(self):
        rule = Rule(target="body", prop="", operator=OperatorEnum.VALID_JSON_SCHEMA, value={"type": "object"})
        request_data = {"body": {"user": "Alice", "age": 30}}
        assert rule.evaluate(request_data) is True  # The entire body should match schema


if __name__ == "__main__":
    unittest.main()
