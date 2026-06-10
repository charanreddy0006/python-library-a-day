import pendulum

# Current date and time
now = pendulum.now()

print("Current Date & Time:")
print(now)

# Current date
print("\nCurrent Date:")
print(now.to_date_string())

# Current time
print("\nCurrent Time:")
print(now.to_time_string())

# Add days
future = now.add(days=10)

print("\nAfter 10 Days:")
print(future)

# Subtract days
past = now.subtract(days=5)

print("\n5 Days Ago:")
print(past)

# Difference between dates
new_year = pendulum.datetime(2026, 1, 1)

difference = now.diff(new_year)

print(
    "\nDays Until New Year:",
    difference.in_days()
)

# Human readable format
print(
    "\nHuman Friendly:"
)

print(
    future.diff_for_humans()
)