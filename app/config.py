import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    max_file_size: int = 10_485_760  # 10MB
    allowed_content_types: list = ["text/csv", "application/vnd.ms-excel"]
    
    class Config:
        env_file = ".env"

settings = Settings()