# Day 71 - SQLAlchemy Library

# 📌 Overview

On Day 71, I explored Python's **SQLAlchemy** library, one of the most popular Object Relational Mappers (ORMs) for Python.

SQLAlchemy allows developers to interact with relational databases using Python objects instead of writing raw SQL queries.

It combines the flexibility of SQL with the simplicity of Python programming.

SQLAlchemy is widely used in:

- Flask Applications
- FastAPI Projects
- Enterprise Software
- Data Engineering
- Database Management Systems
- REST APIs

---

# 📦 Installation

Install SQLAlchemy using pip:

```bash
pip install sqlalchemy
```

---

# 🧠 Importing the Library

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
```

---

# 📖 What is an ORM?

ORM stands for:

```text
Object Relational Mapper
```

An ORM allows developers to work with database tables as Python classes.

Instead of writing SQL like:

```sql
SELECT * FROM students;
```

You can write:

```python
session.query(Student).all()
```

This makes code cleaner, easier to maintain, and more secure.

---

# 🚀 Creating a Database Engine

Example:

```python
engine = create_engine(
    "sqlite:///students.db"
)
```

This creates a connection to an SQLite database.

---

# 🏗️ Creating a Base Class

Example:

```python
Base = declarative_base()
```

This is the base class for all database models.

---

# 📋 Defining a Table

Example:

```python
class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    course = Column(String)
```

Each class represents a table in the database.

---

# 🏗️ Creating Tables

Example:

```python
Base.metadata.create_all(engine)
```

Creates all tables defined in your models.

---

# 🔄 Creating a Session

Example:

```python
Session = sessionmaker(bind=engine)

session = Session()
```

A session manages database transactions.

---

# ➕ Inserting Data

Example:

```python
student = Student(
    name="Alice",
    course="Python"
)

session.add(student)

session.commit()
```

Adds a new record to the database.

---

# 🔍 Querying Data

Example:

```python
students = session.query(Student).all()
```

Retrieves all records from the table.

---

# ✏️ Updating Data

Example:

```python
student.name = "Bob"

session.commit()
```

Updates an existing record.

---

# ❌ Deleting Data

Example:

```python
session.delete(student)

session.commit()
```

Deletes a record from the database.

---

# 💻 Complete Example

```python
student = Student(
    name="John",
    course="AI"
)

session.add(student)

session.commit()

students = session.query(Student).all()

for s in students:
    print(s.name)
```

---

# 🚀 Real-World Uses

## Web Applications

Manage user accounts and application data.

---

## E-commerce Platforms

Store products, customers, and orders.

---

## Student Management Systems

Maintain student records.

---

## REST APIs

Connect backend services to databases.

---

## Enterprise Software

Handle complex database operations.

---

# ⚡ Advantages of SQLAlchemy

- Reduces SQL code
- Supports multiple databases
- Secure against SQL injection
- Easy to maintain
- Powerful ORM features
- Industry standard

---

# 🆚 SQLAlchemy vs Raw SQL

| Feature | SQLAlchemy | Raw SQL |
|---------|------------|---------|
| Easy to Read | ✅ | ❌ |
| Database Independent | ✅ | ❌ |
| Secure | ✅ | ⚠️ |
| Python Integration | ✅ | Limited |
| ORM Support | ✅ | ❌ |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What an ORM is
- How SQLAlchemy works
- How to connect to a database
- How to create tables using Python
- How to insert, query, update, and delete records

---

# 🚀 Conclusion

SQLAlchemy is one of the most important Python libraries for working with relational databases.

It enables developers to:

- Build database-driven applications
- Simplify SQL operations
- Improve code readability
- Work with multiple database systems

Learning SQLAlchemy is valuable for:

- Backend Development
- FastAPI
- Flask
- Data Engineering
- Enterprise Applications
- Python Development

SQLAlchemy is considered the industry-standard ORM for Python and is an essential skill for modern backend developers.