from sqlalchemy import Column, Integer, String, DECIMAL
from database import BaseTable


class ProductTable(BaseTable):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    merchant_id = Column(Integer, index=True)
    name = Column(String)
    price = Column(DECIMAL)
    stock = Column(Integer)
