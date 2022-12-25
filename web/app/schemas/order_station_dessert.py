from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationDessertBase(BaseModel):
    dessert_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationDessertCreate(OrderStationDessertBase):
    dessert_id: UUID
    count: int


class OrderStationDessertUpdate(OrderStationDessertBase):
    pass


class OrderStationDessert(OrderStationDessertBase):
    from app.schemas.dessert import Dessert

    dessert: Optional[Dessert]
