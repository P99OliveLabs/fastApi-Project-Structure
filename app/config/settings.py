import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment
load_dotenv()

class Settings:
    """Configuration settings loaded from environment variables."""
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_NAME: str = os.getenv("DB_NAME", "mydatabase")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")

# Instantiate a settings object to be used across the app
settings = Settings()
