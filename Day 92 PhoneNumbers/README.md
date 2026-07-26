# 📱 Day 92 - International Phone Number Validator using PhoneNumbers

## 📌 Overview

On Day 92 of my **Python Library A Day** challenge, I explored the **PhoneNumbers** library by building an **International Phone Number Validator**.

This application validates international phone numbers, identifies their country, telecom carrier, timezone, and displays the number in international format.

The project demonstrates how Google's **libphonenumber** library can be used in Python applications for reliable phone number validation.

---

## 🎯 Project Objective

The objective of this project is to learn how to validate and analyze international phone numbers using Python.

The application can:

- Validate phone numbers
- Check if a number is possible
- Detect the country or region
- Identify the mobile carrier
- Display timezone information
- Format phone numbers internationally

---

## 📂 Project Structure

```
Day 92 PhoneNumbers/
│── phone_validator.py
└── README.md
```

---

## ✨ Features

- 📱 Validate international phone numbers
- 🌍 Detect country/region
- 📡 Display telecom carrier
- 🕒 Identify timezone
- 🌐 Format phone numbers
- ❌ Handle invalid phone numbers gracefully

---

## 📦 Installation

Install the required library:

```bash
pip install phonenumbers
```

---

## ▶️ Run the Project

```bash
python phone_validator.py
```

---

## 📖 Example

### Input

```
+919876543210
```

### Output

```
Phone Details

Valid Number : True
Possible Number : True
Country : India
Carrier : Airtel
Timezone : Asia/Kolkata
International Format : +91 98765 43210
```

---

## 🔄 Workflow

```
Start
   │
   ▼
Enter Phone Number
   │
   ▼
Parse Number
   │
   ▼
Validate Number
   │
   ▼
Extract Country
   │
   ▼
Extract Carrier
   │
   ▼
Extract Timezone
   │
   ▼
Display Information
```

---

## 🌍 Real-World Applications

- User Registration Systems
- Banking Applications
- CRM Software
- Contact Management Systems
- E-commerce Platforms
- Mobile Applications
- Customer Verification Systems

---

## 📚 Concepts Covered

- Phone Number Validation
- International Number Formatting
- Country Detection
- Carrier Identification
- Timezone Detection
- Exception Handling
- Python Modules

---

## 🚀 Why PhoneNumbers?

The **PhoneNumbers** library is Google's official Python port of **libphonenumber**, one of the most trusted libraries for parsing and validating phone numbers worldwide. It supports hundreds of countries and ensures accurate validation according to international standards.

---

## 🎯 Learning Outcome

After completing this project, you will understand:

- How international phone numbers are structured
- How to validate phone numbers
- How to detect country and carrier information
- How to format phone numbers correctly
- How phone validation is implemented in real-world applications

---

## 🏆 Conclusion

The **PhoneNumbers** library provides a reliable and efficient way to validate and process international phone numbers. It is widely used in modern applications to improve data accuracy and user experience.

---

## 📌 Library Used

- **Library:** PhoneNumbers
- **Version:** Latest Stable Release

---

⭐ **Python Library A Day — Day 92**