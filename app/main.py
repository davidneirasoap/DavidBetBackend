import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import users, bets, bet_placements
from app.db.session import engine, Base

app = FastAPI(title="Betting App API")

# Crear tablas si no existen
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Incluye routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(bets.router, prefix="/api/v1/bets", tags=["bets"])
app.include_router(bet_placements.router, prefix="/api/v1/bet_placements", tags=["bet_placements"])

if __name__ == "__main__":
    uvicorn.run("app.main:app",
                host="0.0.0.0",
                port=int(settings.PORT),
                reload=True)
