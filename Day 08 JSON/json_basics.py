import json

# --- Python dictionary ---
data = {
    "name": "Chakri",
    "age": 19,
    "skills": ["Python", "ML", "JSON"]
}

# --- convert Python -> JSON string ---
json_data = json.dumps(data, indent=4)
print("JSON Format:\n", json_data)

# --- convert JSON string -> Python ---
python_data = json.loads(json_data)
print("\nBack to Python:\n", python_data)

# --- write JSON to file ---
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nData written to data.json")

# --- read JSON from file ---
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("\nData read from file:\n", loaded_data)

# --- mini example: add new skill ---
loaded_data["skills"].append("Data Analysis")

print("\nUpdated Data:\n", loaded_data)