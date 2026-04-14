from fastapi import FastAPI
from routes.filme_route import router

app = FastAPI()
app.include_router(router)