import unittest

from ruleenginex.exceptions import InvalidTargetError, UnsupportedOperatorError


class TestExceptions(unittest.TestCase):
    def test_invalid_target_error(self):
        with self.assertRaises(InvalidTargetError) as context:
            error_msg = "invalid_target"
            raise InvalidTargetError(error_msg)
        self.assertEqual(
            str(context.exception),
            "Invalid target 'invalid_target'. Must be one of: body, params, headers, route_params, path, method, number, global_variable, data_bucket",  # noqa: E501
        )

    def test_unsupported_operator_error(self):
        with self.assertRaises(UnsupportedOperatorError) as context:
            msg = "UNSUPPORTED_OPERATOR"
            raise UnsupportedOperatorError(msg)
        self.assertEqual(
            str(context.exception),
            "Unsupported operator: UNSUPPORTED_OPERATOR",
        )


if __name__ == "__main__":
    unittest.main()
