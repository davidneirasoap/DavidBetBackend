from pydantic import BaseModel
from datetime import datetime

class BetPlacementBase(BaseModel):
    bet_id: int
    amount: float

class BetPlacementCreate(BetPlacementBase):
    pass

class BetPlacementOut(BetPlacementBase):
    id: int
    user_id: int
    placed_at: datetime

    class Config:
        orm_mode = True
