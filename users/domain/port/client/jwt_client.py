from abc import ABC, abstractmethod


class JWTClient(ABC):
    @abstractmethod
    def create_token(self, username: str) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: str) -> str | None:
        pass
