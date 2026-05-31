# Day 40 - SQLite3 Module

# 📌 Overview

On Day 40, I explored Python's built-in **sqlite3 module**, which allows Python applications to work with SQLite databases.

SQLite is a lightweight database system that stores data in a single file.

Unlike large database systems such as MySQL and PostgreSQL, SQLite does not require a separate server.

It is commonly used in:

- Desktop Applications
- Mobile Applications
- Student Management Systems
- Inventory Systems
- Local Data Storage
- Small Business Applications

---

# 🧠 What is a Database?

A database is an organized collection of data.

Example:

| ID | Name | Marks |
|----|------|--------|
| 1 | Chakri | 95 |
| 2 | Rahul | 88 |

Instead of storing data in files manually, databases allow structured storage and retrieval.

---

# 📦 Importing sqlite3

```python
import sqlite3
```

SQLite support is built into Python.

No installation required.

---

# 🔗 Connecting to Database

```python
conn = sqlite3.connect("students.db")
```

If the database doesn't exist:

- SQLite automatically creates it.

---

# 🎯 Creating a Cursor

```python
cursor = conn.cursor()
```

The cursor is used to execute SQL commands.

---

# 📋 Creating a Table

```python
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")
```

This creates a table for storing student information.

---

# ➕ Inserting Data

```python
cursor.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    ("Chakri", 95)
)
```

Adds a new record.

---

# 💾 Saving Changes

```python
conn.commit()
```

Without commit():

Data will not be permanently stored.

---

# 🔍 Retrieving Data

```python
cursor.execute("SELECT * FROM students")
```

Fetch all records:

```python
rows = cursor.fetchall()
```

---

# ❌ Deleting Data

```python
cursor.execute(
    "DELETE FROM students WHERE id=1"
)
```

Removes a record.

---

# ✏️ Updating Data

```python
cursor.execute(
    "UPDATE students SET marks=98 WHERE id=1"
)
```

Updates existing information.

---

# 🔒 Closing Database

```python
conn.close()
```

Always close connections after use.

---

# 🚀 Real-World Uses

SQLite is used in:

- Attendance Systems
- Student Management Systems
- Expense Trackers
- To-Do Applications
- Inventory Management
- Offline Desktop Applications

---

# ⚡ Advantages of SQLite

- Built into Python
- No server required
- Lightweight
- Fast
- Easy to learn
- Portable

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What databases are
- How SQLite works
- How to create tables
- How to insert data
- How to retrieve records
- How to update and delete data

---

# 🚀 Conclusion

The sqlite3 module is one of the most important built-in Python modules for data storage.

It helps developers:

- Store information permanently
- Build data-driven applications
- Create management systems
- Learn database fundamentals

Learning sqlite3 is useful for:

- Python Development
- Desktop Applications
- Backend Development
- Database Management
- Software Projects