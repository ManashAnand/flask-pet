from contextlib import asynccontextmanager
from fastapi import FastAPI 


@asynccontextmanager
async def lifeSpan(app:FastAPI):
    
    yield


app = FastAPI(lifeSpan = lifeSpan)

@app.get("/")
async def read_root() -> dict[str,str]:
    return {"Hello":"Pet project world"}