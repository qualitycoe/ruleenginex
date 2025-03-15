import re
from functools import reduce
from operator import getitem
from typing import Any

from jsonpath_ng import parse

from ruleenginex.constants import TARGET_OPERATOR_MAP, OperatorEnum
from ruleenginex.exceptions import InvalidTargetError, JsonPathParsingError, UnsupportedOperatorError
from ruleenginex.operatorx import OperatorEvaluator


class Rule:
    """Represents a rule that evaluates a request against a condition."""

    JSONPATH_PATTERN = re.compile(r"^\$")

    def __init__(
        self,
        target: str,
        prop: str,
        op: str,
        value: Any,
        invert: bool = False,  # noqa: FBT001, FBT002
    ):
        op = op.strip().upper()

        try:
            operator_enum = OperatorEnum[op]
        except KeyError:
            raise UnsupportedOperatorError(op)  # noqa: B904

        self.target = target
        self.prop = prop
        self.operator = OperatorEvaluator(operator_enum, value)
        self.invert = invert

        # Validate target and operator
        self._validate_target()
        self._validate_operator()

    def _validate_target(self):
        """Validates that the target is supported."""
        if self.target not in TARGET_OPERATOR_MAP:
            raise InvalidTargetError(self.target)

    def _validate_operator(self):
        """Validates that the operator is supported for the target."""
        supported_operators = TARGET_OPERATOR_MAP[self.target]
        if self.operator.operator not in supported_operators:
            raise UnsupportedOperatorError(str(self.operator))

    def _is_jsonpath(self) -> bool:
        """Detects whether the property string is a JSONPath."""
        return bool(self.JSONPATH_PATTERN.match(self.prop))

    def _get_object_path_value(self, data: dict, property_path: str) -> Any:
        """Retrieves a nested value from a dictionary using dot-separated keys."""
        if not property_path:
            return data
        try:
            return reduce(getitem, property_path.split("."), data)
        except (KeyError, TypeError):
            return None  # Return None if any key is missing

    def _get_jsonpath_value(self, data: dict, jsonpath: str) -> Any:
        """Evaluates JSONPath expression on the given data."""
        if not jsonpath:
            return data
        try:
            jsonpath_expr = parse(jsonpath)
            results = [match.value for match in jsonpath_expr.find(data)]
            return results[0] if len(results) == 1 else results
        except Exception as e:
            msg = f"Invalid JSONPath syntax: {jsonpath}"
            raise JsonPathParsingError(msg) from e

    def evaluate(self, request_data: dict[str, Any]) -> bool:
        """Evaluates the rule using the OperatorEvaluator class."""
        target_data = request_data.get(self.target, {})  # Get the top-level target data

        # If property is empty or None, use full target data
        if not self.prop:
            actual_value = target_data
        elif self._is_jsonpath():
            actual_value = self._get_jsonpath_value(target_data, self.prop)
        else:
            actual_value = self._get_object_path_value(target_data, self.prop)

        result = self.operator.apply(actual_value)
        return not result if self.invert else result
