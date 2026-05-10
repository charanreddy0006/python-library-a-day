# Day 20 - OpenPyXL Library

# 📌 Overview

On Day 20, I explored Python’s powerful **OpenPyXL library**, which is used for working with Excel files (.xlsx).

OpenPyXL allows Python programs to:

* create Excel files
* read spreadsheet data
* update existing files
* automate Excel tasks

It is widely used in:

* business reporting
* data analysis
* office automation
* report generation
* analytics systems

---

# 📦 Installing OpenPyXL

Install using pip:

```bash id="jlwm90"
pip install openpyxl
```

---

# 🧠 Importing the Library

```python id="jlwm29"
from openpyxl import Workbook, load_workbook
```

---

# 📗 What is a Workbook?

A workbook represents an Excel file.

Example:

```python id="jlwm73"
workbook = Workbook()
```

This creates a new Excel workbook.

---

# 📄 What is a Worksheet?

A worksheet represents a sheet inside an Excel file.

Example:

```python id="jlwm88"
sheet = workbook.active
```

---

# ✍️ Writing Data to Excel

Example:

```python id="jlwm12"
sheet["A1"] = "Name"
sheet["B1"] = "Marks"
```

This writes data into Excel cells.

---

# 💾 Saving Excel Files

Example:

```python id="jlwm61"
workbook.save("students.xlsx")
```

This creates the Excel file.

---

# 📖 Loading Existing Excel Files

Example:

```python id="jlwm84"
load_workbook("students.xlsx")
```

Used for:

* editing files
* reading data
* updating spreadsheets

---

# 🔍 Reading Data from Excel

Example:

```python id="jlwm44"
for row in sheet.iter_rows(values_only=True):
    print(row)
```

This reads row-by-row data.

---

# 💻 Complete Example

```python id="jlwm55"
from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

sheet["A1"] = "Python"

workbook.save("demo.xlsx")
```

---

# 🚀 Real-World Uses

OpenPyXL is used in:

* report automation
* attendance systems
* analytics dashboards
* invoice generation
* employee management systems

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how Excel automation works
* how Python interacts with spreadsheets
* how to create and read Excel files
* basics of report automation

---

# 🚀 Conclusion

OpenPyXL is a powerful Python library for Excel automation.

It helps developers:

* automate repetitive Excel tasks
* generate reports
* manage spreadsheet data efficiently

Learning OpenPyXL is useful for:

* automation
* data analysis
* backend development
* business applications
