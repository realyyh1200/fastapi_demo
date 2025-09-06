from ..aggregation.user import User
from ..port.client.password_encryption_client import PasswordEncryptionClient
from ..port.client.jwt_client import JWTClient
from ..port.repository.user_repository import UserRepository


class UserService:
    def __init__(self,
                 password_encryption_client: PasswordEncryptionClient,
                 user_repository: UserRepository,
                 jwt_client: JWTClient):
        self.password_encryption_client = password_encryption_client
        self.user_repository = user_repository
        self.jwt_client = jwt_client

    def register(self, user: User) -> bool:
        encrypted_password = self.password_encryption_client.encrypt(user.password)
        return self.user_repository.add_user(user.user_name, encrypted_password)

    def login(self, user: User) -> str | None:
        queried_user = self.user_repository.query_user(user.user_name)
        if queried_user is None:
            return None
        result = self.password_encryption_client.verify(user.password, queried_user.password)
        if not result:
            return None
        token = self.jwt_client.create_token(queried_user.user_name)
        return token





