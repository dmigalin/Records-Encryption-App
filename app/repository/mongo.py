from bson.objectid import ObjectId

from db.mongo import mongodb
from utils.repository import AbstractDBRepository


class MongoRepository(AbstractDBRepository):
    @staticmethod
    async def write(document):
        res = await mongodb.Records.insert_one(document)
        return str(res.inserted_id)
    
    @staticmethod
    async def get_by_prime_key(object_id):
        return await mongodb.Records.find_one(
            {'_id': ObjectId(f'{object_id}')})
    
    @staticmethod    
    async def delete(object_id):
        await mongodb.Records.find_one_and_delete(
            {'_id':ObjectId(object_id)})