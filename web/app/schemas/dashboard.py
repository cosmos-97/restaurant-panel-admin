from pydantic import BaseModel


class OrdersCount(BaseModel):
    orders_count: int
