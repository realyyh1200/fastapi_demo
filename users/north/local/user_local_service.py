from logger import logger
from ...domain.aggregation.user import User
from ..contract.user_local_cmd import RegisterUserCmd
from ...domain.service.user_service import UserService
from ...south.client_adapter.password_encryption_adapter import PasswordEncryptionClientAdapter
from ...south.repository_adapter.user_repository_adapter import UserRepositoryAdapter


class UserLocalService:
    def __init__(self):
        self.password_encryption_client = PasswordEncryptionClientAdapter()
        self.user_repository = UserRepositoryAdapter()
        self.user_service = UserService(password_encryption_client=self.password_encryption_client,
                                        user_repository=self.user_repository)

    def register_user(self, register_user_cmd: RegisterUserCmd) -> bool:
        try:
            logger.info(f"[user]:Registering user {register_user_cmd.user_name}")
            register_user = User(**register_user_cmd.model_dump())
            res = self.user_service.register(register_user)
            if not res:
                return False
        except Exception as e:
            logger.error(f"[user]:Failed to register user {register_user_cmd.user_name}: error: {e}")
            return False
        return True
