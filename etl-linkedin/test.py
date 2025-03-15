from sqlalchemy import create_engine
from config import Config


cfg = Config()
print(cfg.SQLALCHEMY_DATABASE_URI)
engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)

# import psycopg2

# conn = psycopg2.connect(
#     dbname="job_data",
#     user="postgres",
#     password="123123",
#     host="localhost",
#     port="5432"
# )
# print("Conexión exitosa")
# conn.close()
