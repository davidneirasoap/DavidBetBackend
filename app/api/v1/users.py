from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserOut
from app.repositories.user import UserRepository
from app.dependencies import get_db
from app.core.security import create_access_token, verify_password

router = APIRouter()

@router.post("/", response_model=UserOut)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    if await repo.get_by_email(user_in.email):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    user = await repo.create(user_in.email, user_in.password)
    return user

# Login, token endpoint, user info…
