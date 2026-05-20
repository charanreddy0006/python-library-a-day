# Day 29 - Python Dotenv Library

# 📌 Overview

On Day 29, I explored Python’s powerful **python-dotenv library**, which is used for managing environment variables securely.

Environment variables help developers store:

* API keys
* passwords
* database URLs
* secret tokens
* configuration settings

without directly writing sensitive information inside Python code.

The python-dotenv library allows Python programs to:

* load environment variables
* access secret configurations
* separate settings from code
* improve security

It is widely used in:

* backend applications
* AI projects
* API integrations
* web development
* production systems

---

# 📦 Installing Python-Dotenv

Install using pip:

```bash id="env291e"
pip install python-dotenv
```

---

# 🧠 Importing Libraries

```python id="env291f"
from dotenv import load_dotenv
import os
```

---

# 🔐 What is an Environment Variable?

Environment variables are external values stored outside the source code.

Examples:

* API keys
* passwords
* secret tokens
* database configurations

This improves:

* security
* code organization
* project management

---

# 📄 What is a .env File?

A `.env` file stores environment variables.

Example:

```env id="env291g"
API_KEY=abcdef12345
SECRET_KEY=mysecret
```

---

# ⚡ Loading Environment Variables

Example:

```python id="env291h"
load_dotenv()
```

This loads variables from the `.env` file.

---

# 🔍 Accessing Variables

Example:

```python id="env291i"
os.getenv("API_KEY")
```

This retrieves the stored value.

---

# 💻 Complete Example

```python id="env291j"
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("SECRET_KEY"))
```

---

# 🚀 Real-World Uses

Python-dotenv is used in:

* Flask applications
* Django projects
* AI applications
* API integrations
* cloud systems

---

# ⚡ Why Environment Variables are Important

Environment variables help:

* secure sensitive data
* separate configuration from code
* improve project safety
* manage production settings

---

# ⚠️ Important Security Note

Never upload `.env` files to GitHub.

Add `.env` inside:

```text id="env291k"
.gitignore
```

This prevents secret keys from being exposed publicly.

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how environment variables work
* how Python loads configuration values
* basics of secret management
* secure coding practices

---

# 🚀 Conclusion

The python-dotenv library is essential for secure Python development.

It helps developers:

* protect sensitive information
* manage project configurations
* build secure applications

Learning python-dotenv is useful for:

* backend development
* AI projects
* web applications
* production systems
