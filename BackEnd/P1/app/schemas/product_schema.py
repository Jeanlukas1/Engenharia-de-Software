from pydantic import BaseModel

class Product(BaseModel):
    nome: str
    preco: float
    quantidade: int