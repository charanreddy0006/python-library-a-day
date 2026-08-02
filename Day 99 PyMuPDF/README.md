# 📄 Day 99 - PDF Analyzer using PyMuPDF

## 📌 Overview

On Day 99 of my **Python Library A Day** challenge, I explored the **PyMuPDF** library by building a **PDF Analyzer**.

This application reads PDF documents, extracts important metadata, counts the number of pages, extracts all text content, and saves the extracted text into a separate file.

PyMuPDF is widely recognized as one of the fastest Python libraries for PDF processing and is frequently used in document management systems, AI applications, and enterprise software.

---

# 🎯 Project Objective

The objective of this project is to understand how PDF files can be analyzed and processed programmatically.

The application allows users to:

- Open PDF files
- Display document metadata
- Count pages
- Extract text
- Save extracted text to a file

---

# 📂 Project Structure

```
Day 99 PyMuPDF/
│── pdf_analyzer.py
│── sample.pdf
│── extracted_text.txt
└── README.md
```

---

# ✨ Features

- 📄 Open PDF documents
- 📊 Display PDF metadata
- 📑 Count total pages
- 📝 Extract text from every page
- 💾 Save extracted text
- ⚡ High-performance PDF processing

---

# 📦 Installation

```bash
pip install pymupdf
```

---

# ▶️ Run

```bash
python pdf_analyzer.py
```

---

# 📖 Example

### Input

```
sample.pdf
```

### Output

```
Pages : 8

Title : Python Guide

Author : John Smith

Producer : Microsoft Word

Text extracted successfully.
```

---

# 🔄 Workflow

```
Start
   │
   ▼
Open PDF
   │
   ▼
Read Metadata
   │
   ▼
Count Pages
   │
   ▼
Extract Text
   │
   ▼
Save Text File
```

---

# 🌍 Real-World Applications

- Resume Parsing
- Document Search Engines
- AI Document Analysis
- Digital Libraries
- Legal Document Processing
- Invoice Processing
- OCR Workflows

---

# 📚 Concepts Covered

- PDF Processing
- Metadata Extraction
- File Handling
- Text Extraction
- Loops
- Python Libraries

---

# 🚀 Why PyMuPDF?

PyMuPDF is significantly faster than many PDF libraries and supports advanced document operations including annotations, images, metadata, and rendering pages.

---

# 🎯 Learning Outcome

After completing this project, you will understand:

- How PDF documents are structured
- How to extract metadata
- How to read text from PDFs
- How document processing works in Python

---

# 🏆 Conclusion

PyMuPDF is one of the most powerful libraries for PDF processing in Python. It enables developers to build document management systems, AI-powered document analyzers, search tools, and enterprise automation solutions with minimal code.

---

## 📌 Library Used

- **Library:** PyMuPDF (`fitz`)
- **Version:** Latest Stable Release

---

⭐ **Python Library A Day — Day 99**