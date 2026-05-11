# Day 21 - CSV Module

# 📌 Overview

On Day 21, I explored Python’s built-in **csv module**, which is used for reading and writing CSV (Comma Separated Values) files.

CSV files are one of the most commonly used formats for storing and exchanging tabular data.

The csv module helps Python programs:

* create CSV files
* read spreadsheet-like data
* process datasets
* automate data storage

It is widely used in:

* data analysis
* machine learning
* Excel data export
* report generation
* backend systems

---

# 📦 Importing the CSV Module

```python id="jlwm31"
import csv
```

---

# 📄 What is a CSV File?

CSV stands for:

```text id="jlwm42"
Comma Separated Values
```

A CSV file stores data in table format.

Example:

```text id="jlwm53"
Name,Marks
Chakri,95
Rahul,88
```

Each line represents a row.

---

# ✍️ Writing Data to CSV

Example:

```python id="jlwm64"
writer = csv.writer(file)
```

This creates a CSV writer object.

---

# 🧾 Writing Rows

Example:

```python id="jlwm75"
writer.writerow(["Name", "Marks"])
```

This writes a row into the CSV file.

---

# 💾 Creating a CSV File

Example:

```python id="jlwm86"
with open("students.csv", mode="w") as file:
```

Explanation:

* `"w"` → write mode
* creates a new file

---

# 📖 Reading CSV Files

Example:

```python id="jlwm97"
reader = csv.reader(file)
```

This reads CSV data row by row.

---

# 🔍 Reading Rows

Example:

```python id="jlwm18"
for row in reader:
    print(row)
```

Output:

```text id="jlwm29"
['Name', 'Marks']
['Chakri', '95']
```

---

# 💻 Complete Example

```python id="jlwm30"
import csv

with open("demo.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Python", "Library"])
```

---

# 🚀 Real-World Uses

CSV files are widely used in:

* machine learning datasets
* Excel exports
* analytics systems
* attendance management
* report automation

---

# ⚡ Why CSV is Popular

CSV files are:

* lightweight
* simple
* easy to process
* supported by Excel and databases

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how CSV files work
* how Python reads and writes CSV data
* basics of tabular data storage
* dataset handling fundamentals

---

# 🚀 Conclusion

The csv module is an essential Python module for working with structured tabular data.

It helps developers:

* process datasets
* automate spreadsheet tasks
* exchange data between applications

Learning the csv module is important for:

* data science
* machine learning
* backend development
* automation projects
