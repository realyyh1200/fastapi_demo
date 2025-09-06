from abc import ABC, abstractmethod
from ...aggregation.user import User


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user_name: str, encrypted_password: str) -> bool:
        pass

    @abstractmethod
    def query_user(self, user_name: str) -> User:
        pass
