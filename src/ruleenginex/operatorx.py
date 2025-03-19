import logging
import re
from typing import Any

from jsonschema import ValidationError, validate

from ruleenginex.constants import OperatorEnum
from ruleenginex.exceptions import UnsupportedOperatorError

logger = logging.getLogger(__name__)


class OperatorEvaluator:
    """Handles evaluation logic for different operators."""

    def __init__(self, operator: OperatorEnum, expected_value: Any):
        self.operator = operator
        self.expected_value = expected_value

    def apply(self, actual_value: Any) -> bool:
        """Applies the operator logic to the actual value."""

        logger.debug(
            "Applying operator=%s on actual_value=%r with expected_value=%r",
            self.operator,
            actual_value,
            self.expected_value,
        )

        match self.operator:
            case OperatorEnum.EQUALS:
                return actual_value == self.expected_value
            case OperatorEnum.ARRAY_INCLUDES:
                return isinstance(actual_value, list) and self.expected_value in actual_value
            case OperatorEnum.EMPTY_ARRAY:
                return isinstance(actual_value, list) and len(actual_value) == 0
            case OperatorEnum.REGEX:
                return bool(re.match(self.expected_value, str(actual_value)))
            case OperatorEnum.REGEX_CASE_INSENSITIVE:
                return bool(re.match(self.expected_value, str(actual_value), re.IGNORECASE))
            case OperatorEnum.NULL:
                return actual_value is None
            case OperatorEnum.VALID_JSON_SCHEMA:
                return self._validate_json_schema(actual_value)
            case _:
                raise UnsupportedOperatorError(str(self.operator))

    def _validate_json_schema(self, actual_value: Any) -> bool:
        """Validates the actual value against the expected JSON schema."""
        try:
            validate(instance=actual_value, schema=self.expected_value)
            return True
        except ValidationError:
            return False
