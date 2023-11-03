from repository.sqlalchemy import SQLAlchemyRepository
from repository.mongo import MongoRepository
from repository.encrypt import EncryptionRepository
from repository.hashing import HashingRepository

from services.texts import TextService

                        
def text_service():
    return TextService(
        SQLAlchemyRepository,
        MongoRepository,
        EncryptionRepository,
        HashingRepository)