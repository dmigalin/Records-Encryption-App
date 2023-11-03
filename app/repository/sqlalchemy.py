import os
from utils.repository import AbstractDBRepository
from models.texts import Text
from db.pgs import engine, async_session_maker, get_async_session

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select



class SQLAlchemyRepository(AbstractDBRepository):
    model = Text
    
    
    @staticmethod
    async def write(data:str, session=async_session_maker):
        async with session.begin() as session:
            session.add(data)
        await session.commit()
    

    @staticmethod
    async def get_by_prime_key(object_id, session=async_session_maker):
        async with session.begin() as session:
            data  =  await session.get(Text,object_id)
        await session.commit()
        return data if data else None
    

    @classmethod
    async def delete(cls,object_id,session=async_session_maker):
        old_text = await cls.get_by_prime_key(object_id,session)
        if not old_text:
            return 404
        async with session.begin() as session:
            await session.delete(old_text)
        await session.commit()
        return 200
    

    @staticmethod
    async def get_by_status():
        async with engine.connect() as connection:
            stmt = select(Text).where(Text.status == True)
            data = await connection.execute(stmt)
        await connection.commit()
        return data.fetchall() if data else None


    @staticmethod
    async def update_status(object_id,session=async_session_maker):
        async with session.begin() as session:
            old_text  =  await session.get(Text,object_id)
            if not old_text:
                return 404
            old_text.status=False
        await session.commit()
        return 200
    
    
    @staticmethod
    async def del_file(object_id):
        try:
            os.remove(f'passwords/{object_id}.txt')
        except:
            return {'file':'.txt file does not exist'}
        return {'file':'Deleted'} 