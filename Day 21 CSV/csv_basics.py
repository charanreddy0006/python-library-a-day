import csv

# --- writing to CSV file ---
with open("students.csv", mode="w", newline="") as file:

    writer = csv.writer(file)

    # header
    writer.writerow(["Name", "Marks"])

    # rows
    writer.writerow(["Chakri", 95])
    writer.writerow(["Rahul", 88])
    writer.writerow(["Aman", 91])

print("CSV file created successfully")

# --- reading CSV file ---
print("\nReading CSV File:\n")

with open("students.csv", mode="r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)