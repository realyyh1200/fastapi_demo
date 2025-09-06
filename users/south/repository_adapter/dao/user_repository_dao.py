from .tables.user_table import UserTable


class UserRepositoryDao:
    def __init__(self, db):
        self.db = db

    def add_user(self, user: UserTable):
        self.db.add(user)

    def query_user(self, username: str) -> UserTable:
        res = self.db.query(UserTable).filter(UserTable.username == username).one_or_none()
        return res
