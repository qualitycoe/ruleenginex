from ruleenginex.rule import Rule


class Rules:
    """Represents a collection of rules that must all match for a scenario to activate."""

    def __init__(self, rules: list[dict]):
        self.rules = [Rule(**rule) for rule in rules]

    def evaluate(self, request_data: dict) -> bool:
        """Evaluates all rules in this collection."""
        return all(rule.evaluate(request_data) for rule in self.rules)
