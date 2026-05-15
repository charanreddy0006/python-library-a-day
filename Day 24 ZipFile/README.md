# Day 24 - ZipFile Module

# 📌 Overview

On Day 24, I explored Python’s built-in **zipfile module**, which is used for creating, reading, and extracting ZIP files.

ZIP files help compress files and folders into a smaller size for:

* storage
* sharing
* backups
* transfer

The zipfile module allows Python applications to:

* create compressed archives
* extract ZIP files
* inspect ZIP contents
* automate backup systems

It is widely used in:

* automation systems
* cloud storage
* software distribution
* file management tools

---

# 📦 Importing the Module

```python id="jlwm86"
import zipfile
```

---

# 🗜️ What is a ZIP File?

A ZIP file is a compressed archive format used to reduce file size and combine multiple files into one package.

Example:

```text id="jlwm87"
documents.zip
photos.zip
backup.zip
```

---

# ✍️ Creating a ZIP File

Example:

```python id="jlwm88"
zipfile.ZipFile("sample.zip", "w")
```

Explanation:

* `"sample.zip"` → ZIP filename
* `"w"` → write mode

---

# 📄 Adding Files to ZIP

Example:

```python id="jlwm89"
zipf.write("example.txt")
```

This adds a file into the ZIP archive.

---

# 📖 Reading ZIP Files

Example:

```python id="’wini90"
zipfile.ZipFile("sample.zip", "r")
```

Explanation:

* `"r"` → read mode

---

# 📋 Listing ZIP Contents

Example:

```python id="’wini91"
zipf.namelist()
```

This returns all files inside the ZIP archive.

---

# 📂 Extracting ZIP Files

Example:

```python id="’wini92"
zipf.extractall("folder_name")
```

This extracts all files into a folder.

---

# 💻 Complete Example

```python id="’wini93"
import zipfile

with zipfile.ZipFile("demo.zip", "w") as zipf:
    zipf.write("test.txt")
```

---

# 🚀 Real-World Uses

The zipfile module is used in:

* backup systems
* cloud uploads
* software packaging
* report compression
* automation scripts

---

# ⚡ Why ZIP Compression is Important

Compression helps:

* reduce storage space
* improve transfer speed
* organize multiple files

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how ZIP compression works
* how Python creates ZIP archives
* how to extract compressed files
* basics of backup automation

---

# 🚀 Conclusion

The zipfile module is a powerful tool for file compression and archive management.

It helps developers:

* automate backups
* compress files
* manage archives efficiently

Learning zipfile is useful for:

* automation
* backend systems
* cloud applications
* file management tools
