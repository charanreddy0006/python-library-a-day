from functools import reduce, lru_cache, partial

# --- reduce (apply function repeatedly) ---
numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", result)

# --- lru_cache (memoization for faster performance) ---
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci(10):", fibonacci(10))

# --- partial (fix some arguments) ---
def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print("\nDouble of 5:", double(5))