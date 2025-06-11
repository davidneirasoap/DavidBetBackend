from pydantic import BaseModel
from datetime import datetime

class BetBase(BaseModel):
    title: str
    description: str | None = None
    odds: float
    event_date: datetime

class BetCreate(BetBase):
    pass

class BetOut(BetBase):
    id: int
    created_by_id: int

    class Config:
        orm_mode = True
