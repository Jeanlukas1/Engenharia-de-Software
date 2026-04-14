from pymongo import mongo_client

client = mongo_client["localhost:27018"]
db = client["film_database"]
film_collection = db["films"]