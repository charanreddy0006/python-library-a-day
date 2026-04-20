Day 01 - NumPy
📌 About NumPy

NumPy (Numerical Python) is a library used for working with numbers in Python.
It helps us perform mathematical operations quickly and efficiently using arrays.

Instead of using normal Python lists, NumPy provides a special data structure called an array, which is faster and more powerful.

🚀 Why NumPy?
Faster than Python lists
Easy to perform mathematical operations
Useful for data science, machine learning, and scientific computing
Supports multi-dimensional arrays (like matrices)
📚 What I Learned
1. Creating Arrays
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a)

👉 Converts a Python list into a NumPy array.

2. Basic Operations
print("Mean:", a.mean())
print("Max:", a.max())
print("Min:", a.min())
print("Sum:", a.sum())

👉 NumPy can directly perform calculations on arrays without loops.

3. Standard Deviation
print("Standard Deviation:", a.std())

👉 Shows how spread out the values are.

4. 2D Arrays (Matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print("Shape:", matrix.shape)

👉 Used to represent rows and columns (like a table).

5. Array Operations
b = np.array([1, 2, 3, 4, 5])

print(a + b)
print(a * 2)

👉 Operations are applied to all elements at once.

💡 Real Example
prices = np.array([450000, 620000, 380000, 910000])

print("Average Price:", prices.mean())
print("Highest Price:", prices.max())
print("Lowest Price:", prices.min())

👉 Useful for analyzing real-world data like prices.

🎯 Summary
NumPy is used for fast numerical calculations
Arrays are faster than lists
No need for loops in most calculations
Supports both 1D and 2D data
✅ Conclusion

Today I learned the basics of NumPy and how it simplifies working with numbers and arrays in Python.
This will be very useful for future topics like data analysis and machine learning.

Done Day 01 ✅