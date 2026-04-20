import numpy as np

# --- arrays ---
a = np.array([10, 20, 30, 40, 50])
print("Array     :", a)
print("Mean      :", a.mean())
print("Max       :", a.max())
print("Min       :", a.min())
print("Std Dev   :", a.std())

# --- 2D array ---
matrix = np.array([[1, 2], [3, 4]])
print("Shape     :", matrix.shape)

# --- car price example ---
prices = np.array([450000, 620000, 380000, 910000])
print("Avg Price :", prices.mean())

# --- no loop math ---
kms = np.array([12000, 45000, 78000])
print("Miles     :", kms * 0.621)

# --- random ---
np.random.seed(42)
print("Random    :", np.random.randint(1, 100, size=5))