from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_active_user
from app.repositories.bet_placement import BetPlacementRepository
from app.schemas.bet_placement import BetPlacementCreate, BetPlacementOut

router = APIRouter()

@router.post("/{bet_id}", response_model=BetPlacementOut, dependencies=[Depends(get_current_active_user)])
async def place_bet(
    bet_id: int,
    placement_in: BetPlacementCreate,
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_active_user)
):
    # Verificar que bet_id coincide
    if placement_in.bet_id != bet_id:
        raise HTTPException(status_code=400, detail="El ID de apuesta no coincide")
    repo = BetPlacementRepository(db)
    return await repo.create(placement_in, user.id)

@router.get("/", response_model=list[BetPlacementOut], dependencies=[Depends(get_current_active_user)])
async def list_my_placements(
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_active_user)
):
    repo = BetPlacementRepository(db)
    return await repo.get_by_user(user.id)
