import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    PG_CREDS = {
        "database": os.environ.get("POSTGRES_DB"),
        "user": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "host": os.environ.get("POSTGRES_HOST"),
    }


settings = Settings()
