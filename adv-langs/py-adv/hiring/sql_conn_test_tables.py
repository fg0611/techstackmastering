import pg8000

db_params = {
    'host': 'localhost',
    'database': 'training',
    'user': 'postgres',
    'password': '123123',
    'port': 5432
}

try:
    conn = pg8000.connect(**db_params)
    cursor = conn.cursor()

    # Consulta SQL para obtener la lista de tablas
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

    # Obtener los resultados de la consulta
    tables = cursor.fetchall()

    # Imprimir la lista de tablas
    if tables:
        print("Lista de tablas en la base de datos 'training':")
        for table in tables:
            print(table[0])  # table[0] contiene el nombre de la tabla
    else:
        print("No se encontraron tablas en la base de datos 'training'.")

except pg8000.Error as e:
    print(f"Error de conexión o consulta: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()