from dotenv import load_dotenv
import os

# --- load .env file ---
load_dotenv()

# --- access environment variables ---
api_key = os.getenv("API_KEY")

database = os.getenv("DATABASE_URL")

secret = os.getenv("SECRET_KEY")

print("API KEY:", api_key)

print("Database URL:", database)

print("Secret Key:", secret)