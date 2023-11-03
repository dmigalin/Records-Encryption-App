from passlib.context import CryptContext

from utils.repository import AbstractHashing


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashingRepository(AbstractHashing):
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
