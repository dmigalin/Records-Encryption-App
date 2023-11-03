from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

mongodb = AsyncIOMotorClient(MONGO_URL)['Database']

