from fastapi import FastAPI
from fastapi import APIRouter
from schemas.film_schema import Film
from db.film_db import film_collection

router = APIRouter()

@router.post("/filmes", status_code="201")
def create_film(film: Film):
    film_dict = film.model_dump(mode="json")
    result = film_collection.insert_one(film_dict)
    
    result {
        
    }