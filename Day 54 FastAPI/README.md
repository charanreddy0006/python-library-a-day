# Day 54 - FastAPI Library

# 📌 Overview

On Day 54, I explored Python's modern **FastAPI framework**, which is used for building APIs and backend applications.

FastAPI is one of the fastest-growing Python frameworks because it provides:

- High Performance
- Automatic Documentation
- Data Validation
- Easy Development
- Modern Python Features

It is widely used in:

- AI Applications
- Backend Development
- Web Services
- Cloud Systems
- Microservices

---

# 🌐 What is an API?

API stands for:

Application Programming Interface

An API allows different applications to communicate with each other.

Example:

```text
Mobile App
      ↓
    API
      ↓
 Database
```

---

# 📦 Installation

Install FastAPI:

```bash
pip install fastapi
```

Install server:

```bash
pip install uvicorn
```

---

# 🧠 Importing FastAPI

```python
from fastapi import FastAPI
```

---

# 🚀 Creating an Application

Example:

```python
app = FastAPI()
```

This creates a FastAPI application.

---

# 🏠 Creating Routes

Example:

```python
@app.get("/")
```

This creates a route.

When users visit:

```text
/
```

they receive a response.

---

# 📤 Returning Data

Example:

```python
return {
    "message": "Hello"
}
```

FastAPI automatically converts Python dictionaries into JSON.

---

# 📥 Path Parameters

Example:

```python
@app.get("/user/{name}")
```

Users can provide values dynamically.

Example:

```text
/user/Chakri
```

Output:

```json
{
  "username": "Chakri"
}
```

---

# 📄 Automatic Documentation

One of FastAPI's most powerful features:

```text
/docs
```

Automatically generates interactive API documentation.

---

# 💻 Complete Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }
```

---

# 🚀 Real-World Uses

## AI Applications

Serve machine learning models.

---

## Backend Systems

Build REST APIs.

---

## Cloud Applications

Create scalable services.

---

## Mobile Applications

Provide backend support.

---

## Microservices

Build independent services.

---

# ⚡ Advantages of FastAPI

- Extremely Fast
- Easy to Learn
- Automatic Docs
- Type Validation
- Modern Design

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What APIs are
- How FastAPI works
- How routes are created
- How JSON responses work
- How backend services are developed

---

# 🚀 Conclusion

FastAPI is one of the most powerful modern Python frameworks.

It helps developers:

- Build APIs quickly
- Create backend applications
- Serve AI models
- Develop scalable services

Learning FastAPI is useful for:

- Backend Development
- AI Engineering
- Cloud Computing
- Web Services
- Software Development

It is one of the most valuable Python technologies to learn today.