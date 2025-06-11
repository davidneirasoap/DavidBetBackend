from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.dependencies import get_db, get_current_superuser, get_current_active_user
from app.services.bet_service import BetService
from app.schemas.bet import BetOut

router = APIRouter()

@router.post("/from-query", response_model=BetOut, dependencies=[Depends(get_current_superuser)])
async def create_bet_from_query(
    query: str,
    event_date: datetime,
    db: AsyncSession = Depends(get_db),
    superuser = Depends(get_current_superuser)
):
    svc = BetService(db, superuser.id)
    return await svc.create_from_query(query, event_date)

@router.get("/", response_model=list[BetOut], dependencies=[Depends(get_current_active_user)])
async def list_bets(db: AsyncSession = Depends(get_db)):
    from app.repositories.bet import BetRepository
    repo = BetRepository(db)
    return await repo.get_all()

