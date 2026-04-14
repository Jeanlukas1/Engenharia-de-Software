from fastapi import APIRouter
from fastapi import HTTPException
from bson import ObjectId
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

@router.put("/filmes/{_id}", status_code=200)
def update_film(_id: str, film: Film):
    film_dict = film.model_dump(mode="json")
    result = film_collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": film_dict}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"message": "Film updated succefully!"}

@router.delete("/filmes/{_id}", status_code=200)
def delete_film(_id: str):
    filter_object = {"_id": ObjectId(_id)}
    result = film_collection.delete_one(filter_object)
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404 , detail="Film not found!")
    return {"message": "Film deleted succefully!", "id": _id}