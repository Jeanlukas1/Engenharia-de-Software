from pydantic import BaseModel

class Film(BaseModel):
    title: str
    description: str
    genre: str
    year: int