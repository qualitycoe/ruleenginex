import unittest

from ruleenginex.constants import OperatorEnum
from ruleenginex.exceptions import UnsupportedOperatorError
from ruleenginex.operatorx import OperatorEvaluator


class TestOperatorEvaluator(unittest.TestCase):
    def test_equals_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.EQUALS, 5)
        self.assertTrue(evaluator.apply(5))
        self.assertFalse(evaluator.apply(3))

    def test_array_includes_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.ARRAY_INCLUDES, "apple")
        self.assertTrue(evaluator.apply(["apple", "banana"]))
        self.assertFalse(evaluator.apply(["banana", "cherry"]))

    def test_empty_array_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.EMPTY_ARRAY, None)
        self.assertTrue(evaluator.apply([]))
        self.assertFalse(evaluator.apply(["item"]))

    def test_regex_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.REGEX, r"\d{3}-\d{2}-\d{4}")
        self.assertTrue(evaluator.apply("123-45-6789"))
        self.assertFalse(evaluator.apply("123-456-789"))

    def test_regex_case_insensitive_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.REGEX_CASE_INSENSITIVE, r"hello")
        self.assertTrue(evaluator.apply("Hello World"))
        self.assertFalse(evaluator.apply("Hi World"))

    def test_null_operator(self):
        evaluator = OperatorEvaluator(OperatorEnum.NULL, None)
        self.assertTrue(evaluator.apply(None))
        self.assertFalse(evaluator.apply("Not None"))

    def test_valid_json_schema_operator(self):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
            },
            "required": ["name", "age"],
        }
        evaluator = OperatorEvaluator(OperatorEnum.VALID_JSON_SCHEMA, schema)
        valid_data = {"name": "John", "age": 30}
        invalid_data = {"name": "John", "age": "thirty"}
        self.assertTrue(evaluator.apply(valid_data))
        self.assertFalse(evaluator.apply(invalid_data))

    def test_unsupported_operator(self):
        with self.assertRaises(UnsupportedOperatorError):
            evaluator = OperatorEvaluator("UNSUPPORTED_OPERATOR", None)
            evaluator.apply("test")


if __name__ == "__main__":
    unittest.main()
