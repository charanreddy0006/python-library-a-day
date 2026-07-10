# Day 76 - Cachetools Library

# 📌 Overview

On Day 76, I explored Python's **Cachetools** library, a powerful caching library used to improve application performance.

Caching stores the results of expensive operations so they can be reused instead of recalculated every time.

This reduces execution time and improves the efficiency of applications.

Cachetools is widely used in:

- Web Applications
- REST APIs
- Machine Learning
- Data Processing
- Backend Development
- Performance Optimization

---

# 📦 Installation

Install Cachetools using pip:

```bash
pip install cachetools
```

---

# 🧠 Importing the Library

```python
from cachetools import cached, TTLCache
```

---

# 📖 What is Caching?

Caching is the process of storing frequently used data temporarily so that future requests can be served faster.

Without Cache:

```text
Request
↓

Calculate Again
↓

Return Result
```

With Cache:

```text
Request
↓

Check Cache

↓

Return Stored Result
```

This reduces computation time.

---

# 🚀 Creating a Cache

Example:

```python
cache = TTLCache(
    maxsize=100,
    ttl=30
)
```

Parameters:

- **maxsize** → Maximum number of cached items
- **ttl** → Time To Live (in seconds)

After the TTL expires, cached data is automatically removed.

---

# 🎯 Caching a Function

Example:

```python
@cached(cache)
def square(number):
    return number * number
```

The first call computes the result.

Future calls with the same input return the cached result instantly.

---

# ⏱️ Time To Live (TTL)

TTL stands for **Time To Live**.

Example:

```python
TTLCache(
    maxsize=100,
    ttl=60
)
```

The cached value remains available for 60 seconds before expiring.

---

# 💻 Complete Example

```python
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=10, ttl=20)

@cached(cache)
def multiply(a, b):
    return a * b

print(multiply(5, 4))
```

---

# 🚀 Real-World Uses

## REST APIs

Store frequently requested responses.

---

## Database Applications

Cache database query results.

---

## Machine Learning

Store prediction results for repeated inputs.

---

## Web Applications

Reduce page loading time.

---

## Data Processing

Avoid repeating expensive calculations.

---

# ⚡ Advantages of Cachetools

- Easy to use
- Improves performance
- Supports TTL caching
- Multiple cache strategies
- Lightweight
- Pure Python

---

# 🆚 Cache vs No Cache

| Feature | Cache | No Cache |
|---------|--------|----------|
| Speed | Fast | Slower |
| Repeated Calculations | ❌ Avoided | ✅ Repeated |
| Resource Usage | Lower | Higher |
| Performance | Better | Normal |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What caching is
- How Cachetools stores results
- How TTL (Time To Live) works
- How cached functions improve performance
- Why caching is important in modern applications

---

# 🚀 Conclusion

Cachetools is a lightweight and efficient caching library that helps improve the performance of Python applications.

It enables developers to:

- Cache function results
- Reduce repeated calculations
- Improve application speed
- Optimize resource usage

Learning Cachetools is useful for:

- Backend Development
- REST APIs
- Machine Learning
- Data Processing
- Performance Optimization

Cachetools is an excellent library for building faster and more efficient Python applications.