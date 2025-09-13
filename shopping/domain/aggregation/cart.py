from typing import Optional

from pydantic import BaseModel


class Cart(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    selected: Optional[bool] = None
