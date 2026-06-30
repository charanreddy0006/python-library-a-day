# Day 67 - Polars Library

# 📌 Overview

On Day 67, I explored Python's **Polars** library, a fast and efficient DataFrame library designed for modern data processing.

Polars is considered one of the best alternatives to Pandas for working with medium and large datasets.

Unlike Pandas, Polars is built using the Rust programming language, making it significantly faster and more memory-efficient.

It is widely used in:

* Data Engineering
* Data Analytics
* Machine Learning
* ETL Pipelines
* Big Data Processing

---

# 📦 Installation

Install Polars using pip:

```bash
pip install polars
```

---

# 🧠 Importing the Library

```python
import polars as pl
```

The alias `pl` is commonly used.

---

# 📊 What is a DataFrame?

A DataFrame is a table of data organized into rows and columns.

Example:

| Name    | Age | City      |
| ------- | --: | --------- |
| Alice   |  23 | Delhi     |
| Bob     |  30 | Mumbai    |
| Charlie |  27 | Hyderabad |

DataFrames make it easy to store, analyze, and manipulate structured data.

---

# 🚀 Creating a DataFrame

Example:

```python
df = pl.DataFrame(
    {
        "Name": ["Alice", "Bob"],
        "Age": [23, 30]
    }
)
```

Creates a new DataFrame.

---

# 👀 Viewing Data

Example:

```python
df.head()
```

Displays the first few rows.

---

# 📋 Viewing Columns

Example:

```python
df.columns
```

Returns all column names.

---

# 📈 Statistical Operations

Example:

```python
df["Age"].mean()
```

Calculates the average age.

Other useful functions include:

* `sum()`
* `max()`
* `min()`
* `median()`
* `std()`

---

# 🔍 Filtering Data

Example:

```python
df.filter(
    pl.col("Age") > 25
)
```

Returns only rows that satisfy the condition.

---

# ➕ Selecting Columns

Example:

```python
df.select(["Name", "Age"])
```

Returns only selected columns.

---

# 💾 Reading CSV Files

Example:

```python
df = pl.read_csv("cars.csv")
```

Loads a CSV file into a DataFrame.

---

# 📤 Saving CSV Files

Example:

```python
df.write_csv("output.csv")
```

Exports data to a CSV file.

---

# ⚡ Why Choose Polars?

Compared to Pandas, Polars offers:

* Faster execution
* Lower memory usage
* Better performance on large datasets
* Parallel processing
* Cleaner syntax for many operations

---

# 🚀 Real-World Uses

## Data Engineering

Process millions of records efficiently.

---

## ETL Pipelines

Extract, transform, and load data.

---

## Business Analytics

Analyze sales, customers, and financial reports.

---

## Machine Learning

Prepare datasets before model training.

---

## Big Data Processing

Handle large datasets with improved performance.

---

# ⚡ Advantages of Polars

* Extremely fast
* Memory efficient
* Easy to learn
* Supports CSV, Parquet, and JSON
* Excellent for modern analytics workflows

---

# 🆚 Polars vs Pandas

| Feature                   | Polars    | Pandas  |
| ------------------------- | --------- | ------- |
| Speed                     | ⭐⭐⭐⭐⭐     | ⭐⭐⭐     |
| Memory Usage              | Low       | Higher  |
| Parallel Processing       | ✅ Yes     | Limited |
| Beginner Friendly         | ✅ Yes     | ✅ Yes   |
| Large Dataset Performance | Excellent | Good    |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* What Polars is
* How DataFrames work
* How to create and filter data
* How to calculate statistics
* Why Polars is becoming popular in Data Engineering

---

# 🚀 Conclusion

Polars is one of the fastest modern DataFrame libraries in Python.

It helps developers:

* Process large datasets
* Perform analytics efficiently
* Build ETL pipelines
* Prepare data for machine learning

Learning Polars is valuable for:

* Data Engineering
* Data Analytics
* Machine Learning
* Big Data
* Python Development

As modern datasets continue to grow, Polars is becoming an important tool for high-performance data processing.
