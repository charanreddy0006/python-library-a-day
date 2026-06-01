# Day 41 - HTTPX Library

# 📌 Overview

On Day 41, I explored Python's modern **HTTPX library**, which is used for sending HTTP requests and interacting with web APIs.

HTTPX is often considered the next-generation alternative to the requests library because it provides:

- Simple syntax
- Better performance
- Async support
- Modern API design

It is widely used in:

- FastAPI applications
- Backend systems
- API integrations
- AI applications
- Cloud services

---

# 🌐 What is HTTP?

HTTP stands for:

HyperText Transfer Protocol

It is the protocol used for communication between:

- Clients
- Servers
- Websites
- APIs

Whenever you open a website, your browser sends an HTTP request.

---

# 📦 Installing HTTPX

Install using pip:

```bash
pip install httpx
```

---

# 🧠 Importing HTTPX

```python
import httpx
```

---

# 🚀 Sending a GET Request

Example:

```python
response = httpx.get(url)
```

This sends a request to the server.

---

# 📊 Status Codes

Every request returns a status code.

Common status codes:

| Code | Meaning |
|--------|--------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |

Example:

```python
print(response.status_code)
```

---

# 📦 JSON Responses

Most modern APIs return data in JSON format.

Convert JSON into Python:

```python
data = response.json()
```

Now the data becomes:

- Lists
- Dictionaries
- Nested Objects

---

# 🔍 Accessing Data

Example:

```python
data[0]["name"]
```

Returns the first user's name.

Example:

```python
data[0]["email"]
```

Returns the user's email.

---

# 💻 Complete Example

```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/users"
)

data = response.json()

print(data[0]["name"])
```

---

# ⚡ Async Support

One major advantage of HTTPX:

```python
async
await
```

support.

This makes it faster for modern web applications.

Example:

```python
async with httpx.AsyncClient() as client:
    response = await client.get(url)
```

---

# 🚀 Real-World Uses

HTTPX is used in:

- FastAPI Applications
- AI Projects
- API Clients
- Cloud Systems
- Automation Tools
- Data Collection Applications

---

# ⚡ Advantages of HTTPX

- Modern Design
- Async Support
- Fast Performance
- Easy API Integration
- Beginner Friendly

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How HTTP communication works
- How Python sends requests
- How APIs return data
- How JSON responses are processed
- Basics of modern API integration

---

# 🚀 Conclusion

The HTTPX library is a modern and powerful HTTP client for Python.

It helps developers:

- Communicate with APIs
- Fetch web data
- Build backend services
- Create modern applications

Learning HTTPX is useful for:

- Backend Development
- FastAPI
- AI Applications
- Cloud Services
- API Integration