from cryptography.fernet import Fernet
from utils.repository import AbstractEncryption


class EncryptionRepository(AbstractEncryption):
    @staticmethod
    def encrypt(data:str):
        key = Fernet.generate_key()
        secret_data = Fernet(key).encrypt(bytes(data, "utf8"))
        return {'secret_key': str(key)[2:-1],
                'secret_data':str(secret_data)[2:-1]}
    
    @staticmethod
    def decrypt(secret_key:str,secret_data:str):
        secret_data = Fernet(bytes(secret_key, "utf8")).decrypt(
            bytes(secret_data, "utf8")).decode("utf8") 
        return secret_data
