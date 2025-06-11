import asyncio
from app.db.session import AsyncSessionLocal
from app.repositories.user import UserRepository

async def main():
    async with AsyncSessionLocal() as db:
        repo = UserRepository(db)
        user = await repo.create("admin@example.com", "tu_password_segura")
        # Marca como superuser
        user.is_superuser = True
        await db.commit()
        print("Superusuario creado:", user.email)

if __name__ == "__main__":
    asyncio.run(main())
