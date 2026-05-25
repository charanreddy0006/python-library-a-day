# Day 34 - Tkinter Library

# 📌 Overview

On Day 34, I explored Python’s built-in **tkinter library**, which is used for creating Graphical User Interface (GUI) applications.

Tkinter allows Python developers to build desktop applications with:

* windows
* buttons
* labels
* text fields
* forms
* interactive elements

It is one of the easiest GUI libraries for beginners in Python.

Tkinter is widely used in:

* calculator applications
* desktop utilities
* form systems
* educational software
* automation tools

---

# 📦 Importing Tkinter

```python id="tk341c"
import tkinter as tk
```

---

# 🖥️ Creating a Window

Example:

```python id="tk341d"
window = tk.Tk()
```

This creates the main application window.

---

# 🏷️ Setting Window Title

Example:

```python id="tk341e"
window.title("My App")
```

This sets the application title.

---

# 📏 Setting Window Size

Example:

```python id="tk341f"
window.geometry("400x250")
```

This defines:

* width
* height

---

# 📝 Labels

Example:

```python id="tk341g"
tk.Label(window, text="Hello")
```

Labels display text inside the GUI.

---

# 🔘 Buttons

Example:

```python id="tk341h"
tk.Button(window, text="Click")
```

Buttons trigger actions when clicked.

---

# ⚡ Button Commands

Example:

```python id="tk341i"
command=button_click
```

This connects a function to the button.

---

# 🔄 Main Event Loop

Example:

```python id="tk341j"
window.mainloop()
```

This keeps the application running and responsive.

---

# 💻 Complete Example

```python id="tk341k"
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Python GUI")

label.pack()

window.mainloop()
```

---

# 🚀 Real-World Uses

Tkinter is used in:

* desktop applications
* calculators
* attendance systems
* file management tools
* automation software

---

# ⚡ Why Tkinter is Important

Tkinter helps developers:

* build visual applications
* create interactive tools
* understand GUI programming

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how GUI applications work
* how Python creates windows and buttons
* basics of event-driven programming
* user interaction handling

---

# 🚀 Conclusion

The tkinter library is one of the best beginner-friendly GUI libraries in Python.

It helps developers:

* create desktop applications
* build interactive software
* design graphical interfaces

Learning tkinter is useful for:

* desktop development
* automation tools
* beginner software projects
* GUI application design
