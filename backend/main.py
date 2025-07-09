from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.connection import connect_to_mongo, close_mongo_connection
from database.collections import collections
from api.routes import links, folders
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    await collections.initialize()
    print("SaveIt API started successfully")
    
    yield
    
    # Shutdown
    await close_mongo_connection()
    print("SaveIt API shutdown complete")

app = FastAPI(title="SaveIt API", lifespan=lifespan)

# Include routers
app.include_router(links.router, prefix="/api/links", tags=["links"])
# app.include_router(folders.router, prefix="/api/folders", tags=["folders"])

@app.get("/")
def read_root():
    return {"message": "SaveIt API is running!"}
