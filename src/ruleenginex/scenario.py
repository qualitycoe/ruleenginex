from ruleenginex.rules import Rules


class Scenario:
    """Represents a scenario containing rules and a response."""

    def __init__(self, scenario_name: str, rules: list[dict], response: dict):
        self.scenario_name = scenario_name
        self.rules = Rules(rules)
        self.response = response

    def evaluate(self, request_data: dict) -> bool:
        """Evaluates whether this scenario should be used based on request data."""
        return self.rules.evaluate(request_data)

    def get_response(self) -> dict:
        """Returns the response associated with this scenario."""
        return self.response
