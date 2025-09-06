from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from logger import logger
from ...domain.aggregation.user import User
from ...domain.service.user_service import UserService
from ...south.client_adapter.password_encryption_adapter import PasswordEncryptionClientAdapter
from ...south.repository_adapter.user_repository_adapter import UserRepositoryAdapter
from ...south.client_adapter.jwt_client_adapter import JWTClientAdapter


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserLocalService:
    def __init__(self):
        self.password_encryption_client = PasswordEncryptionClientAdapter()
        self.user_repository = UserRepositoryAdapter()
        self.jwt_client = JWTClientAdapter()
        self.user_service = UserService(password_encryption_client=self.password_encryption_client,
                                        user_repository=self.user_repository,
                                        jwt_client=self.jwt_client)

    def register_user(self, user_name: str, password: str) -> bool:
        try:
            logger.info(f"[user]:Registering user {user_name}")
            register_user = User(user_name=user_name, password=password)
            res = self.user_service.register(register_user)
            if not res:
                return False
        except Exception as e:
            logger.error(f"[user]:Failed to register user {user_name}: error: {e}", exc_info=True)
            return False
        return True

    def login_user(self, user_name, password) -> str | None:
        try:
            logger.info(f"[user]:Logging user {user_name}")
            login_user = User(user_name=user_name, password=password)
            res = self.user_service.login(login_user)
            return res
        except Exception as e:
            logger.error(f"[user]:Failed to login user {user_name}: error: {e}", exc_info=True)
            return None


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
    try:
        jwt_adapter = JWTClientAdapter()
        return jwt_adapter.get_current_user(token)
    except Exception as e:
        logger.error(f"[user]:Failed to get current user: {e}", exc_info=True)
        raise
