from tabulate import tabulate

# Sample Data
students = [
    ["Chakri", 95, "A"],
    ["Rahul", 88, "B+"],
    ["Aman", 91, "A-"],
    ["Sneha", 97, "A+"]
]

headers = ["Name", "Marks", "Grade"]

# Print table
print(tabulate(students, headers=headers, tablefmt="grid"))