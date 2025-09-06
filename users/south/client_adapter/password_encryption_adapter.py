from passlib.context import CryptContext
from ...domain.port.client.password_encryption_client import PasswordEncryptionClient


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordEncryptionClientAdapter(PasswordEncryptionClient):
    def encrypt(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
