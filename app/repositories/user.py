from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(self, email: str, password: str) -> User:
        user = User(
            email=email,
            hashed_password=get_password_hash(password)
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
