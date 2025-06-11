from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.bet_placement import BetPlacement
from app.schemas.bet_placement import BetPlacementCreate

class BetPlacementRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, placement_in: BetPlacementCreate, user_id: int) -> BetPlacement:
        db_obj = BetPlacement(**placement_in.dict(), user_id=user_id)
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def get_by_user(self, user_id: int):
        result = await self.db.execute(select(BetPlacement).where(BetPlacement.user_id == user_id))
        return result.scalars().all()
