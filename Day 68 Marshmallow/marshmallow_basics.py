from marshmallow import Schema, fields, ValidationError

# Create Schema
class StudentSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    email = fields.Email(required=True)

student = {
    "name": "Chakri",
    "age": 20,
    "email": "chakri@gmail.com"
}

schema = StudentSchema()

# Serialize Data
result = schema.dump(student)

print("Serialized Data:")
print(result)

# Deserialize & Validate
try:
    data = schema.load(student)

    print("\nValidated Data:")
    print(data)

except ValidationError as err:
    print(err.messages)