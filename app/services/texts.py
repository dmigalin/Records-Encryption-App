import time

from fastapi import HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from repository.sqlalchemy import SQLAlchemyRepository
from repository.mongo import MongoRepository
from repository.encrypt import EncryptionRepository
from repository.hashing import HashingRepository

from schemas.texts import TextSchemaCreate
from models.texts import Text
from config import REMOVE_INTERVALS as RMI


class TextService:
    def __init__(self, sqlalchemy_repo: SQLAlchemyRepository,
            mongo_repo: MongoRepository,
            encrypt_repo: EncryptionRepository,
            hashing_repo: HashingRepository):
        self.sqlalchemy_repo: SQLAlchemyRepository = sqlalchemy_repo()
        self.mongo_repo: MongoRepository = mongo_repo()
        self.encrypt_repo: EncryptionRepository = encrypt_repo()
        self.hashing_repo: HashingRepository = hashing_repo()


    async def create_record(self, session:AsyncSession, data:TextSchemaCreate) -> dict:
        data = data.model_dump()
        encrypt = self.encrypt_repo.encrypt(data['text'])
        plain_password = encrypt['secret_key'][:-1]
        hashed_password = self.hashing_repo.get_password_hash(plain_password)
        
        document = {
            'password':hashed_password,
            'text':encrypt['secret_data']
            }
        
        object_id = await self.mongo_repo.write(document)
        new_text=Text(user_id=object_id,
                      date=time.strftime('%d.%m.%Y',time.localtime()),
                      time=time.strftime('%H:%M:%S',time.localtime())
                      )
        await self.sqlalchemy_repo.write(session, new_text)
        return {'object_id': object_id, 'password': plain_password}


    async def get_record(self, object_id:str,password:str) -> FileResponse:
        secret_data = await self.mongo_repo.get_by_prime_key(object_id)
        if secret_data == None:
            raise HTTPException(
                status_code=404, detail='Text with this ID does not exsist.')
        if self.hashing_repo.verify_password(
            password,secret_data['password']):
            password = password + '='
            secret_data = self.encrypt_repo.decrypt(
                password,
                secret_data['text'])
            with open(f"/app/passwords/{object_id}.txt",'w') as file:
                file.write(secret_data)
            return FileResponse(
                path=f"/app/passwords/{object_id}.txt",
                filename=f"{object_id}.txt",
                media_type='text/txt')
        else:
            raise HTTPException(status_code=404,detail='Wrong Password.')
        

    async def update_records(self,session:AsyncSession):
        status = await self.sqlalchemy_repo.get_by_status()
        if status:
            for i in status:
                changes = 0
                if time.time() - time.mktime(
                    time.strptime(i[1]+i[2],'%d.%m.%Y%H:%M:%S')) > RMI: 
                    object_id = i[0]
                    await self.sqlalchemy_repo.update_status(session,object_id)
                    await self.mongo_repo.delete(object_id)
                    await self.sqlalchemy_repo.del_file(object_id)
                    changes += 1
            if changes > 0:
                return 'RECORDS HAVE BEEN UPDATED'
        return 'THERE ARE NO RECORDS TO UPDATE'