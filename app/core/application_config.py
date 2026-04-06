import os
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV_PATH = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    model_config = {
        "env_file": ENV_PATH,
        "env_file_encoding": "utf-8"
    }

settings = Settings()