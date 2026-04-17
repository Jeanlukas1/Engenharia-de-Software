from fastapi import FastAPI
from routes.film_route import router

app = FastAPI()
app.include_router(router)