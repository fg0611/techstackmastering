import asyncio
from database import create_connection, get_google_query

async def exec():
    conn = await create_connection()
    if conn:
        res = await get_google_query(conn, "python dev")
        if res:
            print(res)
        await conn.close()
    else:
        print("DB conn error")

asyncio.run(exec())