from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.database import Base

class BookModel(Base):
    __tablename__ = "books"  # Исправлено: двойные подчеркивания вместо жирного текста

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    title: Mapped[str]