import asyncio
from typing import Optional
import asyncpg
from config import DB, HOST, PASS, USER

# async def run():
#     conn = await asyncpg.connect(user='postgres', password='123123',
#                                  database='job_finder', host='127.0.0.1')
#     values = await conn.fetch(
#         'SELECT * FROM jobs WHERE id = $1',
#         10,
#     )
#     print(values)
#     await conn.close()

# asyncio.run(run())


async def create_connection():
    """Crea y devuelve una conexión a la base de datos."""
    """Creates and returns a connection to the database."""
    try:
        conn = await asyncpg.connect(user=USER, password=PASS, database=DB, host=HOST)
        # conn = await asyncpg.connect(DATABASE_URL)
        return conn
    except asyncpg.exceptions.PostgresError as e:
        print(f"Conn error: {e}")
        return None
    
async def get_google_query(conn, query: str) -> Optional[int]:
    """Inserta la query de Google en la tabla google_query y devuelve su ID."""
    """Insert the Google query in the table and return it's ID"""
    try:
        print('')
        res = await conn.fetchrow("select id, query from google_query where query = $1", query)
        return res
    except asyncpg.exceptions.PostgresError as e:
        print(f"Insertion error {e}")
        return None

async def insert_google_query(conn, query: str) -> Optional[int]:
    """Inserta la query de Google en la tabla google_query y devuelve su ID."""
    """Insert the Google query in the table and return it's ID"""
    try:
        query_exists = await get_google_query(conn, query)
        if not query_exists:
            res = await conn.fetchrow("insert into google_query (query) values ($1) returning id", query)
            return res.get('id', None)
        return query_exists.get('id', None)
    except asyncpg.exceptions.PostgresError as e:
        print(f"Insertion error {e}")
        return None

async def insert_google_query_url(conn, google_query_id: int, url: str) -> Optional[bool]:
    """Inserta una URL de Google en la tabla google_queries_urls."""
    try:
        await conn.execute(
            "INSERT INTO google_queries_urls (google_query_id, url) VALUES ($1, $2)",
            google_query_id,
            url
        )
        return True
    except asyncpg.exceptions.PostgresError as e:
        print(f"Error al insertar la URL: {e}")
        return None
    
