import httpx

# Send GET request
response = httpx.get(
    "https://jsonplaceholder.typicode.com/users"
)

print("Status Code:", response.status_code)

# Convert JSON response
data = response.json()

print("\nFirst User:")

print("Name:", data[0]["name"])

print("Email:", data[0]["email"])

print("Company:", data[0]["company"]["name"])