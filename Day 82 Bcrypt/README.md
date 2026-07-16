# 🔐 Day 82 - Bcrypt

## 📌 Overview

On Day 82 of my **Python Library A Day** challenge, I explored the **bcrypt** library by building a **Password Hashing & Verification System**.

Instead of storing passwords as plain text, modern applications use password hashing to improve security. This project demonstrates how to securely hash passwords and verify user credentials using bcrypt.

---

# 🚀 Project Objective

The goal of this project is to understand how secure password storage works.

The application allows users to:

- Create a password
- Hash the password securely
- Verify the password during login
- Prevent storing plain-text passwords

---

# 📂 Project Structure

```
Day 82 Bcrypt/
│── password_manager.py
└── README.md
```

---

# ✨ Features

- Secure password hashing
- Password verification
- Interactive command-line interface
- Uses salted hashes automatically
- Beginner-friendly implementation

---

# 📦 Installation

Install bcrypt using pip:

```bash
pip install bcrypt
```

---

# ▶️ Run the Project

```bash
python password_manager.py
```

---

# 🔄 Project Workflow

```
User Password
      │
      ▼
Generate Salt
      │
      ▼
Hash Password
      │
      ▼
Store Hash
      │
      ▼
User Login
      │
      ▼
Verify Password
      │
      ▼
Login Success / Failed
```

---

# 💻 Example

### Input

```
Password:
Python@123
```

### Output

```
Hashed Password:
$2b$12$...

Login Successful ✅
```

---

# 🌍 Real-World Applications

- User Authentication Systems
- Banking Applications
- E-commerce Websites
- Social Media Platforms
- Hospital Management Systems
- Enterprise Software
- Cloud Applications

---

# 📚 Concepts Covered

- Password Hashing
- Password Verification
- Salting
- Secure Authentication
- User Input Handling
- Functions in Python

---

# ⭐ Why Use Bcrypt?

Compared to storing passwords as plain text:

- Passwords are encrypted using strong hashing algorithms
- Each password gets a unique salt
- Resistant to brute-force attacks
- Industry standard for authentication systems

---

# 🎯 Learning Outcome

After completing this project, I learned:

- What password hashing is
- Why hashing is important
- How bcrypt generates secure hashes
- How password verification works
- Why applications should never store plain-text passwords

---

# 🏆 Conclusion

bcrypt is one of the most trusted libraries for password security in Python.

This mini project demonstrates how modern applications securely store and verify user passwords using salted hashing.

Understanding bcrypt is an essential skill for backend development, authentication systems, and secure application design.