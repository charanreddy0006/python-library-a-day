# Day 25 - PyPDF2 Library

# 📌 Overview

On Day 25, I explored Python’s powerful **PyPDF2 library**, which is used for reading, editing, and manipulating PDF files.

PDF is one of the most commonly used document formats in the world.

The PyPDF2 library allows Python programs to:

* read PDF files
* extract text
* merge documents
* split pages
* rotate pages
* create new PDFs

It is widely used in:

* document automation
* business applications
* report generation
* resume processing
* PDF management systems

---

# 📦 Installing PyPDF2

Install using pip:

```bash id="’wini98"
pip install PyPDF2
```

---

# 🧠 Importing the Library

```python id="’wini99"
from PyPDF2 import PdfReader, PdfWriter
```

---

# 📄 Reading a PDF File

Example:

```python id="’wini11"
reader = PdfReader("sample.pdf")
```

This loads the PDF file into Python.

---

# 📑 Accessing PDF Pages

Example:

```python id="’wini12"
reader.pages[0]
```

This accesses the first page.

---

# 📊 Counting Total Pages

Example:

```python id="’wini13"
len(reader.pages)
```

Used for:

* document analysis
* page navigation

---

# 🔍 Extracting Text from PDF

Example:

```python id="’wini14"
text = page.extract_text()
```

This extracts readable text from the page.

---

# ✍️ Creating a New PDF

Example:

```python id="’wini15"
writer = PdfWriter()
```

Used for:

* creating PDFs
* copying pages
* merging documents

---

# ➕ Adding Pages

Example:

```python id="’wini16"
writer.add_page(page)
```

This adds a page into the new PDF.

---

# 💾 Saving PDF Files

Example:

```python id="’wini17"
writer.write(file)
```

This writes the PDF to disk.

---

# 💻 Complete Example

```python id="’wini18"
from PyPDF2 import PdfReader

reader = PdfReader("demo.pdf")

print(len(reader.pages))
```

---

# 🚀 Real-World Uses

PyPDF2 is used in:

* resume parsers
* invoice systems
* report automation
* legal document processing
* PDF editors

---

# ⚡ Why PDF Processing is Important

PDF automation helps:

* reduce manual work
* automate reports
* manage large documents efficiently

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how Python reads PDF files
* how text extraction works
* basics of PDF automation
* PDF page management

---

# 🚀 Conclusion

The PyPDF2 library is a powerful tool for PDF document processing.

It helps developers:

* automate document workflows
* manage PDFs programmatically
* build document management systems

Learning PyPDF2 is useful for:

* automation
* backend development
* business applications
* document processing systems
