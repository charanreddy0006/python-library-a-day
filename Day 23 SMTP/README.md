# Day 23 - SMTP Library

# 📌 Overview

On Day 23, I explored Python’s built-in **smtplib module**, which is used for sending emails using Python programs.

SMTP stands for:

```text id="jlwm72"
Simple Mail Transfer Protocol
```

It is the standard protocol used for sending emails over the internet.

The smtplib module allows Python applications to:

* send emails
* automate notifications
* send OTP messages
* generate automated reports
* build email-based systems

It is widely used in:

* authentication systems
* backend applications
* automation projects
* business software
* notification systems

---

# 📦 Importing the Library

```python id="jlwm73"
import smtplib
```

---

# 📧 What is SMTP?

SMTP stands for:

```text id="jlwm74"
Simple Mail Transfer Protocol
```

It is responsible for sending emails between servers.

When an email is sent:

1. Python connects to SMTP server
2. Login is verified
3. Email is transferred
4. Receiver gets the message

---

# 🧠 EmailMessage Class

Example:

```python id="jlwm75"
from email.message import EmailMessage
```

This helps create structured email messages.

---

# ✍️ Creating an Email

Example:

```python id="jlwm76"
msg = EmailMessage()
```

---

# 📨 Setting Email Details

Example:

```python id="jlwm77"
msg["Subject"] = "Python Email"
msg["From"] = sender
msg["To"] = receiver
```

This defines:

* subject
* sender
* receiver

---

# 📝 Adding Email Content

Example:

```python id="jlwm78"
msg.set_content("Hello from Python")
```

This sets the email body.

---

# 🔐 SMTP_SSL Connection

Example:

```python id="jlwm79"
smtplib.SMTP_SSL("smtp.gmail.com", 465)
```

Explanation:

* secure encrypted connection
* Gmail SMTP server
* port 465 used for SSL

---

# 🔑 Login Authentication

Example:

```python id="jlwm80"
smtp.login(sender, password)
```

This verifies email credentials.

---

# 📤 Sending Email

Example:

```python id="jlwm81"
smtp.send_message(msg)
```

This sends the email.

---

# ⚠️ Gmail App Password

For Gmail:

* normal password usually will not work
* App Password is required

Generate from:

* Google Account
* Security
* 2-Step Verification
* App Passwords

---

# 💻 Complete Example

```python id="jlwm82"
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg.set_content("Hello")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)
```

---

# 🚀 Real-World Uses

SMTP is used in:

* OTP verification systems
* password reset systems
* automated reporting
* email notifications
* marketing systems

---

# ⚡ Why SMTP is Important

Email automation is essential in:

* web applications
* backend systems
* business automation
* enterprise software

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how email systems work
* how Python sends emails
* SMTP basics
* email automation concepts

---

# 🚀 Conclusion

The smtplib module is a powerful Python library for email automation.

It helps developers:

* automate communication
* build notification systems
* integrate email functionality into applications

Learning SMTP is useful for:

* backend development
* automation
* web applications
* authentication systems
