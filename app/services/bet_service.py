# app/services/bet_service.py
from app.services.serp import SerpService
from app.repositories.bet import BetRepository
from app.schemas.bet import BetCreate
from datetime import datetime

class BetService:
    def __init__(self, db, user_id: int):
        self.repo = BetRepository(db)
        self.serp = SerpService()
        self.user_id = user_id

    async def create_from_query(self, query: str, event_date: datetime):
        results = self.serp.search(query)
        # por simplicidad, creamos una sola apuesta con el primer resultado
        first = results[0]
        bet_in = BetCreate(
            title=first.get("title", query),
            description=first.get("snippet", ""),
            odds=1.0,            # por defecto
            event_date=event_date
        )
        return await self.repo.create(bet_in, self.user_id)
