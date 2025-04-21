from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    publication_year: Optional[int] = None
    authors: Optional[str] = None