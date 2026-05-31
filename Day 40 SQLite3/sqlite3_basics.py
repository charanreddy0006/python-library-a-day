import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cursor.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    ("Chakri", 95)
)

# Save changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Student Records:\n")

for row in rows:
    print(row)

# Close connection
conn.close()