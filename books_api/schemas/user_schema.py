from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: Optional[str] = None
    email: str
