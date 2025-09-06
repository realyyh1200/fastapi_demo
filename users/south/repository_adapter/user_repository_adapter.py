from logger import logger
from database import get_db
from utils.to_model import to_model
from ...domain.port.repository.user_repository import UserRepository
from ...domain.aggregation.user import User
from .dao.tables.user_table import UserTable
from .dao.user_repository_dao import UserRepositoryDao


class UserRepositoryAdapter(UserRepository):
    def add_user(self, username: str, encrypted_password: str) -> bool:
        try:
            user_table = UserTable(username=username, password=encrypted_password)
            with get_db() as db:
                user_repo = UserRepositoryDao(db=db)
                user_repo.add_user(user_table)
        except Exception as e:
            logger.error(f"[user]添加用户:{username}失败, error:{e}")
            return False
        return True

    def query_user(self, username: str) -> User | None:
        try:
            with get_db() as db:
                user_repo = UserRepositoryDao(db=db)
                user_table = user_repo.query_user(username)
                if user_table is not None:
                    return to_model(user_table, User)
        except Exception as e:
            logger.error(f"[user]查询用户:{username}失败, error:{e}")
        return None
