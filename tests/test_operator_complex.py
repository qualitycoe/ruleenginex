import unittest
from ruleenginex.constants import OperatorEnum
from ruleenginex.operatorx import OperatorEvaluator


class TestOperatorEvaluatorComplex(unittest.TestCase):
    def test_operator_handles_numbers(self):
        evaluator = OperatorEvaluator(OperatorEnum.EQUALS, 100)
        self.assertTrue(evaluator.apply(100))
        self.assertFalse(evaluator.apply(99))

    def test_operator_handles_booleans(self):
        evaluator = OperatorEvaluator(OperatorEnum.EQUALS, True)
        self.assertTrue(evaluator.apply(True))
        self.assertFalse(evaluator.apply(False))

    def test_operator_handles_nested_dicts(self):
        evaluator = OperatorEvaluator(OperatorEnum.EQUALS, {"user": {"name": "Alice", "age": 30}})
        self.assertTrue(evaluator.apply({"user": {"name": "Alice", "age": 30}}))
        self.assertFalse(evaluator.apply({"user": {"name": "Bob", "age": 25}}))

    def test_operator_handles_lists_with_dicts(self):
        evaluator = OperatorEvaluator(OperatorEnum.ARRAY_INCLUDES, {"id": 1, "status": "active"})
        self.assertTrue(evaluator.apply([{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}]))
        self.assertFalse(evaluator.apply([{"id": 2, "status": "inactive"}]))

    def test_operator_handles_special_characters(self):
        evaluator = OperatorEvaluator(OperatorEnum.REGEX, r"^[a-zA-Z0-9_]+$")  # Alphanumeric with underscores
        self.assertTrue(evaluator.apply("valid_username"))
        self.assertFalse(evaluator.apply("invalid-username!"))


if __name__ == "__main__":
    unittest.main()
