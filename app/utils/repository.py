from abc import ABC, abstractmethod

class AbstractDBRepository(ABC):
    @abstractmethod
    async def write():
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_prime_key():
        raise NotImplementedError
    
    @abstractmethod
    async def delete():
        raise NotImplementedError


class AbstractEncryption(ABC):
    @abstractmethod
    async def encrypt():
        raise NotImplementedError
    
    @abstractmethod
    async def decrypt():
        raise NotImplementedError


class AbstractHashing(ABC):
    @abstractmethod
    async def get_password_hash():
        raise NotImplementedError
    
    @abstractmethod
    async def verify_password():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractDBRepository):
    model = None

class MongoRepository(AbstractDBRepository):
    model = None

