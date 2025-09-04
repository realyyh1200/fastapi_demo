from sqlalchemy import Column, Integer, String
from database import BaseTable


class UserTable(BaseTable):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
