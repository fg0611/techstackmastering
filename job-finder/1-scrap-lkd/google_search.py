import asyncio
import time
import urllib.parse
from playwright.async_api import async_playwright
from typing import List, Optional
import database as db_functions

def generate_google_query_url(query: str, sub_search: str) -> str:
    """Genera la url de busqueda en google"""
    """Generate complete google search url"""
    base_url = "https://www.google.com/search"
    params = {"q": f"site:linkedin.com/jobs {query} {sub_search}"}
    search_url = base_url + "?" + urllib.parse.urlencode(params)
    return search_url


async def extract_google_suggested_urls(url: str) -> List[str]:
    """Extrae listado de urls de Google"""
    """Extract job urls from Google"""
    suggested_urls = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        time.sleep(10)
        
        links = await page.locator("a").all()
        for l in links:
            href = await l.get_attribute("href")
            if href and "linkedin.com/jobs/" in href:
                suggested_urls.append(href)

        await browser.close()
    return list(set(suggested_urls))


async def store_google_suggested_urls(query: str, sub_search: str, conn) -> Optional[None]:
    search_url = generate_google_query_url(query, sub_search)
    suggested_urls = await extract_google_suggested_urls(search_url)

    # guardar la query de google en postgres google_query
    query_id = await db_functions.insert_google_query(conn, query)
    # guardar todas las urls de linkedin en postgres en google_queries_urls con su ID de relacion de google_query
    if query_id and suggested_urls:
        for url in suggested_urls:
            await db_functions.insert_google_query_url(conn, query_id, url)
        print(f"se han almacenado {len(suggested_urls)} en la DB")
    else:
        print(f"error al almacenar la query: {query} en la DB")