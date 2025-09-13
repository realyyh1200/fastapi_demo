from sqlalchemy import Column, Integer, String, DECIMAL
from database import BaseTable


class OrderTable(BaseTable):
    __tablename__ = 'order_table'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, index=True)
    shop_id = Column(Integer, index=True)
    total_amount = Column(DECIMAL(10,2), index=True)
    status = Column(String, default='unpaid')
