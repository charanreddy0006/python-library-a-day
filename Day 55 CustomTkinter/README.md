# Day 55 - CustomTkinter Library

# 📌 Overview

On Day 55, I explored Python's modern **CustomTkinter library**, which is used for creating beautiful desktop GUI applications.

CustomTkinter is an enhanced version of the standard Tkinter library. It provides modern-looking widgets, dark mode support, improved styling, and a professional user interface.

Unlike traditional Tkinter applications, CustomTkinter applications look more modern and visually appealing.

It is widely used in:

* Desktop Applications
* Management Systems
* Productivity Tools
* Dashboard Applications
* Automation Software
* Modern GUI Projects

---

# 📦 Installation

Install CustomTkinter using pip:

```bash
pip install customtkinter
```

---

# 🧠 Importing the Library

```python
import customtkinter as ctk
```

The alias `ctk` is commonly used for easier coding.

---

# 🎨 What is CustomTkinter?

CustomTkinter is a Python GUI library that extends Tkinter with:

* Modern widgets
* Better themes
* Dark mode support
* Improved appearance
* Better user experience

It allows developers to create professional desktop applications with minimal effort.

---

# 🚀 Creating an Application Window

Example:

```python
app = ctk.CTk()
```

This creates the main application window.

---

# 🏷️ Setting Window Title

Example:

```python
app.title("My Application")
```

Sets the title displayed on the window.

---

# 📏 Setting Window Size

Example:

```python
app.geometry("400x300")
```

Defines the window dimensions.

---

# 🌙 Appearance Modes

CustomTkinter supports different themes.

### Dark Mode

```python
ctk.set_appearance_mode("dark")
```

### Light Mode

```python
ctk.set_appearance_mode("light")
```

### System Mode

```python
ctk.set_appearance_mode("system")
```

Automatically follows the operating system theme.

---

# 🎨 Color Themes

CustomTkinter supports built-in themes.

Example:

```python
ctk.set_default_color_theme("blue")
```

Available themes:

* blue
* green
* dark-blue

---

# 📝 Creating Labels

Labels display text on the screen.

Example:

```python
label = ctk.CTkLabel(
    app,
    text="Welcome"
)
```

---

# 🔘 Creating Buttons

Buttons allow users to perform actions.

Example:

```python
button = ctk.CTkButton(
    app,
    text="Click Me"
)
```

---

# ⚡ Button Commands

Example:

```python
def greet():
    print("Hello")

button = ctk.CTkButton(
    app,
    text="Click",
    command=greet
)
```

When clicked, the function executes.

---

# 📥 Entry Widgets

Entry widgets allow users to enter text.

Example:

```python
entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Name"
)
```

Used for:

* Login Forms
* Registration Forms
* Search Boxes

---

# ☑️ Checkboxes

Example:

```python
checkbox = ctk.CTkCheckBox(
    app,
    text="Accept Terms"
)
```

Used for user selections.

---

# 🎚️ Sliders

Example:

```python
slider = ctk.CTkSlider(
    app,
    from_=0,
    to=100
)
```

Used for:

* Volume Control
* Brightness Settings
* Percentage Selection

---

# 📋 Option Menus

Example:

```python
menu = ctk.CTkOptionMenu(
    app,
    values=["Python", "Java", "C++"]
)
```

Creates a dropdown menu.

---

# 💻 Complete Example

```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.geometry("400x300")

label = ctk.CTkLabel(
    app,
    text="Welcome to CustomTkinter"
)

label.pack(pady=20)

app.mainloop()
```

---

# 🚀 Real-World Uses

## Student Management Systems

Create attractive desktop applications for managing student data.

---

## Expense Tracker Applications

Track income and expenses using a modern interface.

---

## Inventory Management Systems

Manage products and stock visually.

---

## Dashboard Applications

Display statistics and reports.

---

## Personal Productivity Tools

Build to-do lists, note-taking apps, and planners.

---

# ⚡ Advantages of CustomTkinter

* Modern appearance
* Dark mode support
* Easy to learn
* Cross-platform
* Better user experience
* Professional UI components

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* How modern GUI applications are created
* How CustomTkinter improves Tkinter
* How to create buttons, labels, and inputs
* How dark mode interfaces work
* Basics of desktop application development

---

# 🚀 Conclusion

CustomTkinter is one of the best Python libraries for building modern desktop applications.

It helps developers:

* Create beautiful interfaces
* Build professional software
* Improve user experience
* Design modern GUI applications

Learning CustomTkinter is useful for:

* Desktop Development
* GUI Programming
* Productivity Applications
* Management Systems
* Python Software Development

It is an excellent library for creating visually appealing desktop applications with Python.
