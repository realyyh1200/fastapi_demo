from enum import Enum


class OrderStatus(str, Enum):
    PAID = "paid"
    UNPAID = "unpaid"
