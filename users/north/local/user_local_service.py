from ...domain.service.user_service import UserService
from ...south.client_adapter.password_encryption_adapter import PasswordEncryptionClientAdapter
from ...south.repository_adapter.user_repository_adapter import UserRepositoryAdapter


class UserLocalService:
    def __init__(self):
        self.password_encryption_client = PasswordEncryptionClientAdapter()
        self.user_repository = UserRepositoryAdapter()
        self.user_service = UserService(password_encryption_client=self.password_encryption_client,
                                        user_repository=self.user_repository)
