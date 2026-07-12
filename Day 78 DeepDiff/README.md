# Day 78 - DeepDiff Library

# 📌 Overview

On Day 78, I explored Python's **DeepDiff** library, a powerful tool used to compare complex Python objects and identify differences between them.

Unlike the standard equality operator (`==`), DeepDiff provides detailed information about what has changed, including added, removed, and modified values.

It is widely used in:

- API Testing
- Configuration Management
- Data Validation
- Unit Testing
- Data Migration
- Automation Scripts

---

# 📦 Installation

Install DeepDiff using pip:

```bash
pip install deepdiff
```

---

# 🧠 Importing the Library

```python
from deepdiff import DeepDiff
```

---

# 📖 What is DeepDiff?

DeepDiff is a library that performs deep comparisons between Python objects.

It can compare:

- Dictionaries
- Lists
- Tuples
- Sets
- JSON Data
- Nested Objects

It reports exactly what has changed.

---

# 🚀 Comparing Dictionaries

Example:

```python
from deepdiff import DeepDiff

dict1 = {
    "name": "Alice",
    "age": 20
}

dict2 = {
    "name": "Alice",
    "age": 21
}

diff = DeepDiff(dict1, dict2)

print(diff)
```

Output:

```text
{
    'values_changed': {
        "root['age']": {
            'old_value': 20,
            'new_value': 21
        }
    }
}
```

---

# 📋 Comparing Lists

Example:

```python
list1 = [1, 2, 3]

list2 = [1, 2, 4]

DeepDiff(list1, list2)
```

Shows the changed list elements.

---

# 🏗️ Comparing Nested Objects

Example:

```python
person1 = {
    "address": {
        "city": "Delhi"
    }
}

person2 = {
    "address": {
        "city": "Mumbai"
    }
}
```

DeepDiff detects nested changes automatically.

---

# ⚙️ Ignoring Order

Example:

```python
DeepDiff(
    [1, 2, 3],
    [3, 2, 1],
    ignore_order=True
)
```

Useful when element order does not matter.

---

# 💻 Complete Example

```python
from deepdiff import DeepDiff

a = {"x": 10}
b = {"x": 20}

print(DeepDiff(a, b))
```

---

# 🚀 Real-World Uses

## API Testing

Compare expected and actual API responses.

---

## Configuration Management

Detect changes in configuration files.

---

## Data Migration

Verify migrated records.

---

## Unit Testing

Compare complex objects in automated tests.

---

## Automation Scripts

Track changes in JSON or dictionary data.

---

# ⚡ Advantages of DeepDiff

- Easy to use
- Detailed comparison results
- Supports nested objects
- Works with many Python data types
- Excellent for testing and debugging

---

# 🆚 DeepDiff vs == Operator

| Feature | DeepDiff | == |
|---------|----------|----|
| Equality Check | ✅ | ✅ |
| Detailed Differences | ✅ | ❌ |
| Nested Comparison | ✅ | Limited |
| Reports Changes | ✅ | ❌ |
| Beginner Friendly | ✅ | ✅ |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How to compare Python objects
- How to detect changes in dictionaries
- How nested comparisons work
- How to compare lists and JSON data
- Why DeepDiff is useful for testing and debugging

---

# 🚀 Conclusion

DeepDiff is a powerful comparison library for Python that simplifies finding differences between complex objects.

It helps developers:

- Compare structured data
- Validate API responses
- Debug applications
- Verify data consistency
- Improve automated testing

Learning DeepDiff is useful for:

- Software Testing
- Backend Development
- Automation
- Data Validation
- Python Development

DeepDiff is an excellent library for any project that involves comparing structured or nested data.