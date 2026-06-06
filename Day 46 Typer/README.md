# Day 46 - Typer Library

# 📌 Overview

On Day 46, I explored Python's modern **Typer library**, which is used for building Command Line Interface (CLI) applications.

Typer is built on top of:

- Click
- Python Type Hints

It allows developers to create professional command-line tools with very little code.

Typer automatically:

- Parses arguments
- Generates help pages
- Validates input types
- Creates user-friendly CLI applications

---

# 📦 Installation

Install Typer using pip:

```bash
pip install typer
```

---

# 🧠 Importing Typer

```python
import typer
```

---

# 🎯 What is a CLI Application?

CLI stands for:

```text
Command Line Interface
```

Instead of using buttons and windows, users interact through terminal commands.

Examples:

```bash
git status

pip install requests

python app.py
```

These are CLI applications.

---

# 🚀 Creating a Typer App

Example:

```python
app = typer.Typer()
```

This creates a command-line application.

---

# 🏷️ Creating Commands

Example:

```python
@app.command()
def greet():
```

Each decorated function becomes a terminal command.

---

# 📥 Accepting Input

Example:

```python
def greet(name: str):
```

Typer automatically:

- Reads the argument
- Validates the type
- Passes the value

---

# 📢 Displaying Output

Example:

```python
typer.echo("Hello")
```

Used instead of:

```python
print("Hello")
```

because it works better for CLI applications.

---

# 📄 Automatic Help Page

Run:

```bash
python typer_basics.py --help
```

Typer automatically generates documentation.

Example:

```text
Usage: typer_basics.py [OPTIONS] COMMAND [ARGS]...
```

This is one of Typer's most powerful features.

---

# 💻 Complete Example

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(
        f"Hello {name}"
    )

app()
```

---

# 🚀 Real-World Uses

Typer is used in:

## Developer Tools

```bash
mytool build
```

---

## Automation Scripts

```bash
backup start
```

---

## AI Applications

```bash
ai_chat ask
```

---

## DevOps Utilities

```bash
deploy production
```

---

# ⚡ Advantages of Typer

- Easy syntax
- Automatic help pages
- Type validation
- Professional CLI applications
- Built on modern Python features

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What CLI applications are
- How Typer works
- How to create commands
- How to accept terminal input
- How professional command-line tools are built

---

# 🚀 Conclusion

The Typer library is one of the best modern Python libraries for creating command-line applications.

It helps developers:

- Build CLI tools quickly
- Validate input automatically
- Create professional interfaces
- Improve user experience

Learning Typer is useful for:

- Automation
- DevOps
- Developer Tools
- AI Applications
- Productivity Software

Typer is a must-learn library for anyone interested in building professional Python tools.