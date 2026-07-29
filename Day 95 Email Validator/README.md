# 📧 Day 95 - Professional Email Validator using Email Validator

## 📌 Overview

On Day 95 of my **Python Library A Day** challenge, I explored the **Email Validator** library by building a **Professional Email Validator**.

This application validates email addresses using industry-standard validation instead of relying only on regular expressions. It checks the email format, extracts the domain, and returns a normalized email address.

---

## 🎯 Project Objective

The objective of this project is to understand how professional applications validate email addresses before storing them in databases.

The application allows users to:

- Validate email addresses
- Detect invalid email formats
- Normalize email addresses
- Extract email domains
- Display meaningful validation messages

---

## 📂 Project Structure

```
Day 95 Email Validator/
│── email_validator_app.py
└── README.md
```

---

## ✨ Features

- 📧 Validate email addresses
- 🌐 Extract email domain
- ✅ Display normalized email
- ❌ Detect invalid email addresses
- ⚡ Fast and lightweight
- 💻 Beginner-friendly CLI application

---

## 📦 Installation

Install the required library:

```bash
pip install email-validator
```

---

## ▶️ Run the Project

```bash
python email_validator_app.py
```

---

## 📖 Example

### Input

```
charan@gmail.com
```

### Output

```
Email is Valid!

Original Email : charan@gmail.com

Normalized Email : charan@gmail.com

Domain : gmail.com
```

---

## 🔄 Workflow

```
Start
   │
   ▼
Enter Email Address
   │
   ▼
Validate Email
   │
   ├── Valid
   │      │
   │      ▼
   │ Show Normalized Email
   │ Show Domain
   │
   └── Invalid
          │
          ▼
     Display Error Message
```

---

## 🌍 Real-World Applications

- User Registration Forms
- Login Systems
- Banking Applications
- E-commerce Platforms
- CRM Software
- Newsletter Subscription Systems
- Customer Management Portals

---

## 📚 Concepts Covered

- Email Validation
- Exception Handling
- User Input
- Data Validation
- Python Libraries
- Domain Extraction

---

## 🚀 Why Email Validator?

The **email-validator** library performs much more reliable validation than regular expressions. It normalizes email addresses and provides detailed validation errors, making it ideal for production-ready applications.

---

## 🎯 Learning Outcome

After completing this project, you will understand:

- How email validation works
- Why regex alone is not enough
- How to normalize email addresses
- How professional applications validate user input

---

## 🏆 Conclusion

The **Email Validator** library provides a simple and reliable way to validate email addresses in Python applications. It is widely used in real-world software to improve data quality and enhance user experience.

---

## 📌 Library Used

- **Library:** Email Validator
- **Version:** Latest Stable Release

---

⭐ **Python Library A Day — Day 95**