from bson import ObjectId
from fastapi import HTTPException
from app.schemas.product_schema import *
from app.repositories.product_repository import *

def convert_id(product):
    product["_id"] = str(product["_id"])
    return product

def create_product_service(product):
    try:
        product_dict = product.model_dump(mode="json")
        result = create_product_repository(product_dict)

        return {
            "message": "Product created succefully",
            "_id": str(result.inserted_id)
        }
    
    except:
        raise HTTPException(status_code=404, detail="Invalid Body")

def get_by_id_service(_id):
    try:
        product = get_by_id_repository(_id)
        if product:
            convert_id(product)
            return product
        else:
            raise HTTPException(status_code=404 ,detail="Product not found")
    except:
       raise HTTPException(status_code=404, detail="Invalid ID")

def list_product_service():
    try:
        products = [convert_id(product) for product in list_product_repository()]

        length = len(products)

        if products:
            return {
                "products": products,
                "length": length
            }
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
def update_product_service(_id, product):
    try:
        product_dict = product.model_dump(mode="json")
        result = update_product_repository(_id, product_dict)

        if result.matched_count == 0:
            return {"error": "Product no found"}
        return {"message": "product updated succefully"}
    except:
        raise HTTPException(status_code=404, detail="invalid Id")

def delete_product_service(_id):
    try:
        result = delete_product_repository(_id)

        if result.deleted_count == 0:
            return {"error": "Product not found"}
        return {"message": "product deleted succefully"}
    except:
        raise HTTPException(status_code=404, detail="item not found")
