import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "fastAPI_project_template"
    # ANY_API_KEY: str = os.getenv("ANY_API_KEY")
    '''

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db") 

    '''


settings = Settings()