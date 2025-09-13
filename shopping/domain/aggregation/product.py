from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[int] = None
    merchant_id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
