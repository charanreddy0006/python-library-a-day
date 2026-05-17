# Day 26 - Psutil Library

# 📌 Overview

On Day 26, I explored Python’s powerful **psutil library**, which is used for system monitoring and process management.

The psutil library allows Python programs to retrieve information about:

* CPU usage
* RAM usage
* disk usage
* battery information
* running processes
* system performance

It is widely used in:

* system monitoring tools
* task manager applications
* DevOps systems
* server monitoring
* automation scripts

---

# 📦 Installing Psutil

Install using pip:

```bash id="ps261d"
pip install psutil
```

---

# 🧠 Importing the Library

```python id="ps261e"
import psutil
```

---

# 🖥️ CPU Monitoring

Example:

```python id="ps261f"
psutil.cpu_percent()
```

This returns CPU usage percentage.

---

# 💾 RAM Information

Example:

```python id="ps261g"
psutil.virtual_memory()
```

This provides:

* total RAM
* used RAM
* available memory
* usage percentage

---

# 💽 Disk Usage

Example:

```python id="ps261h"
psutil.disk_usage('/')
```

This returns:

* total storage
* used storage
* free space

---

# 🔋 Battery Information

Example:

```python id="ps261i"
psutil.sensors_battery()
```

This gives:

* battery percentage
* charging status

---

# ⚙️ Running Processes

Example:

```python id="ps261j"
psutil.pids()
```

Used to:

* monitor applications
* track processes
* build task managers

---

# 💻 Complete Example

```python id="ps261k"
import psutil

print(psutil.cpu_percent())
```

---

# 🚀 Real-World Uses

Psutil is used in:

* task manager software
* server monitoring dashboards
* performance tracking tools
* DevOps monitoring systems
* automation applications

---

# ⚡ Why Psutil is Important

System monitoring helps:

* improve performance
* track resource usage
* detect issues early
* manage applications efficiently

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* how Python monitors system resources
* how CPU and RAM tracking works
* basics of process monitoring
* system performance analysis

---

# 🚀 Conclusion

The psutil library is a powerful tool for system monitoring and process management.

It helps developers:

* monitor hardware resources
* track running applications
* build monitoring tools

Learning psutil is useful for:

* DevOps
* backend systems
* automation
* monitoring applications
