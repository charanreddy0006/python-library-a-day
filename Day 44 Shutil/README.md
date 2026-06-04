# Day 44 - Shutil Module

# 📌 Overview

On Day 44, I explored Python's built-in **shutil module**, which provides high-level file and directory operations.

The name shutil stands for:

```text
Shell Utilities
```

It helps developers perform common file management tasks such as:

- Copying files
- Moving files
- Renaming files
- Deleting directories
- Creating backups

The shutil module is widely used in:

- Backup Applications
- File Managers
- Automation Scripts
- Deployment Systems
- Data Processing Pipelines

---

# 📦 Importing Shutil

```python
import shutil
```

Since shutil is built into Python, no installation is required.

---

# 🧠 Why Use Shutil?

Without shutil:

Managing files requires multiple low-level operations.

With shutil:

Complex file operations become simple and readable.

Example:

```python
shutil.copy(
    "source.txt",
    "backup.txt"
)
```

One line can copy an entire file.

---

# 📄 Copying Files

Example:

```python
shutil.copy(
    "source.txt",
    "backup.txt"
)
```

This copies:

```text
source.txt
```

to

```text
backup.txt
```

---

# 📁 Copying Entire Folders

Example:

```python
shutil.copytree(
    "source_folder",
    "backup_folder"
)
```

This copies:

- all files
- all subfolders

inside the directory.

---

# 🚚 Moving Files

Example:

```python
shutil.move(
    "old.txt",
    "new_folder/old.txt"
)
```

Used for:

- file organization
- automation scripts
- data processing

---

# ❌ Removing Directories

Example:

```python
shutil.rmtree(
    "old_folder"
)
```

Deletes:

- folder
- subfolders
- files

Use carefully.

---

# 💾 Creating Backups

Example:

```python
shutil.copy(
    "database.db",
    "database_backup.db"
)
```

Used in:

- backup systems
- automation tools

---

# 📊 Getting Disk Usage

Example:

```python
shutil.disk_usage("/")
```

Returns:

- total space
- used space
- free space

---

# 💻 Complete Example

```python
import shutil

shutil.copy(
    "source.txt",
    "backup.txt"
)
```

---

# 🚀 Real-World Uses

## Backup Systems

Create automatic backups.

---

## File Managers

Copy and move files.

---

## Deployment Tools

Transfer project files.

---

## Automation Scripts

Organize directories automatically.

---

## Data Processing

Move processed files into archive folders.

---

# ⚡ Advantages of Shutil

- Built into Python
- Easy to use
- Powerful file operations
- Cross-platform
- Supports folders and files

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How file copying works
- How file moving works
- How directory operations work
- How backups are created
- How automation tools manage files

---

# 🚀 Conclusion

The shutil module is one of Python's most useful built-in libraries for file management.

It helps developers:

- Manage files efficiently
- Create backups
- Organize directories
- Automate file operations

Learning shutil is useful for:

- Automation
- System Administration
- File Management
- Data Processing
- Software Development

It is an essential library for working with files and folders in Python.