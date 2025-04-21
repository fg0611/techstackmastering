import requests

OPEN_LIBRARY_BASE_URL = "https://openlibrary.org"

def search_books(query):
    url = f"{OPEN_LIBRARY_BASE_URL}/search.json?q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("docs", [])
        filtered = []
        if data:
            for l in data:
                filtered.append(
                    {
                        "title": l.get("title", ""),
                        "author_name": l.get("author_name", ""),
                        "first_publish_year": l.get("first_publish_year", ""),
                    }
                )

        return filtered
    except requests.exceptions.RequestException as e:
        print(f"Error on Open Library search: {e}")
        return []


def search_books_by_isbn(isbn):
    url = f"{OPEN_LIBRARY_BASE_URL}/isbn/{isbn}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error on Open Library search by ISBN: {e}")
        return None
