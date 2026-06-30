# Day 66 - Loguru Library

# 📌 Overview

On Day 66, I explored Python's modern **Loguru** library, which is used for logging messages in applications.

Logging is an important part of software development because it helps developers understand what their application is doing, identify errors, and troubleshoot problems.

Unlike Python's built-in `logging` module, Loguru provides a much simpler and cleaner interface while offering many advanced features.

It is widely used in:

* Backend Development
* Data Engineering
* Automation Scripts
* AI & Machine Learning Projects
* DevOps
* Production Applications

---

# 📦 Installation

Install Loguru using pip:

```bash
pip install loguru
```

---

# 🧠 Importing the Library

```python
from loguru import logger
```

The `logger` object is ready to use immediately without any additional configuration.

---

# 📖 What is Logging?

Logging is the process of recording information about how a program runs.

Logs help developers:

* Monitor applications
* Find bugs
* Track user activity
* Record errors
* Analyze performance

Instead of using multiple `print()` statements, developers use logging to generate organized and professional output.

---

# 🚀 Writing a Log Message

Example:

```python
from loguru import logger

logger.info("Application started")
```

This displays an informational message in the console.

---

# 🔍 Log Levels

Loguru supports different logging levels.

### Debug

Used while developing applications.

```python
logger.debug("Debug message")
```

---

### Info

General information about program execution.

```python
logger.info("Application started")
```

---

### Success

Indicates that an operation completed successfully.

```python
logger.success("File uploaded successfully")
```

---

### Warning

Used when something unexpected happens but the program can continue.

```python
logger.warning("Low disk space")
```

---

### Error

Used when an operation fails.

```python
logger.error("Database connection failed")
```

---

### Critical

Used for serious errors that may stop the application.

```python
logger.critical("Application crashed")
```

---

# 💾 Saving Logs to a File

Loguru can automatically save log messages into a file.

Example:

```python
logger.add("app.log")
```

Now every log message will also be stored in **app.log**.

---

# 📄 Logging to Multiple Files

Example:

```python
logger.add("errors.log", level="ERROR")
```

Only **ERROR** and **CRITICAL** messages will be saved to `errors.log`.

---

# 🎨 Formatted Log Messages

Example:

```python
logger.info("Welcome, {}!", "Chakri")
```

Output:

```text
Welcome, Chakri!
```

This makes string formatting simple and readable.

---

# 💻 Complete Example

```python
from loguru import logger

logger.add("application.log")

logger.info("Application Started")

logger.success("Login Successful")

logger.warning("Low Memory")

logger.error("Unable to Connect to Server")
```

---

# 🚀 Real-World Uses

## Backend Applications

Record API requests and server activity.

---

## Automation Scripts

Track the progress of automated tasks.

---

## Data Engineering

Log ETL processes and data pipeline execution.

---

## AI & Machine Learning

Store model training logs and prediction results.

---

## DevOps

Monitor servers and application performance.

---

## Desktop Applications

Save application errors for troubleshooting.

---

# ⚡ Advantages of Loguru

* Extremely easy to use
* Beautiful console output
* Automatic timestamps
* Supports log files
* Supports log rotation
* Built-in formatting
* Better than basic print statements
* Simpler than Python's built-in logging module

---

# 🆚 Loguru vs Python Logging

| Feature             | Loguru     | Logging Module           |
| ------------------- | ---------- | ------------------------ |
| Easy to Use         | ✅ Yes      | ❌ Requires Configuration |
| Built-in Formatting | ✅ Yes      | ❌ Manual Setup           |
| Colored Output      | ✅ Yes      | ❌ No                     |
| File Logging        | ✅ Easy     | ✅ Supported              |
| Log Rotation        | ✅ Built-in | ⚠️ More Configuration    |
| Beginner Friendly   | ⭐⭐⭐⭐⭐      | ⭐⭐⭐                      |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* What logging is
* Why logging is important
* Different logging levels
* How to save logs to files
* How Loguru simplifies logging
* Real-world uses of application logs

---

# 🚀 Conclusion

The **Loguru** library is one of the best logging libraries available for Python.

It helps developers:

* Monitor applications
* Debug programs
* Track errors
* Save logs automatically
* Build production-ready software

Learning Loguru is useful for:

* Backend Development
* Data Engineering
* AI Projects
* Automation
* DevOps
* Professional Python Applications

Loguru is an excellent replacement for simple `print()` statements and makes debugging and monitoring Python applications much easier.
