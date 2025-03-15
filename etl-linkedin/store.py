# from airflow import DAG
# import psycopg2
from sqlalchemy import create_engine
from config import Config

def store_jobs(df):
    # sql db connection
    # DB_NAME = "job_data"
    # DB_USER = "postgres"
    # DB_PASSWORD = "123123"
    # DB_HOST = "localhost"
    # DB_PORT = "5432"

    cfg = Config()
    print(cfg.SQLALCHEMY_DATABASE_URI)
    engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)
    # engine = create_engine(
    #     f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    # )
    try:
        # Intentar escribir el DataFrame en la base de datos
        df.to_sql("job_listings", engine, if_exists="append", index=False)
        print("Datos insertados correctamente.")
    except Exception as e:
        # Manejar cualquier error que ocurra
        print(f"Error al insertar datos: {e}")
    finally:
        # Cerrar la conexión a la base de datos
        engine.dispose()
