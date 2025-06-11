from pydantic import BaseSettings

class Settings(BaseSettings):
    PORT: int
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SERPAPI_API_KEY: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        env_file = ".env"

settings = Settings()
