from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pymongo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
    allow_headers=["*"],  
)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["users"]

class User(BaseModel):
    username: str
    password: str
    email: str
    phoneNumber: str
    confirmPassword: str

@app.post("/register")
async def register_user(user: User):
    print("whatttt")
    if len(user.username) <= 5:
        raise HTTPException(status_code=400, detail="Username must be more than 5 characters.")
    if len(user.password) <= 6:
        raise HTTPException(status_code=400, detail="Password must be more than 6 characters.")
    if user.password != user.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match.")
    if len(user.phoneNumber) != 11:
        raise HTTPException(status_code=400, detail="Phone number must have exactly 11 digits.")
    existing_user_email = collection.find_one({"email": user.email})
    if existing_user_email:
        # raise HTTPException(status_code=400, detail="Email already exists.")
        return {"message": "Email already exists."}
    existing_user_phone = collection.find_one({"phoneNumber": user.phoneNumber})
    if existing_user_phone:
        # raise HTTPException(status_code=400, detail="Phone number already exists.")
        return {"message": "Phone Number already exists."}
    try:
        collection.insert_one(user.dict())
    except Exception as e:
        return {"message": "Error registering user."}
        # raise HTTPException(status_code=500, detail="Error registering user.")
    return {"message": "User registered successfully."}