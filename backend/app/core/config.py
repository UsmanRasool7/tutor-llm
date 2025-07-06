# app/core/config.py
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Tell Pydantic v2 to load .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # Project
    PROJECT_NAME: str = "LLM Tutor"

    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Chroma
    CHROMA_API_URL: str = Field(..., env="CHROMA_API_URL")

    # Embedding
    EMBEDDING_MODEL: str = Field(
        "sentence-transformers/all-MiniLM-L6-v2",
        env="EMBEDDING_MODEL"
    )
    CHUNK_SIZE: int = Field(500, env="CHUNK_SIZE")
    TOP_K: int = Field(3,   env="TOP_K")

    # Groq LLM
    GROQ_MODEL: str = Field(...,  env="GROQ_MODEL")
    GROQ_API_KEY: str = Field(..., env="GROQ_API_KEY")
    GROQ_TEMPERATURE: float = Field(0.7,  env="GROQ_TEMPERATURE")
    GROQ_MAX_TOKENS:  int   = Field(1024, env="GROQ_MAX_TOKENS")

# Instantiate once
settings = Settings()
