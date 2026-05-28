# Day 37 - Plyer Library

# 📌 Overview

On Day 37, I explored Python’s useful **plyer library**, which is used for accessing platform-independent features such as desktop notifications.

The plyer library allows Python applications to:

* show desktop notifications
* send reminders
* create alerts
* interact with system features

It is widely used in:

* reminder applications
* productivity tools
* automation systems
* desktop utilities
* monitoring applications

---

# 📦 Installing Plyer

Install using pip:

```bash id="pl371d"
pip install plyer
```

---

# 🧠 Importing the Library

```python id="pl371e"
from plyer import notification
```

---

# 🔔 What is a Desktop Notification?

A desktop notification is a popup message displayed by the operating system.

Examples:

* WhatsApp notifications
* email alerts
* calendar reminders
* software updates

---

# ⚡ Creating a Notification

Example:

```python id="pl371f"
notification.notify()
```

This displays a desktop notification.

---

# 📝 Notification Title

Example:

```python id="pl371g"
title="Python Notification"
```

This defines the notification heading.

---

# 💬 Notification Message

Example:

```python id="pl371h"
message="Hello from Python"
```

This sets the notification content.

---

# ⏳ Notification Timeout

Example:

```python id="pl371i"
timeout=10
```

This controls how long the notification stays visible.

---

# 💻 Complete Example

```python id="pl371j"
from plyer import notification

notification.notify(
    title="Reminder",
    message="Drink Water"
)
```

---

# 🚀 Real-World Uses

Plyer is used in:

* reminder applications
* task managers
* monitoring systems
* productivity tools
* automation scripts

---

# ⚡ Why Notifications are Important

Notifications help:

* alert users instantly
* improve productivity
* automate reminders
* track important events

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how desktop notifications work
* how Python interacts with system notifications
* basics of alert systems
* notification automation techniques

---

# 🚀 Conclusion

The plyer library is a simple yet powerful tool for desktop notifications in Python.

It helps developers:

* build reminder systems
* create notification-based applications
* improve user interaction

Learning plyer is useful for:

* desktop applications
* automation
* productivity tools
* monitoring systems
