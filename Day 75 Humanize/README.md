# Day 75 - Humanize Library

# 📌 Overview

On Day 75, I explored Python's **Humanize** library, a utility library that converts numbers, dates, times, and file sizes into formats that are easier for humans to read.

Instead of displaying raw technical values, Humanize transforms them into meaningful, user-friendly text.

It is widely used in:

- Dashboard Applications
- Reporting Tools
- File Managers
- Analytics Platforms
- Web Applications
- Desktop Applications

---

# 📦 Installation

Install Humanize using pip:

```bash
pip install humanize
```

---

# 🧠 Importing the Library

```python
import humanize
```

---

# 📖 Why Use Humanize?

Computers often display values in technical formats.

Example:

```text
1536000 bytes
```

Humanize converts it to:

```text
1.5 MB
```

This makes applications much easier for users to understand.

---

# 🔢 Formatting Large Numbers

Example:

```python
humanize.intcomma(123456789)
```

Output:

```text
123,456,789
```

Adds commas for better readability.

---

# 💾 Formatting File Sizes

Example:

```python
humanize.naturalsize(1536000)
```

Output:

```text
1.5 MB
```

Useful for displaying storage sizes.

---

# ⏰ Displaying Relative Time

Example:

```python
humanize.naturaltime(past)
```

Output:

```text
2 days ago
```

Instead of showing an exact timestamp, Humanize shows relative time.

---

# 🔢 Ordinal Numbers

Example:

```python
humanize.ordinal(21)
```

Output:

```text
21st
```

Useful for rankings and reports.

---

# 📈 Large Number Words

Example:

```python
humanize.intword(2500000)
```

Output:

```text
2.5 million
```

Converts very large numbers into readable words.

---

# 💻 Complete Example

```python
import humanize

print(humanize.intcomma(1000000))
print(humanize.naturalsize(5000000))
```

---

# 🚀 Real-World Uses

## Dashboard Applications

Display statistics clearly.

---

## File Managers

Show readable file sizes.

---

## Analytics Platforms

Format reports and metrics.

---

## Web Applications

Improve the user interface with readable values.

---

## Business Reports

Present large numbers in a simple format.

---

# ⚡ Advantages of Humanize

- Easy to use
- Lightweight
- Improves readability
- Supports numbers, dates, and sizes
- Perfect for dashboards and reports

---

# 🆚 Humanize vs Manual Formatting

| Feature | Humanize | Manual Code |
|----------|----------|-------------|
| File Size Formatting | ✅ | ❌ |
| Relative Time | ✅ | ❌ |
| Number Formatting | ✅ | ⚠️ |
| Easy to Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How to format large numbers
- How to display readable file sizes
- How to show relative time
- How to improve application readability
- Why Humanize is useful in dashboards and reports

---

# 🚀 Conclusion

Humanize is a lightweight but powerful library that makes application output more user-friendly.

It helps developers:

- Format numbers
- Display readable file sizes
- Show relative dates and times
- Improve user experience

Learning Humanize is useful for:

- Dashboard Development
- Web Applications
- Reporting Systems
- Analytics
- Python Development

Humanize is an excellent utility library that improves the readability and professionalism of Python applications.