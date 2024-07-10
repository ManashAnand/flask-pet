from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..pet_project.settings import settings

def get_mongoDb() -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.MongoDB_Url)
    return client.get_database(settings.MongoDB_DB)