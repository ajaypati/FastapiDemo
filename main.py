
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# JSON request body ka structure
class User(BaseModel):
    name: str
    email: str
    age: int

# Temporary database
users = []

# POST API - Receive JSON data
@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    userdata = {
        "name": "ajay",
        "email": "ajay@example.com",
        "age": 45
        }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "data": new_user,
        "userdata": userdata
    }

@app.post("/postdata")
def post_data(data: dict):
    return {
        "message": "Data received successfully",
        "data": data
    }   


# GET API - Return JSON data
@app.get("/users")
def get_users():
    return {
        "message": "Users fetched successfully and data is provided!",
        "data": users
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {
                "message": "User fetched successfully and data is provided!!!",
                "data": user
            }
    return {
        "message": "User not found",
        "data": None
    }
