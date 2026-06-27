from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read values
api_key = os.getenv("API_KEY")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print("API Key:", api_key)
print("Username:", username)
print("Password:", password)