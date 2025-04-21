import datetime as dt
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None # supabase id
    email: str
