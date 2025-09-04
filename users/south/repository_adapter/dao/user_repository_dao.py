from .tables.user_table import UserTable
from database import get_db


def repo_add_user(user: UserTable):
    with get_db() as db:
        db.add(user)
