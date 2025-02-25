from ruleenginex.constants import TARGET_OPERATOR_MAP


class UnsupportedOperatorError(Exception):
    """Exception raised when an unsupported operator is used."""

    def __init__(self, operator: str):
        super().__init__(f"Unsupported operator: {operator}")


class RuleValidationError(Exception):
    """Base exception for rule validation errors."""


class JsonPathParsingError(Exception):
    """Base exception for jsonpath validation errors."""


class InvalidTargetError(RuleValidationError):
    """Exception raised when an invalid target is provided."""

    def __init__(self, target: str):
        super().__init__(f"Invalid target '{target}'. Must be one of: {', '.join(TARGET_OPERATOR_MAP.keys())}")
