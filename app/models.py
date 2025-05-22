from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[str] = None

