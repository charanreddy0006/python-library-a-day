# Day 50 - Pendulum Library

# 📌 Overview

On Day 50, I explored Python's modern **Pendulum library**, which is used for working with dates, times, durations, and time zones.

Pendulum is considered a better alternative to Python's built-in datetime module because it provides:

- Simpler syntax
- Better timezone support
- Human-readable dates
- Easier date calculations

It is widely used in:

- Backend Applications
- Scheduling Systems
- Analytics Platforms
- Automation Scripts
- Time-Based Applications

---

# 📦 Installation

Install Pendulum using pip:

```bash
pip install pendulum
```

---

# 🧠 Importing Pendulum

```python
import pendulum
```

---

# ⏰ Getting Current Date and Time

Example:

```python
now = pendulum.now()
```

Returns:

```text
2025-08-10 12:30:45
```

(Current system date and time)

---

# 📅 Getting Date Only

Example:

```python
now.to_date_string()
```

Output:

```text
2025-08-10
```

---

# 🕒 Getting Time Only

Example:

```python
now.to_time_string()
```

Output:

```text
12:30:45
```

---

# ➕ Adding Time

Example:

```python
future = now.add(days=10)
```

Adds 10 days to the current date.

---

# ➖ Subtracting Time

Example:

```python
past = now.subtract(days=5)
```

Subtracts 5 days.

---

# 🌍 Working with Time Zones

Example:

```python
pendulum.now("Asia/Kolkata")
```

Returns current Indian time.

Example:

```python
pendulum.now("America/New_York")
```

Returns current New York time.

---

# 📊 Date Difference

Example:

```python
date1.diff(date2)
```

Used for:

- Countdown timers
- Event tracking
- Scheduling systems

---

# 💬 Human Readable Dates

Example:

```python
future.diff_for_humans()
```

Output:

```text
in 10 days
```

This feature makes Pendulum very user-friendly.

---

# 💻 Complete Example

```python
import pendulum

today = pendulum.now()

print(today.to_date_string())
```

---

# 🚀 Real-World Uses

## Scheduling Systems

Manage appointments and events.

---

## Analytics Dashboards

Track daily and monthly data.

---

## Automation Scripts

Run tasks based on time.

---

## Attendance Systems

Calculate working hours.

---

## Backend Development

Handle timestamps and user activity.

---

# ⚡ Advantages of Pendulum

- Easy to learn
- Modern syntax
- Timezone support
- Human-readable dates
- Powerful date calculations

---

# 🎯 Learning Outcome

After completing this topic, I learned:

- How modern date libraries work
- How to handle time zones
- How to calculate date differences
- How to create human-friendly dates
- How scheduling systems manage time

---

# 🚀 Conclusion

The Pendulum library is one of the best Python libraries for handling dates and times.

It helps developers:

- Manage time efficiently
- Handle multiple time zones
- Build scheduling systems
- Perform date calculations easily

Learning Pendulum is useful for:

- Backend Development
- Automation
- Analytics
- Scheduling Applications
- Real-World Projects

It is a modern and powerful alternative to Python's built-in datetime module.