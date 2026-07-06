from tinydb import TinyDB, Query

# Create/Open Database
db = TinyDB("database.json")

# Insert Data
db.insert({
    "name": "Chakri",
    "age": 20,
    "course": "Python"
})

db.insert({
    "name": "Rahul",
    "age": 22,
    "course": "AI"
})

print("All Records:")
print(db.all())

# Search
Student = Query()

result = db.search(Student.age > 20)

print("\nStudents Older Than 20:")
print(result)

# Update
db.update({"course": "Data Science"}, Student.name == "Rahul")

print("\nUpdated Records:")
print(db.all())

# Delete
db.remove(Student.name == "Chakri")

print("\nAfter Deletion:")
print(db.all())