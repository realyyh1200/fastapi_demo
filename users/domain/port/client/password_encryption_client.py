from abc import ABC, abstractmethod


class PasswordEncryptionClient(ABC):
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        pass
