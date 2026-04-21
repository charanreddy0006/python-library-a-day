# Day 02 - Pandas Basics

## 📌 Overview

On Day 02, I explored **Pandas**, a powerful Python library used for data analysis and data manipulation.

Pandas is built on top of NumPy and provides easy-to-use data structures like **Series** and **DataFrame**.

---

## 🧠 Topics Covered

* Creating Series
* Creating DataFrames
* Viewing data (head, tail)
* Selecting columns and rows
* Filtering data
* Adding new columns
* Basic statistics (mean, max)
* Exporting data to CSV

---

## 💻 Code Explanation

### 1. Series

A one-dimensional labeled array.

```python
pd.Series([10, 20, 30])
```

### 2. DataFrame

A table-like structure with rows and columns.

```python
pd.DataFrame(data_dict)
```

### 3. Data Selection

* Column: `df["Price"]`
* Row: `df.loc[1]`

### 4. Filtering

```python
df[df["Price"] > 600000]
```

### 5. Adding Columns

```python
df["New"] = df["Price"] / 100000
```

---

## 🚀 Learning Outcome

* Understood how to work with tabular data
* Learned basic data manipulation techniques
* Gained foundation for data analysis and machine learning

---

## 📁 Output File

The script generates:

* `cars_data.csv` → Stored dataset

---

## 🎯 Next Plan

Tomorrow I will explore another Python library to continue building consistency 🚀
