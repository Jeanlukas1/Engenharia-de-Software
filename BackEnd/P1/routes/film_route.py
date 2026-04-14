from fastapi import APIRouter
from bson import objectid
from schemas.film_schema import Film
from db.film_db import film_collection

router = APIRouter()

@router.post("/filmes", status_code=201)
def create_film(film: Film):
    film_dict = film.model_dump(mode="json")
    result = film_collection.insert_one(film_dict)
    
    return {
        "message": "Film Created",
        "id": str(result.inserted_id)
    }
    
@router.get("/filmes", status_code=200)
def list_films():
    films = []
    
    for film in film_collection.find():
        film["_id"] = str(film["_id"])
        films.append(film)
        
    length = len(films)
        
    return {
        "films": films, 
        "length": length
    }

