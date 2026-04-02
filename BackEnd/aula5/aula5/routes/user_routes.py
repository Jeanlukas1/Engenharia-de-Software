from fastapi import APIRouter
from bson import ObjectId
from db.database import users_collection
from schema.user_schema import User

router = APIRouter()

@router.get("/users")
def list_users():
    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    
    return users

@router.post("/users")
def create_user(user: User):
    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)

    return {
        "message": "User Created",
        "id": str(result.inserted_id)
    }

@router.get("/users/{id}")
def get_user_by_id(id:str):
    user = users_collection.find_one({"_id": ObjectId(id)})

    if user:
        user["_id"] = str(user["_id"])
        return user

    return {"error": "User not found"}

@router.put("/users/{user_id}")
def update_user(user_id:str, user: User):
    user_dict = user.model_dump()
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_dict}
    )

    if result.matched_count == 0:
        return {"error": "users not found"}, 404
    return {"message": "user updated"}, 200

@router.delete("/users/{user_id}")
def delete_user(user_id:str):
    result = users_collection.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.matched_count == 0:
        return {"error": "user not found"}, 404
    return {"message": "user deleted succefully"}, 200