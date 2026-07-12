from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    room_code: Mapped[str] = mapped_column(
        String(6),
        unique=True,
        nullable=False,
    )

    host_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    topic: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    difficulty: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="Easy",
    )

    num_questions: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=10,
    )

    time_per_question: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=20,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="waiting",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    host: Mapped["User"] = relationship("User", back_populates="hosted_rooms")