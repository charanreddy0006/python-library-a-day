from cerberus import Validator

# Define Schema
schema = {
    "name": {
        "type": "string",
        "required": True
    },
    "age": {
        "type": "integer",
        "min": 18
    },
    "email": {
        "type": "string",
        "regex": r".+@.+\..+"
    }
}

# Data to Validate
student = {
    "name": "Chakri",
    "age": 20,
    "email": "chakri@gmail.com"
}

validator = Validator(schema)

if validator.validate(student):
    print("✅ Data is Valid")
else:
    print("❌ Validation Errors")
    print(validator.errors)