# Day 73 - Cerberus Library

# 📌 Overview

On Day 73, I explored Python's **Cerberus** library, a lightweight and flexible data validation library.

Cerberus validates dictionaries against predefined schemas, ensuring that data follows the expected structure before it is processed.

Instead of manually checking every field, Cerberus automatically validates data and reports errors.

It is widely used in:

- REST APIs
- Backend Development
- Data Validation
- Configuration Management
- Automation Scripts

---

# 📦 Installation

Install Cerberus using pip:

```bash
pip install cerberus
```

---

# 🧠 Importing the Library

```python
from cerberus import Validator
```

---

# 📖 What is Data Validation?

Data validation is the process of checking whether input data is correct before using it.

Validation helps prevent:

- Missing values
- Incorrect data types
- Invalid email addresses
- Invalid numbers
- Unexpected input

Example:

```python
{
    "name": "Alice",
    "age": 25
}
```

A validation library ensures the data follows the expected rules.

---

# 🏗️ Creating a Schema

A schema defines the structure and rules for the data.

Example:

```python
schema = {
    "name": {
        "type": "string"
    },
    "age": {
        "type": "integer"
    }
}
```

---

# 🚀 Creating a Validator

Example:

```python
validator = Validator(schema)
```

The Validator object checks whether the data follows the schema.

---

# ✅ Validating Data

Example:

```python
validator.validate(student)
```

Returns:

- `True` if the data is valid
- `False` if validation fails

---

# ⚠️ Viewing Validation Errors

Example:

```python
print(validator.errors)
```

Displays detailed information about validation failures.

Example Output:

```text
{
    'age': ['min value is 18']
}
```

---

# 📋 Common Validation Rules

Cerberus supports many rules.

### Required Field

```python
"required": True
```

Makes the field mandatory.

---

### Data Type

```python
"type": "string"
```

Checks the value's type.

---

### Minimum Value

```python
"min": 18
```

Ensures numeric values meet the minimum requirement.

---

### Maximum Value

```python
"max": 100
```

Limits numeric values.

---

### Regular Expression

```python
"regex": r".+@.+\..+"
```

Validates text patterns such as email addresses.

---

# 💻 Complete Example

```python
from cerberus import Validator

schema = {
    "name": {"type": "string"}
}

data = {
    "name": "Python"
}

validator = Validator(schema)

print(validator.validate(data))
```

---

# 🚀 Real-World Uses

## REST APIs

Validate incoming request data.

---

## Configuration Files

Ensure application settings are correct.

---

## Form Validation

Verify user input before saving.

---

## Data Pipelines

Validate records before processing.

---

## Automation Scripts

Prevent invalid data from entering workflows.

---

# ⚡ Advantages of Cerberus

- Lightweight
- Easy to learn
- Flexible schema definitions
- Detailed error messages
- Pure Python
- Beginner-friendly

---

# 🆚 Cerberus vs Marshmallow

| Feature | Cerberus | Marshmallow |
|----------|----------|-------------|
| Validation | ✅ | ✅ |
| Serialization | ❌ | ✅ |
| Lightweight | ✅ | ✅ |
| Easy Schema Definition | ✅ | ✅ |
| Best For | Validation | Validation + Serialization |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What data validation is
- How schemas define data rules
- How to validate dictionaries
- How to detect invalid input
- How Cerberus simplifies validation

---

# 🚀 Conclusion

Cerberus is a lightweight yet powerful library for validating structured data.

It helps developers:

- Validate input
- Improve data quality
- Prevent invalid information
- Build reliable applications

Learning Cerberus is useful for:

- Backend Development
- REST APIs
- Automation
- Configuration Management
- Python Development

Cerberus is an excellent choice for projects that require fast and reliable data validation.