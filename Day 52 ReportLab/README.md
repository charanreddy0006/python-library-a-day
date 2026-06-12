# Day 52 - ReportLab Library

# 📌 Overview

On Day 52, I explored Python's powerful **ReportLab library**, which is used for generating PDF documents programmatically.

ReportLab allows developers to create professional PDF files directly from Python code.

The library can:

- Create PDF documents
- Add text
- Insert images
- Draw shapes
- Generate invoices
- Build reports

It is widely used in:

- Billing Systems
- Certificate Generators
- Business Applications
- Reporting Systems
- Document Automation

---

# 📦 Installation

Install ReportLab using pip:

```bash
pip install reportlab
```

---

# 🧠 Importing the Library

```python
from reportlab.pdfgen import canvas
```

---

# 📄 What is ReportLab?

ReportLab is a Python library used for creating PDF files.

Instead of manually designing PDFs, Python can generate them automatically.

Example:

- Invoices
- Certificates
- Reports
- Receipts

---

# 🚀 Creating a PDF

Example:

```python
pdf = canvas.Canvas("sample.pdf")
```

This creates a new PDF document.

---

# ✍️ Writing Text

Example:

```python
pdf.drawString(
    100,
    750,
    "Hello Python"
)
```

Parameters:

- X Position
- Y Position
- Text Content

---

# 💾 Saving PDF

Example:

```python
pdf.save()
```

This writes the PDF file to disk.

---

# 📍 Understanding Coordinates

PDF pages use coordinates.

Example:

```python
pdf.drawString(
    100,
    700,
    "Python"
)
```

- 100 → Horizontal Position
- 700 → Vertical Position

---

# 💻 Complete Example

```python
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(
    "demo.pdf"
)

pdf.drawString(
    100,
    750,
    "Welcome"
)

pdf.save()
```

---

# 🚀 Real-World Uses

## Invoice Generation

Automatically create customer invoices.

---

## Certificate Systems

Generate certificates dynamically.

---

## Student Reports

Create mark sheets and reports.

---

## Business Reports

Export analytics into PDF format.

---

## Receipt Generation

Create payment receipts automatically.

---

# ⚡ Advantages of ReportLab

- Professional PDFs
- Easy automation
- Fast generation
- Supports images
- Supports graphics

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How PDF generation works
- How Python creates documents
- How to write text inside PDFs
- How coordinate systems work
- How document automation is performed

---

# 🚀 Conclusion

The ReportLab library is one of the most powerful PDF-generation libraries in Python.

It helps developers:

- Create PDF documents
- Automate reporting
- Generate invoices
- Build certificate systems

Learning ReportLab is useful for:

- Business Applications
- Automation
- Reporting Systems
- Billing Software
- Document Management

It is one of the most practical libraries for generating professional documents with Python.