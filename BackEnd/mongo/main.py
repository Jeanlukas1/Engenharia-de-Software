from pymongo import MongoClient

client = MongoClient("localhost:27017")

db = client["python"]

collection = db["user"]

print(list(collection.find()))

print(collection.insert_one({
    "nome": "Jean Lukas de Marins Costa"
}))

print(db.list_collections)

