
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.timestamp_mixin import created_at, intpk


class Reviews(Base):
    __tablename__ = "reviews"

    id: Mapped[intpk]
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[created_at]
