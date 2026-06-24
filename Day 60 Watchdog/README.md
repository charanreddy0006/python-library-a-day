# Day 60 - Watchdog Library

# 📌 Overview

On Day 60, I explored Python's powerful Watchdog library, which is used for monitoring files and folders in real time.

Watchdog allows Python applications to detect:

* File creation
* File deletion
* File modification
* Folder changes
* File movement

Instead of repeatedly checking files manually, Watchdog automatically notifies the program whenever changes occur.

It is widely used in:

* File Monitoring Systems
* Backup Applications
* Synchronization Tools
* Automation Scripts
* Development Tools

---

# 📦 Installation

Install Watchdog using pip:

```bash
pip install watchdog
```

---

# 🧠 Importing the Library

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
```

---

# 👀 What is File Monitoring?

File monitoring means continuously watching files and folders for changes.

Examples:

* Detect new files
* Detect deleted files
* Detect modifications
* Trigger automation tasks

---

# 🚀 Creating an Event Handler

Example:

```python
class MyHandler(
    FileSystemEventHandler
):
    pass
```

The handler responds whenever file events occur.

---

# 📄 Detecting File Creation

Example:

```python
def on_created(
    self,
    event
):
    print("File Created")
```

Triggered whenever a new file is created.

---

# ✏️ Detecting File Modification

Example:

```python
def on_modified(
    self,
    event
):
    print("File Modified")
```

Triggered when a file changes.

---

# ❌ Detecting File Deletion

Example:

```python
def on_deleted(
    self,
    event
):
    print("File Deleted")
```

Triggered when a file is removed.

---

# 🎯 Creating an Observer

Example:

```python
observer = Observer()
```

The observer watches the selected directory.

---

# 📂 Monitoring a Folder

Example:

```python
observer.schedule(
    handler,
    ".",
    recursive=True
)
```

This watches the current folder and all subfolders.

---

# ▶️ Starting Monitoring

Example:

```python
observer.start()
```

Begins monitoring.

---

# ⏹️ Stopping Monitoring

Example:

```python
observer.stop()
```

Stops monitoring safely.

---

# 💻 Complete Example

```python
from watchdog.observers import Observer

observer = Observer()

observer.start()
```

---

# 🚀 Real-World Uses

## Backup Software

Automatically backup modified files.

---

## Folder Synchronization

Keep folders updated.

---

## Development Tools

Detect source code changes.

---

## Automation Systems

Trigger actions when files appear.

---

## Security Monitoring

Detect unauthorized file modifications.

---

# ⚡ Advantages of Watchdog

* Real-time monitoring
* Easy to use
* Lightweight
* Cross-platform
* Automation friendly

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* How file monitoring works
* How events are detected
* How automation reacts to file changes
* How observers monitor folders
* Basics of real-time system monitoring

---

# 🚀 Conclusion

The Watchdog library is a powerful Python tool for monitoring file and folder changes.

It helps developers:

* Build monitoring systems
* Create backup tools
* Automate workflows
* Detect file events

Learning Watchdog is useful for:

* Automation
* System Monitoring
* Development Tools
* Backup Applications
* Python Projects

It is one of the most practical libraries for real-time file monitoring.
