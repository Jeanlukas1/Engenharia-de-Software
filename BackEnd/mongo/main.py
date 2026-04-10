from pymongo import MongoClient

client = MongoClient("localhost:27017")

db = client["python"]

collection = db["user"]

collection.insert_one({
    "nome": "Jean Lukas de Marins Costa"
})

