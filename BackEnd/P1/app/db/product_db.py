from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["loja_db"]
collection = db["produtos"]