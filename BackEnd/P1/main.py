from fastapi import FastAPI
from app.routers.product_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Olá, esta é a API de produtos utilizando o FastAPI + MongoDB + Docker"}
