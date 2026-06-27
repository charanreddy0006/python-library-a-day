# Day 63 - Python-Dotenv Library

# 📌 Overview

On Day 63, I explored Python's **python-dotenv** library, which is used to manage environment variables.

Instead of storing sensitive information directly inside Python code, developers can keep it in a separate `.env` file.

This improves:

* Security
* Code organization
* Project portability
* Team collaboration

It is widely used in:

* Flask Applications
* FastAPI Projects
* Django Applications
* AI Projects
* Backend Development

---

# 📦 Installation

Install python-dotenv using pip:

```bash
pip install python-dotenv
```

---

# 🧠 Importing the Library

```python
from dotenv import load_dotenv
import os
```

---

# 🌱 What is an Environment Variable?

An environment variable stores configuration values outside your program.

Examples:

* API Keys
* Database Passwords
* Secret Tokens
* Email Credentials

Instead of writing:

```python
API_KEY = "123456"
```

you store it in a `.env` file.

---

# 📄 Creating a .env File

Example:

```env
API_KEY=abcdef123456
USERNAME=Chakri
PASSWORD=my_password
```

The `.env` file should **not** be shared publicly.

---

# 📥 Loading Environment Variables

Example:

```python
load_dotenv()
```

This loads all variables from the `.env` file into your application.

---

# 📖 Reading Variables

Example:

```python
api_key = os.getenv("API_KEY")
```

Returns the value stored in the `.env` file.

---

# 🛡️ Why Use python-dotenv?

Benefits include:

* Keeps secrets out of source code
* Makes applications more secure
* Easy to change configuration
* Supports different environments (development, testing, production)

---

# 💻 Complete Example

```python
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("USERNAME"))
```

---

# 🚀 Real-World Uses

## API Integration

Store API keys securely.

---

## Database Connections

Store usernames and passwords.

---

## AI Projects

Protect OpenAI, Gemini, or Hugging Face API keys.

---

## Web Applications

Manage application settings.

---

## Cloud Deployment

Load environment-specific configurations.

---

# ⚡ Advantages of Python-Dotenv

* Easy to use
* Improves security
* Cleaner code
* Production-friendly
* Widely adopted

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* What environment variables are
* How to use a `.env` file
* How to load environment variables
* Why secrets should not be hardcoded
* Best practices for secure configuration management

---

# 🚀 Conclusion

The python-dotenv library is an essential tool for secure Python development.

It helps developers:

* Protect sensitive information
* Organize configuration
* Build production-ready applications
* Follow industry best practices

Learning python-dotenv is useful for:

* Backend Development
* Web Applications
* AI Projects
* API Integration
* Secure Software Development

It is one of the first libraries every Python backend developer should learn.
