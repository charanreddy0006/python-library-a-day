import math

# --- basic functions ---
print("Square root of 25:", math.sqrt(25))
print("Power (2^3):", math.pow(2, 3))

# --- rounding ---
print("Ceil of 4.3:", math.ceil(4.3))
print("Floor of 4.7:", math.floor(4.7))

# --- constants ---
print("Value of Pi:", math.pi)
print("Value of e:", math.e)

# --- factorial ---
print("Factorial of 5:", math.factorial(5))

# --- absolute value ---
print("Absolute value of -10:", abs(-10))

# --- trigonometry ---
print("sin(90°):", math.sin(math.radians(90)))
print("cos(0°):", math.cos(math.radians(0)))

# --- logarithm ---
print("log(10):", math.log(10))
print("log10(100):", math.log10(100))

# --- mini example: area of circle ---
radius = 7
area = math.pi * radius * radius
print("\nArea of circle:", area)