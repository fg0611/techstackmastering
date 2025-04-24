import asyncio
from database import create_connection
from google_search import store_google_suggested_urls

async def exec():
    conn = await create_connection()
    if conn:
        queries_to_search = ["python dev"]
        sub_search_terms = "remote english spanish latam"

        for query in queries_to_search:
            await store_google_suggested_urls(query, sub_search_terms, conn)
        await conn.close()
    else:
        print("DB conn error")

asyncio.run(exec())