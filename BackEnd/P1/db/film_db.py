from pymongo import mongo_client

client = mongo_client["mongodb://localhost:27018/"]
db = client["film_database"]
film_collection = db["films"]