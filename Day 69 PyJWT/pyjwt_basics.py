import jwt

# Secret Key
SECRET_KEY = "my_secret_key"

# Payload
payload = {
    "username": "Chakri",
    "role": "Student"
}

# Generate JWT Token
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("Generated Token:\n")
print(token)

# Decode JWT Token
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

print("\nDecoded Data:")
print(decoded)