# 🌐 Day 88 - Website Ping Checker using Ping3

## 📌 Overview

On Day 88 of my **Python Library A Day** challenge, I explored the **Ping3** library by building a **Website Ping Checker**.

The application checks whether a website or IP address is reachable and measures the response time in milliseconds.

This project demonstrates how Python can be used for basic network diagnostics without relying on operating system commands.

---

# 🚀 Project Objective

The objective of this project is to:

- Check if a website or IP address is reachable
- Measure network response time
- Learn basic network programming with Python

---

# 📂 Project Structure

```
Day 88 Ping3/
│── ping_checker.py
└── README.md
```

---

# ✨ Features

- Ping websites or IP addresses
- Display response time
- Detect unreachable hosts
- Simple command-line interface
- Exception handling

---

# 📦 Installation

```bash
pip install ping3
```

---

# ▶️ Run

```bash
python ping_checker.py
```

---

# 🔄 Workflow

```
Start
   │
   ▼
Enter Website/IP
   │
   ▼
Send Ping Request
   │
   ▼
Receive Response
   │
   ├── Reachable → Show Response Time
   └── Unreachable → Display Error
```

---

# 💻 Example

Input:

```
google.com
```

Output:

```
✅ google.com is reachable.

Response Time: 24.63 ms
```

---

# 🌍 Real-World Applications

- Server Monitoring
- Network Diagnostics
- DevOps Tools
- Cloud Infrastructure Monitoring
- IT Support Utilities
- System Administration

---

# 📚 Concepts Covered

- Network Programming
- Ping Requests
- Exception Handling
- Functions
- User Input
- CLI Applications

---

# ⭐ Why Use Ping3?

Unlike calling the system's `ping` command, Ping3 provides a pure Python interface that works directly within your application, making it easier to integrate into monitoring tools.

---

# 🎯 Learning Outcome

After completing this project, you will understand:

- How ICMP ping works
- How to measure network latency
- How to check host availability
- How to build simple network utilities in Python

---

# 🏆 Conclusion

Ping3 is a lightweight library for performing ping operations directly in Python. It is ideal for network monitoring, diagnostics, and automation scripts where connectivity checks are required.