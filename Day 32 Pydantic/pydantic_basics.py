from pydantic import BaseModel

# --- create data model ---
class Student(BaseModel):

    name: str
    age: int
    marks: float
    passed: bool

# --- sample data ---
student = Student(
    name="Chakri",
    age=20,
    marks=92.5,
    passed=True
)

# --- print object ---
print(student)

# --- convert to dictionary ---
print("\nDictionary Format:")

print(student.model_dump())

# --- JSON output ---
print("\nJSON Format:")

print(student.model_dump_json(indent=4))