from datetime import datetime, date, time, timedelta

# --- current date and time ---
now = datetime.now()
print("Current Date & Time:", now)

# --- only date ---
today = date.today()
print("Today's Date:", today)

# --- create custom date ---
custom_date = date(2026, 4, 21)
print("Custom Date:", custom_date)

# --- create time ---
current_time = time(14, 30, 0)
print("Custom Time:", current_time)

# --- formatting date ---
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date:", formatted)

# --- adding days ---
future = today + timedelta(days=10)
print("After 10 Days:", future)

# --- difference between dates ---
d1 = date(2026, 4, 1)
d2 = date(2026, 4, 21)
difference = d2 - d1
print("Difference:", difference.days, "days")

# --- mini example: countdown ---
exam_date = date(2026, 5, 10)
remaining = exam_date - today
print("Days left for exam:", remaining.days)