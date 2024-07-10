from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"
        
    MongoDB_Url: str
    MongoDB_DB: str
    
settings = AppSettings()