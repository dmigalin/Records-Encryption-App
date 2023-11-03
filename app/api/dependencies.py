# from repositories.tasks import TasksRepository
# from repositories.users import UsersRepository

from repository.sqlalchemy import SQLAlchemyRepository
from repository.mongo import MongoRepository
from repository.encrypt import EncryptionRepository
# from services.tasks import TasksService
# from services.users import UsersService
from services.texts import TextService


# def sqlalchemy_service():
#     return SQLAlchemyService(SQLAlchemyRepository)


# def mongo_service():
#     return MongoService(MongoRepository)

# def encrypt_service():
#     return EncryptionService(EncryptionRepository)                         

def text_service():
    return TextService(
        SQLAlchemyRepository,
        MongoRepository,
        EncryptionRepository)