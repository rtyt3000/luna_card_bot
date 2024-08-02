from sqlalchemy import BIGINT, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = 'cards'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    rarity: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    point_count: Mapped[int] = mapped_column(Integer, default=0)
    cards: Mapped[MutableList[int]] = mapped_column(MutableList.as_mutable(ARRAY(Integer)), nullable=False, default=[])
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False)
