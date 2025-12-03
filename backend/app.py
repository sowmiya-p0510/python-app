# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn
from contextlib import asynccontextmanager
from routes.routes import router
from database import db_pool
from utils.config import (
    DB_POOL_MIN, 
    DB_POOL_MAX,
    API_HOST,
    API_PORT,
    RELOAD,
    get_cors_config,
)
from sqlmodel import SQLModel
from models import *
from database import db_pool

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifecycle"""
    logger = logging.getLogger(__name__)
    
    # Startup
    logger.info("Initializing application...")
    db_pool.initialize_pool(minconn=DB_POOL_MIN, maxconn=DB_POOL_MAX)
    SQLModel.metadata.create_all(db_pool._engine)
    logger.info("Application started successfully")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")
    db_pool.close_all_connections()
    logger.info("Application shutdown complete")

# Create FastAPI app
app = FastAPI(
    title="Real-estate Agent",
    redoc_url=None,
    # docs_url=None,
    lifespan=lifespan
)

# Configure CORS using config
app.add_middleware(
    CORSMiddleware,
    **get_cors_config()
)

# Include routers
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=API_HOST,
        port=API_PORT,
        reload=RELOAD
    )