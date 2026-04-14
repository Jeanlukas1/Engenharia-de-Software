from fastapi import FastAPI
from fastapi import APIRouter
from schemas.film_schema import Film

router = APIRouter()

@router.post("filmes", status_code="201")
def create_film(film: Film):
    pass