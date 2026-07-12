from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)

    username:Mapped[str]=mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    email:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    rating:Mapped[str]=mapped_column(
        Integer,
        default=1000
    )
    hosted_rooms: Mapped[list["Room"]] = relationship(
        "Room",
        back_populates="host",
    )