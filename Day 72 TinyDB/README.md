# Day 72 - TinyDB Library

# 📌 Overview

On Day 72, I explored Python's **TinyDB** library, a lightweight document-oriented NoSQL database written entirely in Python.

TinyDB stores data in JSON files instead of traditional database servers, making it simple to use and ideal for small applications.

Unlike SQL databases, TinyDB does not require installation or configuration.

It is widely used in:

- Desktop Applications
- CLI Tools
- Personal Projects
- Configuration Storage
- Small Databases
- Rapid Prototyping

---

# 📦 Installation

Install TinyDB using pip:

```bash
pip install tinydb
```

---

# 🧠 Importing the Library

```python
from tinydb import TinyDB, Query
```

---

# 📖 What is TinyDB?

TinyDB is a lightweight NoSQL database that stores information in JSON format.

Unlike SQLite or MySQL:

- No database server is required
- No SQL queries are needed
- Data is stored as JSON documents
- Very easy to learn

---

# 🚀 Creating a Database

Example:

```python
db = TinyDB("database.json")
```

If the file does not exist, TinyDB automatically creates it.

---

# ➕ Inserting Data

Example:

```python
db.insert({
    "name": "Alice",
    "age": 21
})
```

Adds a new document to the database.

---

# 📄 Viewing All Records

Example:

```python
db.all()
```

Returns all stored documents.

---

# 🔍 Searching Data

Example:

```python
Student = Query()

db.search(Student.age > 20)
```

Searches for records matching a condition.

---

# ✏️ Updating Records

Example:

```python
db.update(
    {"course": "AI"},
    Student.name == "Alice"
)
```

Updates matching records.

---

# ❌ Deleting Records

Example:

```python
db.remove(
    Student.name == "Alice"
)
```

Removes matching records.

---

# 💻 Complete Example

```python
from tinydb import TinyDB

db = TinyDB("database.json")

db.insert({
    "name": "John"
})

print(db.all())
```

---

# 🚀 Real-World Uses

## Personal Projects

Store small amounts of structured data.

---

## Configuration Files

Save application settings.

---

## Desktop Applications

Store user preferences.

---

## CLI Applications

Maintain local records without a database server.

---

## Rapid Prototyping

Quickly build applications without configuring SQL databases.

---

# ⚡ Advantages of TinyDB

- Pure Python
- No database server required
- Stores data in JSON
- Easy to learn
- Lightweight
- Cross-platform

---

# 🆚 TinyDB vs SQLite

| Feature | TinyDB | SQLite |
|---------|---------|---------|
| Database Server | ❌ No | ❌ No |
| SQL Required | ❌ No | ✅ Yes |
| Storage Format | JSON | Database File |
| Beginner Friendly | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Best For | Small Apps | Medium Applications |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What a NoSQL database is
- How TinyDB stores data
- How to insert records
- How to search documents
- How to update and delete records

---

# 🚀 Conclusion

TinyDB is an excellent lightweight database for Python applications.

It helps developers:

- Store structured data
- Build small applications
- Create prototypes quickly
- Manage JSON-based databases

Learning TinyDB is useful for:

- Python Development
- Automation
- Desktop Applications
- CLI Tools
- Rapid Prototyping

TinyDB is one of the easiest NoSQL databases for beginners and is a great choice for lightweight Python projects.