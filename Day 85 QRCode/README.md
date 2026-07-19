# 📱 Day 85 - QR Code Generator using QRCode

## 📌 Overview

On Day 85 of my **Python Library A Day** challenge, I explored the **QRCode** library by building a **QR Code Generator**.

This project allows users to convert any text or URL into a QR code image, which can be scanned using smartphones or QR scanners.

---

# 🚀 Project Objective

The objective of this project is to generate QR codes from user input and save them as image files.

The application allows users to:

- Enter text or a website URL
- Generate a QR code
- Save the QR code as a PNG image

---

# 📂 Project Structure

```
Day 85 QRCode/
│── qr_generator.py
│── my_qrcode.png
└── README.md
```

---

# ✨ Features

- Generate QR codes from text or URLs
- Save QR codes as PNG images
- User-defined output file names
- Simple command-line interface
- Lightweight and beginner-friendly

---

# 📦 Installation

```bash
pip install qrcode[pil]
```

---

# ▶️ Run

```bash
python qr_generator.py
```

---

# 🔄 Workflow

```
User Input
     │
     ▼
Enter Text / URL
     │
     ▼
Generate QR Code
     │
     ▼
Save as PNG Image
     │
     ▼
Ready to Scan
```

---

# 💻 Example

### Input

```
https://github.com/charanreddy0006
```

### Output

```
github_profile.png
```

The generated image can be scanned by any QR code scanner.

---

# 🌍 Real-World Applications

- Business Cards
- Restaurant Menus
- Digital Payments (UPI)
- Website Sharing
- Event Tickets
- Product Labels
- Wi-Fi Sharing

---

# 📚 Concepts Covered

- QR Code Generation
- User Input
- Image File Creation
- Functions
- File Handling

---

# ⭐ Why Use QRCode?

QRCode makes it easy to generate scannable QR codes with just a few lines of Python code. It is reliable, lightweight, and widely used in modern applications.

---

# 🎯 Learning Outcome

After completing this project, I learned:

- How QR codes are generated
- How to use the QRCode library
- How to save generated images
- How QR codes are used in real-world applications

---

# 🏆 Conclusion

The QRCode library is an excellent choice for creating QR codes in Python. This project demonstrates a practical application that can be integrated into websites, payment systems, inventory tools, and many other software solutions.