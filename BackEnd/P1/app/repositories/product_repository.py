from app.db.product_db import collection
from bson import ObjectId

def create_product_repository(product):
    return collection.insert_one(product)

def get_by_id_repository(_id):
    return collection.find_one({"_id": ObjectId(_id)})

def list_product_repository():
    return collection.find()

def update_product_repository(_id, product):
    return collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": product}
    )

def delete_product_repository(_id):
    return collection.delete_one({"_id": ObjectId(_id)})