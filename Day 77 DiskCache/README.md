# Day 77 - DiskCache Library

# 📌 Overview

On Day 77, I explored Python's **DiskCache** library, a high-performance caching library that stores cached data on disk.

Unlike traditional in-memory caching, DiskCache saves cached objects in a local directory, allowing data to remain available even after the application is closed.

DiskCache combines the speed of caching with the persistence of file storage.

It is widely used in:

- Web Applications
- REST APIs
- Machine Learning
- Automation Scripts
- Desktop Applications
- Data Processing

---

# 📦 Installation

Install DiskCache using pip:

```bash
pip install diskcache
```

---

# 🧠 Importing the Library

```python
from diskcache import Cache
```

---

# 📖 What is Disk Caching?

Disk caching stores frequently accessed data on the computer's storage instead of RAM.

Unlike memory caches, the stored data is preserved even after the program terminates.

Benefits include:

- Faster repeated access
- Persistent storage
- Reduced computation time
- Improved application performance

---

# 🚀 Creating a Cache

Example:

```python
cache = Cache("cache")
```

This creates a folder named **cache** where cached data is stored.

---

# 💾 Storing Data

Example:

```python
cache["username"] = "Alice"
```

Stores a value using a key.

---

# 📥 Retrieving Data

Example:

```python
print(cache["username"])
```

Returns the stored value.

---

# 🔍 Checking if a Key Exists

Example:

```python
if "username" in cache:
    print("Found")
```

Checks whether a key is present.

---

# ❌ Deleting Data

Example:

```python
del cache["username"]
```

Removes the specified key from the cache.

---

# 🔑 Viewing All Keys

Example:

```python
list(cache.iterkeys())
```

Returns all stored keys.

---

# 🔒 Closing the Cache

Example:

```python
cache.close()
```

Closes the cache safely after use.

---

# 💻 Complete Example

```python
from diskcache import Cache

cache = Cache("cache")

cache["language"] = "Python"

print(cache["language"])

cache.close()
```

---

# 🚀 Real-World Uses

## REST APIs

Cache API responses to reduce server load.

---

## Machine Learning

Store prediction results for repeated inputs.

---

## Data Science

Cache processed datasets to avoid recalculating results.

---

## Desktop Applications

Save user settings and preferences.

---

## Automation Scripts

Store intermediate results between script executions.

---

# ⚡ Advantages of DiskCache

- Persistent storage
- Fast data retrieval
- Easy to use
- Lightweight
- Works with large objects
- Pure Python

---

# 🆚 DiskCache vs Cachetools

| Feature | DiskCache | Cachetools |
|---------|-----------|------------|
| Stores on Disk | ✅ | ❌ |
| Persistent | ✅ | ❌ |
| In-Memory Speed | ⚠️ Slightly Slower | ✅ |
| Suitable for Large Data | ✅ | ⚠️ Limited |
| Automatic Persistence | ✅ | ❌ |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- What persistent caching is
- How DiskCache stores data
- How to save and retrieve cached values
- How to manage cache keys
- Why persistent caching improves application performance

---

# 🚀 Conclusion

DiskCache is a powerful caching library that stores data persistently on disk, allowing applications to reuse previously computed results across multiple executions.

It helps developers:

- Improve application performance
- Reduce repeated computations
- Store temporary data efficiently
- Build faster and more responsive applications

Learning DiskCache is useful for:

- Backend Development
- Machine Learning
- Data Science
- Automation
- Desktop Applications

DiskCache is an excellent library for applications that require fast and persistent caching.