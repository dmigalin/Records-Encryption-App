from typing import Generator

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config import ASYNC_POSTGRES_URL

engine = create_async_engine(ASYNC_POSTGRES_URL,echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False,class_=AsyncSession)


class Base(DeclarativeBase):
    pass

async def get_async_session():
    async with async_session_maker() as session:
        yield session



# async def get_async_session() -> Generator:
#     """Dependency for getting async session"""
#     try:
#         session: AsyncSession = async_session_maker()
#         yield session
#     finally:
#        await session.close()