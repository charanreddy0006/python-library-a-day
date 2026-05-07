# Day 17 - Subprocess Module

# 📌 Overview

On Day 17, I explored Python’s built-in **subprocess module**, which is used to execute system commands and interact with the terminal directly from Python programs.

The subprocess module is one of the most powerful modules in Python because it allows Python scripts to communicate with the operating system.

It is widely used in:

* Automation scripts
* DevOps tools
* Backend systems
* System administration
* Running external applications
* Executing shell commands

Using subprocess, Python can:

* Run terminal commands
* Open applications
* Execute other Python files
* Capture command output
* Automate repetitive tasks

---

# 🧠 Why Subprocess is Important

Normally, we execute commands manually in terminal like:

```bash
python --version
dir
ping google.com
```

With the subprocess module, Python can execute these commands automatically.

This helps developers build:

* automation tools
* deployment scripts
* monitoring systems
* command-line applications

---

# 📦 Importing the Module

```python
import subprocess
```

---

# ⚙️ Main Function Used

The most commonly used function is:

```python
subprocess.run()
```

It runs a system command from Python.

---

# 💻 Basic Example

```python
import subprocess

subprocess.run(["echo", "Hello"])
```

### Output

```text
Hello
```

Explanation:

* `echo` is a terminal command
* Python executes it using subprocess

---

# 🧾 Understanding subprocess.run()

Syntax:

```python
subprocess.run(command)
```

Example:

```python
subprocess.run(["python", "--version"])
```

This command checks the installed Python version.

---

# 🔍 Important Parameters

---

## 1. capture_output=True

Used to capture terminal output inside Python.

Example:

```python
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

### Output

```text
Python 3.x.x
```

### Explanation

* `stdout` stores command output
* Without `capture_output=True`, output only appears in terminal

---

# 2. text=True

Converts output into readable text format.

Without it:

```python
b'Python 3.x.x'
```

With it:

```python
Python 3.x.x
```

---

# 3. shell=True

Allows execution of shell commands.

Example:

```python
subprocess.run("dir", shell=True)
```

### Explanation

* `dir` is a Windows shell command
* `shell=True` allows shell execution

For Linux/Mac:

```python
subprocess.run("ls", shell=True)
```

---

# 📂 Listing Files in Directory

Example:

```python
files = subprocess.run(
    ["dir"],
    shell=True,
    capture_output=True,
    text=True
)

print(files.stdout)
```

### What Happens?

* Python executes `dir`
* Directory contents are captured
* Output is printed

---

# 🧠 Understanding stdout and stderr

When a command runs:

* stdout → normal output
* stderr → error output

Example:

```python
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
```

---

# ❌ Handling Errors

Example:

```python
result = subprocess.run(
    ["wrongcommand"],
    capture_output=True,
    text=True
)

print(result.stderr)
```

### Explanation

If command is invalid:

* error message goes to stderr

---

# 🚀 Real-World Uses of Subprocess

---

## 1. Running Python Files

```python
subprocess.run(["python", "test.py"])
```

Used in:

* automation
* task scheduling

---

# 2. Opening Applications

Example (Windows):

```python
subprocess.run("notepad", shell=True)
```

This opens Notepad automatically.

---

# 3. Network Commands

```python
subprocess.run(["ping", "google.com"])
```

Used for:

* network testing
* server monitoring

---

# 4. Git Commands

```python
subprocess.run(["git", "status"])
```

Used in:

* DevOps
* deployment automation

---

# ⚠️ Important Notes

---

## Avoid shell=True when unnecessary

Why?
Because it can create security risks if user input is passed directly.

Safer:

```python
subprocess.run(["dir"])
```

Less safe:

```python
subprocess.run("dir", shell=True)
```

---

# 🔥 Difference Between os.system() and subprocess

| os.system()            | subprocess           |
| ---------------------- | -------------------- |
| Old method             | Modern method        |
| Less control           | More powerful        |
| Hard to capture output | Easy output handling |
| Limited features       | Advanced features    |

Today, subprocess is preferred.

---

# 🧪 Complete Example Program

```python
import subprocess

# run echo command
result = subprocess.run(
    ["echo", "Hello from Python"],
    capture_output=True,
    text=True
)

print(result.stdout)

# check python version
version = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(version.stdout)

# list directory files
files = subprocess.run(
    ["dir"],
    shell=True,
    capture_output=True,
    text=True
)

print(files.stdout)
```

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how Python executes terminal commands
* how to capture command outputs
* how automation scripts work
* how Python communicates with the operating system
* basics of system scripting

---

# 🚀 Conclusion

The subprocess module is a powerful tool for automation and system interaction.

It allows Python programs to:

* communicate with the operating system
* execute terminal commands
* automate workflows
* build professional tools

It is an important module for:

* Python developers
* automation engineers
* DevOps engineers
* backend developers

Learning subprocess helps in building real-world automation projects and advanced Python applications.
