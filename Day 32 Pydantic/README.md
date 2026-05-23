# Day 32 - Pydantic Library

# 📌 Overview

On Day 32, I explored Python’s powerful **pydantic library**, which is used for data validation and structured data handling.

Pydantic allows developers to define data models with type annotations and automatically validates incoming data.

It helps Python programs:

* validate user input
* enforce data types
* parse JSON data
* manage structured information
* build reliable APIs

It is widely used in:

* FastAPI applications
* backend systems
* AI applications
* API development
* data processing systems

---

# 📦 Installing Pydantic

Install using pip:

```bash id="pyd321d"
pip install pydantic
```

---

# 🧠 Importing the Library

```python id="pyd321e"
from pydantic import BaseModel
```

---

# 📄 What is a Data Model?

A data model defines the structure of data.

Example:

* name should be string
* age should be integer
* marks should be float

Pydantic automatically checks whether the data follows the correct structure.

---

# 🏗️ Creating a Model

Example:

```python id="pyd321f"
class Student(BaseModel):
```

This creates a structured data model.

---

# 🔤 Type Validation

Example:

```python id="pyd321g"
name: str
age: int
```

Pydantic validates:

* strings
* integers
* floats
* booleans
* lists
* nested objects

---

# ⚡ Creating an Object

Example:

```python id="pyd321h"
student = Student(name="Chakri", age=20)
```

Pydantic validates the provided data automatically.

---

# 📖 Dictionary Conversion

Example:

```python id="pyd321i"
student.model_dump()
```

This converts the model into dictionary format.

---

# 📦 JSON Conversion

Example:

```python id="pyd321j"
student.model_dump_json()
```

Used for:

* APIs
* web applications
* data exchange

---

# 💻 Complete Example

```python id="pyd321k"
from pydantic import BaseModel

class User(BaseModel):
    name: str

user = User(name="Python")
```

---

# 🚀 Real-World Uses

Pydantic is widely used in:

* FastAPI projects
* AI systems
* backend APIs
* data validation pipelines
* configuration management

---

# ⚡ Why Pydantic is Important

Pydantic helps:

* reduce bugs
* validate data automatically
* improve code reliability
* simplify JSON handling

---

# ⚠️ Important Note

If invalid data is provided:

* Pydantic raises validation errors automatically

Example:

```python id="pyd321l"
age="hello"
```

This prevents incorrect data from entering the system.

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how data validation works
* how structured models are created
* basics of type enforcement
* JSON serialization techniques

---

# 🚀 Conclusion

The pydantic library is one of the most important modern Python libraries for structured data validation.

It helps developers:

* build reliable systems
* validate input automatically
* manage APIs efficiently

Learning pydantic is useful for:

* backend development
* FastAPI
* AI applications
* data processing systems
