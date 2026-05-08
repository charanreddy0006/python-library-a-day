import requests

# --- GET request ---
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

# --- status code ---
print("Status Code:", response.status_code)

# --- convert response to JSON ---
data = response.json()

print("\nFirst User:")
print(data[0])

# --- print specific values ---
print("\nName:", data[0]["name"])
print("Email:", data[0]["email"])

# --- headers ---
print("\nHeaders:")
print(response.headers)

# --- mini example: fetch posts ---
posts_url = "https://jsonplaceholder.typicode.com/posts"

posts = requests.get(posts_url).json()

print("\nFirst Post Title:")
print(posts[0]["title"])