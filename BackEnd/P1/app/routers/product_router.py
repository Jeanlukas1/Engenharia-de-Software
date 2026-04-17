from fastapi import APIRouter
from app.services.product_services import *
from app.schemas.product_schema import Product

router = APIRouter()

@router.post("/produtos")
def create_product(product: Product):
    return create_product_service(product)

@router.get("/produtos/{_id}")
def get_product_by_id(_id: str):
    return get_by_id_service(_id)

@router.get("/produtos")
def list_products():
    return list_product_service()

@router.put("/produtos/{_id}")
def update_product(_id: str, product: Product):
    return update_product_service(_id, product)

@router.delete("/produtos/{_id}")
def delete_product(_id: str):
    return delete_product_service(_id)