# RuleEngineX

[![PyPI - Version](https://img.shields.io/pypi/v/ruleenginex.svg)](https://pypi.org/project/ruleenginex)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ruleenginex.svg)](https://pypi.org/project/ruleenginex)
![RuleEngineX](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/github/actions/workflow/status/qualitycoe/ruleenginex/ci.yml)

-----

## 📖 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Basic Rule Evaluation](#basic-rule-evaluation)
  - [Using JSONPath Queries](#using-jsonpath-queries)
  - [Chaining Multiple Rules](#chaining-multiple-rules)
  - [Scenarios](#scenarios)
- [Supported Operators](#supported-operators)
- [Use Cases](#use-cases)
- [Performance Benchmarking](#performance-benchmarking)
- [License](#license)
- [Contact](#contact)

---

## 🚀 Introduction

**RuleEngineX** is an advanced, flexible, and lightweight rule evaluation engine for **validating JSON data** (or Python dictionaries). It leverages **JSONPath** and **object-path** lookups to extract specific fields for evaluation, and supports a range of powerful operators. RuleEngineX is designed for scenarios like:

- Validating incoming payloads in API gateways
- Filtering JSON events (e.g., in data pipelines)
- Dynamically matching request parameters for mock servers
- Building conditional logic for workflow automation

---

## 🔥 Features

✔ **Supports JSONPath and Dot-Notation Paths** for flexible data extraction
✔ **Multiple Operators** including `EQUALS`, `REGEX_CASE_INSENSITIVE`, `ARRAY_INCLUDES`, `VALID_JSON_SCHEMA`
✔ **Scenario-Based** approach for grouping multiple rules under one logical outcome
✔ **Extensible**: Easy to customize or add new operators
✔ **Lightweight and Fast** — optimized for quick evaluations
✔ **Benchmark Scripts** for testing performance at scale
✔ **Easy Integration** with other Python projects (e.g., mocking tools, test frameworks)

---

## 📦 Installation

### From PyPI

```sh
pip install ruleenginex
```

> *Note: If not yet published to PyPI, you can install directly from GitHub:*
> ```sh
> pip install "ruleenginex @ git+https://github.com/qualitycoe/ruleenginex.git@main#egg=ruleenginex"
> ```

### Via Hatch (Recommended for contributors)

```sh
# 1) Ensure Hatch is installed: pip install hatch
# 2) Create a local environment and install dev dependencies
hatch env create
# 3) (Optional) Run tests
hatch run test
```

---

## 🚀 Quick Start

### 1️⃣ Basic Rule Evaluation

```python
from ruleenginex.rule import Rule

# Sample request data
request_data = {
    "body": {
        "user": {
            "name": "Alice",
            "age": 25
        }
    }
}

# Create a rule to check if 'body.user.name' == 'Alice'
rule = Rule(target="body", prop="user.name", op="EQUALS", value="Alice")
print(rule.evaluate(request_data))  # Output: True
```

### 2️⃣ Using JSONPath Queries

```python
from ruleenginex.rule import Rule
from ruleenginex.constants import OperatorEnum

# Using JSONPath to find 'id' in an array
rule = Rule(
    target="body",
    prop="$.users[*].id",
    op="ARRAY_INCLUDES",  # or OperatorEnum.ARRAY_INCLUDES
    value=42
)

request_data = {
    "body": {
        "users": [
            {"id": 1},
            {"id": 42},
            {"id": 100}
        ]
    }
}

print(rule.evaluate(request_data))  # Output: True
```

### 3️⃣ Chaining Multiple Rules

```python
from ruleenginex.rules import Rules

rules = [
    {"target": "method", "prop": "", "op": "EQUALS", "value": "POST"},
    {"target": "body",   "prop": "$.items[*].sku", "op": "ARRAY_INCLUDES", "value": "ABC-123"}
]

combined_rules = Rules(rules)
request_data = {
    "method": "POST",
    "body": {
        "items": [{"sku": "ABC-123"}, {"sku": "XYZ-999"}]
    }
}
print(combined_rules.evaluate(request_data))  # True if both rules match
```

### 4️⃣ Scenarios

```python
from ruleenginex.scenario import Scenario

scenario = Scenario(
    scenario_name="Discount Scenario",
    rules=[
        {
            "target": "body",
            "prop": "user.membership",
            "op": "EQUALS",
            "value": "premium"
        },
        {
            "target": "body",
            "prop": "user.coupon",
            "op": "REGEX_CASE_INSENSITIVE",
            "value": "^DISCOUNT-\\d+$"
        }
    ],
    response={
        "status": 200,
        "data": {"msg": "Eligible for discount!"}
    }
)

request_data = {
    "body": {
        "user": {
            "membership": "premium",
            "coupon": "DISCOUNT-1234"
        }
    }
}

if scenario.evaluate(request_data):
    print("Response =>", scenario.get_response())
```

---

## ✅ Supported Operators

| Operator                   | Description                                                                |
|----------------------------|----------------------------------------------------------------------------|
| `EQUALS`                   | Checks if two values are strictly the same                                 |
| `REGEX`                    | Case-sensitive regex match                                                 |
| `REGEX_CASE_INSENSITIVE`   | Case-insensitive regex match                                               |
| `NULL`                     | Checks if the value is `None`                                              |
| `EMPTY_ARRAY`              | Checks if the value is an empty list                                       |
| `ARRAY_INCLUDES`           | Checks if a list contains a specific element                               |
| `VALID_JSON_SCHEMA`        | Validates the value against a [JSON Schema](https://json-schema.org/)      |

---

## ⚡ Use Cases

### 🔹 API Request Validation
```python
rule = Rule(target="body", prop="order_id", op="REGEX", value=r"^ORD-[0-9]+$")
```

### 🔹 Event Processing
```python
rule = Rule(target="body", prop="event.type", op="EQUALS", value="purchase")
```

### 🔹 Testing & Mocking
```python
# Combine rules to match certain request data in test frameworks or mock servers
rules = [
    {"target": "headers", "prop": "X-Custom-Header", "op": "EQUALS", "value": "Test123"},
    {"target": "body", "prop": "items", "op": "EMPTY_ARRAY", "value": None}
]
```

---

## 🚀 Performance Benchmarking

RuleEngineX ships with example **benchmark scripts** in the `benchmarks/` folder:

```bash
python benchmarks/benchmark_jsonpath.py
python benchmarks/benchmark_rules.py
```

**Example**: `benchmark_rules.py` tests large data sets of 100,000+ items to measure how quickly a rule like `ARRAY_INCLUDES` can evaluate.

```python
import time
from ruleenginex.rule import Rule
from ruleenginex.constants import OperatorEnum

def benchmark_large_json():
    large_data = {"body": {"users": [{"id": i} for i in range(100000)]}}
    rule = Rule(target="body", prop="$.users[*].id", op="ARRAY_INCLUDES", value=50000)

    start_time = time.time()
    result = rule.evaluate(large_data)
    end_time = time.time()

    print(f"Evaluation took {end_time - start_time:.5f} seconds. Result: {result}")

if __name__ == "__main__":
    benchmark_large_json()
```

---

## 📖 License

RuleEngineX is distributed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

- **Issues & Questions**: Please open a GitHub issue at [RuleEngineX Issues](https://github.com/qualitycoe/ruleenginex/issues).
- **Email**: For direct inquiries, contact `qualitycoe@outlook.com`.
