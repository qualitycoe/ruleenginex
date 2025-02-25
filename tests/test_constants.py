import unittest

from ruleenginex.constants import TARGET_OPERATOR_MAP, OperatorEnum


class TestConstants(unittest.TestCase):
    def test_operator_enum_members(self):
        expected_members = {
            "ARRAY_INCLUDES",
            "EMPTY_ARRAY",
            "EQUALS",
            "NULL",
            "REGEX",
            "REGEX_CASE_INSENSITIVE",
            "VALID_JSON_SCHEMA",
        }
        actual_members = set(OperatorEnum.__members__.keys())
        self.assertEqual(expected_members, actual_members)

    def test_operator_enum_values(self):
        self.assertEqual(str(OperatorEnum.ARRAY_INCLUDES), "array includes")
        self.assertEqual(str(OperatorEnum.EMPTY_ARRAY), "empty array")
        self.assertEqual(str(OperatorEnum.EQUALS), "equals")
        self.assertEqual(str(OperatorEnum.NULL), "null")
        self.assertEqual(str(OperatorEnum.REGEX), "regex")
        self.assertEqual(str(OperatorEnum.REGEX_CASE_INSENSITIVE), "regex case insensitive")
        self.assertEqual(str(OperatorEnum.VALID_JSON_SCHEMA), "valid json schema")

    def test_target_operator_map_keys(self):
        expected_keys = {
            "body",
            "params",
            "headers",
            "route_params",
            "path",
            "method",
            "number",
            "global_variable",
            "data_bucket",
        }
        actual_keys = set(TARGET_OPERATOR_MAP.keys())
        self.assertEqual(expected_keys, actual_keys)

    def test_target_operator_map_values(self):
        self.assertIn(OperatorEnum.EQUALS, TARGET_OPERATOR_MAP["body"])
        self.assertIn(OperatorEnum.REGEX, TARGET_OPERATOR_MAP["params"])
        self.assertNotIn(OperatorEnum.EMPTY_ARRAY, TARGET_OPERATOR_MAP["path"])
        # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
