from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27018/")
db = client["film_database"]
film_collection = db["films"]