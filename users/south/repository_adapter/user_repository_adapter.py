from logger import logger
from ...domain.port.repository.user_repository import UserRepository
from .dao.tables.user_table import UserTable
from .dao.user_repository_dao import repo_add_user


class UserRepositoryAdapter(UserRepository):
    def add_user(self, user_name: str, encrypted_password: str) -> bool:
        try:
            user_table = UserTable(user_name=user_name, password=encrypted_password)
            repo_add_user(user_table)
        except Exception as e:
            logger.error(f"[user]添加用户:{user_name}失败, error:{e}")
            return False
        return True

