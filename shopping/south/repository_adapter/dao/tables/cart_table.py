from sqlalchemy import Column, Integer, Boolean
from database import BaseTable


class CartTable(BaseTable):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer)
    selected = Column(Boolean)
