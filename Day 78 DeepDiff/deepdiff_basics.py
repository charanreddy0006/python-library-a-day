from deepdiff import DeepDiff

# Dictionary 1
student1 = {
    "name": "Chakri",
    "age": 20,
    "course": "Python"
}

# Dictionary 2
student2 = {
    "name": "Chakri",
    "age": 21,
    "course": "Python",
    "city": "Hyderabad"
}

# Compare
difference = DeepDiff(student1, student2)

print("Differences:")
print(difference)