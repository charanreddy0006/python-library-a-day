# Day 69 - PyJWT Library

# 📌 Overview

On Day 69, I explored Python's **PyJWT** library, which is used for creating and verifying **JSON Web Tokens (JWTs)**.

JWT is a compact and secure method of transmitting information between systems as JSON objects. It is widely used for user authentication and authorization in modern web applications.

PyJWT allows developers to:

- Generate JWT tokens
- Decode JWT tokens
- Verify token signatures
- Secure API endpoints
- Implement authentication systems

It is widely used in:

- REST APIs
- FastAPI Applications
- Flask Applications
- Backend Development
- Authentication Systems
- Microservices

---

# 📦 Installation

Install PyJWT using pip:

```bash
pip install PyJWT
```

---

# 🧠 Importing the Library

```python
import jwt
```

---

# 🔐 What is JWT?

JWT stands for:

```text
JSON Web Token
```

It is a secure token used to identify users after successful login.

Instead of sending a username and password with every request, the client sends a JWT.

---

# 🏗️ Structure of a JWT

A JWT has three parts:

```text
Header
.
Payload
.
Signature
```

Example:

```text
xxxxx.yyyyy.zzzzz
```

---

# 📝 Header

The header contains metadata about the token.

Example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

---

# 📦 Payload

The payload contains user information.

Example:

```json
{
  "username": "Chakri",
  "role": "Student"
}
```

The payload should not contain sensitive information like passwords.

---

# 🔒 Signature

The signature ensures that the token has not been modified.

It is generated using:

- Secret Key
- Header
- Payload

---

# 🚀 Creating a JWT Token

Example:

```python
token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)
```

This generates a secure JWT token.

---

# 📥 Decoding a JWT

Example:

```python
decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)
```

Returns the original payload after verifying the signature.

---

# ⚠️ Handling Invalid Tokens

Example:

```python
try:
    decoded = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )
except jwt.InvalidTokenError:
    print("Invalid Token")
```

This prevents unauthorized access.

---

# 💻 Complete Example

```python
import jwt

SECRET_KEY = "my_secret_key"

payload = {
    "username": "Alice"
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print(token)

print(
    jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )
)
```

---

# 🚀 Real-World Uses

## User Authentication

Authenticate users after login.

---

## API Security

Protect API endpoints using JWT.

---

## Authorization

Control user permissions and access.

---

## Microservices

Secure communication between services.

---

## Single Sign-On (SSO)

Enable secure authentication across multiple applications.

---

# ⚡ Advantages of PyJWT

- Easy to use
- Secure token generation
- Lightweight
- Widely adopted
- Compatible with FastAPI and Flask
- Industry standard

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What JWT is
- How JWT authentication works
- How to generate JWT tokens
- How to decode and verify tokens
- Why JWT is widely used in backend development

---

# 🚀 Conclusion

PyJWT is an essential library for implementing secure authentication in Python applications.

It helps developers:

- Create secure tokens
- Verify user identity
- Protect APIs
- Build authentication systems
- Improve application security

Learning PyJWT is useful for:

- Backend Development
- FastAPI
- Flask
- REST APIs
- Authentication Systems
- Web Security

PyJWT is one of the most important libraries for modern Python backend development.