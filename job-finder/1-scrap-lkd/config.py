import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")


# class Config:
#     NAME = os.environ.get('NAME')
#     pass
