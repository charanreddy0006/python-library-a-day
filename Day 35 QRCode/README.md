# Day 35 - QRCode Library

# 📌 Overview

On Day 35, I explored Python’s powerful **qrcode library**, which is used for generating QR codes.

QR codes are machine-readable codes that store information such as:

* URLs
* text
* contact details
* payment information
* authentication tokens

The qrcode library allows Python programs to:

* generate QR codes
* save QR images
* encode website links
* build sharing systems

It is widely used in:

* payment applications
* ticket booking systems
* authentication systems
* digital business cards
* product tracking systems

---

# 📦 Installing QRCode Library

Install using pip:

```bash id="qr351d"
pip install qrcode[pil]
```

---

# 🧠 Importing the Library

```python id="qr351e"
import qrcode
```

---

# 📱 What is a QR Code?

QR stands for:

```text id="qr351f"
Quick Response
```

A QR code stores information that can be scanned using:

* smartphones
* scanners
* cameras

Examples:

* website URLs
* payment links
* WiFi passwords

---

# ⚡ Creating a QR Code

Example:

```python id="qr351g"
qrcode.make(data)
```

This generates a QR image.

---

# 💾 Saving QR Code

Example:

```python id="qr351h"
qr.save("image.png")
```

This saves the generated QR code.

---

# 🌐 Encoding URLs

Example:

```python id="qr351i"
data = "https://github.com"
```

The QR code opens the website when scanned.

---

# 💻 Complete Example

```python id="qr351j"
import qrcode

img = qrcode.make("Python")

img.save("python_qr.png")
```

---

# 🚀 Real-World Uses

QRCode systems are used in:

* UPI payments
* ticket booking systems
* login authentication
* digital menus
* inventory tracking

---

# ⚡ Why QR Codes are Important

QR codes help:

* share information quickly
* reduce manual typing
* improve digital access
* enable contactless systems

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how QR codes work
* how Python generates QR images
* basics of QR encoding
* image generation techniques

---

# 🚀 Conclusion

The qrcode library is a simple yet powerful Python library for QR code generation.

It helps developers:

* automate QR creation
* build sharing systems
* integrate QR functionality into applications

Learning qrcode is useful for:

* automation
* payment systems
* authentication systems
* digital applications
