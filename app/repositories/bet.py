from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.bet import Bet
from app.schemas.bet import BetCreate

class BetRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, bet_in: BetCreate, created_by_id: int) -> Bet:
        db_obj = Bet(**bet_in.dict(), created_by_id=created_by_id)
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def get_all(self) -> list[Bet]:
        result = await self.db.execute(select(Bet))
        return result.scalars().all()

    async def get_by_id(self, bet_id: int) -> Bet | None:
        result = await self.db.execute(select(Bet).where(Bet.id == bet_id))
        return result.scalars().first()
