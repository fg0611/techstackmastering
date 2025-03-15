from sqlalchemy import create_engine, text


# sql db connection
DB_NAME = "job_data"
DB_USER = "postgres"
DB_PASSWORD = "123123"
DB_HOST = "localhost"
DB_PORT = "5432"

# engine = create_engine("postgresql://scott:tiger@localhost/test")
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Consulta SQL para obtener la primera fila
query = text("SELECT * FROM job_listings LIMIT 1")

try:
    with engine.connect() as connection:
        # Ejecutar la consulta
        result = connection.execute(query)
        # Obtener la primera fila
        first_row = result.fetchone()
        if first_row:
            print("Primera fila de la tabla:", first_row)
        else:
            print("La tabla está vacía.")
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    # Cerrar la conexión a la base de datos
    engine.dispose()