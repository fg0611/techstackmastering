import datetime as dt
from typing import Optional
from pydantic import BaseModel


class Favorite(BaseModel):
    id: Optional[int] = None
    user_id: str  # Referencia al ID de usuario de Supabase
    book_id: int
    active: bool
    added_at: Optional[dt.datetime] = None