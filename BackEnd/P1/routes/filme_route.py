from fastapi import FastAPI
from fastapi import APIRouter


router = APIRouter()

@router.post("filmes", status_code="201")
def create_filme():
    pass