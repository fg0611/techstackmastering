import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    # Cadena de conexión de PostgreSQL con asyncpg
    DATABASE_URL = os.getenv("DATABASE_URL")