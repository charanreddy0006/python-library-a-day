# Day 64 - APScheduler Library

# 📌 Overview

On Day 64, I explored Python's **APScheduler** library, which is used for scheduling tasks and automating repetitive jobs.

APScheduler stands for **Advanced Python Scheduler**.

It allows developers to execute functions automatically at specific times, fixed intervals, or according to cron expressions.

Unlike simple scheduling tools, APScheduler provides advanced scheduling features suitable for production applications.

It is widely used in:

* Automation Systems
* Server Maintenance
* Reminder Applications
* Data Processing Pipelines
* Backend Services

---

# 📦 Installation

Install APScheduler using pip:

```bash
pip install apscheduler
```

---

# 🧠 Importing the Library

```python
from apscheduler.schedulers.blocking import BlockingScheduler
```

---

# ⏰ What is Task Scheduling?

Task scheduling means executing a task automatically without manual intervention.

Examples:

* Send daily email reports
* Backup files every night
* Clean temporary files
* Generate weekly reports
* Run data processing jobs

---

# 🚀 Creating a Scheduler

Example:

```python
scheduler = BlockingScheduler()
```

This creates a scheduler that runs continuously until stopped.

---

# 🔁 Running Jobs at Intervals

Example:

```python
scheduler.add_job(
    show_time,
    "interval",
    seconds=5
)
```

This runs the function every 5 seconds.

---

# 📅 Running Jobs on Specific Dates

Example:

```python
scheduler.add_job(
    task,
    "date",
    run_date="2026-07-01 10:00:00"
)
```

Runs the task only once at the specified date and time.

---

# 📆 Cron Scheduling

Example:

```python
scheduler.add_job(
    task,
    "cron",
    hour=9,
    minute=0
)
```

Runs the task every day at **9:00 AM**.

---

# ▶️ Starting the Scheduler

Example:

```python
scheduler.start()
```

Starts executing scheduled jobs.

---

# ⏹️ Stopping the Scheduler

Stop the scheduler by pressing:

```text
Ctrl + C
```

---

# 💻 Complete Example

```python
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def hello():
    print("Hello!")

scheduler.add_job(
    hello,
    "interval",
    seconds=10
)

scheduler.start()
```

---

# 🚀 Real-World Uses

## Email Automation

Send scheduled emails.

---

## Backup Systems

Create automatic backups.

---

## Data Pipelines

Process data at regular intervals.

---

## Reminder Applications

Send reminders at specific times.

---

## Server Maintenance

Run cleanup and maintenance tasks.

---

# ⚡ Advantages of APScheduler

* Easy to use
* Supports interval scheduling
* Supports date scheduling
* Supports cron expressions
* Reliable for production applications

---

# 🎯 Learning Outcome

After completing this topic, I learned:

* What task scheduling is
* How to automate repetitive jobs
* How interval scheduling works
* How cron scheduling works
* How production schedulers are built

---

# 🚀 Conclusion

APScheduler is a powerful scheduling library for Python that helps automate repetitive tasks efficiently.

It enables developers to:

* Schedule recurring jobs
* Automate workflows
* Execute tasks at fixed times
* Build reliable automation systems

Learning APScheduler is useful for:

* Automation
* Backend Development
* DevOps
* Data Engineering
* Python Projects

It is an excellent library for building professional automation and scheduling applications.
