from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

from config import ASYNC_POSTGRES_URL

engine = create_async_engine(ASYNC_POSTGRES_URL,echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False,class_=AsyncSession)


class Base(DeclarativeBase):
    pass

async def get_async_session():
    """Dependency for getting async session"""
    async with async_session_maker() as session:
        yield session

