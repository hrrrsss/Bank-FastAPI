import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    account_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    currency: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[float] = mapped_column(Numeric(15, 2), nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # For use object User without connection to DB
    owner: Mapped["User"] = relationship(back_populates="accounts")