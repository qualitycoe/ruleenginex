# RuleEngineX

[![PyPI - Version](https://img.shields.io/pypi/v/ruleenginex.svg)](https://pypi.org/project/ruleenginex)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ruleenginex.svg)](https://pypi.org/project/ruleenginex)

![RuleEngineX](https://img.shields.io/badge/version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Build](https://img.shields.io/github/actions/workflow/status/qualitycoe/ruleenginex/ci.yml)

-----

## 📖 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Supported Operators](#supported-operators)
- [Use Cases](#use-cases)
- [Performance Benchmarking](#performance-benchmarking)
- [License](#license)
- [Contact](#contact)

---

## 🚀 Introduction
**RuleEngineX** is an advanced, flexible, and lightweight rule evaluation engine for **validating JSON data**. It allows users to define and evaluate **rules and scenarios** with support for:

- **Nested JSON Path Extraction**
- **JSONPath Query Evaluations**
- **Customizable Rule Sets**
- **Multiple Data Targets (Body, Headers, Params, etc.)**
- **Complex Scenarios with Multiple Rules**
- **Performance-Optimized Execution**

---

## 🔥 Features
✔ **Supports JSONPath and Object Paths** for flexible data extraction.
✔ **Multiple operators** including `EQUALS`, `REGEX`, `ARRAY_INCLUDES`, and `VALID_JSON_SCHEMA`.
✔ **Scenarios with multiple rules** for complex decision making.
✔ **Lightweight and Fast** — optimized for performance.
✔ **Use in API Testing, Webhooks, and Event Processing.**
✔ **Benchmarking support** for large JSON datasets.
✔ **Easy-to-use Python API** with intuitive rule definitions.

---

## 📦 Installation

You can install RuleEngineX via `pip`:
```sh
pip install ruleenginex
```
Or install using **Hatch**:
```sh
hatch env create
hatch run dev:test
```

---

## 🚀 Quick Start

### 1️⃣ **Basic Rule Evaluation**
```python
from ruleenginex.rule import Rule
from ruleenginex.constants import OperatorEnum

rule = Rule(target="body", prop="user.name", op="equals", value="Alice")

request_data = {"body": {"user": {"name": "Alice"}}}
print(rule.evaluate(request_data))  # Output: True
```

### 2️⃣ **Using JSONPath Queries**
```python
rule = Rule(target="body", prop="$.users[*].id", operator=OperatorEnum.ARRAY_INCLUDES, value=42)

request_data = {"body": {"users": [{"id": 1}, {"id": 42}, {"id": 100}]}}
print(rule.evaluate(request_data))  # Output: True
```

---

## ✅ Supported Operators
| Operator | Description |
|----------|------------|
| `EQUALS` | Checks if two values are the same |
| `REGEX` | Matches a string using a regular expression |
| `REGEX_CASE_INSENSITIVE` | Case-insensitive regex matching |
| `NULL` | Checks if a field is null |
| `EMPTY_ARRAY` | Checks if a field is an empty list |
| `ARRAY_INCLUDES` | Checks if a list contains a specific value |
| `VALID_JSON_SCHEMA` | Validates data against a JSON Schema |

---

## ⚡ Use Cases
### 🔹 **Mock API Request Validation**
Ensure **all orders** have a valid `order_id`:
```python
rule = Rule(target="body", prop="order_id", operator=OperatorEnum.REGEX, value=r"^ORD-[0-9]+$")
```

### 🔹 **Webhook & Event Processing**
Check if an event payload has `status = "approved"`:
```python
rule = Rule(target="body", prop="event.status", op="equals", value="approved")
```

### 🔹 **Automated Workflow Triggers**
Trigger workflows based on `priority = high`:
```python
rule = Rule(target="body", prop="ticket.priority", op="equals", value="high")
```

---

## 🚀 Performance Benchmarking
Run benchmarks on **large datasets**:
```sh
hatch run benchmark:run
```
Example benchmark script:
```python
import time
from ruleenginex.rule import Rule
from ruleenginex.constants import OperatorEnum

rule = Rule(target="body", prop="$.users[*].id", operator=OperatorEnum.ARRAY_INCLUDES, value=50000)

large_data = {"body": {"users": [{"id": i} for i in range(100000)]}}
start = time.time()
print(rule.evaluate(large_data))
print(f"Execution Time: {time.time() - start:.5f} seconds")
```

---

## 📖 License
RuleEngineX is licensed under the **MIT License**.

---

## 📬 Contact
For any issues, submit an issue on GitHub: [GitHub Issues](https://github.com/qualitycoe/ruleenginex/issues).
