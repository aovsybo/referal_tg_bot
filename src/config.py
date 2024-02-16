import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')


settings = Settings()
