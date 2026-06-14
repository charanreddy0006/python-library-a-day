from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI 🚀"
    }

# User Route
@app.get("/user/{name}")
def get_user(name: str):

    return {
        "username": name
    }