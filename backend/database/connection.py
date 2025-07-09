from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import os

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()

async def get_database():
    return db.database

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    db.database = db.client.saveit_db
    print(f"Connected to MongoDB Atlas and db = {db.database}")

async def close_mongo_connection():
    db.client.close()
    print("Disconnected from MongoDB Atlas")
