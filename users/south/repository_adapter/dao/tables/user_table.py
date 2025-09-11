from sqlalchemy import Column, Integer, String, Boolean
from database import BaseTable


class UserTable(BaseTable):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_merchant = Column(Boolean, nullable=False, default=False)
