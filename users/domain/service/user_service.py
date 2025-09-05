from ..aggregation.user import User
from ..port.client.password_encryption import PasswordEncryptionClient
from ..port.repository.user_repository import UserRepository


class UserService:
    def __init__(self,
                 password_encryption_client: PasswordEncryptionClient,
                 user_repository: UserRepository):
        self.password_encryption_client = password_encryption_client
        self.user_repository = user_repository

    def register(self, user: User):
        encrypted_password = self.password_encryption_client.encrypt(user.password)
        return self.user_repository.add_user(user.user_name, encrypted_password)

