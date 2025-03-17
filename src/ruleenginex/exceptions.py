from ruleenginex.constants import TARGET_OPERATOR_MAP


class UnsupportedOperatorError(Exception):
    """Exception raised when an unsupported operator is used."""

    def __init__(self, op: str):
        super().__init__(f"Unsupported operator: {op}")


class RuleValidationError(Exception):
    """Base exception for rule validation errors."""


class JsonPathParsingError(Exception):
    """Base exception for jsonpath validation errors."""


class InvalidTargetError(RuleValidationError):
    """Exception raised when an invalid target is provided."""

    def __init__(self, target: str):
        super().__init__(f"Invalid target '{target}'. Must be one of: {', '.join(TARGET_OPERATOR_MAP.keys())}")
