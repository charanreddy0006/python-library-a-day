# Day 42 - Tabulate Library

# 📌 Overview

On Day 42, I explored Python's **tabulate library**, which is used to display data in beautiful table formats.

Normally, when printing lists or dictionaries, the output can become difficult to read.

The tabulate library solves this problem by converting data into structured tables.

It is commonly used in:

- Command Line Applications
- Reporting Tools
- Automation Scripts
- Data Analysis
- Admin Dashboards
- System Monitoring Tools

---

# 📦 Installation

Install the library using pip:

```bash
pip install tabulate
```

---

# 🧠 Importing Tabulate

```python
from tabulate import tabulate
```

---

# 📋 What is Tabulate?

Tabulate is a Python library that converts data into well-formatted tables.

Instead of:

```python
[['Chakri', 95], ['Rahul', 88]]
```

You can display:

| Name | Marks |
|------|--------|
| Chakri | 95 |
| Rahul | 88 |

which is much easier to read.

---

# 📊 Creating a Basic Table

Example:

```python
from tabulate import tabulate

data = [
    ["Python", 95],
    ["Java", 90]
]

print(tabulate(data))
```

---

# 🏷️ Adding Headers

Example:

```python
headers = ["Language", "Score"]
```

```python
tabulate(data, headers=headers)
```

This creates meaningful column names.

---

# 🎨 Table Formats

Tabulate supports many styles.

### Grid Format

```python
tablefmt="grid"
```

Output:

```text
+----------+--------+
| Name     | Marks  |
+----------+--------+
| Chakri   | 95     |
+----------+--------+
```

---

### Fancy Grid

```python
tablefmt="fancy_grid"
```

---

### Pipe Format

```python
tablefmt="pipe"
```

Useful for Markdown tables.

---

### Simple Format

```python
tablefmt="simple"
```

Used in CLI applications.

---

# 💻 Complete Example

```python
from tabulate import tabulate

students = [
    ["Chakri", 95],
    ["Rahul", 88]
]

headers = ["Name", "Marks"]

print(
    tabulate(
        students,
        headers=headers,
        tablefmt="grid"
    )
)
```

---

# 🚀 Real-World Uses

## Student Reports

```python
tabulate(student_data)
```

---

## Employee Records

```python
tabulate(employee_data)
```

---

## Server Monitoring

Display:

- CPU Usage
- Memory Usage
- Disk Usage

in table format.

---

## Data Analysis

Present datasets clearly.

---

# ⚡ Advantages of Tabulate

- Easy to use
- Professional output
- Multiple table styles
- Improves readability
- Lightweight library

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How to create formatted tables
- How to add headers
- Different table styles
- How to present structured data
- Better CLI output formatting

---

# 🚀 Conclusion

The Tabulate library is a simple but powerful Python library for displaying structured data.

It helps developers:

- Create readable reports
- Improve terminal output
- Build professional CLI applications
- Present data clearly

Learning Tabulate is useful for:

- Data Analysis
- Automation
- Reporting Systems
- CLI Applications
- Developer Tools

It is one of the best libraries for making console output look professional.