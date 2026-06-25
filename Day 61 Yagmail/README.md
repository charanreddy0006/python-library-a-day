# Day 61 - Yagmail Library

# 📌 Overview

On Day 61, I explored Python's **Yagmail library**, which provides a simple and user-friendly way to send emails directly from Python.

Yagmail is built on top of Python's built-in `smtplib` module, making email sending much easier with fewer lines of code.

Using Yagmail, developers can:

* Send emails
* Send HTML emails
* Attach files
* Automate notifications
* Deliver reports

It is widely used in:

* Automation Scripts
* Report Generation
* Monitoring Systems
* Business Applications
* Notification Services

---

# 📦 Installation

Install Yagmail using pip:

```bash
pip install yagmail
```

---

# 🧠 Importing the Library

```python
import yagmail
```

---

# 📧 What is Yagmail?

Yagmail is a Python library that simplifies sending emails through Gmail.

Instead of writing complex SMTP code, you can send emails with just a few lines.

---

# 🔑 Connecting to Gmail

Example:

```python
yag = yagmail.SMTP(
    user="your_email@gmail.com",
    password="your_app_password"
)
```

Use a **Google App Password** for better security instead of your normal Gmail password.

---

# ✉️ Sending an Email

Example:

```python
yag.send(
    to="friend@gmail.com",
    subject="Hello",
    contents="This email was sent using Python."
)
```

This sends a simple text email.

---

# 📎 Sending Attachments

Example:

```python
yag.send(
    to="friend@gmail.com",
    subject="Report",
    contents="Please find the report attached.",
    attachments="report.pdf"
)
```

You can attach:

* PDF files
* Images
* Excel files
* Word documents
* ZIP files

---

# 🌐 Sending HTML Emails

Example:

```python
html = "<h1>Hello!</h1><p>This is an HTML email.</p>"

yag.send(
    to="friend@gmail.com",
    subject="HTML Email",
    contents=html
)
```

HTML emails support:

* Colors
* Headings
* Images
* Links

---

# 💻 Complete Example

```python
import yagmail

yag = yagmail.SMTP(
    "your_email@gmail.com",
    "your_app_password"
)

yag.send(
    to="receiver@gmail.com",
    subject="Test Email",
    contents="Hello from Python!"
)
```

---

# 🚀 Real-World Uses

## Daily Report Automation

Automatically send reports every day.

---

## Notification Systems

Notify users when important events occur.

---

## Attendance Systems

Email attendance reports to teachers.

---

## Backup Systems

Send backup confirmation emails.

---

## Business Applications

Deliver invoices and receipts.

---

# ⚡ Advantages of Yagmail

* Easy to use
* Supports attachments
* HTML email support
* Cleaner than smtplib
* Great for automation

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* How Python sends emails
* How to connect to Gmail
* How to send attachments
* How automated email systems work
* Basics of email automation

---

# 🚀 Conclusion

The Yagmail library makes email automation simple and efficient.

It helps developers:

* Send emails programmatically
* Automate notifications
* Deliver reports
* Build communication features

Learning Yagmail is useful for:

* Automation Projects
* Business Applications
* Monitoring Systems
* Reporting Tools
* Python Development

It is an excellent library for adding email functionality to Python applications.
