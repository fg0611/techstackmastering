import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
USER = os.environ.get("DB_USER")
PASS = os.environ.get("DB_PASSWORD")
DB = os.environ.get("DB_NAME")
HOST = os.environ.get("DB_HOST")


# class Config:
#     NAME = os.environ.get('NAME')
#     pass
