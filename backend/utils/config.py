import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration - unified for both local and Cloud SQL
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")  # Use only for local
DB_PORT = int(os.getenv("DB_PORT", "5432"))  # Use only for local

# Cloud SQL configuration (if present, Cloud SQL is used)
CLOUD_SQL_CONNECTION_NAME = os.getenv("CLOUD_SQL_CONNECTION_NAME")
USE_PRIVATE_IP = os.getenv("USE_PRIVATE_IP", "false").lower() == "true"

# Connection pool settings
DB_POOL_MIN = int(os.getenv("DB_POOL_MIN", "5"))
DB_POOL_MAX = int(os.getenv("DB_POOL_MAX", "20"))

# FastAPI Configuration
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", "8000"))
RELOAD = os.getenv("RELOAD", "false").lower() == "true"
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# JWT Configuration
JWT_SECRET = os.getenv("JWT_SECRET", "change-this-in-production-please-use-a-secure-random-string")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION_DAYS = int(os.getenv("JWT_EXPIRATION_DAYS", "7"))

def get_cors_config() -> dict:
    """
    Get CORS configuration.
    
    Returns:
        dict: CORS configuration for FastAPI middleware
    """
    return {
        "allow_origins": ALLOWED_ORIGINS,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }
