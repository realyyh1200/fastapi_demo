from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from .vo import OrderStatus


class Order(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    shop_id: Optional[int] = None  # 所属商铺id，外键关联
    total_amount: Optional[Decimal] = None
    status: Optional[OrderStatus] = None
