from diskcache import Cache

# Create cache directory
cache = Cache("cache")

# Store values
cache["username"] = "Chakri"
cache["course"] = "Python"

print("Stored Successfully!")

# Retrieve values
print("\nUsername:", cache["username"])
print("Course:", cache["course"])

# Check if key exists
if "username" in cache:
    print("\nUsername Found!")

# Delete a key
del cache["course"]

print("\nRemaining Keys:")
print(list(cache.iterkeys()))

# Close cache
cache.close()