from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class BetPlacement(Base):
    __tablename__ = "bet_placements"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bet_id = Column(Integer, ForeignKey("bets.id"), nullable=False)
    amount = Column(Float, nullable=False)
    placed_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="placements")
    bet = relationship("Bet", back_populates="placements")
