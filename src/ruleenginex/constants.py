from enum import Enum, auto


class OperatorEnum(Enum):
    """Enum representing all supported operators."""

    ARRAY_INCLUDES = auto()
    EMPTY_ARRAY = auto()
    EQUALS = auto()
    NULL = auto()
    REGEX = auto()
    REGEX_CASE_INSENSITIVE = auto()
    VALID_JSON_SCHEMA = auto()

    def __str__(self):
        """Returns a user-friendly string representation of the OperatorEnum."""
        return self.name.lower().replace("_", " ")


TARGET_OPERATOR_MAP: dict[str, set[OperatorEnum]] = {
    "body": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.EMPTY_ARRAY,
        OperatorEnum.ARRAY_INCLUDES,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
    "params": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.EMPTY_ARRAY,
        OperatorEnum.ARRAY_INCLUDES,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
    "headers": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.EMPTY_ARRAY,
        OperatorEnum.ARRAY_INCLUDES,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
    "route_params": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
    "path": {OperatorEnum.EQUALS, OperatorEnum.REGEX, OperatorEnum.REGEX_CASE_INSENSITIVE},
    "method": {OperatorEnum.EQUALS, OperatorEnum.REGEX, OperatorEnum.REGEX_CASE_INSENSITIVE},
    "number": {OperatorEnum.EQUALS, OperatorEnum.REGEX, OperatorEnum.REGEX_CASE_INSENSITIVE},
    "global_variable": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.EMPTY_ARRAY,
        OperatorEnum.ARRAY_INCLUDES,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
    "data_bucket": {
        OperatorEnum.EQUALS,
        OperatorEnum.REGEX,
        OperatorEnum.REGEX_CASE_INSENSITIVE,
        OperatorEnum.NULL,
        OperatorEnum.EMPTY_ARRAY,
        OperatorEnum.ARRAY_INCLUDES,
        OperatorEnum.VALID_JSON_SCHEMA,
    },
}
