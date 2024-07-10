from contextlib import asynccontextmanager
from fastapi import FastAPI 
from .db.utils import get_mongoDb


@asynccontextmanager
async def lifeSpan(app:FastAPI):
    mongodb = get_mongoDb()
    app.mongodb = mongodb
    yield
    app.mongodb.close()

app = FastAPI(lifeSpan = lifeSpan)

@app.get("/")
async def read_root() -> dict[str,str]:
    return {"Hello":"Pet project world"}